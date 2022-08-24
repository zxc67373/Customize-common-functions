import base64
import cv2
import numpy as np
img = base64.b64decode()
encode_image = np.asarray(bytearray(img), dtype="uint8")  # 转换np序列
img_array = cv2.imdecode(encode_image, flags=cv2.IMREAD_GRAYSCALE)  # 转换Opencv格式BGR

def image_to_base64(image_np):
  image = cv2.imencode('.jpg', image_np)[1]
  image_base64 = base64.b64encode(image)
  return image_base64

image_path1 = 'm/aBFhNXI.png'
frame1 = cv2.imread(image_path1)
base64_data = image_to_base64(frame1)

