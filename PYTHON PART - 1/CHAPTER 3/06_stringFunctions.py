story ='''once upon a time there was a youtuber named HarryBhai 
who uploaded complete python course notes once upon HarryBhai'''

print(story[:5])
print(story[:4])

#string Functions :-)

print(len(story))
print(story.endswith("hello harsha"))
print(story.endswith("notes"))
print(story.count("a"))
print(story.count('O'))
print(story.count("notes"))
print(story.count(" "))
print(story.count(" once"))#gives 1 
print(story.count("wa "))
print(story.capitalize())#capitalizes only the first of whole para
print(story.find("once"))
print(story.find("Once"))#gives -1
print(story.find("upon"))#this will give the first one "upon" itself
print(story.replace("HarryBhai","Code With Harry"))
#this replace function will replace every occurance where as the
# find function will find only the first word itself







