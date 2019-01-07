var value = prompt("Type TRUE or FALSE or something else: ")
if (value.toString().toLowerCase() === "true"){
    alert("You've typed [if TRUE]: "+value)
} else if (value.toString().toLowerCase() === "false"){
    alert("You've typed [if FALSE]: "+value)
} else {
    alert("You've typed [else]: "+value)
}