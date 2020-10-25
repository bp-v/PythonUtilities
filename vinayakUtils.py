import os
import io
import json


def get_script_directory():
  # Directory of the script being run
  # directory_of_script = os.path.dirname(os.path.abspath(__file__))
  return os.path.dirname(os.path.abspath(__file__))


def get_current_working_directory():
  # Current working directory
  # current_working_directory = os.path.abspath(os.getcwd())
  return os.path.abspath(os.getcwd())


def loadFile(filename):
  text = ""
  with io.open(filename, 'r', encoding='utf8') as f:
    text = f.read()
  return text


def saveFile(filename, text):
  with io.open(filename, 'w', encoding='utf8') as f:
    f.write(text)
    
    
def saveJsonToFile(filename, data_dict):
  # data is generally a dict
  text = json.dumps(data_dict, sort_keys=False, indent=4)
  saveFile(filename, text)
  
  
def loadJsonToFile(filename):
  text = loadFile(filename)
  return json.loads(text)

