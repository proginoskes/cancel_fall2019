import codecs, sys, json

fil = json.load(open("cancel_formatted.json",'r', encoding='utf-8'))

#list_values=data.values()

filestring = ""

for i in range(len(fil['all_tweets'])):
    filestring = filestring + fil['all_tweets'][i]['tweet']+"\n"
    if i % 2500==0: print((i/len(fil['all_tweets']))*100)


with open("cancel_tweets.txt",'w') as newfile:
    newfile.write(filestring)

#print(list_values)
