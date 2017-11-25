void foreachpixel(IplImage * input, void * ( * red)(unsigned char * ), void * ( * green)(unsigned char * ), void * ( * blue)(unsigned char * )) {
  unsigned char * pixel;
  pixel = (unsigned char * ) input - > imageData;

  for (int i = 0; i < input - > width * input - > height * input - > nChannels; i += 3) {

    ( * red)(pixel);
    pixel += 3;
  }
  pixel = (unsigned char * ) input - > imageData + 1;
  for (int i = 0; i < input - > width * input - > height * input - > nChannels; i += 3) {

    ( * green)(pixel);
    pixel += 3;
  }

    pixel = (unsigned char * ) input - > imageData + 2;
  for (int i = 0; i < input - > width * input - > height * input - > nChannels; i += 3) {

    ( * blue)(pixel);
    pixel += 3;
  }
}