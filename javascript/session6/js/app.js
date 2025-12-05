const addBtn = document.querySelector('button')
const divElem = document.querySelector('div')
const pElem = document.querySelector('p')

addBtn.addEventListener('click', () => divElem.style.animation ='move 4s 3')

function startH(){

}

function startR(){

}
function startE(){

}


divElem.addEventListener('animationstart', startH)
divElem.addEventListener('animationiteration', startR)
divElem.addEventListener('animationend', startE)


const add  = () => a + b

console.log(add(2,3))