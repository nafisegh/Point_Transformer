import torch
import torch.nn as nn
from torch_geometric.nn import PointTransformerConv

class PointTransformerSeg(nn.Module):

  def __init__(self, in_channels=3, hidden_dim=64, num_classes=5):
    super(PointTransformerSeg, self).__init__()
    self.conv1 = PointTransformerConv(in_channels, hidden_dim)
    self.conv2 = PointTransformerConv(hidden_dim, hidden_dim)
    self.conv3 = PointTransformerConv(hidden_dim, hidden_dim)
    self.fc = nn.Linear(hidden_dim, num_classes)

 def forward(self, x, pos, batch):
    
    x = self.conv1(x, pos, batch)
    x = self.conv2(x, pos, batch)
    x = self.conv3(x, pos, batch)
    x = self.fc(x)

    return x
