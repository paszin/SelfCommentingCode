
import os



path = "/Users/irm-concussion/Documents/Projects/soundcloudfire/app/modules"
endings = ["js"]

for dirpath, dirnames, filenames in os.walk(path):
    for fn in filenames:
        if fn.split('.')[-1] in endings:
            print("Found File:", fn)
            with open(os.path.join(dirpath, fn)) as f:
                print("Content: ", f.read())
            print(3*'\n')
