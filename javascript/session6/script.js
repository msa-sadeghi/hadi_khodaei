function handler(event){
    console.log("selected", event.target.selectionStart)
    console.log("selected", event.target.selectionEnd)
}

el.blur()
el.style.filter =  "blur(0px)"

const anim = el.animate(
    [
        {
            transform:'translateX() scale()', opacity:1
        },
    ],
    [
        {'duration':400, iteration:1, easing:"ease" }   ]
)

anim.play()