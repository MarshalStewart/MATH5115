"""
assignment 2
U.S Bureau of Labor Statistics
https://www.bls.gov/oes/
"""

import matplotlib.pyplot as plt
import numpy as np
import time


def main():

    # Project employment by STEM occupational group, 2019-29
    data = [[30, 25, 50, 20],
            [40, 23, 51, 17],
            [35, 22, 45, 19]]
    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar("", data[0], color='b', width=0.25)
    ax.bar("", data[1], color='g', width=0.25)
    ax.bar("", data[2], color='r', width=0.25)

    plt.xlabel('STEM Occupations')
    plt.ylabel('IDEK')

    plt.show()


if __name__ == '__main__':
    main()
    # input("Press any key to exit...")
