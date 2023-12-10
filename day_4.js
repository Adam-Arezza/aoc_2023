const fs = require("fs")

let inputs = fs.readFileSync('inputs/day_4.txt').toString().split("\n")
inputs.pop()

let example = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

for(let i = 0 ; i < inputs.length - 1; i++){
    inputs[i] = inputs[i].split("|")
    inputs[i][0] = inputs[i][0].split(":")[1]
    inputs[i][0] = inputs[i][0].replaceAll(" ", ",").split(",")
    inputs[i][1] = inputs[i][1].replaceAll(" ", ",").split(",")
}

let total = 0
for(let i = 0; i < inputs.length-1; i++){
    let points = 0
    let winning_numbers = inputs[i][0]
    let player_numbers = inputs[i][1]
    for(let n = 0; n < player_numbers.length; n++){
        if(winning_numbers.includes(player_numbers[n]) && player_numbers[n] !== ""){
            if(points === 0){
                points++
            }
            else{
                points = points * 2
            }
        }
    } 
    total = total + points
}

//PART 1
console.log(total)


//PART 2

for(let i = 0 ; i < example.length - 1; i++){
example[i] = example[i].split("|")
example[i][0] = example[i][0].split(":")[1]
example[i][0] = example[i][0].replaceAll(" ", ",").split(",")
example[i][1] = example[i][1].replaceAll(" ", ",").split(",")
}

let cards = {}

for(let i = 0; i < inputs.length; i++){
    cards[i] = 1
}

let total_cards = 0
for(let i = 0; i < inputs.length; i++){
    let matches = 0
    let winning_numbers = inputs[i][0]
    let player_numbers = inputs[i][1]
    for(let n = 0; n < player_numbers.length; n++){
        if(winning_numbers.includes(player_numbers[n]) && player_numbers[n] !== ""){
            matches++
        }
    }
    for(let c = 0; c < cards[i]; c++){
        for(let m = 1; m < matches+1; m++){
            cards[i + m] = cards[i + m] + 1
        }
    }
}

for(let k = 0; k < Object.keys(cards).length;k++){ 
    total_cards = total_cards + cards[k]
}

console.log(`Total cards: ${total_cards}`)

