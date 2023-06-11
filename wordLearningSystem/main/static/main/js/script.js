window.addEventListener('scroll', function() {
  var navbar = document.getElementById('navbar');
  var scrolled = window.scrollY > 0; // Перевірка, чи прокручено сторінку

  if (scrolled) {
    navbar.classList.add('scrolled'); // Додати клас, який встановлює напівпрозорий фон
  } else {
    navbar.classList.remove('scrolled'); // Видалити клас, який встановлює напівпрозорий фон
  }
});


// $(document).ready(function() {
//   $('#lets-go_btn').click(function() {
//     var windowHeight = $(window).height();
//     $('html, body').animate({scrollTop: '+=' + windowHeight}, 'slow');
//   });
// });