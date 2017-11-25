void calcula_histograma(IplImage * img) {
  for (int i = 0; i < 256; i++) {
    histograma[i] = 0;
  }
  histMax = 0;
  foreachpixel(img, calc_hist, nothing, nothing);
}

void * calc_hist(unsigned char * w) {
  temp[ * w]++;
  if (temp[ * w] > histMax) {
    histMax = temp[ * w];
  }
}

IplImage * desenha_histograma(int HISTSIZE) {
  int HISTOFFSET;
  HISTOFFSET = HISTSIZE / 256;
  IplImage * ret;
  float a, b, c;
  b = histMax;
  int DrawHist[256];

  for (int i = 0; i < 256; i++) {
    a = (float) histograma[i];
    c = a / b;
    DrawHist[i] = (int)(c * HISTSIZE);
  }
  ret = cvCreateImage(cvSize(HISTSIZE, HISTSIZE), IPL_DEPTH_8U, 3);
  for (int i = 0; i < 256; i++) {
    cvRectangle(ret, cvPoint(i * HISTOFFSET + 1, HISTSIZE - DrawHist[i]), cvPoint(i * HISTOFFSET + HISTOFFSET, HISTSIZE), cvScalar(255, 127, 127), CV_FILLED);
  }
  return ret;
}