# AmartyaCode

Project Overview -

This project automates the transcription and summarization of audio recordings from MacBook Voice Memos into detailed notes. The code processes audio files by converting them to a suitable format, segments them into manageable chunks, and uses an AI transcription model to convert speech into text. Subsequently, it automates the interaction with web-based ChatGPT-4 to refine and summarize the text into the aforementioned notes. The whole program is entirely automated and requires no user imput. 

How the code works
The program essentially boils down to 4 major, distinguishable components:- 
1) Audio file integration and formatting - The program starts by fetching the audio recordings stored on the MacBook. It moves these files into a folder named Amartyag as well as a backup folder in the event that there are any problems and then converts these files in Amartyag from their original format (.m4a) to .wav, preparing them for transcription by whisperAI an OpenAI, opensource transcription API which is extremely accurate, even with audio that is somewhat unclear or too soft. 
2) Transcription -  The second component of the model is  OpenAI's Whisper model, which  transcribes the audio files. Before this, the audio file is split into 10-minute chunks to manage the character limits of input of AI software like ChatGPT. The transcribed files are printed for reference as well as saved as .txt files in a folder named Transcripts. It deletes the files in Amartyag as it transcribes them, effectively resetting itself.
3) Note Summarization - Using the pyautogui library in Python, the code then automates browser interactions by pasting the transcribed text into ChatGPT via a web interface. It deletes the .txt file in transcripts that are pasted and then waits for a set amount of time for the notes to be generated. The amount of time the program halts was determined by multiple trials to make the process as efficient as possible. Lastly, the ChatGPT-generated output is copied.
4) Export to Google Docs - The summarized notes are then automatically pasted into Google Docs, and formatted to ensure easy readability.

Limitations: - 
The main limitation of the program is its specificity to my system, this specificity is a product of the inability to use ChatGPT and other AI systems as APIs at the time of writing this code due to the requirement of API tokens which have to be purchased. This limitation has now been addressed by the presence of many powerful offline models with no character input limitations such as Meta's Llama. 

Future Improvements: - 
1) Integration with Offline AI Models - Addressing the current limitations, future renditions of the program will explore the integration with offline AI models like Meta's LLaMA. This will allow the application to be less dependent on web-based AI, reducing the need for manual token management, enhancing the universality of the script, and preventing the need for splitting the audio file due to the elimination of the maximum characters of input limitation.
2) App Development: I plan on working towards the development of an app using the base structure of the code provided over the summer with the hopes that this program can help many students like me who have difficulty multitasking in lectures. 


