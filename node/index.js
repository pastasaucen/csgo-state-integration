const CSGameState = new (require('cs-gamestate'))(3000, '127.0.0.1');
var express = require('express')
var ex = express()
var port = 3001

var allData = {}

// The events are being reffered to like objects
// in this case the function will be called whenever 'player.state.health' changes
CSGameState.on('player.state', function (health, previous, data) {
    // If you need any other information (e.g. money) you can access it via the data object
    // In the case of the players money that would be 'data.player.state.money'

    //var keys = Object.keys(data.allplayers)

    allData = data.allplayers

    //console.log(allData)

    keys.forEach(function (element) {
        //console.log(data.allplayers[element].name)
    })

    //CSGameState.parse(data.allplayers)

    //console.log(keys)
    // => OUTPUT: Health of Hansiiii has changed: 72
});

ex.get('/test', (req, res) => {
    res.send(allData);
});

ex.listen(port, () => console.log(`Example app listening on port ${port}!`))