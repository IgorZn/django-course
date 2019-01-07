var fName = prompt("Your First name: ")
var lName = prompt("Your Last name: ")
var age = prompt("Your age: ")
var height = prompt("Your height: ")
var petName = prompt("Yours pet name: ")
var values = [fName, lName, age, height, petName]

for (var vol=0; vol<values.length; vol++){
    document.write("<br>"+values[vol])
}

if (fName[0] == lName[0] && (age > 20 && age < 30) && height >= 170 && petName[petName.length-1] == "y"){
    document.write("<br>Welcome Comrade! You've passed the Spy test!")
} else {
    document.write("<br>Sorry")
}

