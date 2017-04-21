$(document).ready(function () {
    $('#post-form').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!"); // sanity check
    });
});