import re
line="my name is python iam most powerful language in this universe"
#methods
print(re.match(r".*",line)) # r".*"  here r means regular expression and "" mark meanigs of raw string  and dot meaning any character and * means one or more carecther can 
print(re.match(r".+",line)) # + means there can be one or more character but it can't be zero

print(re.match(r"[a-zA-Z]+",line)) # what this match character does it only match first character 
print(re.search(r"[a-zA-Z]+",line))#it basicaly earch through line by line .. onece it found match it return
#
# 
print(re.search("ab?",line)) 
# he pattern being searched for is "ab?".

# "a" matches the character "a" literally.
# "b?" matches the character "b" zero or one time. The question mark (?) makes the preceding character optional.

 

