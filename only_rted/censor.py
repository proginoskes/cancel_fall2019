import re,codecs

fil = open("cancel_tweets.txt",'r', encoding='utf-8')

line = fil.read()
fil.close()

line = re.sub('\n[^\n]*nigger[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*nigga[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*retard[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*tranny[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*kike[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*dyke[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*faggot[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*fag[^\n]*\n','\n', line)
line = re.sub('\n[^\n]*gypsy[^\n]*\n','\n', line)
# remove @
#\n@user ejgoeijg
#tijeoijgh @user meotig 
line = re.sub('@[\w,-]*','', line) #replies
#line = re.sub(r'^https?:\/\/.*', ' ', line)#urls
line = re.sub(r'http\S+', ' ', line)#urls




#for i in range(len(fil['all_tweets'])):
#    filestring = filestring + fil['all_tweets'][i]['tweet']+"\n"
#    print(fil['all_tweets'][i]['tweet']+"\n")

with open("cancel_tweets_clean_no_at_no_url.txt",'w') as newfile:
    newfile.write(line)

