# SegmentazioneNoduliCerebrali con Mask R-CNN – BRISC2025

## ℹ️ Nota sulla licenza dei dati
Il dataset incluso è distribuito secondo i termini della licenza **Creative Commons Attribution 4.0 International (CC BY 4.0)**, che consente la condivisione e l’adattamento per qualsiasi scopo, incluso quello commerciale, a condizione che vengano forniti i dovuti crediti agli autori originali.

## 🔍 Descrizione del progetto
Questo repository contiene un progetto per la segmentazione automatica di tumori cerebrali su immagini MRI, utilizzando un modello Mask R-CNN con backbone ResNet-50 + FPN implementato tramite la libreria Detectron2.

Il sistema è stato addestrato e testato sul dataset pubblico **_BRISC2025_**, convertito in formato COCO con segmentazioni pixel-wise codificate tramite **Run-Length Encoding (RLE)**.

## 📁 Contenuto del repository
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
    - Script per clonare repo github
    - Script per collegarsi a drive e salvare eventualmente una copia di backup
    - Setup per installare detectron2 pytorch e torchvision
    - Script per estrazione di eventuali file .zip
    - Script per registrazione istanze COCO
    - Script per Training del modello
    - Script debug per validare mapper e augmentation usati in training
    - Script per evaluation con COCOEvaluator
    - Script per visualizzare eventi training su TensorBoard
    - Script per eseguire inferenza su un'immagine caricata dal proprio PC
    - Script Gradio per testing modello
    - Script per inferenza e generazione report CSV
    - Script lettura report CSV e generazione report metriche aggregate CSV

- **📁 `detectron2/`**  
  - Versione della libreria Detectron2 utilizzata, con tutti i pacchetti necessari.  
  - Link ufficiale Detectron2: [https://github.com/facebookresearch/detectron2](https://github.com/facebookresearch/detectron2)

## 📑 Dataset
Il dataset utilizzato è **BRISC2025**, disponibile pubblicamente su Kaggle e distribuito sotto licenza **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

- Dataset originale: [BRISC2025 su Kaggle](https://www.kaggle.com/datasets/briscdataset/brisc2025)
- 🔗 Licenza originale: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
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
