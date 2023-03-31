import cv2 as cv
import numpy as np
from PIL import Image
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw

def agreement_generator(info):
    agreement = list()

    path = Path(__file__).parent.absolute()


    agreement_template_path = f"{path}/blank_template/1.jpg"
    agreement_template_path2 = f"{path}/blank_template/2.jpg"
    font_path = f"{path}/font/Calibri/Calibri.ttf"
        
    img = Image.open(agreement_template_path)
    img2 = Image.open(agreement_template_path2)



    object = ImageDraw.Draw(img)
    object2 = ImageDraw.Draw(img2)

    font = ImageFont.truetype(font_path, 30)


    object2.text((800,660), str(info.get("uname")), font=font, fill=(0,0,0))
    object2.text((800,712), str(info.get("nid")), font=font, fill=(0,0,0))
    object2.text((800,765), str(info.get("present_address")), font=font, fill=(0,0,0))
    object2.text((800,845), str(info.get("phone")), font=font, fill=(0,0,0))
    object2.text((800,900), str(info.get("email")), font=font, fill=(0,0,0))
    object2.text((800,950), str(info.get("dob")), font=font, fill=(0,0,0))
    object2.text((800,1005), str(info.get("education_degree")), font=font, fill=(0,0,0))
    object2.text((570,1137), str(info.get("uname")), font=font, fill=(0,0,0))
    object2.text((415,1242), str(info.get("uname")), font=font, fill=(0,0,0))
    object2.text((1085,1242), str(info.get("nid")), font=font, fill=(0,0,0))

    object.text((315,1883), str(info.get("uname")), font=font, fill=(0,0,0))
    # object.text((760,2040), "999999999999", font=font, fill=(0,0,0))
    # object.text((1220,2040), "999999999999", font=font, fill=(0,0,0))


    img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    img2 = cv.cvtColor(np.array(img2), cv.COLOR_RGB2BGR)


    agreement.append(img2)
    agreement.append(img)

    return agreement







