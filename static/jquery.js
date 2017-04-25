// A $( document ).ready() block.
$(document).ready(function () {

    $("li").click(function () {
        $(this).toggleClass("completed");
    });


});