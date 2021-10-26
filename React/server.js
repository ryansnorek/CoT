// Express server
const express = require('express')
const cothistoryRoutes = require('./src/DB/routes')
const app = express()
const port = 3000

// Allows us to post and get json from endpoints
app.use(express.json())

// CORS fix
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    next();
    });

app.get('/', (req, res) => {
    res.send('HOME PAGE')
})
// Use this path, once we get there send cothistoryRoutes
app.use('/api/v1/cothistory', cothistoryRoutes)

app.listen(port, () => console.log(`server is listening on port ${port}`))