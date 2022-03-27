""""
this file is where we go through one 
training regimen for our neural network

TODO: train on COCO dataset and print out eval results
"""

import torch
from torchvision import datasets
import random
import cv2
import os

COCO_imgs = datasets.CocoDetection
COCO_labels = datasets.CocoCaptions

##TODO: BRING YOUR DATALOADER HERE



print("hello world!")