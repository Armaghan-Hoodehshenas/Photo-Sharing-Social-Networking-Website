(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://winki.com:8000/site_statics/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();
