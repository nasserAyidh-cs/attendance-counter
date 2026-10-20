from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

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

    # اسم الدالة المسؤولة عن قراءة XML
    #  وتحليل بنيته
tree = ET.parse(annotation_paths[0])
root = tree.getroot()
head_objects = root.findall("object")

print("Annotated heads in first image:", len(head_objects))

image_path = Path("data/raw/SCUT_HEAD_Part_A/JPEGImages/PartA_00000.jpg")
image = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(image)

for head in head_objects:
    box = head.find("bndbox")

    xmin = int(box.findtext("xmin"))
    ymin = int(box.findtext("ymin"))
    xmax = int(box.findtext("xmax"))
    ymax = int(box.findtext("ymax"))

    draw.rectangle((xmin, ymin, xmax, ymax), outline="lime", width=2)

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

output_path = output_dir / "PartA_00000_annotated.jpg"
image.save(output_path)

print("Saved:", output_path)
