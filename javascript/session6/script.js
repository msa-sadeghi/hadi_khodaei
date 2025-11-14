
// Music
const songs = [
  {
    path:
      "html.m4a",
    displayName: "Html Padcast",
    artist: "Ozbi",
    cover:
      "https://images.genius.com/ee202c6f724ffd4cf61bd01a205eeb47.1000x1000x1.jpg",
  },
  {
    path: "media/kar.m4a",
    displayName: "Developing",
    artist: "Flora Cash",
    cover: "images/peakpx.jpg",
  },
  {
    path:
      "media/bazar.m4a",
    displayName: "Earn",
    artist: "Linkin Park",
    cover:
      "https://images.genius.com/c5a58cdaab9f3199214f0e3c26abbd0e.1000x1000x1.jpg",
  },
];


let isPlaying = false

const nextButton = document.getElementById("next")
const prevButton = document.getElementById("prev")
const playButton = document.getElementById("play")
const artist = document.getElementById("artist")
const title = document.getElementById("title")
const cover = document.getElementById("cover")
const duration = document.getElementById("duration")
const currentTime = document.getElementById("current-time")
const progress = document.getElementById("progress")
const audio = document.querySelector("audio")

function playSong(){
    isPlaying = true
    playButton.classList.replace('fa-play', 'fa-pause')
    playButton.setAttribute("title", "Pause")
    audio.play()

}
function pauseSong(){
    isPlaying = false
    playButton.classList.replace('fa-pause', 'fa-play')
    playButton.setAttribute("title", "Play")
    audio.pause()
}

playButton.addEventListener('click', function(){
    if(isPlaying){
        pauseSong()
    }else{
        playSong()
    }
})

function loadSong(song){
    audio.src = song.path
    title.textContent = song.displayName
    artist.textContent = song.artist
    cover.src = song.cover
   
}

loadSong(songs[0])

audio.addEventListener('timeupdate', function(e){
    if(isPlaying){

        const duration = e.target.duration
        const currentTime = e.target.currentTime

        const progressContent = currentTime/duration * 100
        progress.style.width = progressContent  + "%"
        
    }
})