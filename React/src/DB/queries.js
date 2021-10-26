const year = '2020'
const getCotData = `SELECT * FROM cothistory${year};`
const getHistoryByName = `SELECT * FROM cothistory${year} WHERE Market_and_Exchange_Names = 'CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE';`

module.exports = {
    getCotData,
    getHistoryByName
}