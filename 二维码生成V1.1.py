
import qrcode
import os
 
 #定义生成二维码函数
def create_qr(self, url, qrcodename):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,  # pixel of each box
    border=1,  # round blocks
 
    )
 
    qr.add_data(url)
    qr.make(fit=True)
 
    img = qr.make_image()
    img = img.convert("1")
 
    img.show()
    img.save(os.getcwd() + '/' + qrcodename + '.png', quality=100)

#开始交互
qrcodename=input('请输入二维码文件名称：')

#调用函数实现
create_qr(1, 'https://www.yuque.com/hehao-b1fmd/gw971k/chrh36', 'qrcodename')