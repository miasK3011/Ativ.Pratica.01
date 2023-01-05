from PIL import Image
from Histograma import *
import sys

def loadImage(path):
    try:
        img = Image.open(path)

        print('-----------------------------------------\nImagem carregada!!')
        return img
    except:
        print(f'Endereço ou arquivo inválido!')
        sys.exit(1)

def main(argv):
    
    img = loadImage(argv)
    matrix = img.load()
    x, y = img.size[0], img.size[1]
    
    print('Processando...\n-----------------------------------------')
    h = Histograma(matrix, x, y)
    h.run()
    
    #img_normalizada = h.create_image()
    #img_normalizada.save('Out/Lena-Normalizado.jpeg')

     
if __name__ == '__main__':
    main(sys.argv[1])