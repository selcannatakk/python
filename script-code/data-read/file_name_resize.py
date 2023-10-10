import cv2
import os

# open images folder
image_folder = "../data/"
# output_folder = "../data-output/"
os.mkdir(os.path.join("./", "new_data"))
# get the frames one by one with order
count = 0
# for filename in sorted(os.listdir(image_folder), key=lambda x:float(re.findall("(\d+)",x)[0])):
for filename in os.listdir(image_folder):
    frame = cv2.imread(image_folder + "/" + filename)  # image_folder+"/"+filename)
    # print(image_folder + "/" + filename)
    # print("filename", filename)
    frame = cv2.resize(frame, (416, 416), interpolation=cv2.INTER_AREA)  # resize them (620X620)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     # be sure color

    filename = str(output_folder) + "/new_data%d.jpg" % count;
    count += 1
    cv2.imwrite(filename, frame)
    # cv2.imshow("filename", frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()  #closing all open windows
