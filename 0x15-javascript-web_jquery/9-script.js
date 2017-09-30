/* 9-script.js */
const $ = window.$;
const url = "https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%\
20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.p\
laces(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json"
$.get(url, function (data) {
  let wind = data.query.results.channel.wind;
  $('DIV#sf_wind_speed').text(wind.speed);
});
