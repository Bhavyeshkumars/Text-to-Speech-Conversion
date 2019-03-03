# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = "Kriti Sanon (born 27 July 1990) is an Indian actress who appears predominantly in Hindi films. Born and raised in New Delhi, she pursued an engineering degree from the Jaypee Institute of Information Technology, after which she briefly worked as a model. She made her acting debut with the Telugu psychological thriller 1: Nenokkadine (2014) and had her first Hindi film release in Sabbir Khan's action film Heropanti (2014), for which she won the Filmfare Award for Best Female Debut."

# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome1.wav") 
  
# Playing the converted file 
os.system("welcome1.wav")