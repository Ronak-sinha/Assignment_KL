import json

wordsFile=open("words.json", "r", encoding='UTF-8')
word=json.loads(wordsFile.read())
resWord={} #resultant words
for i in word:
    key1=i["word"] #home
    value1=i["meanings"] #partsofspeech
    value={} #dict for partsofspeech
    for k in value1:
        list=[] 
        key2=k["partOfSpeech"]
        value2=k["definitions"]
        for d in value2:
            list.append(d["definition"]) #adding all the values of partsofspeech
        value[key2]=list #dict of partsofspeech
    resWord[key1]=value #dict of resultant words
with open("word_details.json","w") as f2:
    json.dump(resWord, f2, indent=2)
wordsFile.close()
f2.close()