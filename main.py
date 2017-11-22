'''
ANTES DE RODAR O PROGRAMA, PRECISAM SER INSTALADOS OS MÓDULOS:
Pillow	        4.3.0	4.3.0
PyWavelets	    0.5.2	0.5.2
cv2wrap	        1.0	1.0
cycler	        0.10.0
decorator	    4.1.2	4.1.2
matplotlib	    2.1.0	2.1.0rc1
networkx	    2.0	2.0
numpy	        1.13.3	1.13.3
olefile	        0.44	0.44
opencv-python	3.3.0.10	3.3.0.10
pip	9.0.1	    9.0.1
pyparsing	    2.2.0	2.2.0
python-dateutil	2.6.1	2.6.1
pytz	        2017.3	2017.3
scipy	        1.0.0	1.0.0rc2
setuptools	    28.8.0	37.0.0
six	            1.11.0	1.11.0
'''

import os

ans=True
while ans:
    print ('''
    0. Manipulação
        a. Histograma
        b. Equalização do Histograma
        c. Converter em Escala Cinza
        
    1. Operações
        d. Rotação (horário e anti-horário)
        e. Redimensionamento (escala)
        f. Espelhamento (vertical e horizontal)
        g. Negativo
        h. Brilho e contraste
        
    2. Passa Alta
        i. Sobel
        j. Prewitt
        k. Roberts
        l. Canny
        m. Laplaciano
        n. LoG
    
    3. Passa Baixa
        o. Média
        p. Mediana
        q. Gaussiano
        r. Moda
    
    4. Sair
    ''')

    ans=input('O que você quer fazer, Dani? ')
    if ans=='a':
        os.system('python histogram.py')
    elif ans == 'b':
        os.system('python hist_eq.py')
    elif ans == 'c':
        os.system('python convert_to_gray.py')
    elif ans == 'd':
        os.system('python rotacao.py')
    elif ans == 'e':
        os.system('python redimensionar.py')
    elif ans == 'f':
        os.system('python espelho_hor.py')
        os.system('python espelho_vert.py')
    elif ans == 'g':
        os.system('python negativo.py')
    elif ans == 'h':
        os.system('python brilho.py')
        os.system('python contraste.py')
    elif ans == 'i':
        os.system('python pa_sobel.py')
    elif ans == 'j':
        os.system('python pa_prewitt.py')
    elif ans == 'k':
        os.system('python pa_roberts.py')
    elif ans == 'l':
        os.system('python pa_canny.py')
    elif ans == 'm':
        os.system('python pa_laplacian.py')
    elif ans == 'n':
        os.system('python pa_log.py')
    elif ans == 'o':
        os.system('python pb_average.py')
    elif ans == 'p':
        os.system('python pb_median.py')
    elif ans == 'q':
        os.system('python pb_gaussian.py')
    elif ans == 'r':
        os.system('python pb_mode.py')
    elif ans == '4':
      exit()