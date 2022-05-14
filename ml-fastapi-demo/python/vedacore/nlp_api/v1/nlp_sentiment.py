from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()


class Sentiment:
    def __init__(self, model_name="cardiffnlp/twitter-roberta-base-sentiment"):
        self.classifier = pipeline(task="text-classification", model=model_name)

    def predict_sentiment(self, text):
        return self.classifier(text)


class News(BaseModel):
    content: str


SENSE = Sentiment()


@router.get("/")
async def get_root():
    return "Welcome to NLP API"


@router.post('/get-sentiment')
async def get_sentiment_route(request: News):
    text = request.content
    # check input
    if len(text) <= 0 or not isinstance(text, str):
        return ""

    # call your ml model here
    def _get_sentiment(doc):
        return SENSE.predict_sentiment(doc)

    return _get_sentiment(doc=text)
