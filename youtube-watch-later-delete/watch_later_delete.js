var items = $('body').getElementsByClassName("yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup pl-video-edit-remove yt-uix-tooltip");

function deleteWL(i){
    setInterval(function(){
        items[i].click();
    },500);
}

for(var i = 0; i < 1; ++i)
    deleteWL(i);

// From this YouTube video: https://www.youtube.com/watch?v=1RPzeFAHQpQ