for x in xrange(xoffset,nw):
        for y in xrange(yoffset,nh):
            ox, oy = affine_t(x-cx, y-cy, *mrotate(-r, cx, cy))
            if ox > -1 and ox < ow and oy > -1 and oy < oh:
                pt = bilinear(bmp, ox, oy) if interpol else nn(bmp, ox, oy)
                draw.point([(x+mx,y+my),],fill=pt)