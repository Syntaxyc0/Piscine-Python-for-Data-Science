import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    '''
    program to apply a 90° rotation on a specific JPEG file
    '''
    img = ft_load("animal.jpeg")
    print(img)
    zoomed_img_array = img[100:500, 450:850, :]
    zoomed_img = Image.fromarray(zoomed_img_array)
    zoomed_gray_img = zoomed_img.convert("L")
    new_img_array = np.array(zoomed_gray_img)
    result = np.zeros((400, 400))
    for x in range(400):
        for y in range(400):
            result[x][y] = new_img_array[y][x]
    transposed_img = Image.fromarray(result)
    print(f"New shape after Transpose: {result.shape}")
    print(result)
    plt.imshow(transposed_img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
