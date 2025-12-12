<<<<<<< HEAD


let allImages = ["",""]
let index = 0

let img = document.querySelector('img')
function NextBtn(){
    img.setAttribute('src', allImages[index])
}


function PrevBtn(){

}
setInterval(NextBtn, 3000)
=======
const boxElem = document.querySelector('.box')

console.log(boxElem.style)

let boxStyles = getComputedStyle(boxElem)
console.log(boxStyles.backgroundColor)
console.log(boxStyles.getPropertyValue('width'))


>>>>>>> 27073f3d2e2bc68f38e4d13561e38d1f03f9251b
