const { Pool } = require('pg')

const pool = new Pool({
    host: 'localhost',
    user: 'postgres',
    port: 5433,
    password: 'UNAVAILABLE',
    database: 'cot'
})

module.exports = pool
