import matplotlib.pyplot as plt


def smallsq():

    Xax = [3, 3, 4, 4, 3]
    Yax = [3, 4, 4, 3, 3]

    plt.plot(Xax, Yax, 'r:o')


def medsq():

    Xax = [2, 2, 5, 5, 2]
    Yax = [2, 5, 5, 2, 2]

    plt.plot(Xax, Yax, 'g--s')


def lrgsq():

    Xax = [1, 1, 6, 6, 1]
    Yax = [1, 6, 6, 1, 1]

    plt.plot(Xax, Yax, 'b-p')


def run():

    smallsq()
    medsq()
    lrgsq()
    plt.show()


run()
