let citiesData = {
  tehran: {city: 'Tehran', temp: 12, 
    weather: 'Sunny', humidity: 23, windSpeed: 32},
  shiraz: {city: 'Shiraz', temp: 9, 
    weather: 'windy', humidity: 12, windSpeed: 14},
  tabriz: {city: 'Tabriz', temp: 1, 
    weather: 'rainy', humidity: 43, windSpeed: 12},
  mashhad: {city: 'Mashhad', temp: 16, 
    weather: 'snowy', humidity: 7, windSpeed: 24},
  esfahan: {city: 'Esfahan', temp: 23,
     weather: 'Sunny', humidity: 15, windSpeed: 18},
}


let searchBtn = document.querySelector('#search')
let weatherWrapper = document.querySelector('.weather')
let inputElem = document.getElementsByTagName('input')[0]
let cityElem = document.querySelector('.city')
searchBtn.addEventListener('click', function(){
    let inputVal =  inputElem.value
    let data = citiesData[inputVal]
    if(data){
        weatherWrapper.classList.remove('loading')
        cityElem.innerHTML = "Weather in " + data.city
    }
})