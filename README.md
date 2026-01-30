# finetune-merged-lora-model-peft

<p align="center">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000" />
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=fff" />
  <img alt="Transformers" src="https://img.shields.io/badge/Transformers-4051B5?style=for-the-badge&logo=huggingface&logoColor=fff" />
  <img alt="PEFT" src="https://img.shields.io/badge/PEFT-2F6FEB?style=for-the-badge&logo=python&logoColor=fff" />
  <img alt="TRL" src="https://img.shields.io/badge/TRL-111827?style=for-the-badge&logo=python&logoColor=fff" />
  <img alt="bitsandbytes" src="https://img.shields.io/badge/bitsandbytes-0B5FFF?style=for-the-badge&logo=nvidia&logoColor=fff" />
  <img alt="Accelerate" src="https://img.shields.io/badge/Accelerate-4B5563?style=for-the-badge&logo=python&logoColor=fff" />
  <img alt="Weights & Biases" src="https://img.shields.io/badge/Weights%20%26%20Biases-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=000" />
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=fff" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff" />
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=fff" />
</p>

## Overview
This repository is my **collection of end-to-end fine-tuning notebooks** (LoRA / QLoRA-style) using the modern Hugging Face stack.
It includes examples across model families and sizes (Phi, Gemma, DialoGPT, SmolLM, DeepSeek distills), plus an example W&B training chart from one of my fine-tuning runs.

## Contents
- **Notebooks**: Fine-tuning runs (4-bit) + adapter/merge flows.
- **Assets**: Example training results (W&B chart exports). Hugging Face login helpers.

## Repo structure
```text
.
├── assets/
│   └── wandb/
│       └── wandb-chart-2026-01-29-235217.png
├── fine_tune_*.ipynb
├── finetune_*.ipynb
└── README.md
```

## Tech stack
- **Core**: PyTorch, Transformers, PEFT, TRL
- **Efficiency**: bitsandbytes (4-bit), Accelerate
- **Experiment tracking**: Weights & Biases (W&B)
- **Authoring**: Jupyter / Colab-style notebooks

## Notebooks (high level)
This repo contains multiple fine-tuning notebooks, including:
- **Microsoft Phi**
  - `fine_tune_microsoft_phi_1_4bit.ipynb`
  - `fine_tune_Lora_microsoft_Phi_3_mini_4k_instruct_4bit.ipynb`
  - `finetune_LoRA_Phi_3_mini_4k.ipynb`
  - `finetune_LoRA_Phi_3_mini_4k_raw_text.ipynb`
- **Google Gemma**
  - `fine_tune_google_gemma_3_270m_4bit.ipynb`
  - `fine_tune_Lora_google_gemma_2_2b_it_4bit.ipynb`
- **DialoGPT**
  - `fine_tune_Lora_microsoft_DialoGPT_medium_4bit.ipynb`
  - `fine_tune_Lora_microsoft_DialoGPT_small_4bit.ipynb`
  - `fine_tune_Lora_microsoft_DialoGPT_small_4bit (1).ipynb`
- **SmolLM**
  - `fine_tune_Lora_HuggingFaceTB_SmolLM_360M_Instruct_4bit.ipynb`
- **DeepSeek distill**
  - `fine_tune_deepseek_ai_DeepSeek_R1_Distill_Qwen_1_5B_4bit.ipynb`

## Example training result (W&B export)
Below is a W&B training chart export from my **`Llama-3.2-3B-ChatGPT-Prompts-Instruct`** fine-tuning run:

![W&B training chart example](assets/wandb/wandb-chart-2026-01-29-235217.png)

## Quickstart (recommended pattern)
Most notebooks follow this flow:
1. Install dependencies
2. Load base model + tokenizer
3. Configure 4-bit quantization (bitsandbytes)
4. Apply LoRA (PEFT)
5. Train (TRL / SFTTrainer)
6. Save adapter / merge / export
7. (Optional) Push artifacts to Hugging Face Hub (use env-based auth)

