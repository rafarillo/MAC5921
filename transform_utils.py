import torch


def gaussian_noise(tensor, mean=0.0, std=0.1):
    noise = torch.randn(tensor.size()) * std + mean
    return torch.clamp(tensor + noise, 0.0, 1.0)
