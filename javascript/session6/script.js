const element = document.getElementsByName('test')[0]
const x = element.value
console.log(x)
const btn = document.getElementsByTagName('button')[0]

const ulEl = document.getElementsByTagName('ul')[0]
const inputElem = document.querySelector('input')
btn.addEventListener("click", function(){
    var elem1 = document.createElement("li")
    elem1.setAttribute('id', "test2")
    elem1.setAttribute('class', "test")
    elem1.innerHTML= inputElem.value
    elem1.style.color = 'green'
    var elem = document.createElement("li")
    // elem.setAttribute('id', "test2")
    // elem.setAttribute('class', "test")
    elem.innerHTML= inputElem.value
    // elem.style.color = 'green'
    // elem.classList.add('test')
    // ulEl.append(elem1, elem)
    ulEl.append(elem)
})

// یک عکس لامپ و یک دکمه داشته باشید
// با کلیک روی دکمه، لامپ روشن و خاموش بشه

// (src تغییر)