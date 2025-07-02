import os
import random
import json
from PIL import Image
import matplotlib.pyplot as plt
from pycocotools import mask as mask_utils
import numpy as np

base_path = r"B:\Dataset Brain Tumor 3 Tipi\brisc2025\segmentation_task"
split = 'train'

images_dir = os.path.join(base_path, split, "images")
annotation_file = os.path.join(base_path, split, "annotation.coco.json")

# Carica annotazioni COCO
with open(annotation_file, 'r') as f:
    coco = json.load(f)

# Prendi un'immagine random
image_info = random.choice(coco['images'])
image_id = image_info['id']
file_name = image_info['file_name']

# Carica immagine
img_path = os.path.join(images_dir, file_name)
img = Image.open(img_path)

# Trova annotazioni per questa immagine
annots = [a for a in coco['annotations'] if a['image_id'] == image_id]

# Visualizza immagine e maschere
plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.axis('off')

for annot in annots:
    rle = annot['segmentation']
    mask = mask_utils.decode(rle)
    plt.imshow(mask, alpha=0.4, cmap='jet')

plt.title(f"Image: {file_name} with {len(annots)} mask(s)")
plt.show()
