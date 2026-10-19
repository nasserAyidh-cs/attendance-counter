from pathlib import Path
import xml.etree.ElementTree as ET

data_dir = Path("data/raw")

if not data_dir.is_dir():
    raise FileNotFoundError("Extract the dataset into data/raw first.")

image_paths = sorted(data_dir.rglob("*.jpg"))
annotation_paths = sorted(data_dir.rglob("*.xml"))

print("Images:", len(image_paths))
print("Annotation files:", len(annotation_paths))

if image_paths:
    print("First image:", image_paths[0])

if annotation_paths:
    print("First annotation:", annotation_paths[0])
