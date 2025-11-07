let inputField = document.querySelector('#input-field')
let colorBoxes = document.querySelectorAll('.color-box')
let btnSave = document.querySelector('#btn-save')
let btnDelete = document.querySelector('#btn-delete')
let notes = document.querySelector('#listed')

colorBoxes.forEach(function(cb){
    cb.addEventListener('click', function(event){
        let c = event.target.style.backgroundColor;
        inputField.style.backgroundColor = c
    })
})

const clearInput = function(){
    inputField.style.backgroundColor = 'white'
    inputField.value = ''

}


function removeNote(e){
    e.target.parentElement.remove()
}

function getnerateNote(){
    let newParentDiv = document.createElement('div')
    newParentDiv.className = 'card shadow-sm rounded'
    let inputBgColor = inputField.style.backgroundColor
    newParentDiv.style.backgroundColor = inputBgColor
    let newP = document.createElement('p')
    newP.className = "card-text p-3"
    newP.innerHTML = inputField.value
    newParentDiv.append(newP)
    notes.append(newParentDiv)
    newParentDiv.addEventListener('click', removeNote)
    clearInput()
}





btnDelete.addEventListener('click', clearInput)
btnSave.addEventListener('click', getnerateNote)


function my(event){
    console.log(document.documentElement.scrollTop, window.screenTop)
}

document.addEventListener('scroll', my)