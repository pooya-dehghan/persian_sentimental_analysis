import torch
import torch.nn as nn

class TextCNN(nn.Module) : 
    def __init__(self,  vocab_size , embedding_dim): 
        self.embedding = nn.Embedding()
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
