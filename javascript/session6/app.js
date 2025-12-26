const bookList = document.getElementById("book-list")
const submitBtn = document.querySelector("[type='submit']")
const titleElem = document.getElementById('title')
const author = document.getElementById('author')
const year = document.getElementById('year')
submitBtn.addEventListener('click', (e)=>{
        e.preventDefault()
        let titlevalue = titleElem.value
        let authorvalue = author.value
        let yearvalue = year.value

        console.log(titleElem)
        let newTr = document.createElement('tr')
        let tdTitle = document.createElement('td')
        tdTitle.innerHTML = titlevalue
        let authorTd = document.createElement('td')
        authorTd.innerHTML = authorvalue
        let yearTd = document.createElement('td')
        yearTd.innerHTML = yearvalue

        newTr.append(tdTitle, authorTd, yearTd)
        bookList.append(newTr)
        
})