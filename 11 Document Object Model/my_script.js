var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

headOne.addEventListener("mouseover", function () {
    headOne.textContent = "Mouse over me";
    headOne.style.color = "red";
})

headOne.addEventListener("mouseout", function () {
    headOne.textContent = "Hover over me";
    headOne.style.color = "black";
})

headTwo.addEventListener("click", function () {
    headTwo.textContent = "GOPA";
    headTwo.style.color = 'green';
})

headTwo.addEventListener("dblclick", function () {
    headTwo.textContent = "Hren!!";
    headTwo.style.color = 'blue';
})