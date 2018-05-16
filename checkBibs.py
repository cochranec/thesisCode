import re
import glob

litFile = '/home/chris/Dropbox/THESIS/Inputs/Introduction.tex'
allInputs = glob.glob('/home/chris/Dropbox/THESIS/Inputs/*.tex')

def getCites(inFile):
    fileList = []
    with open(inFile) as origin:
        for line in origin:
            if line[0] is not '%':
                regex = ur"\\cite\{(.+?)\}"
                rr = re.findall(regex, line)
                for ll in rr:
                    fileList += [x.strip() for x in ll.split(',')]
            else:
                # These lines are commented out in the TeX file
                continue
    return set(fileList)

missing_set = set([])

a = getCites(litFile)

for thisFile in allInputs:
    b = getCites(thisFile)
    missing_set = missing_set|(b-a)

print "%d References in Input Files but not Lit. Review:" % (len(missing_set))

for s in missing_set:
    print s