#Documentation:

#load(save,all,line,alllines,create,createlines)
#
#save:savename as an string ('save.txt')
#all: returns all content(True/False)
#line: returns the content of 1 line starts at line 0 needs to be an intiger
#create:create save if not there
#createlines:if create create int emty lines


#save(save,text,replaceall,line,appennt)
#
#save:savename as an string ('save.txt')
#text: the text that will be saved(str)
#replaceall:replace all in the document(bool)
#line: replace only 1 line (int) starts at 0
#appennt:create data at end of document(bool)


#loadvalue(save,key,create,seperator)
#
#save:savename as an string ('save.txt')
#key:key to the value(str)
#create:create save if not there(bool)
#seperator:betwen key and value(str)


#savevalue(save,key,value,seperator=' ')
#
#save:savename as an string ('save.txt')
#key:key to the value(str)
#value: the value that you want to save
#seperator:betwen key and value(str)
#

import os
def loadvalue(save,key,create=True,seperator=' '):
  path = os.path.abspath('') + '/save/saves/'
  try:
    temp = open(f'{path}{save}','r')
    temp.close()
  except:
    if create == True:
      temp = open(f'{path}{save}','x')
      writetext = ''
      temp.write(writetext)
      temp.close()
    else:
      return None
  f = open(f'{path}{save}','r')
  lines = f.readlines()
  for i in lines:
    temp = i.split(seperator)
    try:
      if str(temp[0]) == key:
        return str(temp[1])
    except:
      pass
  return None  
def savevalue(save,key,value,seperator=' '):
  original = load(save,alllines=True)
  path = os.path.abspath('') + '/save/saves/'
  f = open(f'{path}{save}','w')
  text = ''
  inf = False
  for i in original:
    temp = i.split(seperator)
    try:
      if str(temp[0]) == key:
        text = text + f'\n{key}{seperator}{str(value)}'
        inf = True
      else:
        text = text + f'\n{i}'
    except:
      pass
  if inf == False:
    text = text + f'\n{key}{seperator}{str(value)}'
  text = text.replace('\n\n','\n')
  f.write(text)
def load(save,all=False,line=0,alllines=False,create=True,createlines=0):
  path = os.path.abspath('') + '/save/saves/'
  try:
    temp = open(f'{path}{save}','r')
    temp.close()
  except:
    if create == True:
      temp = open(f'{path}{save}','x')
      writetext = ''
      for i in range(createlines):
        writetext = writetext + '\n'
      temp.write(writetext)
      temp.close()
    else:
      return None
  temp = open(f'{path}{save}','r')
  if all == True:
      return temp.read()
  else:
    if alllines == True:
      lines =temp.readlines()
      temp.close()
      ret = []
      for i in lines:
        ret.append(i.replace('\n',''))
      return ret
    else:
      try:
        ret = temp.readlines()
        return ret[line-1]
      except:
        return None
def save(save,text,replaceall=False,line=1,appennt=False):
  path = os.path.abspath('') + '/save/saves/'
  original = load(save,alllines=True)
  if appennt == True:
    temp = open(f'{path}{save}','a')
    temp.write(f'\n{text}')
    temp.close()
    return
  temp = open(f'{path}{save}','w')
  try:
    if line > len(original):
      for i in range(line-len(original)):
        original.append('')
    original[line-1] = text
    writetext = ''
    for i in original:
      writetext = writetext + i + '\n'
    writetext = writetext[:-1]
    if replaceall == True:
      writetext = text
    temp.write(writetext)
    temp.close()
  except:
    return



