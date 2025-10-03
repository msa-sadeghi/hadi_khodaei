const input = document.getElementsByTagName('input')[0]
const span = document.querySelector('span')

const btn = document.querySelector('button')
btn.addEventListener('click', function(){
    // span.setAttribute('class', 'test')
    span.classList.toggle('test')
})