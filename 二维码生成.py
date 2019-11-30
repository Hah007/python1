# import pyqrcode

# import sys

# number = pyqrcode.create(‘从Scratch到Python——Python生成二维码’,encoding=’utf8′)

# number.save(‘.\a.png’,50)

import qrcode
import os
 
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data('https://www.yuque.com/hehao-b1fmd/gw971k/chrh36')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.show()

img.save(os.getcwd() + '/' + 'qrcodename .png', quality=100)