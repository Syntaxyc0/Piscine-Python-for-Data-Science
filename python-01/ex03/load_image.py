from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    '''
    loads an image (JPG or JPEG) displays its shape,
    its pixel representation (R, G, B)
    and returns it as an array
    '''
    try:
        with Image.open(path) as img:
            img_array = np.array(img)
            print(f"The shape of image is: {img_array.shape}")
            # pixels = list(img.getdata())
            # rgb_pixels = [f"({r},{g},{b})" for r, g, b in pixels]
            # print(f"Pixel Content (RGB Format): {rgb_pixels}")
            return img_array

    except FileNotFoundError:
        print(f"Error: File not found - {path}")
    except IOError as e:
        print(f"Error: Unable to open image - {path}\nDetails: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred\nDetails: {e}")
