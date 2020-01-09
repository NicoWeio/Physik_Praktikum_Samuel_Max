import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data/biegung_beidseitig_eckig.csv' ) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header_row=next(reader)
        x, D_0, D = [], [], []
        for row in reader:
            x.append(row[0])
            D_0.append(row[1])
            D.append(row[2])
        x=np.array(x,dtype=int)
        D_0=np.array(D_0,dtype=float)
        D=np.array(D,dtype=float)
        D = 10-D
        D_0 = 10-D_0
        D_a = D-D_0
        plt.xlabel(r'$x/cm$')
        plt.ylabel(r'$D(x)/mm$')
        plt.plot(x,D_a, 'x', label='absolute Auslenkung')
        plt.legend()
        plt.grid()
        plt.savefig('plot_beidseitig_eckig.pdf')
        plt.show()

