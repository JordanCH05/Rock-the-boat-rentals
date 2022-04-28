document.addEventListener('DOMContentLoaded', starRating);

$("#id_score")[0].addEventListener('input', starRating);

function starRating() {
    var score_input = $("#id_score")[0].value;
    var stars = $('.stars-inner');
    var rating = (score_input / 5) * 100;
    var ratingRounded = `${Math.round
    ((rating) / 10) * 10}%`;
    stars[0].style.width = ratingRounded;
}