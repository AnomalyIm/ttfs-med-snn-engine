# 🧠 Time-to-First-Spike (TTFS) Decoding Engine for Medical Imaging

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Repo Size](https://img.shields.io/github/repo-size/AnomalyIm/ttfs-med-snn-engine)
![Last Commit](https://img.shields.io/github/last-commit/AnomalyIm/ttfs-med-snn-engine)
![Issues](https://img.shields.io/github/issues/AnomalyIm/ttfs-med-snn-engine)

## 🔬 Project Overview
This project implements a **biologically inspired Spiking Neural Network (SNN)** to analyze medical imaging data using **Time-to-First-Spike (TTFS)** decoding. Unlike traditional artificial neural networks, this model mimics how real neurons in the brain communicate — using spikes (discrete events over time) — to process and classify medical images like **MRI** or **EEG scans**. We simulate **spike-based encoding**, transmission, and decoding in a **full pipeline** that’s fast, sparse, and highly energy-efficient.

## 🚀 Key Features
- 🧠 Implements **biologically plausible SNN** with spike-timing dynamics
- ⚡ Uses **TTFS encoding**: brighter pixels fire earlier
- 📉 Supports **STDP** (Spike-Timing Dependent Plasticity) for unsupervised learning
- 🧪 Trained on **real medical imaging datasets** (MRI / EEG)
- 📊 Visualizes spike maps, raster plots, synaptic weights
- 🛠️ Full **MLOps pipeline** planned: training, deployment, monitoring
- 🌍 Easily extendable to **neuromorphic hardware** like Intel Loihi or SpiNNaker

## 💡 Why Spiking Neural Networks?
| Traditional ANNs | Spiking Neural Networks (SNNs) |
|------------------|--------------------------------|
| Dense, continuous activations | Sparse, event-driven spikes |
| High energy usage | Energy-efficient, low-power |
| Batch-based processing | Real-time, temporal processing |
| Less biologically accurate | Closely mimics brain behavior |

TTFS-based decoding is ultra-fast and interpretable: the **first neuron to spike** determines the predicted class.

## 🗺️ Project Architecture
MRI Image (.png, .nii)  
      ↓  
TTFS Encoder (Pixel → Spike Time)  
      ↓  
Spiking Neural Network (SNN)  
      ↓  
Time-to-First-Spike Decoding  
      ↓  
Prediction + Visualization + Deployment

## 📁 Repository Structure
ttfs-med-snn-engine/  
├── data/             # MRI/EEG datasets  
├── outputs/          # Spike maps, plots, weight visualizations  
├── notebooks/        # Jupyter notebooks for EDA, testing  
├── src/  
│   ├── encoding/     # TTFS encoding logic  
│   ├── models/       # SNN architectures  
│   ├── utils/        # Plotting, I/O helpers  
│   └── pipeline/     # Training & inference scripts  
├── tests/            # Unit tests for core modules  
├── configs/          # Experiment configs (Tmax, neuron count)  
├── requirements.txt  # All dependencies  
├── .gitignore  
├── README.md         # You're here!  

## 🧪 Technologies Used
- **Python** 3.10+
- NumPy, OpenCV, Matplotlib
- **BindsNET** or **NEST Simulator**
- PyTorch (backend for SNN)
- HDF5, NumPy I/O
- Streamlit (dashboard)
- FastAPI (inference API)
- MLflow (for tracking, later)
- pytest (unit tests)

## 🔧 How to Run
⚠️ Requires Python 3.10+ and virtual environment setup.

# Clone the repo
git clone https://github.com/your-username/ttfs-med-snn-engine.git  
cd ttfs-med-snn-engine  

# Create virtual environment
python -m venv .venv  
source .venv/bin/activate  # Windows: .venv\Scripts\activate  

# Install dependencies
pip install -r requirements.txt  

# Run unit tests
pytest tests/  

# Run encoder test
jupyter notebook notebooks/01_data_explore.ipynb  

## 🧠 TTFS Encoding Explained
Each pixel is converted to a spike time:  
spike_time = Tmax * (1 - pixel_intensity)  

- **Bright pixel** → fires earlier  
- **Dim pixel** → fires later  
- **No spikes** beyond `Tmax`  

This creates a **spatial-temporal map** of spike times across neurons.

## 📊 Outputs
- 🔥 Spike Time Maps (TTFS encoded)
- 📈 Raster Plots (neuron spike activity over time)
- 🧠 Synaptic Weight Visualizations
- 💡 Class Prediction from First Spike

## ✅ Milestones
| Week | Milestone |
|------|-----------|
| 1    | Dataset + TTFS encoder module |
| 2    | SNN architecture + STDP training |
| 3    | TTFS decoding logic + visualization |
| 4    | ANN comparison + deployment + blog |

## 🔍 Potential Use Cases
- Alzheimer’s classification from MRI
- Seizure detection from EEG
- Brain-inspired low-power inference engines
- On-device AI for embedded medical tools

## 📜 License
MIT License © Neeraj Bhardwaj 2025

## 🙌 Acknowledgments
- OASIS & BraTS for medical imaging datasets
- BindsNET for spiking simulation framework
- NEST, Brian2 for biological modeling
- OpenAI ChatGPT for guidance during design
