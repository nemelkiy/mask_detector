$(document).ready(function(){

	var input_form = document.querySelector('.link-form');

	$(input_form).submit(function(e){

		var user_id = document.querySelector('.form_submit').getAttribute('user_id');
		
		$.ajax({
			type: "POST",
			url: "ajaxSendRequest.php",
			data: $(this).serialize(),
			success: function(data) {

				console.log(data);
				if(data == 'sanded'){

					$('.overlay').fadeIn(250);

					setTimeout(function(){

						var loaderText = document.querySelector('.loader-text');

						loaderText.innerHTML = 'Видео обрабатывается';
						$.ajax({
							type: "POST",
							url: "ajaxGetRequest.php",
							data: "user_id="+user_id,
							success: function(msg){
								console.log(msg);
							}
						})
					  }, 10000);

				}else{
					console.log('Thomething wrong');
				}
			}
		  });

		e.preventDefault();
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