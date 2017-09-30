/* 8-script.js */
const $ = window.$;
$.get('https://swapi.co/api/films/?format=json', function (data) {
  let results = data.results;
  for (let i in results) {
    $('UL#list_movies').append('<LI>' + results[i].title + '</LI>');
  }
  // $('UL#list_movies').text(data.name);
});
