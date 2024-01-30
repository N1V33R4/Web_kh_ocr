from django.http import HttpResponse
from django.shortcuts import render

from PIL import Image
import pytesseract

def show_form(request):
  context = {}
  return render(request, 'form.html', context)

def run_ocr(request):
  img = request.FILES['image']
  print(type(img.file))
  img = Image.open(img.file)
  
  config = r'-l khm+eng --psm 4'
  config = r'-l khm+eng'
  res = pytesseract.image_to_osd(img)
  res += '\n' + pytesseract.image_to_string(img, config=config)
  
  return HttpResponse(res)
