//Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
//What is the sum of the IDs of those games?

//PART 1
let test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

const RED = 12
const GREEN = 13
const BLUE = 14

const fs = require('fs')
let inputs = fs.readFileSync('inputs/day_2.txt').toString().split("\n")

let ids = []
let game_powers = []
inputs.forEach(line => {
    if(!line) {
        return
    }

    let game_id = line.split(":")[0]
    game_id = game_id.split(" " )[1]
    let cubes = line.split(":")[1]
    cubes = cubes.replace(/ /g, "")
    let games = cubes.split(";")
    let blue_count = 0
    let red_count = 0
    let green_count = 0

    for(let i = 0; i < games.length; i++){
        let game = games[i].split(",")
        for(g in game) {
            if(game[g].match("blue")){
                let count = game[g].replace(/[^0-9]/g, "")
                if(count > blue_count) {
                    blue_count = Number(count)
                }
            }
            if(game[g].match("red")){
                let count = game[g].replace(/[^0-9]/g, "")
                if(count > red_count){
                    red_count = Number(count)
                }
            } 
            if(game[g].match("green")){
                let count = game[g].replace(/[^0-9]/g, "")
                if(count > green_count){
                    green_count = Number(count)
                }
            }    
        }
    }

    let game_power = blue_count * red_count * green_count
    game_powers.push(game_power)
    if(red_count > RED || blue_count > BLUE || green_count > GREEN){
        return
    }
    else{
        return ids.push(game_id)
    }
})

console.log(ids)
console.log(game_powers)

let id_sum = 0

for(let n = 0; n < ids.length; n++) {
    id_sum += Number(ids[n])
}

console.log(id_sum)

let power_sum = 0

for(let p = 0; p < game_powers.length; p++){
    power_sum += game_powers[p]
}

console.log(power_sum)
