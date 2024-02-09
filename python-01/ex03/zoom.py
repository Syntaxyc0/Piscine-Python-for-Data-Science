import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    '''
    Program that zooms in and apply a gray filter
    on a particular jpeg file
    '''
    img = ft_load("animal.jpeg")
    print(img)
    zoomed_img_array = img[100:500, 450:850, :]
    zoomed_img = Image.fromarray(zoomed_img_array)
    zoomed_gray_img = zoomed_img.convert("L")
    new_img_array = np.array(zoomed_gray_img).reshape(400, 400, 1)
    print(f"New shape after slicing: {new_img_array.shape}")
    print(new_img_array)
    plt.imshow(zoomed_gray_img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
