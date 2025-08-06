import numpy as np
from src.encoding.ttfs_encoder import ttfs_encode

def test_ttfs_shape():
    dummy_image = np.random.rand(32, 32)
    spike_times = ttfs_encode(dummy_image)
    assert spike_times.shape == dummy_image.shape

def test_ttfs_value_range():
    dummy_image = np.ones((32, 32)) * 0.5
    spike_times = ttfs_encode(dummy_image, Tmax=100)
    assert np.allclose(spike_times, 50.0)