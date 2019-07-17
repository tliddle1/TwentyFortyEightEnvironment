# -*- coding: utf-8 -*-
"""
File for nueral networks
"""

import torch.nn as nn
import torch.nn.functional as F


class AlphaTwentyFortyEight(nn.Module):
    def __init__(self):
        super(AlphaTwentyFortyEight, self).__init__()
        self.conv1 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 32, 3, padding=1)
        self.conv_bn = nn.BatchNorm2d(32)
        self.fc1 = nn.Linear(512, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 1)
        self.fc4 = nn.Linear(64, 4)
        
    def main(self, x):
        x = F.relu(self.conv_bn(self.conv1(x)))
        x = F.relu(self.conv_bn(self.conv2(x)))
        x = F.relu(self.conv_bn(self.conv2(x)))
        return x.view(-1, 4*4*32)
        
    def value_head(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x
    
    def policy_head(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.f4(x))
        return x

    def forward(self, x):
        x = self.main(x)
        value = self.value_head(x)
        policy = self.policy_head(x)
        return value, policy