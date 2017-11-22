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
        os.system('python *.py')
    elif ans == 'i':
        os.system('python *.py')
    elif ans == 'j':
        os.system('python *.py')
    elif ans == 'k':
        os.system('python *.py')
    elif ans == 'l':
        os.system('python *.py')
    elif ans == 'm':
        os.system('python *.py')
    elif ans == 'n':
        os.system('python *.py')
    elif ans == 'o':
        os.system('python *.py')
    elif ans == 'p':
        os.system('python *.py')
    elif ans == 'q':
        os.system('python *.py')
    elif ans == 'r':
        os.system('python *.py')
    elif ans == 'c':
        os.system('python *.py')
    elif ans == 'd':
        os.system('python *.py')


    elif ans == '4':
      os.system('python histogram.py')
