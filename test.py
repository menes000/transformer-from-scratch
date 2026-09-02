import torch.nn as nn
import inspect

print(inspect.getsourcefile(nn.Module))          # dosya yolu
print(inspect.getsource(nn.Module.__init__))
