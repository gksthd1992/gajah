<?php
//session_start();
//$data = $POST['data'];
//$tmp = exec("get_object_for_html.py .$data");
//echo $tmp
//echo "test<br>";
//exec("get_object_for_html.py");
$data = $_POST['data'];
//echo "hello";
$param2 = $_POST['param2'];
echo $param2;

$command = escapeshellcmd('get_object_for_html.py',escapeshellarg(json_encode($param2)));
$output = shell_exec($command);
//echo $output;
echo $data;

/*
$exec('python blibble.py',$output,$ret_code);
php->python and return 값 받기
*/
?>
