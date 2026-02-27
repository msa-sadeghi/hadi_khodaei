async function getAllUsers(url) {
    try{
        const response = await fetch(url);
        const users = await response.json()
        renderUsers(users)
    }
    catch(error){
        console.log(error)
    }
}
window.onload = ()=>{
    getAllUsers('http://127.0.0.1:5000/')
}
const container = document.querySelector(".container")
const renderUsers = (users)=>{
    container.innerHTML = ''
    users.forEach(user => {
        const cardElement = document.createElement('div')
        cardElement.classList.add('product-card')
        const userId = document.createElement("span")
        userId.classList.add('product-button')
        userId.innerText = user.id
        const userName = document.createElement("span")
        userName.innerText = user.name
        userName.classList.add('product-info')
        const userRole = document.createElement("span")
        userRole.innerText = user.role
        userRole.classList.add('product-price')
        const deleteBtn = document.createElement("button")
        deleteBtn.innerText = "delete"
        deleteBtn.addEventListener('click',  async () => {
            const response = await fetch(`http://127.0.0.1:5000/delete-user/${user.id}`,
                {method : 'delete'}
            )
            const users = await response.json()
            renderUsers(users)

        })
        cardElement.append(userId, userName, userRole, deleteBtn)
        container.append(cardElement)
    });
}

const addBtn = document.getElementById('addBtn')
const nameElement = document.getElementById('name')
const roleElement = document.getElementById('role')

addBtn.addEventListener('click', async () => {
    const newUser = {
        name : nameElement.value,
        role : roleElement.value
    }
    const response = await fetch('http://127.0.0.1:5000/add-user',{
        method:'POST',
        headers :{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(newUser)
    })
    const users = await response.json()
    renderUsers(users)
    nameElement.value = ''
    roleElement.value = ''
})