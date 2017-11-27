public class pdi {
 public static void main(String args[] ) throws IOException{
   BufferedImage imagem = null;
   imagem = ImageIO.read(
    new File("C:\\Users\\ufc\\workspace\\PDI\\src\\tux.png")
   );
  
   int w = imagem.getWidth();
   int h = imagem.getHeight();
   //retorna um vetor inteiro representando os pixels da imagem
   int pixels[] = imagem.getRGB(0, 0, w, h, null, 0, w);

   for (int col = 0; col < w; col++) {
     for (int lin = 0; lin < h; lin++) {
  //Pega a cor em cada pixel
  Color c = new Color(pixels[lin*w + col]);
  pixels[lin*w + col] = new 
  Color(255-c.getRed(),255-c.getBlue(),255-c.getGreen()).getRGB();
      }
 }
        //seta um vetor inteiro representando os pixels da imagem
 imagem.setRGB(0, 0, w, h, pixels, 0, w);
 ImageIO.write(imagem, "PNG", 
        new File("C:\\Users\\ufc\\workspace\\PDI\\src\\tux2.png"));
 }
}