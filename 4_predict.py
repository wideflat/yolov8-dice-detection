import os
import random
from ultralytics import YOLO
from PIL import Image
import cv2

# pick random picture
dir = 'valid/images'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir, filename)

# load best model
model = YOLO("runs/detect/train/weights/best.pt")

# predict
results = model.predict(source=path, save=False,  conf=0.5)

# show result
res_plotted = results[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey(0)
cv2.destroyAllWindows() 