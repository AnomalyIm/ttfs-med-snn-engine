import numpy as np

def ttfs_encode(image: np.ndarray, Tmax: float = 100.0) -> np.ndarray:
    """
    Time-to-First-Spike encoding for grayscale images.
    Bright pixels → early spikes.

    Args:
        image (np.ndarray): 2D grayscale image, values [0, 255] or [0,1]
        Tmax (float): Max simulation time (ms)

    Returns:
        np.ndarray: 2D array of spike times
    """
    if image.max() > 1.0:
        image = image / 255.0
    spike_times = Tmax * (1 - image)
    return spike_times