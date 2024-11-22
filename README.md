# Idea del progetto
1. Replicare tecnica di Kelly (OHLC in bianco e nero) su tutte le aziende dell'sp500
2. Provare a cambiare le immagini con candele e colori -> *vediamo se possiamo miglorare la tecnica*
3. Provare a usare una tecnica con gli stessi dati ma non immagini -> *vediamo se le immagini funzionano meglio perche sono immagini oppure perche includono piu dati*
4. Provare ad applicare a dati con candele M15 o H1
5. Provare su altri asset

# Gia fatto
- Trovato dati
- Quasi fatto plotting OHLC (manca solo moving average)
- Quasi fatto plotting Candele (manca volume e moving average)
- Creare 3 dataset OHLC: 5 giorni, 10 giorni e 60 giorni
- Creare 3 dataset Candle: 5 giorni, 10 giorni e 60 giorni

# To do
 Creare e trainare 3 architetture CNN: 5 giorni, 10 giorni e 60 giorni
- Testare OHLC vs Candles e analizzare risultati
- Provare a usare un NN normale con gli stessi dati (Forse)
- Troare altri dati, creare immagini, e applicare CNN trainato
- Scrivere paper
- Fare slide

