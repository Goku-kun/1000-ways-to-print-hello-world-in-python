a1z26 =  {'0':' ','1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', 
'10':'J', '11':'K', '12':'L',  '13':'M', '14':'N',  '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S', 
'20':'T', '21':'U', '22':'V',  '23':'W', '24':'X', '25':'Y', '26':'Z'}

encrypted = '8-5-12-12-15-,-0-23-15-18-12-4-!'

individual = []

my_string = ''
temp_list = encrypted.split('-')
  
for char in temp_list:
  if char in a1z26.keys():
    my_string += a1z26[char]
  else:
    my_string += char

print(my_string)
