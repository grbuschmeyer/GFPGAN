# import argparse
# import cv2
# import glob
# import numpy as np
import os
import torch
# from basicsr.utils import imwrite
from torch._C import _parse_source_def


print("*******************************")
print("CUDA Version")
print(torch.version.cuda)
print("*******************************")


# from gfpgan import GFPGANer
print("*******************************")
print("CUDA Available")
print(torch.cuda.is_available())
print("*******************************")