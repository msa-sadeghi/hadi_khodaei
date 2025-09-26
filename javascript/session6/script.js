const element = document.getElementsByName('test')[0]
console.log(element.innerText)
const element2 = document.getElementsByTagName('li')[1]
console.log(element2.innerText)
const element3 = document.getElementsByClassName('list-item')[2]
console.log(element3.innerText)
const element4 = document.querySelectorAll('.list-item')[3]
console.log(element4.innerText)
const element5 = document.querySelector('.list-item#tt')
console.log(element5.innerText)

const h3Element = document.querySelector('h3')
document.addEventListener('click', function(){

    h3Element.setAttribute('class', 'test')
})