""" 
    Universidade Federal Do Piauí - UFPI
    Autor: Neemias Calebe Pereira Freire
    Ciência da Computação - Processamento Digital de Imagens
"""

import matplotlib.pyplot as plt
from PIL import Image

class Histograma():
    """ 
        Classe que executa algoritmos de normalização e equalização de histograma.
        É possível exibir o histograma original, normalizado e acumulado bem como salvar a imagem
        equalizada. 
    """
    def __init__(self, matrix, x, y):
        self.matrix = matrix
        self.x, self.y = int(x), int(y)
        self.pixels_totais = self.x * self.y
        
    def run(self):
        """ 
        Executa o algoritmo que plota o histograma, histograma normalizado e histograma acumulado
        """
        self.bins = [0] * 256
        for i in range(self.x):
            for j in range(self.y):
                self.bins[self.matrix[i, j]] += 1
        
        self.pdf, self.cdf = self.normalizar()
        
    def normalizar(self):
        """ 
        Calcula o histograma normalizado e o acumulado da imagem.
        """
        pdf = [bin / self.pixels_totais for bin in self.bins]

        cdf = 0
        cdf_values = [0] * 256
        for i in range(256):
            cdf += pdf[i]
            cdf_values[i] = cdf
        
        return pdf, cdf_values
    
    def equalizar(self):
        
        imagem_equalizada = Image.new("L", (self.x, self.y))
        pixels = imagem_equalizada.load()
        
        for i in range(self.x):
            for j in range(self.y):
                pixels[i, j] = int(self.cdf[self.matrix[i, j]] * 255)
        
        return imagem_equalizada
 
        
    def show_histogram(self):
        plt.figure('Histogramas')

        plt.subplot(2, 2, 1)
        plt.bar(range(256), self.bins)

        plt.subplot(2, 2, 2)
        plt.bar(range(256), self.pdf)

        plt.subplot(2, 2, 3)
        plt.bar(range(256), self.cdf)

        plt.show()
        