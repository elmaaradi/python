import numpy as np
import matplotlib.pyplot as plt

def main():
    a = int(input('Entrer a : parametre de c'))#-5
    b = int(input('Entrer b : parametre de c'))#10
    y, x = np.ogrid[-10:10:1000j, -10:10:1000j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()