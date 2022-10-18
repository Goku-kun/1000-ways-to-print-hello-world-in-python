import qrcode
import cv2

text = "hello world"
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(text)
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white")
img.save('hello_world.png')

image = cv2.imread('hello_world.png')
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None:
  print(data)
else:
  print("Data corrupted")
