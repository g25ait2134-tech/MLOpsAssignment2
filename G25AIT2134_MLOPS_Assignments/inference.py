from transformers import pipeline


MODEL_ID = "G25AIT2134/distilbert-goodreads-genres"

classifier = pipeline(
        "text-classification",
        model=MODEL_ID,
        tokenizer=MODEL_ID,
    )

def predict_genre(text: str):
    return classifier(text)


if __name__ == "__main__":
    sample_review = (
        "This book had magic, ancient kingdoms, danger, and a young hero "
        "learning how to survive in a strange new world."
    )
    print(predict_genre(sample_review))
