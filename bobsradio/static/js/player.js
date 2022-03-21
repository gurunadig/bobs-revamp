window.onload = function() {
    document.getElementById("Sample").play();
}


var SampleAudio = document.getElementById("Sample");
function togglePlay() {
return SampleAudio.paused ? SampleAudio.play() : SampleAudio.pause();
};

function muteAudio(){

    SampleAudio.muted = !SampleAudio.muted;
} 