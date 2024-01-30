import os
import cv2
import numpy as np


class LiveWebCam():
  def __init__(self) -> None:
    # RTSP (realtime streaming protocol)
    # rtsp://admin:pw@ip:port/.../channel

    self.vs = cv2.VideoCapture(0)

  def __del__(self):
    self.vs.release()

  def get_img(self):
    ret, img = self.vs.read()

    # convert to bytes to send to client
    _, jpeg = cv2.imencode('.jpg', img)

    return jpeg.tobytes()
  
