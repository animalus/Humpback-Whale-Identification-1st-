from .reader import WhaleDataset, WhaleTestDataset
from .transform import (
    random_erase, random_shift, random_scale, do_gaussian_noise,
    do_speckle_noise, random_angle_rotate, do_brightness_shift,
    do_brightness_multiply, do_gamma, do_clahe, bgr_to_gray
)
