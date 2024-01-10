# Usa un'immagine di Python come base
FROM python:3.11.7-slim

# Imposta la directory di lavoro nell'immagine

# Copia i file necessari nell'immagine
COPY requirements.txt .
COPY main.py /app/main.py
COPY models /app/models
# Installa le dipendenze dell'app
RUN pip install --no-cache-dir -r requirements.txt

COPY init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh
WORKDIR /app

# Esponi la porta su cui l'applicazione ascolterà le richieste
EXPOSE 8080 2222 8000
 
# Comando per eseguire l'applicazione quando il container è avviato
# CMD ["python", "main.py"]

# ENTRYPOINT ["hypercorn", "-b","0.0.0.0:8080", "main:app"]
ENTRYPOINT ["init.sh"]
