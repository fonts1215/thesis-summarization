from quart import Quart, request, Quart
from quart_schema import QuartSchema, validate_request, validate_response
from PyPDF2 import PdfReader
from transformers import BartTokenizer, BartForConditionalGeneration
from spacy import displacy
from models.NerBasic import *
from azure.storage.blob import BlobServiceClient

import spacy

app = Quart(__name__)
QuartSchema(app)

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.route("/ner/basic", methods=['POST'])
@validate_request(NerBasicRequest)
@validate_response(NerBasicResponse, 200)
async def nerBasic(data: NerBasicRequest) -> tuple[NerBasicResponse, int]:
    doc = nlp(data.string_to_ner)
    
    result=[]
    for ent in doc.ents:
        print(ent)
        result.append(NerItem(
            end=ent.end_char,
            label=str(ent.ents[0].label_),
            start=ent.start_char,
            text=str(ent.text)
        ))

    return NerBasicResponse(items=result), 200

@app.route("/ner/blob", methods=['POST'])
@validate_request(NerBlobRequest)
@validate_response(NerBasicResponse, 200)
async def nerBlob(data: NerBlobRequest) -> tuple[NerBasicResponse, int]:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=data.id_file)
    blob_data = blob_client.download_blob()
    content = blob_data.readall()

    local_file_path = "local_file.pdf"
    with open(local_file_path, "wb") as local_file:
        local_file.write(content)

    text = ""

    with open(local_file_path, "rb") as file:
        pdf_reader = PdfReader(file)
        num = 0
        # Estrai il testo da ciascuna pagina del PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    doc = nlp(text)
    
    result=[]
    for ent in doc.ents:
        print(ent)
        result.append(NerItem(
            end=ent.end_char,
            label=str(ent.ents[0].label_),
            start=ent.start_char,
            text=str(ent.text)
        ))

    return NerBasicResponse(items=result), 200



if __name__ == "__main__":
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')    
    # Loading spacy models
    nlp = spacy.load("it_core_news_lg")
    
    # Configurazione delle credenziali di Azure Storage
    container_name = "files"
    blob_name = "aae231f4-0e6f-4440-aca0-c73595c26442"

    # Connessione al contenitore di Azure Blob Storage
    connection_string = "DefaultEndpointsProtocol=https;AccountName=filescontainer001;AccountKey=eapSSLF/qY/W3WeaL30hThbGRvLTOtBsZOWTWfGK09sCFXRoyZVNLzW0ktNtwf3gMAn5mtNOaRuU+AStcZzf4w==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    app.run()
