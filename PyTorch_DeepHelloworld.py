import torch
from torch import optim
import torch.nn as nn
torch.manual_seed(42) # make repeatable
input = torch.randn(13, 128) # fixed input
target = torch.tensor([72, 69, 76, 76, 79, 44, 32, 87, 79, 82, 76, 68, 33]) # fixed target
net = nn.Sequential(nn.Linear(128, 64),
                    nn.ReLU(),
                    nn.Linear(64, 32),
                    nn.ReLU(),
                    nn.Linear(32, 128))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
for i in range(34):
    optimizer.zero_grad()
    output = net(input)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
hello_world = ""
for x in net(input).argmax(1): # decode
    hello_world += chr(x)
print(hello_world.title())