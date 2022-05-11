import qrcode
qr = qrcode.QRCode(version = 1, box_size = 10)

contenido = "Computadoras y Sensores Codigo QR"
qr.add_data(contenido)
qr.make(fit = True)

imagen = qr.make_image(fill = "black" , back_color = "white")
imagen.save("CodigoQR.png")
