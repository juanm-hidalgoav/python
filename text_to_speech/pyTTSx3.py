# works offline
import pyttsx3

text = '''
safety. said. sailing. same. say. schedule. school. science. scotland. sea. see. seen. semester. sentences. set. several. share. ship. shopping. short. sick. significance. significant. simple. since. sister. site. situated. situation. skills. sleep. small. smaller. snack. so. social. software. some. someone. something. sometimes. son. sounds. speaking. specialize. spend. spiritualities. spoken. sport. started. station. stop. stories. strategies. stress. students. studying. successful. sun. sure. systems.
'''

engine = pyttsx3.init()

""" RATE"""
engine.setProperty('rate', 115)    # setting up new voice rate

"""VOLUME"""
engine.setProperty('volume',0.7)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')    #getting details of current voice
engine.setProperty('voice', voices[0].id)    #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)    #changing index, changes voices. 1 for female

engine.say(text)
engine.save_to_file(text, 'text.mp3')
engine.runAndWait()
engine.stop()