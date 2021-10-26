// import postgres connection
const pool = require('../../db')
// import SQL queries object
const queries = require('./queries')

// Use this in the routes
const getCotHistoryData = (req, res) => {
    // query(SQL statement, (err, results))
    pool.query(queries.getCotData, (error, results) => {
        if (error) throw error
        // if its a successful query send back the results in a json object
        res.status(200).json(results.rows)
    })
}

// const getHistoryByNameData = (req, res) => {
//     const name = req.params.name?
//     // query(SQL statement, (err, results))
//     pool.query(queries.getHistoryByName, [name], (error, results) => {
//         if (error) throw error
//         // if its a successful query send back the results in a json object
//         res.status(200).json(results.rows)
//     })
// }

// Post. Sending with json
// const addData = (req, res) => {
    
// }

module.exports = {
    getCotHistoryData,
    // getHistoryByNameData,
    // addData,
}