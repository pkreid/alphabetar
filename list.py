from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("/home/kreid/music"):
     f.extend(dirnames)
     break
print f
