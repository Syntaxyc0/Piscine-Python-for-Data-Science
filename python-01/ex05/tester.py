from load_image import ft_load
from pimp_image import * 

array = ft_load("landscape.jpg")
print(array)
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)