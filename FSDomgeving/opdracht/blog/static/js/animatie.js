
$(document).ready(function () { 
// Animation
    $("#BtnAnimatie").on('click', function(){
        var div = $('#divResult1');

        div.animate({opacity: '0.4'}, "slow");
        div.animate({width: '30%', opacity: '0.8'}, "slow");
        div.animate({opacity: '0.4'}, "slow");
        div.animate({width: '80%', opacity: '1.0'}, "slow");      
    });
});


  

