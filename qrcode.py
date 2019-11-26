# words：字符串类型，链接或者句子作为参数，然后在程序的当前目录中产生相应的二维码图片文件

# version：整型，控制边长，范围是1至40，数字越大边长越大

# level：字符串类型，控制纠错水平，范围是L、M、Q、H，从左到右依次升高

# picture：字符串类型，图片链接，支持png、jpg、bmp、gif（用gif格式的话，生成的二维码就是动态的）

# colorized：布尔类型，True是彩色，False是黑白

# save_name：字符串类型，保存二维码图片的名字，需要写出图片类型。默认输出文件名是“ qrcode.png "，而默认存储位置是当前目录，重名会覆盖当前

# save_dir：字符串类型，保存二维码图片的路径

# constrast：浮点类型，调节生成图片的对比度，1.0表示与原图片一致，更小的值表示更低的对比度

# brightness：浮点类型，调节生成图片的亮度，用法与constrast一致

from MyQR import myqr
import os

#1、黑白、L，其他参数默认
version, level, qr_name = myqr.run(
    words='https://github.com/sylnsfar/qrcode/blob/master/README-cn.md' ,
    version=1,
    level='L',
    picture='.\img\panda.png',
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='1panda_noncolorized.png',
    save_dir=(os.getcwd()+'\img')
   )



#2、彩色、L，其他参数默认
version, level, qr_name = myqr.run(
    words='https://github.com/sylnsfar/qrcode/blob/master/README-cn.md' ,
    version=1,
    level='L',
    picture='.\img\panda.png',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='2panda_colorized.png',
    save_dir=(os.getcwd()+'\img')
   )

#3、彩色动图、L，其他参数默认
version, level, qr_name = myqr.run(
    words='https://github.com/sylnsfar/qrcode/blob/master/README-cn.md' ,
    version=1,
    level='L',
    picture='.\img\扭腰美女.gif',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='3panda_colorized.gif',
    save_dir=(os.getcwd()+'\img')
   )