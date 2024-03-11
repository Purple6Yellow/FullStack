
$(document).ready(function () { 
    alert("Animatie.js geactiveerd")
// Datum priker - plugin
    console.log("tot hier gaat het goed")

    $('#datepicker').datepicker(
        $.datepicker.regional['nl']
    );
// Blog toevoegen
    $("#BtnBlogToevgn").on('click', function URL(){
    
        location.href="/JavaBlog/BlogInvullen.html";
    });
// Animation
    $("#BtnAnimatie").on('click', function(){
        var div = $('#divResult1');

        div.animate({opacity: '0.4'}, "slow");
        div.animate({width: '30%', opacity: '0.8'}, "slow");
        div.animate({opacity: '0.4'}, "slow");
        div.animate({width: '80%', opacity: '1.0'}, "slow");      
    });

});


  

