/* script that updates the text color of the HTML tag HEADER to red (#FF0000) when user click on DIV#red_header */

const $ = window.$;

$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').css({ color: '#FF0000' });
  });
});
