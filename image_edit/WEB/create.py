#!python

print("Content-Type: text/html")  
print() 
import cgi, os

form = cgi.FieldStorage()
#contentsName = form["text1"].value
#styleName = form["text2"].value
print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="How to create an image upload form without page refresh using Bootstrap, jQuery AJAX and PHP.">
    <meta name="author" content="ShinDarth">

    <title>GAJAH</title>

    <link rel="icon" href="11.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <style>body { padding-top:50px; }.navbar-inverse .navbar-nav > li > a { color: #DBE4E1; }</style>

    <!--[if IE]>
      <script src="https://cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">GAJAH</a>
        </div>

        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Mixing</a></li>
          </ul>
        </div><!--.nav-collapse -->
      </div>
    </nav>


    <div class="container">

      <!-- Featured Project Row -->
      <div class="row align-items-center no-gutters mb-4 mb-lg-5">
        <div class="mx-auto text-center">
          <img class="img-fluid mb-3 mb-lg-0" src="bg-masthead.jpg" alt="">
        </div>
        <div class="col-xl-4 col-lg-5">
          <div class="featured-text text-center text-lg-left">
            <h4></h4>
            
          </div>
        </div>
      </div>

      <!-- Header -->
   <header class="masthead">
    <div class="container d-flex h-100 align-items-center">
      <div class="mx-auto text-center">
        <h1 class="mx-auto my-0 text-uppercase"></h1>
        <h2>Image Transfer</h2>
        <h2></h2> Enjoy art however you want !</h2>
        <h2></h2> Capstone Design SW _2</h2>

      </div>
    </div>
   </header>



    <div class="container">

      <div style="max-width: 650px; margin: auto;">
        <h1 class="page-header">1.Image Upload</h1>
        <p class="lead">Select a PNG or JPEG image, having maximum size <span id="max-size"></span> KB.</p>

        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
            <input type="file" name="file" id="file" required>
          </div>
          <button class="btn btn-lg btn-primary" id="upload-button" type="submit" disabled>Upload</button>
        </form> 
  
        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <h1 class="page-header">2. Choose Art</h1>
          <p class="lead">GAJAH Art Default Image <span id="max-size"></span> <span id="max-size"></span></p>  
          <p class="lead"><span id="max-size"></span> <span id="max-size"></span></p> 
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
              <p class="lead">==(flower.jpg)=-=-=-=-=-=(amond.jpg)=-=-=-=-=-=(Stary-night.jpg)= <span id="max-size"></span></p>
              <input type="image" src ="./ben.jpg"  width="200" height="300" type= "summit" >
              <input type="image" src ="./amond.jpg" alt = "amond" width="200" height="300" type= "summit" >
              <input type="image" src ="./Ss.jpg" alt = "Stary-night" width="200" height="300" type= "summit" >
              <p class="lead">===================================================<span id="max-size"></span></p>
              

          </div>

    
        </form>

<!--
       <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
        <h1 class="page-header">GAJAH Art</h1>
        <p class="lead">2. Choose Art <span id="max-size"></span> <span id="max-size"></span></p>  
        <p class="lead">-기본제공 이미지- <span id="max-size"></span> <span id="max-size"></span></p> 
        <div id="image-preview-div" style="display: none">
          <label for="exampleInputFile">Selected image:</label>
          <br>
          <img id="preview-img" src="noimage">
        </div>
        <div class="form-group">
            
            <input type="image" src ="./ben.jpg" alt = "flower" width="200" height="300" type= "summit" >
            <input type="image" src ="./amond.jpg" alt = "amond" width="200" height="300" type= "summit" >
            <input type="image" src ="./Ss.jpg" alt = "Stary-night" width="200" height="300" type= "summit" >
            <input type="file" name="file" id="file" required>
        </div>
        <button class="btn btn-lg btn-primary" id="upload-button" type="submit" disabled>사진 보내기</button>

       </form>
      
  -->    


        <h1 class="page-header">GAJAH Mixing</h1>   
        <div class="form-group">
            <h1 class="lead">Contents Image: </h1>
            <input type="text1" name="ContentsImage" size="20">   # ex) myFace.jpg ...
            <h1 class="lead">Style Image:</h1>
            <input type="text2" name="StyleImage" size="20">   # ex) Stary-night.jpg ...
        </div>
        <p class="lead">  <span id="max-size"></span></p>
        <p class="lead">  <span id="max-size"></span></p>
        <p class="lead"> Are you sure? <span id="max-size"></span></p>
        <button class="btn btn-lg btn-primary" id="Mixing-button" type="submit" disabled>Mixing</button>
       
        <button class="btn btn-lg btn-primary" id="button1" onclick="button1_click();">MIXING</button>
        <script>
        function button1_click() {
          alert("버튼1을 누르셨습니다.");
        }
        </script>
       
       <br>
        <div class="alert alert-info" id="loading" style="display: none;" role="alert">
          Uploading image...
          <div class="progress">
            <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
            </div>
          </div>
        </div>
        <div id="message"></div>
      </div>
    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
  </body>

 <body>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">GAJAH</a>
        </div>

        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Mixing</a></li>
          </ul>
        </div><!--.nav-collapse -->
      </div>
    </nav>

 


</html>

''')  