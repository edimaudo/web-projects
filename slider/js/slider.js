// default start
sliderInt = 1;
sliderNext = 2;

$(document).ready(function() {
    $('#slider > img#1').fadeIn(300);
	startSlider();
});

//moves current to next
function startSlider(){
	count = $("#slider > img").size();

	loop = setInterval(function(){

		if (sliderNext > count){
				sliderNext = 1;
				sliderInt = 1;
			}

		$('#slider > img').fadeOut(300);
		$('#slider > img#' + sliderNext).fadeIn(300);

		sliderInt = sliderNext;
		sliderNext = sliderNext + 1;

		}, 3000)
}

//when button is clicked it moves to the previous image
function prev(){
	newSlide = sliderInt - 1;
	showSlide(newSlide);

}
//stops slider looping sequence
function stopLoop(){
	window.clearInterval(loop);
}

//When button is clicked it moves to the next image
function next(){
	newSlide = sliderInt + 1;
	showSlide(newSlide);
}

//
function showSlide(id){
		stopLoop();
		if (id > count){
			id = 1;
		}else if (id < 1) {
			id = count;
		};

		$('#slider > img').fadeOut(300);
		$('#slider > img#' + id).fadeIn(300);

		sliderInt = id;
		sliderNext = id + 1;
		startSlider();
}

$("#slider > img").hover(
	function(){
		stopLoop();
	},
	function(){
		startSlider();
	}
);


