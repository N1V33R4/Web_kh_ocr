from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import LiveWebCam


def show_cctv(request):
  context = {'title': 'Homepage'}
  return render(request, 'cctv.html', context)

def gen(camera: LiveWebCam):
  while True:
    frame = camera.get_img()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def livecam(request):
  return StreamingHttpResponse(gen(LiveWebCam()), content_type='multipart/x-mixed-replace; boundary=frame')
