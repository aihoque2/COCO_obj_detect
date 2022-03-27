import torch
import random
import cv2
import os

class CocoDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.images = []

    def __getitem__(self):
        pass

    def __len__(self):
        return len(self.images)