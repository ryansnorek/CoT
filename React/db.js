const { Pool } = require('pg')

const pool = new Pool({
    host: 'localhost',
    user: 'postgres',
    port: 5433,
    password: 'oiarfewAPK9',
    database: 'cot'
})

module.exports = pool