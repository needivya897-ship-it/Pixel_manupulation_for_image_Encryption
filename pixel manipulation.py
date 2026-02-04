[04/02/26, 12:05:18 AM] Harini Hostel: Pixel Manipulation for Image Encryption

 Project Description
This project implements a *simple image encryption and decryption tool* using *pixel manipulation techniques*.  
Each pixel value of an image is modified using a mathematical operation with a secret key to protect the image data.

This project is developed as *Task-02: Pixel Manipulation for Image Encryption*.

---

Objectives
•⁠  ⁠To understand pixel-level image processing  
•⁠  ⁠To encrypt an image using a secret key  
•⁠  ⁠To decrypt the encrypted image back to its original form  

---

 Technologies Used
•⁠  ⁠*Python*
•⁠  ⁠*Pillow (PIL)* – Image handling
•⁠  ⁠*NumPy* – Pixel manipulation

---

 Encryption & Decryption Logic
•⁠  ⁠*Encryption:*  
  Each pixel value is increased by a secret key  
•⁠  ⁠*Decryption:*  
  The same key is subtracted from each pixel  
•⁠  ⁠Pixel values are kept within *0–255* using modulo operation  

---

 Project Structure
[04/02/26, 12:06:18 AM] Harini Hostel: ---

 How to Run the Project
 Install Required Libraries
```bash
pip install pillow numpy
[04/02/26, 12:06:28 AM] Harini Hostel: python image_encryption.py
[04/02/26, 12:06:36 AM] Harini Hostel: Encryption completed. Encrypted image saved.
Decryption completed. Decrypted image saved.
[04/02/26, 12:06:53 AM] Harini Hostel: input_image.png – Original image
encrypted_image.png – Encrypted image (distorted)
decrypted_image.png – Original image restored