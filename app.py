
site = input('Введите url сайта: ')
maincolor = input('Введите основной цвет QR кода: ')
darkcolor = input('Введите темный цвет QR кода: ')
lightcolor = input('Введите светлый цвет QR кода: ')
filename = input('Введите название файла и в конце .png: ')
import segno

qrcode = segno.make(site, error='h')
img = qrcode.to_pil(scale=4, dark=maincolor, data_dark=darkcolor,
                   data_light=lightcolor)
img.save(filename)