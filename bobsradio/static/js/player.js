var x = document.getElementById("myAudio"); 

    function playAudio() { 
    x.play(); 
    
} 

function pauseAudio() {
    x.pause();
  }


function muteAudio(){

    Sample.muted = !Sample.muted;
} 