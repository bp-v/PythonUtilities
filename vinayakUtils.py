import os
import json
import io


# Directory of the script being run
directory_of_script = os.path.dirname(os.path.abspath(__file__))

print("directory_of_script: ", directory_of_script)


# Current working directory
current_working_directory = os.path.abspath(os.getcwd())

print("current_working_directory: ", current_working_directory)


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

