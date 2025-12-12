

let allImages = ["",""]
let index = 0

let img = document.querySelector('img')
function NextBtn(){
    img.setAttribute('src', allImages[index])
}


function PrevBtn(){

}
setInterval(NextBtn, 3000)