import cv2
from vidgear.gears import CamGear

# youtube-dl ve vidgear kütüphanelerini indirmelisiniz.
options = {"CAP_PROP_FRAME_WIDTH ": 320, "CAP_PROP_FRAME_HEIGHT": 240, "CAP_PROP_FPS ": 60}
link = "https://www.youtube.com/watch?v=R0KCc9-0i6E"
stream = CamGear(source=link, y_tube=True, time_delay=1, logging=True,
                 **options).start()  # YouTube Video URL as input

while True:

    frame = stream.read()
    if frame is None:
        break
    cv2.imshow("Output Frame", frame)
    key = cv2.waitKey(30)

    if key == ord("q"):
        # Videoyu kapatmak için "q" tuşuna basmalısınız.
        break

cv2.destroyAllWindows()
stream.stop()
