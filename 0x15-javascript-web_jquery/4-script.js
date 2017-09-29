/* 4-script.js */
let toggle = $('DIV#toggle_header');
toggle.on('click', function () {
  let header = $('header');
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
