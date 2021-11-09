# Real-time-object-detection-using-RTSP
Get RTSP stream data from any IPCamera and use it for real-time object detection.

Download YOLOv3 weights from https://pjreddie.com/darknet/yolo/

You can also use YOLOv4, just rename the files in code rest remains same.

## Setup:
1. You shoul have latest opencv 4 installed `pip install opencv-contrib-python`, if you have opencv-python in local, uninstall it as it contradicts with the latest package. Use command `pip uninstall opencv-python` to remove.
2. Add your RTSP stream URL in `camera.py` file. Here I have used multi-threaded camera setup to have better processing.
3. Run `python Object-Detection.py`

*Happy Coding !*
