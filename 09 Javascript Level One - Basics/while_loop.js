var val = 0;
while (val < 5){
    console.log(val);
    document.write('<b>'+val+'</b><br>')
    if(val == 3){
        console.log("Time to go out -- BREAK!")
        break;
    }
    val+=1;
}
