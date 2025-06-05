import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.batch_norm1 = nn.BatchNorm1d(128)
        self.fc2 = nn.Linear(128, 64)
        self.batch_norm2 = nn.BatchNorm1d(64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, output_dim)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.fc1(x)
        if x.shape[0] > 1:
            x = self.batch_norm1(x)
        x = F.relu(x)
        x = self.dropout(x)

        x = self.fc2(x)
        if x.shape[0] > 1:
            x = self.batch_norm2(x)
        x = F.relu(x)

        x = F.relu(self.fc3(x))
        return self.fc4(x)
