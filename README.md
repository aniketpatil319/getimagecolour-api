 <h1 align="center"> getimagecolour-api </h1>
getimagecolour-api allows a client to send an image and required co-ordinates to retrieve the colour name of that pixel.

### Used Packages:
- Flask
- Numpy
- Urllib3
- Base64
- PIL
- IO
- Webcolors

### What does the API do?
getimagecolour-api allows a client to send an image and required co-ordinates to retrieve the colour name of that pixel. 

### What to send? (Request)
#### POST JSON File:
- height
- width
- image   -> must be in base64-URLencoded format. 

### What is the response? (Response)
The response is a string; now it is either the <b>colour name [200 OK]</b> or if the co-ordinates of the requested pixel are incorrect then <b>error in pixel value entered[400 BAD REQUEST]</b> string will be sent. 

### Link to the API: 
[POST] https://getimagecolour-api.herokuapp.com/
