$(document).ready(function() {

    $('#main-menu li').mouseover(function() {
        let description = $(this).data('description');
        $('.action .description .wrapper').text(description);

        let number = $(this).data('number');
        $('.stetic-text .current-item .second .number').text(number);
    });
})