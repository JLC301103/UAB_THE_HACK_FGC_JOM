from gtts import gTTS
import os
particle=""
"""if :
  particle="un asiento"
elif :
  particle="una maquina de billetes"
elif :
  particle="la puerta del tren"
elif :
  particle="escaleras"
elif :
  particle="personas"
else :"""

particle = "o nada, o un objeto sin identificar o irrelevante."
text = "Delante tienes "+particle+"."
tts = gTTS(text=text, lang='es')

# Save the speech to a file
tts.save("output.mp3")

# Play the converted file (this works on most operating systems)
os.system("start output.mp3")
