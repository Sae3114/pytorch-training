import torch
from torch import nn

if __name__=="__main__":

    my_tensor = torch.ones((32, 1024))
    print("===== problem1 =====")
    print(my_tensor.size())

    fc1 = nn.Linear(in_features=1024, out_features=256, bias=True)
    print("===== problem2 =====")
    print(repr(fc1(my_tensor).size()))

    fc2 = nn.Linear(in_features=1024, out_features=2048, bias=True)
    print("===== problem3 =====")
    print(repr(fc2(my_tensor).size()))

    print("===== appendix =====")
    print(repr(fc1(my_tensor).view(-1, 16, 16).size()))