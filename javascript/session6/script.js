

// const textArea = document.querySelector('textarea')
// textArea.addEventListener('copy', function(event){
//     console.log(event.target.value)
// })


const b = document.body
 b.addEventListener('contextmenu', function(event){
        event.preventDefault()
        console.log(event)
    })