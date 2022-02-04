let plants = 1032;
let percentage = 0.035;

let index = 0;

let minutes_running = 24 * 60 * 30 * 3;
while(minutes_running > 0){
  let plants_per_day = plants * percentage;
  var time_till_next_plant = (24 * 60)/plants_per_day;
  minutes_running -= time_till_next_plant -0.5;
  plants++;
  index++;
}
console.log("new rebase time: " + time_till_next_plant)
console.log("amount of plants: " + plants)
console.log("gas fee paid: " + index * 0.09)


let plants_ = 1032;
for(let i = 0; i < 30 * 3; i++){
	plants_ += plants_* 0.035;
  
}
let plants_per_day_ = plants_ * percentage;
let time_till_next_plant_ = (24 * 60)/plants_per_day_;
console.log("new rebase time: " + time_till_next_plant_);
console.log("amount of plants: " + plants_);
console.log("gas fees paid: " + 90 * 0.09)
