import cv2
from tools.OpenPose import OpenPose


if __name__ == "__main__":
    pose = OpenPose()

    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            continue

        people = pose.detect(frame)
        for person in people:
            pose.draw(frame, person)

        cv2.imshow("frame", frame)
        key_code = cv2.waitKey(1)
        if key_code in [27, ord('q')]:
            break
    camera.release()
    cv2.destroyAllWindows()
