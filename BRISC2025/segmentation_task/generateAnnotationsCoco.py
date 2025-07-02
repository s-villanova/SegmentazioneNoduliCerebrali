import os
import json
import numpy as np
from PIL import Image
from pycocotools import mask as mask_utils
from datetime import datetime

base_path = r"B:\Dataset Brain Tumor 3 Tipi\brisc2025\segmentation_task"

category_map = {
    'me': {'id': 1, 'name': 'Meningioma'},
    'gl': {'id': 2, 'name': 'Glioma'},
    'pi': {'id': 3, 'name': 'Pituitario'}
}

info = {
    "year": 2023,
    "version": "1",
    "description": "BRISC2025 tumor segmentation dataset",
    "contributor": "",
    "url": "",
    "date_created": datetime.now().isoformat()
}

licenses = [{
    "id": 1,
    "url": "https://creativecommons.org/licenses/by/4.0/",
    "name": "CC BY 4.0"
}]

categories = [
    {"id": v['id'], "name": v['name'], "supercategory": "tumor"}
    for v in category_map.values()
]

def create_coco_annotation(split):
    split_path = os.path.join(base_path, split)
    images_dir = os.path.join(split_path, "images")
    masks_dir = os.path.join(split_path, "masks")

    coco = {
        "info": info,
        "licenses": licenses,
        "categories": categories,
        "images": [],
        "annotations": []
    }

    image_files = sorted([f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

    annotation_id = 0
    image_id = 0

    for img_file in image_files:
        category_id = None
        for key in category_map:
            if f"_{key}_" in img_file.lower():
                category_id = category_map[key]['id']
                break
        if category_id is None:
            print(f"Skipping file {img_file} because category not found")
            continue

        img_path = os.path.join(images_dir, img_file)
        mask_path = os.path.join(masks_dir, img_file)  # Usa stesso nome di file

        if not os.path.exists(mask_path):
            print(f"Mask not found for image {img_file}, skipping")
            continue

        with Image.open(img_path) as im:
            width, height = im.size

        coco['images'].append({
            "id": image_id,
            "license": 1,
            "file_name": img_file,
            "height": height,
            "width": width,
            "date_captured": None
        })

        mask = np.array(Image.open(mask_path).convert('1'), dtype=np.uint8)

        rle = mask_utils.encode(np.asfortranarray(mask))
        rle['counts'] = rle['counts'].decode('utf-8')

        area = mask_utils.area(rle)
        bbox = mask_utils.toBbox(rle)

        coco['annotations'].append({
            "id": annotation_id,
            "image_id": image_id,
            "category_id": category_id,
            "segmentation": rle,
            "area": float(area),
            "bbox": [float(x) for x in bbox],
            "iscrowd": 0
        })

        annotation_id += 1
        image_id += 1

    output_file = os.path.join(split_path, 'annotation.coco.json')
    with open(output_file, 'w') as f:
        json.dump(coco, f, indent=2)

    print(f"Created COCO annotation for {split} with {len(coco['images'])} images and {len(coco['annotations'])} annotations.")

if __name__ == "__main__":
    create_coco_annotation('train')
    create_coco_annotation('test')
