import speech_recognition as sr
srRec = sr.Recognizer()
print("recognized")
smbm = sr.AudioFile("voice.wav")
print("got wav file")
with smbm as source:
    audio = srRec.record(source)
recdaudio = srRec.recognize_google(audio)
print(recdaudio)
print("should have reccd audio")
