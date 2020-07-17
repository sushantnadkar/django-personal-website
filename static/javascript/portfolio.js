(function($) {

    // Remove no-js class
    $('html').removeClass('no-js');

    // Scroll to top
    $('.js-to-top').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 500);
    });

    // Scroll to first element
    $('.js-lead-down').click(function() {
        var scrollDistance = $('#lead').next().offset().top;
        $('html, body').animate({
            scrollTop: scrollDistance + 'px'
        }, 500);
    });

    $('.js-scroll-to').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    // Load additional projects
    $('.js-view-more-projects').click(function(e) {
        e.preventDefault();
        $(this).fadeOut(300, function() {
            $('#more-projects').fadeIn(300);
            $('.js-view-less-projects').fadeIn(300);
        });
    });

    // Hide additional projects
    $('.js-view-less-projects').click(function(e) {
        e.preventDefault();
        $(this).fadeIn(300, function() {
            $('#more-projects').fadeOut(300);
            $('.js-view-more-projects').fadeIn(300);
            // adjust scroll after hidding #more-projects
            // substract 100 so that ".js-view-more-projects" is not hidden behind navbar
            let scrollDistance = $(".js-view-more-projects").offset().top - 100;
            $('html, body').animate({
                scrollTop: scrollDistance + 'px'
            }, 500);
        });
    });

    // Remove messages after displaying for specified time
    setTimeout(function() {
        $(".msg").fadeOut(500);
    }, 3000);

})(jQuery);