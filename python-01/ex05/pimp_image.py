import numpy as np
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def ft_invert(array: np.array) -> np.array:
    '''
    Inverts the color of the received image
    '''
    inverted_array = 255 - array
    with plt.xkcd():
        new_img = Image.fromarray(inverted_array)
        plt.imshow(new_img)
        plt.show()
    return inverted_array

    
def ft_red(array) -> np.array:
    '''
    Apply a red filter on received image
    '''
    copy = array.copy()
    copy[:, :, 1] = 0
    copy[:, :, 2] = 0
    with plt.xkcd():
        new_img = Image.fromarray(copy)
        plt.imshow(new_img)
        plt.show()
    return copy
        
def ft_green(array) -> np.array:
    '''
    Apply a green filter on received image
    '''
    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 2] = 0
    with plt.xkcd():
        new_img = Image.fromarray(copy)
        plt.imshow(new_img)
        plt.show()
    return copy
    
def ft_blue(array) -> np.array:
    '''
    Apply a blue filter on received image
    '''
    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 1] = 0
    with plt.xkcd():
        new_img = Image.fromarray(copy)
        plt.imshow(new_img)
        plt.show()
    return copy
    
def ft_grey(array) -> np.array:
    '''
    Apply a grey filter on received image
    '''
    copy = 0.2989 * array[:, :, 0] + 0.5870 * array[:, :, 1] + 0.1140 * array[:, :, 2]
    with plt.xkcd():
        new_img = Image.fromarray(copy)
        plt.imshow(new_img)
        plt.show()
    return copy
