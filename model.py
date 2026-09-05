import torch
import torch.nn as nn
import math

class InputEmbedding(nn.Module):

    def __init__(self, d_model: int, vocab_size: int):
        super().__init__()
        self.d_model = d_model 
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, d_model)

    def forward(self, x):
        return self.embedding(x) * math.sqrt(self.d_model) #In the embedding layers, we multiply those weights by √d_model. -Attention Is All You Need
    
class PositionalEncoding(nn.module):
    
    def __init__(self, d_model, seq_len: int, dropout: float):
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)

        pe = torch.zeros(seq_len, d_model)

        # Column vector of positions, shape (seq_len, 1), for broadcasting into the PE table
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1) 

        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        # Add a batch dimension at the front: (seq_len, d_model) -> (1, seq_len, d_model)
        # so it broadcasts across every sequence in a batch when added to x
        pe = pe.unsqueeze(0)

        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + (self.pe[:, :x.shape[1], :]).requires_grad_(False)
        return self.dropout(x) 
    
class LayerNormalization(nn.Module):
    
    def __init__(self, eps: float = 10**-6):
        super().__init__()
        self.eps = eps
        self.alpha = nn.Parameter(torch.ones(1)) # Learnable multiplicative scale, starts at 1 (identity)
        self.bias = nn.Parameter(torch.zeros(1))
    