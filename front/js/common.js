$(document).ready(function(){

	var input_form = document.querySelector('.link-form');
	
	$(input_form).submit(function(){
		$.ajax({
			type: 'POST',
			url: '1.php',
			dataType: 'json',
			data: data,
			success: function(data) {
				
			}
		});
	});

    $('.owl-carousel').owlCarousel({
		items: 4,
		autoplay: true,
		loop: true,
		autoplayTimeout: 4000,
		smartSpeed: 1500,
		dots: false
	});

  });