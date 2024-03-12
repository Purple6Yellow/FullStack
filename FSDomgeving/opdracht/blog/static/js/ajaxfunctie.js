//Ajax functie - button "Haal pagina op"
// Verwijst naar BLog5.html 

$(document).ready(function () { 
   // alert("tot hier werkt het")
//$('#btnLoad').on('click', function () {   
    const urlPagina = '/JavaBlog/Blog5.html';
        $.ajax({
            url: urlPagina, 
            //success: function(data){
            success: function(){
                //console.log(controle);
                //Toon data in de div in de pagina
               // $('#divResult1').html(data);
                $('#divResult1').load('/JavaBlog/Blog5.html #Blog1');
                $('#divResult2').load('/JavaBlog/Blog5.html #Blog2');
                $('#divResult3').load('/JavaBlog/Blog5.html #Blog3');
            },
            error: function(){
                $('#divResult1').html('FOUT: Er is iets fout gegaan!');
            }
            //Overige configuratieparameters
        });
//});
});

