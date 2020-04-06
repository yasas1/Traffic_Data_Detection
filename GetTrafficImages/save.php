<?php 


    $pic_name = filter_input(INPUT_POST, "pic_name");
    $data =filter_input(INPUT_POST, "base64data"); 

    $image = explode('base64',$data);

    file_put_contents('./images/'.$pic_name.'.png',base64_decode($image[1]));

    echo 'Saved';

?>
