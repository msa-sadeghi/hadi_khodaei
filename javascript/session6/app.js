let user = {
    id:1,
    firstName:'sara',
    lastName : 'rezaei',
    age:18
}

user.job = 'developer'


let userProxy = new Proxy(user,{
        get:function(target, property){
            return property in target ? target[property] : null
        },
        set: function(target, property, value){
            if(property === 'age' && value < 0){
                value = 18
            }
            target[property] =  value
        }
    })


userProxy.age = -12
console.log(userProxy.age)

