var matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
for (elem of matrix){
	for(val of elem){
		console.log(val)
        document.write("<br>"+val)

	}
	console.log("next")
    document.write("<br>next")
}

var array1 = ['a', 'b', 'c'];

array1.forEach(function(element) {console.log(element);} );