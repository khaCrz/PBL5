from django.shortcuts import render
import os
import speech_recognition as sr
from .models import FileWav
from django.http import JsonResponse
import pyrebase

Key = {
  "type": "service_account",
  "project_id": "smartglasses-1653630452006",
  "private_key_id": "69ffc73b82575710f68519f693ca07b28a9048f9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDFWUAPCEh+0T6Q\nBov0mgtzMcer5WFbUPsXujE/DoJeXGvRzwhUdDOe62va18iJq9VJTNII0xtttCFk\n9fYVp9jrv9Kq2ZnQ7qiHc0uDnrvkw9lrJbRBFkn/HoOJVkOaclxzldZx+MGjFhXw\n3Q2r1whhON54shL1+DGA14czSDlGYaNp5o6S09YKXmb56y+pxCwV3jGQDdjv3iEQ\nTyhwDFKoK5fLB8todvwEdI5XDF/ncfYiWzo7p/DsKZMJuZX+88wfthQVJWIJiqcg\nuJdjhB1oDLW1+FI3Co1s2Ei0XuS6C96opnXuiGBjlwVWmvwbTKcNzV+ufFowym/u\nAAhITqyvAgMBAAECggEALkYiLiQsE4hu2gie8ojYXHd0sUrEzEutxL+E4ps9WHDl\nWznnYx4oKIBdNuBYBmgDR/+6VBVkHhIZrnm57RQBWi4NcMA7P/FmFPSk5UToG9kM\ndwJNROG8EhUOlLpkeaeNJBEjSnAgv2PjWyoKFZwDPADAsZ5XsdMzkFl5Oz4ZJ/Y9\nmAFoC2hc9Z6MBVrhUiMFId8GMf+OdsCywGJArwME8fiQGGtJLhsJrZI4HYFE5y9E\nNQi5S5SSFmuPU+gL+6ZMnJybeXFr/XfQ9JKgsaV4hlZxZ8o8tUpou6bAbDK7RnaV\nyNYdo5ESFDWl/k6liVTtEDQHwQSOhMjbezur037VkQKBgQDjGK9zvBOa1AWUlMeC\nisa+EEC5GQNpaj8cpiHNlOT0Hgt5qVrzUMPN+82TuHwUhkTFb4PjZN6UCgoQM6qR\nj1u5Eb1bYhiZVRvcgUEkpI1Qc8vdmEDi68+qjR9K9ndkUl0jtsI+mVTFmbeuhgY1\nsbjOiG1y33k+HZxwKeHu3Jm51wKBgQDed1CGl8XW27rVS56K1h4Tu0ebzGwzNgE2\nzp1aTUpBDZtpEHoGIbmdI8IfMM6ow0dr93HDavRh0IUzx/V20npEWaqwXnk6NHYD\ntQODZoSu3vruKzdige+8m2VLdQ01uBkk8IbvHvsrawDnXcXWsE3jQ5HeoYcXMCkD\nesPfbX646QKBgDcmy5Vj268CRsiqyTke0t1dvRo2xOlY8DLY9eSjgGb41Pia9Iea\n2bKwsGBrsVaatSDt0C3tVVDGj2MX6RiopDHx6PbEgAzc6oNGsLdhbyBWvu/2BewW\nMLzOwQbHjH9EsXH29H2XZ0sF5eHwkpl/q84cu9fmBd/b+R4UTdZgpMTJAoGBAM/3\n1m2cYLSVQTm4sYO02vUzNKQvHE9bgxMLYApVCr95yvkTEB+/U1fVX9nstKULuS7z\naYR37fGrD3ryyUPFS8utz2WFS+rftBuPErO6GPupNAeGmwYZ1lYJJ069JBY9/jOM\nL3hHDCLwqy2feh1TP9zfA/SOKE3DFfRMxeOO5tJRAoGAfipLUvxL/YdXtpk4wjMw\nrWTFkbjrhXZV49fl0OLbvKopa92WCcK3idq4rfwYK58JSOKHW7VdOL8qj1HnPb19\ntnebNZyvQI9c14K9C9U0hcpqIBcM73tqFfP+iEE22KedcOtacZUshc1ptPGVyiNh\n2/oL34Ue1J0sZT7hFzU5rX4=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-73lyv@smartglasses-1653630452006.iam.gserviceaccount.com",
  "client_id": "116125344421528621075",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-73lyv%40smartglasses-1653630452006.iam.gserviceaccount.com"
}

config  = {
  "apiKey": "AIzaSyAVU8V2XXwZd6qsQFVYYqZh-6sL06oePVY",
  "authDomain": "smartglasses-1653630452006.firebaseapp.com",
  "databaseURL" : "https://smartglasses-1653630452006-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "smartglasses-1653630452006",
  "storageBucket": "smartglasses-1653630452006.appspot.com",
  "messagingSenderId": "237921897116",
  "appId": "1:237921897116:web:b9f58cd783e76ec7603b59",
  "measurementId": "G-HR984XK0FN",
  "serviceAccount" : Key
}
FileWav.objects.all().delete()
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_on_local = '/content/drive/MyDrive/PBL5/DoAnPBL5/'
path_on_cloud = 'untitled1.wav'
# Create your views here.
def Home(request):
    return render(request, 'home.html', {})

def GetTextFromVoice(url):
    recognizer = sr.Recognizer() 
    fileInput = sr.AudioFile(url)
    with fileInput as source:
        recognizer.adjust_for_ambient_noise(source)
        captured_audio = recognizer.record(source)
    try:
        txt = recognizer.recognize_google(captured_audio)
        return (txt)
    except Exception as e:
        return ("Sorry I understand!")

def GetText(request):
    name = request.GET.get('name')
    print(name)
    file = FileWav.get_file_by_name(name)
    
    storage.child(file.name).download(file.name,file.name)
    Path = os.path.abspath(file.name)
    # Text = GetTextFromVoice(Path)
    
    #get all file
    data = {}
    data['Files'] = file.name
    data['Text'] = Path
    return JsonResponse(data, safe=False)



def Main(request):
  all_files = storage.list_files()
  ListFile = []
  for file in all_files:
    file = FileWav(name = file.name)
    if file.isExists():
      continue
    else:
      file.Save()
  ListFile = FileWav.objects.all()
  data = {}
  data['ListFiles'] = ListFile
  return render(request, 'main.html', data)