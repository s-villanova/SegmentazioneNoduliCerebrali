# SegmentazioneNoduliCerebrali con Mask R-CNN – BRISC2025

## ⚠️ Disclaimer
Questo repository è condiviso esclusivamente a scopo **didattico e di ricerca**, senza alcun fine commerciale.

Il dataset incluso è il risultato di una rielaborazione del dataset pubblico **BRISC2025** disponibile su Kaggle.  
Le annotazioni in formato **COCO**, incluse le maschere codificate tramite **Run-Length Encoding (RLE)**, sono state **interamente generate dal gruppo che contribuisce a questo progetto**.  
Non sono fornite dagli autori del dataset originale, ma create tramite uno script di conversione sviluppato appositamente, con l’obiettivo di rendere il dataset pienamente compatibile con il framework **Detectron2** per il task di segmentazione.
Le immagini sono state caricate per consentire la completa riproducibilità del progetto.  
**Qualora gli autori originali o la piattaforma Kaggle ne richiedessero la rimozione, il dataset sarà immediatamente eliminato dal repository e sostituito con una guida dettagliata per la generazione autonoma del dataset nel formato utilizzato in questo progetto.**


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
    - 🐍 `generateAnnotationsCoco.py` – Script per convertire immagini, categorie e maschere JPG in formato COCO.  
    - 🐍 `visualizzaMaschereRLE.py` – Script per visualizzare immagini random dalle annotazioni COCO con maschera ricostruita per validare la conversione generata. 

- **📁 `model/`**
  - **📁 `augmented/`** - contenente modello addestrato ed eventi visualizzabili in TensorBoard
  - **📁 `augmented_eval/`**  - contenente evaluation di COCOEvaluator

- **📁 `report/`**  
  - 📄 `DocumentazioneSistemiMultimediali.pdf` – Documentazione completa del progetto.  
  - 📊 `report_inferenza_testset.ods` – Report completo dell’inferenza sul test set, con metriche generali e aggregate per classe.

- **📁 `colab/`**  
  - 📓 `tumor_segmentation_colab.ipynb` – Notebook eseguito su Google Colab contenente l’intero workflow del progetto:
    - Script per montare una cartella di google drive in ambiente Colab
    - Setup ambiente
    - Script per estrazione di eventuali file .zip
    - Registrazione istanze COCO
    - Script debug per validare mapper e augmentation usati in training
    - Training del modello
    - Script per evaluation con COCOEvaluator
    - Script per eseguire inferenza su un'immagine caricata dal proprio PC
    - Script Gradio per testing modello
    - Script per inferenza e generazione report CSV
    - Script lettura report CSV e generazione report metriche aggregate CSV

- **📁 `detectron2/`**  
  - Versione della libreria Detectron2 utilizzata, con tutti i pacchetti necessari.  
  - Link ufficiale Detectron2: [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)

## 📑 Dataset
- Dataset originale: [BRISC2025 su Kaggle](https://www.kaggle.com/datasets/briscdataset/brisc2025)  
- Conversione in formato COCO disponibile nella cartella `/BRISC2025/` con script dedicato.

## 📈 Risultati
- **IoU media:** 0.8189  
- **Dice coefficient:** 0.8857  
- **Specificity:** >0.99  
- Report completo disponibile in `/report/`.

## ✍️ Documentazione
Il report completo del progetto è disponibile nella cartella `/report/`, e include:  
- Materiali e metodi
- Risultati quantitativi e qualitativi
- Discussione e Proposte future
- Report CSV inferenza su dataset di test
