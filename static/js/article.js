// chatjs.js
const basicAutocomplete = document.querySelector('#search-autocomplete');
const data = ['One', 'Two', 'Three', 'Four', 'Five'];
const dataFilter = (value) => {
  return data.filter((item) => {
    return item.toLowerCase().startsWith(value.toLowerCase());
  });
};

// new mdb.Autocomplete(basicAutocomplete, {
//   filter: dataFilter
// });

$('#recipeCarousel').carousel({
  interval: 10000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    
    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
        	next = $(this).siblings(':first');
      	}
        
        next.children(':first-child').clone().appendTo($(this));
      }
});

// $(document).ready(function(){
//   $('#question_post').on('submit',function(e){
//   e.preventDefault();
//   console.log('hi di');
//   $.ajax({
//       type:'POST',
//       url:'/article',
//       dataType: "json",
//       data:
//       {
//           question_title:$('#question_title').val(),
//           question_body:$('#question_body').val(),
//           csrfmiddlewaretoken:"{{csrf_token}}",
//       },
//       success: function(response){
//           alert('hello');
//       },
//   });
// });
// });
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}

// function myFunction() {
//   console.log('hi');
//   var divsToHide = document.getElementById("hide-content");
//   console.log(divsToHide.style.display);
//   divsToHide.style.display= "none";
//   // if( divsToHide.style.display== "none"){
//   //   divsToHide.style.display = "block";
//   // }
//   // else{
//   //   divsToHide.style.display = "none";
//   // }    
// }