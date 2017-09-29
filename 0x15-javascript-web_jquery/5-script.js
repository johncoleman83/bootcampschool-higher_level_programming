/* 5-script.js */
let add_item = $('DIV#add_item');
add_item.on('click', function () {
  let my_list = $('UL.my_list');
  my_list.append('<li>Item</li>');
});
