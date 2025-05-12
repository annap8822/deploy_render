from langdetect import detect

testo = "Ciao, sto parlando in italiano"
lingua = detect(testo)

print(f"La lingua rilevata è: {lingua}")


from textblob import TextBlob

frase = "I'm happy!"
blob = TextBlob(frase)

# Se sentiment > 0 allora -> positivo
# Se sentiment < 0 allora -> negativo
# Se sentiment = 0 allora -> neutro
sentiment = blob.sentiment.polarity
print(sentiment)


#esercizio1
@app.get('/analisi_testo')
def analisi_testo(testo):
    lingua = detect(testo)
print(f"La lingua rilevata è: {lingua}") 

