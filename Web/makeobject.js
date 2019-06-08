/*jslint browser: true, white: true, eqeq: true, plusplus: true, sloppy: true, vars: true*/
/*global $, console, alert, FormData, FileReader*/
src="http://code.jquery.com/jquery-latest.js"

var input = document.getElementById('number');
var hw = document.getElementById('makeob');
var click = 0;

var ob_name = new Array();
ob_name[0] = "input/ret0.jpg";
ob_name[1] = "input/ret1.jpg";
ob_name[2] = "input/ret2.jpg";
ob_name[3] = "input/ret3.jpg";
ob_name[4] = "input/ret4.jpg";
ob_name[5] = "input/ret5.jpg";
ob_name[6] = "input/ret6.jpg";
ob_name[7] = "input/ret7.jpg";

$(document).ready(function(){
makeob.addEventListener('click',function(){

    $.ajax({
     type: 'POST',
     url: "show_ob.py?ver=1",
     data : "",
     error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
       },
     success : function(data){
        if(click==0){
            for(var a=1; a<Number(data)+1; a++){
             $('<img>', {
                src: ob_name[a],
                alt: a,
                title: ob_name[a],
                click: function(){
                    alert($(this).attr('title'));
                }
                }).css({
                cursor: 'pointer',
                border: '1px solid black',
                width: '100',
                height: '150',
                padding: '5px 5px 5px 5px',
                backgroundColor: 'white'
                }).appendTo('body');
            }
            click=1;
        }
        },
     complete : function() {
            //alert("complete!");

        }
     });

     alert(data);


     });
});
