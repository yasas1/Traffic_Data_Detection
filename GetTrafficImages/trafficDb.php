<?php 

require "dbcon.php";

$pic_name = filter_input(INPUT_POST, "pic_name");
$date =filter_input(INPUT_POST, "date"); //$_POST['date'];
$day =(int)filter_input(INPUT_POST, "day");
$time = filter_input(INPUT_POST, "time");
$temperature =(float) filter_input(INPUT_POST, "temperature");
$humidity =(float)filter_input(INPUT_POST, "humidity");
$weather_summary = filter_input(INPUT_POST, "weather_summary");

$query="insert into traffic(pic_name,date,day,time,temperature,humidity,weather_summary) values('$pic_name','$date',$day,'$time',$temperature,$humidity,'$weather_summary')  ";

$row=mysqli_query($con, $query);
if($row==1){
    echo "Traffic Entered";

            
}else{
    echo "ERROR";
}

?>

