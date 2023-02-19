$(document).ready(function () {

    // toggle mobile menu
    $('[data-toggle="toggle-nav"]').on('click', function () {
        $(this).closest('nav').find($(this).attr('data-target')).toggleClass('hidden');
        return false;
    });

    // feather icons
    feather.replace();

    // smooth scroll
    var scroll = new SmoothScroll('a[href*="#"]');

    // tiny slider
    $('#slider-1').slick({
        infinite: true,
        prevArrow: $('.prev'),
        nextArrow: $('.next'),
    });

    $('#slider-2').slick({
        dots: true,
        arrows: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        centerMode: true,
        customPaging: function (slider, i) {
            return '<div class="bg-white br-round w-1 h-1 opacity-50 mt-5" id=' + i + '> </div>'
        },
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 1
            }
        }, ]
    });

    $("#team1").mouseover(function (e) {    
        $(this).find("img").attr("src","/static/images/bharani.jpg");
    });
    $("#team1").mouseout(function (e) {    
        $(this).find("img").attr("src","/static/images/bharanibw.jpg");
    });

    $("#team2").mouseover(function (e) {    
        $(this).find("img").attr("src","/static/images/dharsana.jpg");
    });
    $("#team2").mouseout(function (e) {    
        $(this).find("img").attr("src","/static/images/dharsanabw.jpg");
    });

    $("#team3").mouseover(function (e) {    
        $(this).find("img").attr("src","/static/images/chinny.jpg");
    });
    $("#team3").mouseout(function (e) {    
        $(this).find("img").attr("src","/static/images/chinnybw.jpg");
    });
    
});
