# Usa un'immagine di Python come base
FROM python:3.11.7-slim

# Imposta la directory di lavoro nell'immagine
WORKDIR /app

# Copia i file necessari nell'immagine
COPY requirements.txt .
COPY main.py .
COPY models /app/models

# Installa le dipendenze dell'app
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta su cui l'applicazione ascolterà le richieste
EXPOSE 8080

# Comando per eseguire l'applicazione quando il container è avviato
CMD ["python", "main.py"]
