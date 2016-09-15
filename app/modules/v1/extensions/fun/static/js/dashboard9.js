$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 50
        }, 1000);
        return false;
      }
    }
  });
});

$(window).scroll(function() {
  var scrollPos = $(window).scrollTop(),
  whatPos = $('#whatIsResponsiveDesign').offset().top - 50,
  workPos = $('#portfolioSection').offset().top - 50,
  pricingPos = $('#pricing').offset().top - 50,
  contactPos = $('#contact').offset().top - 50;
  servicesPos = $('#services').offset().top - 50;

  if (scrollPos >= whatPos && scrollPos < workPos) {
    $('#whatLink').addClass('active');
  }
  else {
    $('#whatLink').removeClass('active');
  }

  if (scrollPos >= workPos && scrollPos < pricingPos) {
    $('#workLink').addClass('active');
  }
  else {
    $('#workLink').removeClass('active');
  }

  if (scrollPos >= pricingPos && scrollPos < servicesPos) {
    $('#pricingLink').addClass('active');
  }
  else {
    $('#pricingLink').removeClass('active');
  }

  if (scrollPos >= contactPos) {
    $('#contactLink').addClass('active');
  }
  else {
    $('#contactLink').removeClass('active');
  }

  if (scrollPos >= servicesPos && scrollPos < contactPos) {
    $('#servicesLink').addClass('active');
  }
  else {
    $('#servicesLink').removeClass('active');
  }

});
