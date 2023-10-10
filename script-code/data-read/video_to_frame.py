import cv2
import glob

vid_num = 4  # degistir
input_video_file = "./data/"
output_folder = "./data_output/"

for video_file in glob.glob(input_video_file + "*.mp4"):

    vid_num += 1
    cap = cv2.VideoCapture(video_file, cv2.CAP_FFMPEG)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    frame_num = 0
    counter = 0

    # frame width, height = 1920, 1080
    while cap.isOpened():
        ret, frame = cap.read()

        counter += 1
        if ret == True:
            if counter % 10 == 0:
                frame_num += 1
                frame = cv2.resize(frame, (1280, 736), interpolation=cv2.INTER_AREA)  # obj detections!!!!
                # height, width, layers = frame.shape
                # dh, dw, _ = frame.shape
                # img_size = (width, height)
                print('Frame #: ', frame_num)

                filename = str(output_folder) + "data" + str(vid_num) + "_%d.jpg" % frame_num;
                cv2.imwrite(filename, frame)

        if (ret != True):
            break

    cap.release()
    print("Done!")
