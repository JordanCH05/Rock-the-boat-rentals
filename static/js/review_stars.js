var stars = $('.stars-inner');
    for (i = 0; i < stars.length; i++) {
        var classList = stars[i].classList;
        var wClass = classList[1];
        var percent = wClass.split("-")[1];
        stars[i].style.width = `${percent}%`;
    }