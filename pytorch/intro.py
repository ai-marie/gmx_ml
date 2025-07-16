
import torch #import the torch package, download with pip install torch (go to https://pytorch.org/get-started/locally/ for the CUDA version)
x = torch.rand(5, 3) #create a 5*3 matrix, first number is number of rows, second number is number of columns, rand = random numbers generated
print(x) #print the x value
print(torch.__version__)