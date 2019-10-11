#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import azure.cognitiveservices.speech as speechsdk
import json
# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
class speechToText_MS():
    def __init__(self, sub_key, service_region):
        
        
        self.__sub_key = sub_key
        self.__region = service_region
        
       


        
        # Creates a recognizer with the given settings
        speech_config = speechsdk.SpeechConfig(subscription=sub_key, region= service_region)

        # Starts speech recognition, and returns after a single utterance is recognized. The end of a
        # single utterance is determined by listening for silence at the end or until a maximum of 15
        # seconds of audio is processed.  The task returns the recognition text as result. 
        # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
        # shot recognition like command or query. 
        # For long-running multi-utterance recognition, use start_continuous_recognition() instead.

        self.__speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        print("Say something...")
       
        self.__cmd = { "past": "XDas",
                       "now": "default",
                       "1": "Home.",
                       "2": "Company.",
                       "3": "Play."
                     }

    # Checks result.
    def start(self):
        self.__result = self.__speech_recognizer.recognize_once()
        temp = self.__result.text
        if temp == self.__cmd['1'] or temp == self.__cmd['2'] or temp == self.__cmd['3']:
            self.__cmd['now'] = temp
            data = self.__result.json
            if self.__cmd['now'] != self.__cmd['past']:

                # debugging

                print("Recognized: {}".format(temp)) 


                # end debugging

                self.__cmd['past'] = self.__cmd['now']
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    

        
#Testing voice cmd
'''
key = "344213864bc24fb5ab30081d44ba1f15"
region = "westus"
voice_WC = speechToText_MS(key, region)

while(1):
    voice_WC.start()
'''

#End testing
'''
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))

elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))



# Outputing *.json file 

data = result.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
'''



