from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(10)
y1 = x1**2

x2 = np.arange(20)
y2 = x2**2

def function_plot(X,Y, pp):
    plt.figure()
    plt.clf()

    plt.plot(X,Y)
    graph = plt.title('y vs x')
    plt.xlabel('x axis', fontsize = 13)
    plt.ylabel('y axis', fontsize = 13)

    pp.savefig(plt.gcf())


if __name__ == '__main__':

    with PdfPages('test.pdf') as pp:
        function_plot(x1,y1, pp)
        function_plot(x2,y2, pp)

    print('Creating test.pdf')
