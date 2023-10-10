import cv2
import math

vid_num = 1 # degistir
input_video_file = "new_videos_for_training/fe8ddb210f87420f8c00555023213ed9.mp4"
output_folder = "./p/"

cap=cv2.VideoCapture(input_video_file, cv2.CAP_FFMPEG)
fps = cap.get(cv2.CAP_PROP_FPS)

# video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

frame_num = 1050
counter = 0

while cap.isOpened():
    ret, frame = cap.read()

    counter += 1

    if ret == True:
        if counter % 3 == 0:

            frame_num += 1
            # Create ROI coordinates
            # topLeft = (737, 657)
            # bottomRight = (1603,1579)
            # topLeft = (752, 529)
            # bottomRight = (1422,1055)

            # kırmızı yer olan alanın
            # topLeft = (995, 839)
            # bottomRight = (2519,1901)

            # topLeft = (445, 349)  # kırmızı sol
            # bottomRight = (1213, 905)

            topLeft = (1205, 409)  # kırmızı sag
            bottomRight = (1781,865)

            # topLeft = (1325, 1055)  # kırmızı sag asagi
            # bottomRight = (2477,1893)

            # topLeft = (895, 483)  # kırmızı yukari
            # bottomRight = (1633,1221)

            # topLeft = (19, 479)  # yesil sol
            # bottomRight = (1191,1333)

            # topLeft = (1671, 323)  # yesil sağ
            # bottomRight = (1993, 633)

            x, y = topLeft[0], topLeft[1]
            w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

            # Grab ROI with Numpy slicing
            ROI = frame[y:y + h, x:x + w]

            """
             INTER_NEAREST – a nearest-neighbor interpolation 
             INTER_LINEAR – a bilinear interpolation (used by default) 
             
             INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation,
             as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method. 
              
             INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood 
             INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood
             """

            frame = cv2.resize(ROI, (416, 416), interpolation=cv2.INTER_AREA) # obj detections!!!!
            # height, width, layers = frame.shape
            # dh, dw, _ = frame.shape
            # img_size = (width, height)
            print('Frame #: ', frame_num)

            filename= str(output_folder) + "reflective_coveralls" + "%d.jpg" % frame_num;  #
            cv2.imwrite(filename,frame)


    if(ret != True):
        break

cap.release()
print("Done!")