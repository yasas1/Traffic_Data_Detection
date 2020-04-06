<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Take Traffic Screenshots </title>

 
    <script src="js/html2canvas.js"></script>

    <script  src="https://code.jquery.com/jquery-3.2.1.min.js"  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="  crossorigin="anonymous"></script>

    <script src="js/jquery.min.js"></script> 
    

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <style>
        #map{
            height: 500px;
            width: 1100px;
            margin: 10 auto;
            
        }
    </style>

    <style>
        
        #map {
        height: 100%;
        
        }
        #map1 {
            position: absolute;
            left: 10%; top:50px; margin: 5 5 5 -20%;
        }
       
        html, body {
        height: 100%;
        margin: 0;
        padding: 0;
        }
    </style>

</head>
<body>

    <a href="" id="blank" name=""></a>
    <div class="box box-primary">
        
        <div id="map1" class="box-body" style=" height:650px; overflow: auto;" >
            
             <div id="map"> </div>
            
        </div>
               
    </div>
</body>
</html>

<script>

    var zm = 15.5;

    var latitude =  6.8889298;
    var longitude =  79.8710876;

    var caption;
    var date;
    var time; 
    var day;
    var wSummary;
    var temperature;
    var humidity;

    var count = 0;        
    function getScreen(){

        var today = new Date();

        date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        time = today.getHours() + ":" + today.getMinutes();
	timeN = today.getHours() + "-" + today.getMinutes();

        day = today.getDay();

        count++;

        caption ="t"+count+"_"+date+"_"+timeN;   
        $("#caption-text").html(caption);

        
        html2canvas(document.getElementById("map"), {
            useCORS: true,
            dpi: 192,
            onrendered: function(canvas) {
                var imgData = canvas.toDataURL("image/png");
                $.ajax({
                    url:'save.php',
                    type:'post',
                    dataType:'text',
                    data:{base64data:imgData,pic_name:caption},
                    success: function(data){ console.log(data); }
                });
            }
        });

        getWeather();

        setTimeout(trafficDb, 5000);


    }

    
    function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: zm,
            center: {lat: latitude, lng: longitude}, 
            styles: [
                {
                    "featureType": "all",
                    "elementType": "all",
                    "stylers": [
                        { "visibility": "off" }
                    ]
                },
            
            ],
            disableDefaultUI: false,
            mapTypeControl: false,
            scaleControl: false,
            zoomControl: false,
            streetViewControl: false,
            fullscreenControl: false,
        });

        var trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(map);
    }

    function getImage(){
        initMap();
        setTimeout(getScreen, 5000); //waiting to load the map
    }

    function start(){
        
        window.setInterval(getImage, 300000,); //frequency
        
    }

    setTimeout(getScreen, 4000);
    start();

    function trafficDb(){

        $.ajax({
            url: "trafficDb.php",
            type: 'POST',
            data: { pic_name:caption,date:date,day:day,time:time,temperature:temperature,humidity:humidity,weather_summary:wSummary },
            success: function(data)
            {
                console.log(data);
                
            },	
	    error: function(req, err){ console.log('my message' + err); }
        });

    }


    function getWeather(){
        
        var proxy = 'https://cors-anywhere.herokuapp.com/'; //'http://localhost:8080/Traffic/Traffic.php/';
        var dsAPI = "https://api.darksky.net/forecast/";
        var dsKey = "b84697772dd55fe27338da5ffcd82592/";
        var dsParams = "?exclude=minutely,hourly,daily,alerts,flags&units=auto";
        
        var URLRequest = proxy + dsAPI + dsKey + String(latitude) + "," + String(longitude) + dsParams ;
        
        $.getJSON( URLRequest )

            .done(function( data ) {
            wSummary = data.currently.summary;
            temperature = data.currently.temperature;
            humidity = data.currently.humidity;

            console.log(wSummary);
            console.log(temperature);
            console.log(humidity);

            })
            
            .fail(function() {
            	console.log('Sorry, something bad happened when retrieving the weather');
            }
        );
    }   

</script>

<script async defer
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDccLlV_rbSEOElJchCKxcP8ayVoatGNFc&libraries=places&callback=initMap">
</script>
