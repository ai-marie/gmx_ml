import torch
scalar = torch.tensor(7) #zero-dimension tensor
print(scalar)
print(scalar.ndim) #will output 0, because it is zero dimensional
print(scalar.item()) #7 items in the tensor

#vector = single-dimensional tensor
vector = torch.tensor([7 , 7])
print(vector)