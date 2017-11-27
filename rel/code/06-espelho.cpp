        for (line = 0;line < height+gamb/*+1*/ ; line++)
                {//swap height -line with line
                linePt[line] = data;
                data += channels*width;
                buffer =          linePt[line];
 
                }
 
        for (line = 0;line < height/2/*-1*/; line++) //paralelizar ?
                {
 
                memcpy(buffer,linePt[line],sizeof(unsigned char)*width*channels);
 
                memcpy(linePt[line],linePt[height -line-1],sizeof(unsigned char)*width*channels);
 
                memcpy(linePt[height - line-1 ],buffer,sizeof(unsigned char)*width*channels);
                }
 