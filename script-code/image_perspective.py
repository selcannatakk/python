import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

image = cv.imread('data/orjinal_door.jpg')
assert image is not None, "file could not be read, check with os.path.exists()"
rows,cols,ch = image.shape
print(rows,cols,ch)

#input için resimlerin köse koordinatlarını biz veriyoruz
input_pts = np.float32([[149,17],[665,97],[157,1213],[677,1153]])
#output için image köselerin max min degerleri göz önune alarak boyutu verıyoruz.
output_pts = np.float32([[0,0],[500,0],[0,500],[500,500]])

# M(matrix) -> [[1,0,tx],[0,1,ty]] tx ve ty kayma değerleri
# M = dönüsüm matrixi = cos0 -sin0
#                       sin0 cos0
M = cv.getPerspectiveTransform(input_pts,output_pts)

# yukarıdaki boyutla aynı olmasını ıstıyoruz goruntumuzun dogru gelmesi için
dst = cv.warpPerspective(image,M,(500,500))

#görsellestirme
plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

os.mkdir(os.path.join("./","perspective_images"))

img = cv.resize(dst, (500, 500), interpolation=cv.INTER_AREA)
filename = "./perspective_images"


cv.imwrite(filename, img)
plt.show()
