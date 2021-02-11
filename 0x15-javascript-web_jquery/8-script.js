/* script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */

const $ = window.$;

$(document).ready(function () {
  $(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      $.each(data.results, function (index, movie) {
        $('UL#list_movies').append($('<li></li>').text(movie.title));
      });
    });
  });
});
