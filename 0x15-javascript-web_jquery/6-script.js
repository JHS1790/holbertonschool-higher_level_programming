/* script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header */

const $ = window.$;

$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
});
