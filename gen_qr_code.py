import qrcode

def gen_qrcode(link):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 4,
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "blue", black_color = "orange")
    img.save("qrimg.png")

gen_qrcode("")

