import matplotlib.pyplot as plot
from scipy.io import wavfile

samplingFrequency,signalData=wavfile.read('audio.wav')
plot.subplot(211)
plot.title('Spectorgram of audio.wav')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')
plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show