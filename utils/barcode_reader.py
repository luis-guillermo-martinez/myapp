import cv2
from pyzbar.pyzbar import decode

def read_barcode(image_path):
    image = cv2.imread(image_path)
    barcodes = decode(image)
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        return barcode_data
    return None
