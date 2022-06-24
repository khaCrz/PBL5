from django.shortcuts import render
import os
import speech_recognition as sr
from .models import FileWav
import pyrebase

Key = {
  "type": "service_account",
  "project_id": "voice-project-347310",
  "private_key_id": "59b772258c73af14b184633f54bff10774ce5840",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0A8M+e94iXKuV\nmy/u5VGDoqgFubz76QRTcaVfXh4ynHIBuPitA0wUj9bzT658LOTgbG4YbdWtGB2F\nqxsl4Zizsyd9Rebl6t+ZEM9uskiD+P7trapDthh6VaKwZkN+eA3AVckKvZmnia11\nimRCqzXK3DVjN4ojJrHs8uq2Ed2UoprmqGyMbf7zPl6ErYQvoXydZzpAlt9qShaX\nNKtjBFDLF4CHuIkoP+y649SmpfCCj/yVfIE6gy/V8ejmYLElsOn2qxYG3hoVKoq7\naT1sfE4ftcOHFMQuHwLGCiytgVHMBHXLE3QfzpwmgRJZutjKKyd0bGYlmJRmqs85\nlTKPgPo9AgMBAAECggEAMNr2kc43VtcUwFkqVKlLCrFJ7affqPSwNl9ZFP1rr6uy\n61HCt931t3zkRwugnNXoVhpHdPzWKZCqbn0mNI06Dsc4F/ExPcQVZCriSTY8pQie\nU243EAJrOURlj39poPi/Lqx5kB8uBQDCIWzqUge6ZTCHksJfjLOzRU4WMky9+NkF\nXAz3z89WAoBe7Li4AyZ2zRyDJ393F+9AuliArnozmEi9KfH5BGP1HG/NwEMnLR8s\nwdNRMRLelJbC1x+GhHie9ITdDh4SBvNaeLNiLONGjlQnnpnoO9iz9jW/t4tcUaho\nMR/u3NR96hp4ef2CypYcPArDHplA1l543aKFXiueRwKBgQDx2FWzjRgtRyoX6NAg\n2wBcPRdox9/dKQq9NChfvpHKXahhFvJ+Cy+yxoaNs7tXQifD9pmanKEq+ML37LSp\nj3VWBFnSNJGaUmz8W+BaimTMJZPsBR6ZnFAOV6ILhhzWehQaTJj/d4ga2GfMtQ/m\ng4s893gYd1b3mLniRU6sJgrONwKBgQC+jP90S8CeAtWYe1PWqb/kXvf+8/0Z4d/2\n/s/yC+8skpPTV6ftPjJAUy+vT6bHreOe6x/pikHaJ08s4V8XFLVsIjhBkbr0oY1T\nl3XnXNe7wYsXR3Jbrot57VIWeFgvVuiNKAwE093UNP/EQFPbnOAyiXY55kwKhvq+\n0sNejh7hKwKBgQClvP1WlF46QWfuhMWFjrBbhh5x13Bqj0Ll0UXN/7rH9ZF8IA7F\nJINmwDjcCY1cymCYInq4A5lL6rkq0RQqk7702Px5Wz9hhBVeiNRjGC7l3ObXu9Zx\nrTcL7TCHNzyyG22FbHL5uIAU7bONDZS9A+87M9kg40A9ZHQXRioZPeTv1wKBgFkL\nxuzv4Yl1xZ9GMr2kAfqUrsvD9Uk9Fs5z8XUpQpHPxakD04O4hv8sYKJKVKQHjNFd\nC0K1y2RI7mUIxMkick2gCC4MDhP30vV3WC/QYThqj7dHOhfCD4fg8XVys7Mbp/0e\n887lu0pJoiRx8z4zp0m2lzsjdfGNdmvqTkZHoAKVAoGAKSF2i/eGZyXFj06TaZLl\nZ3YjxVD12CiL1kH/TyDk171qqMRUdlF+IL2l82N31C7dLy6xi//b7k8KWcsZwH9E\nRsyklz8SWXf99pP/NQjuekgMNNO2Brk1iD50gi3ZfgWA+UNNTpg+lbPKbYTxa4sg\n9s4owH/+Hmpe+YlBsGtaVa4=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zwzsk@voice-project-347310.iam.gserviceaccount.com",
  "client_id": "104935961280783379901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zwzsk%40voice-project-347310.iam.gserviceaccount.com"
}


config  = {
  "apiKey" : "AIzaSyClu-uLdUaX1UIXS7jx0aqIHsLSj8EKrfw",
  "authDomain" : "voice-project-347310.firebaseapp.com",
  "databaseURL" : "https://voice-project-347310-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId" : "voice-project-347310",
  "storageBucket" : "voice-project-347310.appspot.com",
  "messagingSenderId" : "355231243743",
  "appId" : "1:355231243743:web:0e38399cd0ceea966e786a",
  "measurementId" : "G-C345ZZLNG7",
  "serviceAccount" : Key
}
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
        return ("You said: ' " + txt + " '")
    except Exception as e:
        return ("Sorry I understand!")

def GetText(request):
    id = request.GET.get('id')
    file = FileWav.get_file_by_id(id)
    storage.child(file.name).download(file.name,file.name)
    Path = os.path.abspath(file.name)
    #get all file
    data = {}
    data['Files'] = file
    data['Paths'] = Path
    return render(request, 'result.html', data)



def Main(request):
  # storage.child(path_on_cloud).download("untitled1.wav")
  # URL = path_on_local + "untitled1.wav"
  # print(GetTextFromVoice(URL))
  all_files = storage.list_files()
  ListFile = []
  for file in all_files:
    file = FileWav(name = file.name)
    if file.isExists():
      continue
    else:
      file.Save()
  ListFile = FileWav.objects.all()
  print(len(ListFile))
  data = {}
  data['ListFiles'] = ListFile
  return render(request, 'main.html', data)