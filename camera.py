from threading import Thread, Lock
import cv2


class CameraStream(object):
    def __init__(self, src='rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'):
        self.stream = cv2.VideoCapture(src)

        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()

        if __name__ == "__main__":
            cap = CameraStream().start()
            while True:
                frame = cap.read()
                cv2.imshow('webcam', frame)
                if cv2.waitKey(1) == 27:
                    break
            cap.stop()
            cv2.destroyAllWindows()
