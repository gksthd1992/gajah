/*jslint browser: true, white: true, eqeq: true, plusplus: true, sloppy: true, vars: true*/
/*global $, console, alert, FormData, FileReader*/
src="http://code.jquery.com/jquery-latest.js"

var enternum = document.getElementById('enternum');
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

enternum.addEventListener('click',function(){


    send_data = input.value;
    alert("the enter number is " + Number(send_data));
    var person = {"name":"Andrew", "loves":"Open Source"};
    var asJSON = JSON.stringify(person);
    console.log(`asJSON is of type ${typeof asJSON}`);
    // `person` is of type 'object'
    console.log(`person is of type ${typeof person}`);
    var asObject = JSON.parse(asJSON);
    console.log(`asObject is of type ${typeof asObject}`);

    $.ajax({
     type: 'POST',
     url: "enter_number.py?ver=1",
     //url: "get_object_for_html.py",
     type: "json",
     data: {
        json: asJSON
     },
     //data: send_data,
   //&a=xxx 식으로 뒤에 더 붙이면 됨
     //dataType: "text",
     error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
       },

     success : function(data) {
     alert(data);
        if(click==0){
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
                padding: '12px 12px 20px 12px',
                backgroundColor: 'white'
                }).appendTo('body');
            }
            click=1;
        }
        ,
     complete : function() {
            //alert("complete!");

        }
     });

     alert(data);


     });
});

