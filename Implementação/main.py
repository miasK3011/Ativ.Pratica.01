from PIL import Image
from Histograma import *
import sys

def loadImage(image):
    try:
        caminho = 'Image/'+image
        img = Image.open(caminho)
        
        print(f'-----------------------------------------\nImagem carregada!!- {caminho} ')
        return img
    except:
        print(f'Endereço ou arquivo inválido!')
        sys.exit(1)

def menu(option, h):
    if option == 1:
        h.show_histogram()
    elif option == 2:
        img_equalizada = h.equalizar()
        name = input('Insira o nome da nova imagem: ')
        img_equalizada.save(f'Out/{name}.jpeg')
        print(f'Imagem salva!! - {name}.jpeg')
    elif option == 0:
        sys.exit(1)
    else:
        print('Insira uma das opções exibidas!\n')

def main(argv):
    img = loadImage(argv)
    matrix = img.load()
    x, y = img.size[0], img.size[1]
    
    print('Processando...\n-----------------------------------------')
    h = Histograma(matrix, x, y)
    h.run()
    
    while True:
        option = int(input('\n1-Mostrar Histogramas\n2-Salvar imagem normalizada\n0-Sair\n'))
        menu(option, h)

if __name__ == '__main__':
    main(sys.argv[1])