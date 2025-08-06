# 🧠 Time-to-First-Spike (TTFS) Decoding Engine for Medical Imaging

## 🔬 Project Overview

This project implements a biologically inspired Spiking Neural Network (SNN) to analyze medical imaging data using **Time-to-First-Spike (TTFS)** decoding.

Unlike traditional artificial neural networks, this model mimics how real neurons in the brain communicate — using spikes (discrete events over time) — to process and classify medical images like **MRI** or **EEG scans**.

We simulate spike-based encoding, transmission, and decoding in a full pipeline that’s fast, sparse, and highly energy-efficient.

---

## 🚀 Key Features

- 🧠 Implements **biologically plausible SNN** with **spike-timing dynamics**
- ⚡ Uses **TTFS encoding**: brighter pixels fire earlier
- 📉 Supports **STDP** (Spike-Timing Dependent Plasticity) for unsupervised learning
- 🧪 Trained on **real medical imaging datasets** (MRI / EEG)
- 📊 Visualizes spike maps, raster plots, synaptic weights
- 🛠️ Full MLOps pipeline planned: training, deployment, monitoring
- 🌍 Easily extendable to neuromorphic hardware like Intel Loihi or SpiNNaker

---

## 💡 Why Spiking Neural Networks?

| Traditional ANNs | Spiking Neural Networks (SNNs) |
|------------------|-------------------------------|
| Dense, continuous activations | Sparse, event-driven spikes |
| High energy usage | Energy-efficient, low-power |
| Batch-based processing | Real-time, temporal processing |
| Less biologically accurate | Closely mimics brain behavior |

TTFS-based decoding is ultra-fast and interpretable: the **first neuron to spike** determines the predicted class.

---

## 🗺️ Project Architecture
