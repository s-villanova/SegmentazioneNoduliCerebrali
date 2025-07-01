# SegmentazioneNoduliCerebrali con Mask R-CNN – BRISC2025

## 🔍 Descrizione del progetto
Questo repository contiene un progetto per la segmentazione automatica di tumori cerebrali su immagini MRI, utilizzando un modello Mask R-CNN con backbone ResNet-50 + FPN implementato tramite la libreria Detectron2.

Il sistema è stato addestrato e testato sul dataset pubblico **_BRISC2025_**, convertito in formato COCO con segmentazioni pixel-wise codificate tramite **Run-Length Encoding (RLE)**.

## 🚀 Contenuto del repository
- **📁 `BRISC2025/`**  - Dataset convertito in formato COCO + RLE
  - **📁 `classification_task/`**
    - 📄 cartelle e file relativi a classificazione (non utlizzata in questo progetto)
  - **📁 `segmentation_task/`**
    - **📁 `test/`**
      - **📁 `images/`**
      - **📁 `masks/`**
      - 📄 `annotation.coco.json` – File di annotazione in formato COCO per test set.  
    - **📁 `train/`**
      - **📁 `images/`** - Contenente immagini MRI in formato JPG
      - **📁 `masks/`** - Contenente maschere binarie in formato JPG
      - 📄 `annotation.coco.json` – File di annotazione in formato COCO per train set. 
    - 🐍 `generateAnnotationsCoco.py` – Script per convertire immagini, categorie e maschere PNG in formato COCO.  
    - 🐍 `visualizzaMaschereRLE.py` – Script per visualizzare immagini random dalle annotazioni COCO con maschera ricostruita per validare la conversione generata. 

- **📁 `model/`**  
  - Modello Mask R-CNN addestrato (`model_final.pth`).  
  - Configurazioni e parametri associati.

- **📁 `report/`**  
  - 📄 `documentazioneSistemiMultimediali.pdf` – Documentazione completa del progetto.  
  - 📊 `report_inferenza_testset.ods` – Report completo sull’inferenza sul test set, con risultati immagine per immagine e metriche aggregate.

- **📁 `colab/`**  
  - 📓 `tumor_segmentation_colab.ipynb` – Notebook eseguito su Google Colab contenente l’intero workflow del progetto:  
    - Setup ambiente 
    - Training del modello  
    - Script per inferenza e analisi dei risultati  
    - Salvataggio modello e report in CSV

- **📁 `detectron2/`**  
  - Versione della libreria Detectron2 utilizzata, oppure il file `requirements.txt` con tutti i pacchetti necessari.  
  - Link ufficiale Detectron2: [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)

## 🛠️ Requisiti
- Python 3.9+  
- Detectron2  
- OpenCV  
- NumPy  
- COCO API  
- matplotlib  

## 📑 Dataset
- Dataset originale: [BRISC2025 su Kaggle](https://www.kaggle.com/datasets/briscdataset/brisc2025)  
- Conversione in formato COCO + RLE disponibile nella cartella `/BRISC2025/` con script dedicato.

## 📈 Risultati
- **IoU media:** 0.8189  
- **Dice coefficient:** 0.8857  
- **Specificity:** >0.99  
- Report completo disponibile in `/report/`.

## ✍️ Documentazione
Il report completo del progetto è disponibile nella cartella `/report/`, e include:  
- Metodo  
- Pipeline dati  
- Dettaglio architettura  
- Risultati e analisi  
- Discussione critica e proposte future  

## 🚀 Getting Started
Per riprodurre il progetto:  
1. Clonare il repository.  
2. Installare i requisiti (`pip install -r requirements.txt` oppure configurare tramite il notebook Colab).  
3. Eseguire gli script di conversione e visualizzazione presenti in `/dataset/` per verificare la correttezza delle annotazioni.  
4. Avviare il training tramite il notebook in `/colab/` oppure tramite gli script Python in `/scripts/`.  
5. Eseguire inferenza e valutazione utilizzando il modello salvato in `/model/`.
