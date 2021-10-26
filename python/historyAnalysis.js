// Connect to pSQL 'COT' database that contains Commitment of Traders historical data 
const { Client } = require('pg')

const client = new Client({
    host: 'localhost',
    user: 'postgres',
    port: 5433,
//   Password unavailable
    password: '***********',
    database: 'COT'
})

client.connect()

// Store DB table names to iterate over and a master DATA object to store everything in from each year.
// After running this program, the DATA object...
// 1. Has each cot year as a key. For each key it has...
// 2. 11 sections of market trader position categories (Open Interest, Asset Manager, Hedge Funds, etc.)
// 3. Each 11 sections has 38 assets (Currencies, Indicies, Treasuries, etc)
// 4. All assets have the calculated median, mean, min, and max for that year
const tables = ['cot2015', 'cot2016', 'cot2017', 'cot2018', 'cot2019', 'cot2020']
const DATA = {}

function runQueryByYear(year) {
    client.query(`SELECT * FROM ${year};`, (err, res) => {
        if (!err) {
            const data = res.rows
            // Main program takes in unprocessed data and the year that is being queried
            runProgram(data, year)
        }
        else console.log(err.message)
    })
}
tables.forEach(year => runQueryByYear(year))
client.end

function runProgram(db, year) {
    function organizeData() {
        // Get only the asset name from each line and store in an array called [assetNames]
        let assetNames = db.map(line => line.Market_and_Exchange_Names)
        // Remove duplicates 
        assetNames = [...new Set(assetNames)] 
        // Gather all the weekly report data by asset name and store in an array called [dataArray]
        const filterByName = name => db.filter(line => line.Market_and_Exchange_Names === name)
        const dataArray = assetNames.map(name => filterByName(name))
        // Return an object with the asset names as keys and all the asset's data as values
        const dataObj = {}
        dataArray.forEach((data, i) => dataObj[assetNames[i]] = data)
        return dataObj
    }

    const data = organizeData()
    const names = Object.keys(data)

    // Takes in asset name and the column to pull data from. Then returns median, mean, min, max for the entire data set.
    function getStatsByName(name, column) {
        const values = data[name].map(report => report[column])
        values.sort((a, b) => a - b)
        const half = Math.floor(values.length / 2)
        
        const median = values[half]
        const mean = Math.floor(data[name].reduce((acc, line) => acc += line[`${column}`], 0) / data[name].length)
        const min = values[0]
        const max = values[values.length - 1]
        // Handle odd numbers
        if (!values.length % 2) median = (values[half - 1] + values[half]) / 2.0
        
        return { name, column, median, mean, min, max }
    }

    // Grab only the columns that are useful for pulling stats out of
    const columns = Object.keys(db[0])
    const statColumns = columns.slice(3, 14)
    // Map an array that contains every asset name with a complete list of stats from each column
    const completeStats = statColumns.map(column => {
       return names.map(name => getStatsByName(name, column))
    })

    DATA[year] = completeStats
}

