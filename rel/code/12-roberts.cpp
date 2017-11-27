for (int i = 0; i < (height-roberts.size+1)*(width-roberts.size+1)*4; i++) {
    imga[i] = 0;
}

infoheader.biHeight = height - roberts.size + 1;
infoheader.biWidth = width - roberts.size + 1;

picsize = (height-roberts.size+1)*(width-roberts.size+1);


cur_idx = bitmap.plot(blue_img, roberts);

for (int i = 0; i < picsize; i++) {
    tpp = *cur_idx;
    imga[i*4] = (int) tpp;
    cur_idx++;
}