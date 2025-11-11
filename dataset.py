import torch
from torch_geometric.data import Data, Dataset
import numpy as np
import os

class LidarSegDataset(Dataset):
  def __init__(self, root, split='train', transform=None, pre_transform=None):
    super().__init__(root, tranform, pre_transform)
    self.split = split
    self.files = [f for f in os.listdir(os.path.join(root,split)) if f.endswith('.npz') ]

  def len(self): 
    return len(self.files)

  def get(self, idx):
    data_path =  os.path.join(self.root, self.split, self.files[idx])
    npz = np.load(data_path)
    pos = torch.tensor(npz['xyz'], dtype=torch.float)
    x = torch.tensor(npz['features'], dtype=torch.float) 
    y = torch.tensor(npz['labels'], dtype=torch.long)
    return Data(x=x, pos=pos, y=y)   
