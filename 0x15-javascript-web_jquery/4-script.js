/* script that toggles the class of the HTML tag HEADER when the user clicks on the tag DIV#toggle_header */

const $ = window.$;

$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('HEADER').toggleClass('red green');
  });
});
