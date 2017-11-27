void MainWindow::on_brilho_BW_sliderMoved(int position) {

  brilho = position - brilho_anterior[0];
  brilho_anterior[0] = position;
  foreachpixel(output, brilho_pixel, brilho_pixel, brilho_pixel);
  cvShowImage("OUTPUT", output);
}

void MainWindow::on_brilho_R_sliderMoved(int position) {
  brilho = position - brilho_anterior[1];
  brilho_anterior[1] = position;
  foreachpixel(output, nothing, nothing, brilho_pixel);
  cvShowImage("OUTPUT", output);
}

  void * brilho_pixel(unsigned char * w) {
    int temp;
    temp = * w + brilho;
    if (temp > 255) {
      temp = 255;
    }
    if (temp < 0) {
      temp = 0;
    } * w = (unsigned char) temp;
  }