# from MyQR import myqr

# myqr.run(words='{"a":795,"c":60267}', save_name="1.jpg" )

# # ver,level,qr_name = myqr.run(words="{"a":795,"c":60267}",picture="2.jpg",colorized=False)

import qrcode
img = qrcode.make('{"a":795,"c":60267}')
img.save('qrcode.jpg')
#img.show()
