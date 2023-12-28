from quart import Quart, request
from PyPDF2 import PdfReader
from transformers import BartTokenizer, BartForConditionalGeneration
from spacy import displacy

import spacy

app = Quart(__name__)

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.route("/ner", methods=['POST'])
async def ner():
    print('request', await request.get_json())
    doc = nlp("Apple è un'azienda americana che produce dispositivi e software.")
    
    result = []
    for entità in doc.ents:
        result.append({
            "text": entità.text,
            "label": entità.label_,
            "start": entità.start_char,
            "end": entità.end_char
        })

    return result

if __name__ == "__main__":
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')    
    # Loading spacy models
    nlp = spacy.load("it_core_news_lg")
    app.run()