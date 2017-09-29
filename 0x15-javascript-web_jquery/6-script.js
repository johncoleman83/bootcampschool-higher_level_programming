/* 6-script.js */
let updateHeader = $('DIV#update_header');
updateHeader.on('click', function () {
  let header = $('HEADER');
  header.replaceWith('<header>New Header!!!</header>');
});
