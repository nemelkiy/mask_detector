$(document).ready(function(){

	var input_form = document.querySelector('.link-form');

	$(input_form).submit(function(e){

		var user_id = document.querySelector('.form_submit').getAttribute('user_id');
		var block_id = Math.floor(Math.random() * 900);
		var loaderText = document.querySelector('.loader-text');

		$.ajax({
			type: "POST",
			url: "ajaxSendRequest.php",
			data: $(this).serialize(),
			success: function(data) {

				console.log(data);
				if(data == 'sended'){

					$('.overlay').fadeIn(250);

					setTimeout(function(){

						//var loaderText = document.querySelector('.loader-text');
						
						loaderText.innerHTML = 'Видео обрабатывается';
						$.ajax({
							type: "POST",
							url: "ajaxGetRequest.php",
							data: "user_id="+user_id+"&block_id="+block_id,
							success: function(msg){
								
								
							}
						})
					}, 10000);

					setTimeout(function(){
						
						setTimeout(function(){
							$('.loader').fadeOut(250);
						}, 350);

						$('.success_checkmark').fadeIn(250);
						
						loaderText.innerHTML = 'Видео всё еще обрабатывается.<br>Результату присвоен номер: '+block_id+' <br> Но вы уже можете увидеть <a class="result_btn" href="result_list.php?user_id='+user_id+'&block_id='+block_id+'">Результат</a>';

						setTimeout(function(){
							$('.overlay').fadeOut(250);
						}, 8000);
					}, 20000);

				}else{
					console.log('Something wrong');
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