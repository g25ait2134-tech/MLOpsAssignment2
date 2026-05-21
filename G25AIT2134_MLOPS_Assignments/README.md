# Goodreads Genre Classification with DistilBERT

This project fine-tunes a Hugging Face DistilBERT model to classify Goodreads book reviews into genre categories. Training was performed in a Kaggle Notebook using GPU acceleration, experiment tracking was done with Weights & Biases, evaluation results were saved as a W&B artifact, and the final trained model was pushed to Hugging Face Hub for reuse.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run inference using the trained Hugging Face model:

```bash
python inference.py
```

## Training Platform

Training was done on Kaggle Notebook using GPU acceleration and Kaggle Secrets for `WANDB_API_KEY` and `HF_TOKEN`.

- Kaggle Notebook: https://www.kaggle.com/code/shyamg25ait2134/notebook828cbfd1f6

## Results

| Metric | Score |
|---|---:|
| Accuracy | 0.59 |
| F1 Score | 0.585 |
| Eval Loss | 2.297|

## Links

- Hugging Face model: https://huggingface.co/G25AIT2134/distilbert-goodreads-genres
- W&B dashboard: https://wandb.ai/g25ait2134-iitj/mlops-assignment2/runs/5s2gs1m0?nw=nwuserg25ait2134
