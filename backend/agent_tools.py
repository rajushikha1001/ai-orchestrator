from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def classify_sentiment(text: str):
    result = sentiment_model(text)[0]
    return {
        "label" : result["label"],
        "score" : round(result["score"], 3)
    }