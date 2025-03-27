# import qrcode
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# def generate_qr(data, filename="qr_code.png"):
#     """Generate a QR code from given data and save as an image."""
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code (1 = 21x21 matrix)
#         error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
#         box_size=10,  # Size of each QR box
#         border=4  # Border thickness
#     )
#     qr.add_data(data)
#     qr.make(fit=True)

#     qr_img = qr.make_image(fill="black", back_color="white")
#     qr_img.save(filename)
#     print(f"✅ QR Code generated and saved as {filename}")

# def decode_qr(image_path):
#     """Decode a QR code from an image file."""
#     img = cv2.imread(image_path)
#     qr_codes = decode(img)
    
#     if not qr_codes:
#         print("⚠️ No QR Code found in the image!")
#         return
    
#     for qr in qr_codes:
#         data = qr.data.decode("utf-8")
#         print(f"🔍 Decoded QR Data: {data}")

# def main():
#     while True:
#         print("\n📌 QR Code Encoder/Decoder")
#         print("1️⃣ Generate QR Code")
#         print("2️⃣ Decode QR Code")
#         print("3️⃣ Exit")
        
#         choice = input("👉 Choose an option (1/2/3): ").strip()
        
#         if choice == "1":
#             data = input("📝 Enter data to encode in QR: ")
#             filename = input("💾 Enter filename (or press Enter for default 'qr_code.png'): ").strip() or "qr_code.png"
#             generate_qr(data, filename)
        
#         elif choice == "2":
#             image_path = input("📂 Enter path to QR code image: ")
#             decode_qr(image_path)
        
#         elif choice == "3":
#             print("👋 Exiting program. Goodbye!")
#             break
        
#         else:
#             print("⚠️ Invalid choice! Please enter 1, 2, or 3.")

# if __name__ == "__main__":
#     main()

import qrcode
import cv2
import numpy as np

def generate_qr(data, filename="qr_code.png"):
    """Generate a QR code from given data and save as an image."""
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 = 21x21 matrix)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each QR box
        border=4  # Border thickness
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.save(filename)
    print(f"✅ QR Code generated and saved as {filename}")

def decode_qr(image_path):
    """Decode a QR code from an image file using OpenCV."""
    img = cv2.imread(image_path)
    
    # Initialize OpenCV QRCodeDetector
    detector = cv2.QRCodeDetector()
    
    # Detect and decode the QR code
    data, pts, qr_code = detector(img)
    
    if data:
        print(f"🔍 Decoded QR Data: {data}")
    else:
        print("⚠️ No QR Code found in the image!")

def main():
    while True:
        print("\n📌 QR Code Encoder/Decoder")
        print("1️⃣ Generate QR Code")
        print("2️⃣ Decode QR Code")
        print("3️⃣ Exit")
        
        choice = input("👉 Choose an option (1/2/3): ").strip()
        
        if choice == "1":
            data = input("📝 Enter data to encode in QR: ")
            filename = input("💾 Enter filename (or press Enter for default 'qr_code.png'): ").strip() or "qr_code.png"
            generate_qr(data, filename)
        
        elif choice == "2":
            image_path = input("📂 Enter path to QR code image: ")
            decode_qr(image_path)
        
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
