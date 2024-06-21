import torch
from torch import nn


if __name__== "__main__":

    my_tensor = torch.ones((32, 3, 128, 128))
    conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out1 = conv1(my_tensor)
    print("===== problem1 =====")
    print(repr(out1.size()))
    
    conv2 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=2, padding=0)
    out2 = conv2(my_tensor)
    print("===== problem2 =====")
    print(repr(out2.size()))

    conv1 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out1 = conv1(my_tensor)
    print("===== problem1 =====")
    print(repr(out1.size()))

    conv1 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    out1 = conv1(my_tensor)
    print("===== problem2 =====")
    print(repr(out1.size()))