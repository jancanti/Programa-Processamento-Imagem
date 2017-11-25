 void SwapChar(unsigned char * A, unsigned char * B, int number) {
   unsigned char * C;
   C = (unsigned char * ) calloc(number, sizeof(unsigned char));
   memcpy(C, A, sizeof(unsigned char) * number);
   memcpy(A, B, sizeof(unsigned char) * number);
   memcpy(B, C, sizeof(unsigned char) * number);
   free(C);
 }

 for (column = 0; column < width / 2; column++) {
   destPointer = data + lineSize * line + (column) * channels;
   sourcePointer = data + lineSize * line + (width - column) * channels;
   SwapChar(destPointer, sourcePointer, channels);
 }