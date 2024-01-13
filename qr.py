import segno

qrcode = segno.make('youtube.com', error='h')

qrcode.save('qrcode.png')