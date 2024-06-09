from matplotlib import pyplot as plt
import numpy as np
from cmath import exp, pi

def koch_snowflake(N: int):
    """Return a set of complex numbers modeling the n-th stage of the koch snowflake"""
    a = np.array([1+0j, exp(2j*pi/3), exp(-2j*pi/3)])
    for _ in range(N-1):
        a = next_step(a)
    return a


def next_step(arr):
    # initialization
    n_dots = len(arr)
    new_arr = np.empty(4*n_dots, dtype='cdouble')

    # add 3 dots between each dots
    for i in range(-1,n_dots-1):
        za, zb = arr[i], arr[i+1]
        z_ab = zb - za

        translation = z_ab/3

        new_arr[4*i] = za
        new_arr[4*i+1] = za + translation # translation from A
        new_arr[4*i+2] = za + translation + rotation*z_ab/3 # -π/3 rotation of AB/3 and translation from A
        new_arr[4*i+3] = za + 2*translation # two translations from A
    return new_arr

if __name__ == "__main__":
    rotation = exp(-1j*pi/3)
    a = koch_snowflake(6)

    # plotting the snowflake
    fig = plt.figure(figsize=(5, 5))
    ax = plt.subplot()
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.scatter(a.real, a.imag, s=1, c=np.sqrt(np.square(a.real) + np.square(a.imag)), cmap='plasma_r')
    plt.show()
