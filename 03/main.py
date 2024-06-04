from torch import nn
import torch

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x

if __name__ == "__main__":
    model = MyModel()
    x = torch.rand(1)
    print(x)
    output = model(x)
    print(output)
    