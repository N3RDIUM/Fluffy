const express = require('express')
const training_data = require('./training_data.json')
const fallback_data = require('./fallback_data.json')
const levenshtein = require('fast-levenshtein')
const app = express()
const port = 3000

function randomFallback() {
    return fallback_data[Math.floor(Math.random() * fallback_data.length)]
}

function respond(input){
    try{
        let closest_matches = []

        for(let i = 0; i < training_data.length; i++){
            for(let j = 0; j < training_data[i].length; j++){
                let distance = levenshtein.get(input, training_data[i][j])
                if(distance < 5){
                    closest_matches.push({
                        distance: distance,
                        index: [i, j]
                    })
                }
            }
        }

        closest_matches.sort((a, b) => {
            return a.distance - b.distance
        })

        let closest_match = closest_matches[0]
        if(closest_match.index[1] + 1 < training_data[closest_match.index[0]].length){
            let response = training_data[closest_match.index[0]][closest_match.index[1] + 1]
            return response
        } else {
            return randomFallback()
        }
    } catch(e){
        return randomFallback()
    }
}

app.get('/chatbot/', (req, res) => {
    input = req.query.input
    res.send(respond(input))
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})