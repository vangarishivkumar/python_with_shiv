dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}   # dictionary declaration

for en,fr in dictionary.items():       ### loop for all items (key=en and value =fr
    print(en,'-->',fr)

for fr in dictionary.values():        #only values fr
    print('ony values : ',fr)

for keys in dictionary.keys():           # looping dictionary by keys().
     print(keys,'-->',dictionary[keys])
