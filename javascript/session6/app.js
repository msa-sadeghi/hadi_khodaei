let allProducts = [
    { id: 1, title: 'Album 1', price: 5, img: 'Images/Album 1.png', count: 1 },
    { id: 2, title: 'Album 2', price: 15, img: 'Images/Album 2.png', count: 1 },
    { id: 3, title: 'Album 3', price: 20, img: 'Images/Album 3.png', count: 1 },
    { id: 4, title: 'Album 4', price: 100, img: 'Images/Album 4.png', count: 1 },
    { id: 5, title: 'Coffee', price: 5, img: 'Images/Cofee.png', count: 1 },
    { id: 6, title: 'Shirt', price: 50, img: 'Images/Shirt.png', count: 1 },
]



let userBasket = []

let $ = document
const shopItemsContainer = $.querySelector('.shop-items')
const bastekProductsContainer = $.querySelector('.cart-items')
const removeAllProductsBtn = $.querySelector('#remove-all-products')
const cartTotalPriceElem = $.querySelector('.cart-total-price')

allProducts.forEach(function (product) {
    let productContainer = $.createElement('div')
    productContainer.classList.add('shop-item')

    let productTitleSpan = $.createElement('span')
    productTitleSpan.classList.add('shop-item-title')
    productTitleSpan.innerHTML = product.title

    let productImageElem = $.createElement('img')
    productImageElem.classList.add('shop-item-image')
    productImageElem.setAttribute('src', product.img)

    let productDetailsContainer = $.createElement('div')
    productDetailsContainer.classList.add('shop-item-details')

    let productPriceSpan = $.createElement('span')
    productPriceSpan.innerHTML = product.price
    productPriceSpan.classList.add('shop-item-price')

    let prodcutAddButton = $.createElement('button')
    prodcutAddButton.innerHTML = 'ADD TO CART'
    prodcutAddButton.className = 'btn btn-primary shop-item-button'
    prodcutAddButton.addEventListener('click', function () {
        addProductToBasketArray(product.id)
    })

    productDetailsContainer.append(productPriceSpan, prodcutAddButton)
    productContainer.append(productTitleSpan, productImageElem, productDetailsContainer)
    shopItemsContainer.append(productContainer)

})



function addProductToBasketArray (productId) {

   
}

function basketProductsGenerator (userBasketArray) {
   
}

function removeProductFromBasket (productId) {

   
}

removeAllProductsBtn.addEventListener('click', function () {
    
})

function calcTotalPrice (userBasketArray) {
 
}

function updateProductCount (productId, newCount) {
    
}