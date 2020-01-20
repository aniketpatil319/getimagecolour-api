from flask import Flask,request,jsonify
import numpy as np
import urllib.parse,base64
from PIL import Image
import io,webcolors

app = Flask(__name__)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name



@app.route('/',methods=['POST'])
def color_detection_center():
    data = request.get_json()
    image_urlencoded = data['image']
    image_base64 = urllib.parse.unquote(image_urlencoded)
    image_not_in_format = base64.b64decode(image_base64)
    image_in_format = Image.open(io.BytesIO(image_not_in_format))
    a = np.array(image_in_format)
    center_x = data['height']
    center_y = data['width']
    print(a.shape)
    if center_x > a.shape[0] and center_y > a.shape[1]:
        return 'Error in pixel value entered',400
    else:
        requested_colour = a[center_x][center_y]
        actual_name, closest_name = get_colour_name(requested_colour)

        #print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
        return closest_name,200
    
    
if __name__ == '__main__':
    app.run(debug=True)
