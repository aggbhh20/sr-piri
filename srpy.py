#Teknofest icin aggbhh20 tarafindan yazildi(toplantiyi unuttugum icin pardon)
import speech_recognition as sr
#speechrecognition libini importluyo
srRec = sr.Recognizer() #sr libinin recognizer functionunu cagiriyo
print("recognized")
smbm = sr.AudioFile("smbmbutai.wav")#dosyayi aliyo(.wav)
print("got wav file")
with smbm as source:
    audio = srRec.record(source) #audio yu initliyo
recdaudio = srRec.recognize_google(audio) #printlemek için var a atiyo
print(recdaudio)#cevirilmis audioyu printliyo
print("should have reccd audio")
