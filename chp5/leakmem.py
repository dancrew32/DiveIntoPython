import fileinfo

def leakmem():
    f = fileinfo.FileInfo('/home/dan/Music/jenniferhudson.mp3')

    for i in range(1000):
        leakmem() #mem leaks are rare in python because as soon as f/i go 
#out of scope, they are garbage collected
