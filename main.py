from quart import Quart
from PyPDF2 import PdfReader
from transformers import BartTokenizer, BartForConditionalGeneration
from spacy import displacy

import spacy
import json

app = Quart(__name__)

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.route("/ner")
async def ner():
    doc = nlp("Apple è un'azienda americana che produce dispositivi e software.")
    
    result = []
    for entità in doc.ents:
        result.append({
            "text": entità.text,
            "label": entità.label_,
            "start": entità.start_char,
            "end": entità.end_char
        })

    print(result)

    return result

if __name__ == "__main__":
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')    
    # Loading spacy models
    nlp = spacy.load("it_core_news_lg")
    app.run()