import matplotlib.pyplot as plt
from PIL import Image

class Histograma():
    def __init__(self, matrix, x, y):
        self.matrix = matrix
        self.x, self.y = x, y
        self.pixels_totais = x*y

    def run(self):
        """ 
        Executa o algoritmo que plota o histograma, histograma normalizado e histograma acumulado
        """
        self.bins = [0] * 256
        for i in range(self.x):
            for j in range(self.y):
                self.bins[self.matrix[i, j]] += 1

        cdf, pdf = self.normalizar()
        
        plt.figure('Histograma')
        plt.bar(range(256), self.bins)
        
        plt.figure('Histograma Normalizado')
        plt.bar(range(256), pdf)
        
        plt.figure('Histograma Acumulado')
        plt.bar(range(256), cdf)
        
        plt.show()

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
        
        return cdf_values, pdf

    def create_image(self):
        
        pdf = self.normalizar()

        image = Image.new("L", (self.x, self.y))
        pixels = image.load()
        
        for i in range(self.x):
            for j in range(self.y):
                pixels[i, j] = int(pdf[self.matrix[i, j]] * 255)

        return image
