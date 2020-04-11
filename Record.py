import soundfile as sf
import sounddevice as sd
def sync_record(filename, duration, sr, channels):
    print('recording')
    my_rec = sd.rec(samplerate=sr, channels=channels, frames=int(duration*sr))
    sd.wait()
    sf.write(filename, data=my_rec, samplerate=sr)
    print('done recording')
sync_record("record.wav", 10, 22050, 1)
