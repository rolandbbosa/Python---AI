import whisper

model = whisper.load_model('base')
result = model.transcribe('AUDIO_FILE')
file = open('i.txt', 'w')
words = result['text']
file.write(words)
print(words)