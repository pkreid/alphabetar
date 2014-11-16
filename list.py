from os import walk
import subprocess 
import string

f = []
for (dirpath, dirnames, filenames) in walk("/home/kreid/music"): #TODO: Generalize this PS1
     f.extend(dirnames)   #get the names of the music folders
     break
f = sorted(f, key=str.lower)

tarball = ()
for letter in string.ascii_uppercase:
    for file in f:
        if file[0][0] == letter:         #Match the folders up with the corresponding tarball
            tarball = tarball + ("/home/kreid/music/" + str(file),)  #Append to the tuple with path written in

        elif len(tarball) != 0:
           clean = ' '.join(str(i) for i in (tarball))     #format it nicely
           subprocess.Popen(["bash","-c" ,"tar cvf Music_" + str(letter) +".tar " + str(clean)])   #TODO make the file names optional, preferably incoporating $(date)
           tarball = ()      #reset
	   
	   
