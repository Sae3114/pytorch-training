from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):

    def __init__(self, dataset_dir):
        self.dataset_dir = Path(dataset_dir).resolve()
        self.paths = list(self.dataset_dir.glob("*"))

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        path = self.paths[idx]
        return path

dataloader = DataLoader(dataset = MyDataset("."), batch_size = 2)