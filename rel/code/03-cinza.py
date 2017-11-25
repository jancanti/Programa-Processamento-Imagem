for i in range(img.width):
    for j in range(img.height):
        pix = image.Pix(img.getPixel(i, j))
        lum = int(pix[0]*0.3 + pix[1]*0.59 + pix[2]*0.11)

        img.setPixel(i, j, image.Pix((lum, lum, lum)))