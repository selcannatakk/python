import aspore.words as aw
import glob
import os
from PIL import Image

doc = aw.Document()
builder = aw.DocumentBuilder(doc)
# builder.writeln("Hello Aspose.Words for Python via .NET")

input_dir = './data'
for file in glob.glob(input_dir + "*.jpg"):
    Image.open(file).save("./newdata/" + file + ".bmp")
    print(file)
