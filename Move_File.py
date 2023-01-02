import shutil
import os

source = "C:/Users/frank/Desktop/Byjus Coding Proffesional/Extracted/PRO-C111/Universe"
destination = "C:/Users/frank/Desktop/Byjus Coding Proffesional/Extracted/PRO-C111/Document_Files"

files = os.listdir(source)

for file_name in files:
  name, extension = os.path.splitext(file_name)

  if extension == '':
      continue
  if extension in ['.txt', '.pdf', '.doc', '.docx']:
      path1 = source + '/' + file_name
      path2 = destination + '/' + "Document_Files"
      path3 = destination + '/' + "Document_Files" + '/' + file_name
      if os.path.exists(path2):
        print("Moving " + file_name + ".....")
        shutil.move(path1, path3)

      else:
        os.makedirs(path2)
        print("Moving " + file_name + ".....")
        shutil.move(path1, path3)