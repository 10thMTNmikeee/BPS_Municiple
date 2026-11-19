import pymupdf
from pathlib import Path

dir = Path(__file__).resolve().parent.parent / '02_RENDERS'


files = [
    "BPS_EAST_01.jpg",
    "BPS_WEST_01.jpg",
    "ATL_BPS01_MECH.pdf",
    "gswc-standard-drawings-pg89.pdf",
    "gswc-standard-drawings-pg91.pdf",
    "gswc-standard-drawings-pg92.pdf"
]

merged_pdf = pymupdf.open()

for file in files:
    doc = pymupdf.open(dir / file)
    if file.lower().endswith(".jpg"):
        pdf_bytes = doc.convert_to_pdf()
        img_pdf = pymupdf.open("pdf", pdf_bytes)
        merged_pdf.insert_pdf(img_pdf)
    else:
        merged_pdf.insert_pdf(doc)

merged_pdf.save("Booster_Pump_Station.pdf")