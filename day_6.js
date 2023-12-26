const fs = require("fs")

let inputs = fs.readFileSync("inputs/day_6.txt").toString()

let races = inputs.split("\n")
races.pop()
console.log(races)
let races_obj = {}
for(let i = 0; i < races.length; i++){
    let key = races[i].split(":")[0].toLowerCase()
    let times = races[i].split(":")[1]
    races_obj[key] = Number(times.trim().replaceAll(" ", ""))
   // races_obj[key] = times.trim().split(" ").filter(t => {
   //     if(t && t.length > 0){
   //         return t
   //     }
   // }) 
}

races_obj["count"] = []
//for(let i = 0; i < races_obj["time"]; i++){
//    let t = races_obj["time"]
//    let r = races_obj["distance"]
//    let count = 0
//    //console.log(t)
//    //console.log(r)
//    for(let n = 0; n < t; n++){
//        let remaining = t - n
//        if(n * remaining > r){
//            count++
//        }
//    }
//    //races_obj["count"].push(count)
//    races_obj["count"] = count
//}

let t = races_obj["time"]
let r = races_obj["distance"]
let count = 0
    //console.log(t)
    //console.log(r)
for(let n = 0; n < t; n++){
    let remaining = t - n
    if(n * remaining > r){
        count++
       }
    }
    //races_obj["count"].push(count)
races_obj["count"] = count

console.log(races_obj)
//let total = races_obj.counts.reduce((acc,current) => {return current * acc})


