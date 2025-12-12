const boxElem = document.querySelector('.box')

console.log(boxElem.style)

let boxStyles = getComputedStyle(boxElem)
console.log(boxStyles.backgroundColor)
console.log(boxStyles.getPropertyValue('width'))


