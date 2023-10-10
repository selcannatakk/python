import cv2
import os


class DataRead:
    def __int__(self, data_dir):
        self.data_dir = data_dir

    def read_image(self, image):

        count = 0
        for file in os.listdir(self.data_dir):
            image_path = os.path.join(self.data_dir, file)
            image = cv2.imread(image_path)
            cv2.imrite(os.path.join(self.data_dir + ".jpeg"), image)
            cv2.imshow('image', image)
            count + 1

    def read_video(self):
        count = 0
        for file in os.listdir(self.data_dir):
            # read video
            video_path = os.path.join(self.data_dir, file)

            video = cv2.VideoCapture(video_path)

            # visualize video
            ret = True
            while ret:
                ret, frame = video.read()

                if ret:
                    cv2.imshow('frame', frame)
                    cv2.waitKey(40)

        video.release()
        cv2.destroyAllWindows()

    def read_webcam(self):

        # read webcam
        webcam = cv2.VideoCapture(0)

        # visualize webcam

        while True:
            ret, frame = webcam.read()

            cv2.imshow('frame', frame)
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break

        webcam.release()
        cv2.destroyAllWindows()


DataRead.read_image("./data")
