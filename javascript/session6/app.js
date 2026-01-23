    const listItems = [
    { id: 1, name: 'reza', family: 'ahmadi Rad' },
    { id: 2, name: 'Amir', family: 'Zehtab' },
    { id: 3, name: 'mohammad', family: 'yegane' },
    { id: 4, name: 'armin', family: 'mohammadzade' },
    { id: 5, name: 'ata', family: 'nadi Zadeh' },

    { id: 6, name: 'reza', family: 'ahmadi Rad' },
    { id: 7, name: 'Amir', family: 'Zehtab' },
    { id: 8, name: 'sara', family: 'ariamanesh' },
    { id: 9, name: 'arman', family: 'dara' },
    { id: 10, name: 'ladan', family: 'poua Zadeh' },

    { id: 11, name: 'abbas', family: 'tehrani' },
    { id: 12, name: 'peyman', family: 'minaee' },
    { id: 13, name: 'javad', family: 'rasoli' },
    { id: 14, name: 'Mehran', family: 'Ali Pour' },
    { id: 15, name: 'Amir mohammad', family: 'naderi' },

    { id: 16, name: 'paria', family: 'maleki' },
    { id: 17, name: 'dara', family: 'jabbari' },
    { id: 18, name: 'sara', family: 'ariamanesh' },
    { id: 19, name: 'Fatemeh', family: 'ataei' },
    { id: 20, name: 'arash', family: 'tahaei' },

    { id: 21, name: 'mina', family: 'rad' },
    { id: 22, name: 'Matin', family: 'rezapour' },
    
];

let usersContainer = document.getElementById("list")
let pagesContainer = document.getElementById("pagination")

let currentPage = 1
let rowsCount = 5

function displayUsersList(allUsersArray, usersContainer, rowsCount, currentPage){
        usersContainer.innerHTML = ''
        let endIndex = rowsCount *  currentPage
        let startIndex = endIndex - rowsCount
        let paginatedUsers = allUsersArray.slice(startIndex, endIndex)
        paginatedUsers.forEach(element => {
                let userElement = document.createElement('div')
                userElement.classList.add('.item')
                userElement.innerHTML = `${element.name} ${element.family}`
                usersContainer.append(userElement)
        });

}


function setupPagination(allUsersArray, pagesContainer, rowsCount){
        pagesContainer.innerHTML =  ''
        for(let i=1; i <= Math.ceil(allUsersArray.length/rowsCount); i++){

                let button = paginationButtonGenerator(i)
                pagesContainer.append(button)
        }
        
        
}

function paginationButtonGenerator(page){
        let button = document.createElement('button')
        if(currentPage === page){
                button.classList.add('active')
        }
        button.innerHTML = page
        return button
}
displayUsersList(listItems, usersContainer,  5, 1)
setupPagination(listItems, pagesContainer, rowsCount)