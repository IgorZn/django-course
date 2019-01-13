var tds = document.querySelectorAll('#game-table td')
var clearVals = document.querySelector('#clr_btn')

function resetVals() {
    tds.forEach(function (elem) {
        elem.textContent = '';
    })
}

clearVals.addEventListener("click", resetVals)


function addX(elem){
    elem.textContent = "X";
}
function addO(elem){
    elem.textContent = "O";
}

function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
      // console.log(marker)
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};


tds.forEach(function (elem) {
    console.log(elem)
    elem.addEventListener("click", changeMarker);
})


