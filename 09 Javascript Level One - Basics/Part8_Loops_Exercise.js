/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var a=1
while (a<6){
    document.write("WHILE loop value is: <b>"+a+") hello</b><br>")
    a++
}
document.write("<br>")
// For Loop
for(var i=1; i<6; i++){
    document.write("FOR loop value is: <b>"+i+") hello</b><br>")
}
document.write("<br>")


/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var a=1
while (a<25){
    if(a%2 !== 0){
        document.write("WHILE loop ODD number is: <b>"+a+") hello</b><br>")
    }
    a++
}
document.write("<br>")


// METHOD TWO
// For Loop
for(i=1; i<25; i++){
    if(i%2 !== 0){
        document.write("FOR loop ODD number is: <b>"+i+") hello</b><br>")
    }
}