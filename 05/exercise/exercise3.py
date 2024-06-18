import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
from torchvision import transforms
from torch.utils.data import Dataset

class MyDataset(Dataset):

    def __init__(self, dataset_dir):
        dir_path_resolved = Path(dataset_dir).resolve()
        dir_list = list(dir_path_resolved.glob("*"))
        self.transform = transforms.Compose([
            transforms.ToTensor(),
        ])

        self.img_list = []
        for image in dir_list:
            img_list = list(image.glob("*.png"))
            self.img_list += img_list

    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)
        img_tensor = self.transform(img)
        # ファイル名からラベルの取得
        img_path = Path(img_path)
        parts = img_path.parts
        label = int(parts[-2])

        return img_tensor, label
    

if __name__ == "__main__":
    my_dataset = MyDataset("./data")
    # for i in range(50):
    #     img, label = my_dataset[i]
    #     print(i, label)
    img, label = my_dataset[46]
        
    print("===== problem1.1 =====")
    print(img.size())
    print("===== problem1.2 =====")
    print(label)