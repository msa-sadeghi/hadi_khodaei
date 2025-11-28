const switchElement = document.querySelector('.switch')

switchElement.addEventListener('click', function(element){
    document.documentElement.classList.toggle('dark')
    if(document.documentElement.classList.contains('dark')){
        localStorage.setItem('theme',  'dark')
    }else{
        localStorage.setItem('theme', 'light')
    }
})

