void MainWindow::on_Constrate_valueChanged(double value) {
  output = cvLoadImage(fn.toStdString().c_str());
  contraste = (float) value;
  switch (contraste_select) {
  case CONTRASTE_ALL:
    foreachpixel(output, contraste_pixel, contraste_pixel, contraste_pixel);

    break;
  case CONTRASTE_RED:
    foreachpixel(output, nothing, nothing, contraste_pixel);
    break;
  case CONTRASTE_BLUE:
    foreachpixel(output, nothing, contraste_pixel, nothing);
    break;
  case CONTRASTE_GREEN:
    foreachpixel(output, contraste_pixel, nothing, nothing);
    break;
  }
  cvShowImage("OUTPUT", output);
}
Onde a função para modificar o contraste de cada pixel é:
  void * contraste_pixel(unsigned char * w) {
    float temp;
    temp = ( * w) * contraste;
    if (temp > 255) {
      temp = 255;
    }
    if (temp < 0) {
      temp = 0;
    } * w = (unsigned char) temp;
  }