// var numbers = [1,2,3,4,5]

// numbers.splice(2,2,6,56)
// console.log(numbers)

// var users = [
//     {id:1, name:'sara', age:23},
//     {id:2, name:'artin', age:29},
//     {id:3, name:'armin', age:33}
// ]

// var userIndex = users.findIndex(function(user){
//     return user.name === 'artin'
// })
// console.log(userIndex)


// پروژه فروشگاه را در نظر بگیرید

// محصولات فروشگاه را داخل آرایه ای ذخیره کرده 
// و آرایه ای برای سبد خرید در نظر بگیرید
// و داخل سبد خرید 3 محصول بطور دیفالت قرار دهید

// منویی را به کاربر نمایش دهید که شامل 2 گزینه است
// گزینه ای برای حذف محصول از سبد خرید
// و گزینه ای برای اضافه کردن محصول به سبد خرید

// عملیات لازم برای هر گزینه را پیاده سازی کنید


// var allProducts = [
//   { id: 1, name: "laptop", price: 17000000 },
//   { id: 2, name: "phone", price: 7000000 },
//   { id: 3, name: "milk", price: 35000 },
//   { id: 4, name: "pen", price: 12000 },
//   { id: 5, name: "pencil", price: 9000 },
//   { id: 6, name: "cable", price: 55000 },
//   { id: 7, name: "water", price: 6000 },
//   { id: 8, name: "soft drink", price: 13000 },
// ];

// var userBasket = [
//   { id: 1, name: "milk", price: 35000 },
//   { id: 2, name: "water", price: 6000 },
// ];

// var userRequest = "2"
// if(userRequest === "1"){
//     var userProductName = "laptop"
//     var selectedProduct;
//     var isInShop = allProducts.some(function(p){
//         if (p.name === userProductName){
//             selectedProduct = p
//             return true
//         }
//     })
//     if (isInShop){
//         var newProduct = {
//             id:userBasket.length ,
//             name:userProductName,
//             price:selectedProduct.price
//         }
//         userBasket.push(newProduct)
//         console.log(userBasket)
//     }else{
//         console.log("not exists")
//     }
// }else if(userRequest === "2"){
//     var userProductName = "milk"
//     var pi = userBasket.findIndex(function(p){
//         return p.name == userProductName
//     })
//     userBasket.splice(pi, 1)
//     console.log(userBasket)

// }


// var numbers = [1,2,3,4,5]

// var newNumbers =  numbers.map(function(n){
//         return n ** 2
// })

// console.log(newNumbers)
// var newNumbers =  numbers.filter(function(n){
//         return n > 2
// })

// console.log(newNumbers)



// یک پروژه فروشگاه آنلاین پیاده سازی کنید

// به این صورت که یک آرایه به عنوان سبد خرید کاربر
//  در نظر بگیرید که 6 محصول به طور دیفالت دارد

// سیاست کاری فروشگاه به این شکل است که
//  برای محصولاتی که بالای 100 هزار تومان باشند،
//  از مشتری هزینه پست دریافت نمی شود

// اما محصولاتی که زیر 100 هزار تومان قیمت داشته باشند، برای 
// هر کدام 1000 تومان هزینه ارسال (هزینه پست) دریافت میشه

// لطفا قیمت کل سبد خرید را همراه با
//  هزینه پست محاسبه کرده و به کاربر نمایش دهید

var numbers = [1,2,3,4,5,1]

console.log(typeof numbers)

console.log(Array.isArray(numbers))
console.log(numbers.indexOf(1))
console.log(numbers.lastIndexOf(1))
console.log(numbers.slice(2,4))
console.log(numbers.join(''))
console.log(numbers.reverse())

var x = "bla lal alal"

console.log(x.split(" "))

// کلمه ای از کاربر دریافت کرده و چک کنید 
// که کلمه وارد شده از هر دو سمت چپ و راست به یک صورت خوانده 
// می شود یا خیر

// به عنوان مثل کلمه 
// gig 
// از هر دو طرف به یک صورت خوانده می شود