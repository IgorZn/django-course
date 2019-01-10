// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function addNew(name) {
    roster.push(name);
    document.write("<br><b>"+name+"</b> :was added to roster");
}
// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT
function remove(name){
    if (roster.includes(name)){
        var index = roster.indexOf(name);
        roster.splice(index,1);
        document.write("<br><b>"+name+"</b> :was deleted.");
        document.write("<br>"+roster)
    } else {
        document.write("<br>No such name!");
    }

}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
    document.write("<br> Here is what we get in arr: <b>"+roster+"</b>")
}

// Start by asking if they want to use the web app
var start = prompt("Would you like to start the roster web app? y/n");
if (start === "y"){
    var action = "";
    while (action !== 'quit'){
        var action = prompt("Please select an action: add, remove, display or quit");
        if (action === 'add'){
            var name = prompt("What name would you like to add?");
            addNew(name);
        }
        if (action === 'remove'){
            var name = prompt("What name would you like to remove?")
            remove(name);
        }
        if (action === 'display'){
            display();
        }
    }
} else {
    document.write("<br> OK, see you later!");
}

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
