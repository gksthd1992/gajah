/*jslint browser: true, white: true, eqeq: true, plusplus: true, sloppy: true, vars: true*/
/*global $, console, alert, FormData, FileReader*/
src="http://code.jquery.com/jquery-latest.js"



var hw = document.getElementById('hw');
var input = document.getElementById('number');
/*
hw.addEventListener('click',function(){
    alert("aa");
    console.log("hi");
    // input.value
   $.post( "get_object_for_html.py", {
        data :input.value
    },
    function(data, status){
        console.log("success");
        //document.getElementById("output").value = data;
    })
*/
$(document).ready(function(){

hw.addEventListener('click',function(){
    send_data = input.value;
    console.log("the data is " + send_data);


    document.id.action="hello_world.py";
    document.id.submit();


/*
$.ajax({
     type: 'POST',
     url: "test.php?ver=1",
     //url: "get_object_for_html.py",
     data: {
					param1		: '10',
					param2		: send_data
				},
   //&a=xxx 식으로 뒤에 더 붙이면 됨
     //dataType: "text",
     error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
       },
     success : function(data) {
            alert("success!" + data);
        },
     complete : function() {
            alert("complete!");
        }
     });
     */
     });
});

