import torch
import numpy as np

if __name__=="__main__":
    data = np.array([[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
     [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

    tensor = torch.tensor(data, dtype=float)
    print("===== problem 1 =====")
    print(repr(tensor.size()))
    
    sort = torch.permute(tensor, (2, 0, 1))
    print("===== problem 2 =====")
    print(repr(sort))
    print(repr(sort.size()))

    sum = sort.sum(dim=0)
    print("===== problem 3 =====")
    print(repr(sum))

    avarage1 = sum.mean(dim=1)
    print("===== problem 4 =====")
    print(avarage1)

    avarage2 = sum.sum(dim=1)
    num_classmate = (sort.size(dim=1))
    avarage2 = avarage2 / num_classmate
    print("===== problem 5 =====")
    print(avarage2)