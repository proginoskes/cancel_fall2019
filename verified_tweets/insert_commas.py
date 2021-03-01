import codecs, sys, json

fi = open("cancel_v_all.json",'r')

fi_string = fi.read()

fi_string = fi_string.replace("\n{",",\n{")
#fi_string = fi_string.replace("]}","]")
with open("cancel_formatted.json",'w') as f:
    f.write(fi_string)


