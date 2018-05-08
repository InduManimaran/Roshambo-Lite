import numpy as np
from skimage import transform,util
import skimage as sk
import scipy
from scipy import ndarray,ndimage
import random

def random_intensity(image_array: ndarray):
    v_min, v_max = np.percentile(image_array, (0.2, 99.8))
    return sk.exposure.rescale_intensity(image_array, in_range=(v_min, v_max))

def random_rotation(image_array: ndarray):
    random_degree = np.random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def rotate_90(image_array: ndarray):
    return sk.transform.rotate(image_array, 90)

def rotate_180(image_array: ndarray):
    return sk.transform.rotate(image_array, 180)

def rotate_270(image_array: ndarray):
    return sk.transform.rotate(image_array, 270)

def random_noise(image_array: ndarray):
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    return image_array[:, ::-1]

def vertical_flip(image_array: ndarray):
    return image_array[::-1, :]

def blur(image_array: ndarray):
    return ndimage.uniform_filter(image_array, size=(5, 5, 1))

