var students = ['ali', 2]
console.log(typeof students)
console.log(Array.isArray(students))
console.log(students.length)
console.log(students[0])

students.push("sara", "reza")
console.log(students)
students.unshift("mary", "artin")
console.log(students)

students.pop()

console.log(students)

students.shift()

console.log(students)

// اعدادی را به تعداد دلخواه از کاربر گرفته 
// و داخل آرایه ای ذخیره کنید
// و سپس میانگین آن ها را محاسبه کرده و نمایش دهید


// یک سامانه ثبت نام پیاده سازی کنید

// به این شکل که یک آرایه برای ذخیره اطلاعات کاربران داشته باشید 
// (3 کاربر را بطور دیفالت در آرایه داشته باشید)
// و از کاربری که قصد ثبت نام دارد نام، نام خانوادگی، سن و ایمیل را دریافت کرده
// و داخل آبجکتی مجزا در آرایه کاربران ذخیره کنید
// پس از انجام عمل ثبت نام، اطلالاعات تک تک کاربران را لاگ بگیرید

// :نکات قابل توجه
// نام حداقل باید 3 کاراکتر و حداکثر 10 کاراکتر داشته باشد
// نام خانوادگی حداقل باید 3 کاراکتر و حداکثر باید 15 کاراکتر داشته باشد
// سن حتما باید عدد بوده و حداکثر 3 رقم باشد


// var user = {
//     id: 1, name:'reza', family:'rezaei'
// }

// console.log(typeof user)
// console.log(user.id)
// console.log(user.name)
// var p = 'age'
// console.log(user.p)
// console.log(user[p])

var users =[
    'sara', 'jack'
]
var f = function(n){
    console.log(n)
}
users.forEach(f)


// دیتابیسی برای ذخیره اطلاعات کاربران داشته باشید
//  (آرایه ای از آبجکت ها)
// و سپس به کمک متد فورایچ، اطلاعات هر یوزر را
//  به صورت جداگانه در کنسول نمایش دهید