<?php 
	/*$host = "localhost";
    $user = "root";
    $db = "jbs";*/

    $host = "localhost";
    $user = "root";
    $db = "traffic";
    // connect database
    $con=mysqli_connect($host,$user,'root',$db);
	if($con)
		echo "Connection is successful )";
	else
		echo "Connection Error ";
?>
