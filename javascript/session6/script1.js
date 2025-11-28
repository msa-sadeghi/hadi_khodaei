let buttons = document.querySelectorAll('button')

buttons[0].addEventListener('click', function(e){
    localStorage.setItem('name',  "sara")
})
buttons[1].addEventListener('click', function(e){
    let name = localStorage.getItem('name')
    alert(name)
})
buttons[2].addEventListener('click', function(e){
    localStorage.clear()
})