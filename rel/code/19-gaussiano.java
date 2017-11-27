private double getBlurColor(int x, int y,int whichColor){

    double blurGray = 0;
    double[][] colorMat = getColorMatrix(x,y,whichColor);

    int length = blurRadius*2+1;
    for (int i = 0;i<length;i++){
        for (int j=0; j<length; j++ ){
            blurGray += weightArr[i][j]*colorMat[i][j];
        }
    }

    return blurGray;
}