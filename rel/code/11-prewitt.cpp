for (int i = 0; i < (height-prewitt.size+1)*(width-prewitt.size+1)*4; i++) {
    imgb[i] = 0;
}

infoheader.biHeight = height - prewitt.size + 1;
infoheader.biWidth = width - prewitt.size + 1;

picsize = (height-prewitt.size+1)*(width-prewitt.size+1);


cur_idx = bitmap.plot(blue_img, prewitt);

for (int i = 0; i < picsize; i++) {

    tpp = *cur_idx;
    imgb[i*4] = tpp;
    cur_idx++;

}