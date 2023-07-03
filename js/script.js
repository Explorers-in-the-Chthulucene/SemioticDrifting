(function($) {

  "use strict";

  // init Chocolat light box
  var initChocolat = function() {
    Chocolat(document.querySelectorAll('.image-link'), {
      imageSize: 'contain',
      loop: true,
    })
  }

  var initCharts = function() {

    if ($(".chart")[0]){
    
      var barColors = [
        "#F4BE37",
        "#E2EAF1"
      ];

      new Chart("orphans", {
        type: "doughnut",
        data: {
          labels: ['Needs Help','Priviledged'],
          datasets: [{
            backgroundColor: barColors,
            data: [65, 49]
          }]
        },
        options: {
          plugins: {
            legend: false,
            tooltip: false,
          },
          title: {
            display: false,
            text: "World Orphans 2018"
          }
        }
      });

      new Chart("labor", {
        type: "doughnut",
        data: {
          labels: ['Needs Help','Priviledged'],
          datasets: [{
            backgroundColor: barColors,
            data: [35, 65]
          }]
        },
        options: {
          plugins: {
            legend: false,
            tooltip: false,
          },
          title: {
            display: false,
            text: "World Children Labor 2018"
          }
        }
      });

      new Chart("education", {
        type: "doughnut",
        data: {
          labels: ['Needs Help','Priviledged'],
          datasets: [{
            backgroundColor: barColors,
            data: [75, 35]
          }]
        },
        options: {
          plugins: {
            legend: false,
            tooltip: false,
          },
          title: {
            display: false,
            text: "World Children Education 2022"
          }
        }
      });

      new Chart("health", {
        type: "doughnut",
        data: {
          labels: ['Needs Help','Priviledged'],
          datasets: [{
            backgroundColor: barColors,
            data: [85, 25]
          }]
        },
        options: {
          plugins: {
            legend: false,
            tooltip: false,
          },
          title: {
            display: false,
            text: "World Children Health 2022"
          }
        }
      });
    }
  }

  // init jarallax parallax
  var initJarallax = function() {
    jarallax(document.querySelectorAll(".jarallax"));

    jarallax(document.querySelectorAll(".jarallax-keep-img"), {
      keepImg: true,
    });
  }

  var initScrollNav = function() {
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();

        if (scroll >= 200) {
          $('.site-header').addClass("bg-dark");
        }else{
          $('.site-header').removeClass("bg-dark");
        }
    }); 
  }

  $(document).ready(function () {

    // preloader
    $(window).load(function() {
      $("#overlayer").fadeOut("slow");
      $('body').addClass('loaded');
    })

    initScrollNav();
    initChocolat();
    initCharts();
    initJarallax();

    // Animate on Scroll
    AOS.init({
      duration: 600,
      once: true,
    })
  });


})(jQuery);
