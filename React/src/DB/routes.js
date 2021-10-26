const { Router } = require('express')
// Get all data
const controller = require('./controller')

const router = Router()

// ROUTES //
// When you hit this you want to get the query json results and send it back 
// Express knows to call the getCotHistory data function
router.get('/', controller.getCotHistoryData)
// router.get('/:name', controller.getHistoryByNameData)
// router.post('/', controller.addData)

module.exports = router