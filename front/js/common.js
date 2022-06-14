$(document).ready(function(){

	// $.ajax({
	// 	url: "getRequest.php",
	// 	success: function(data){
	// 	  console.log(data);
	// 	}
	//   });  

    $('.owl-carousel').owlCarousel({
		items: 4,
		autoplay: true,
		loop: true,
		autoplayTimeout: 4000,
		smartSpeed: 1500,
		dots: false
	});

  });