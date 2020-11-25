import argparse, os, glob

class renamer:
    def __init__(self):
        pass 

    def createFiles(self):
        for i in range(10):
            os.system("touch lib" + str(i) + ".js")

    def removeFiles(self, removeString, targetFileExt = "js"):
        for i in range(10):
            os.system("rm lib" + str(i) + removeString + "." + targetFileExt)

    def addFileName(self, addValue, targetFileExt = "js"):
        for i in glob.glob('*.' + targetFileExt):
            fileStruct = os.path.splitext(i)
            if (addValue not in fileStruct[0]):
                os.rename(i,fileStruct[0] + addValue + "." + targetFileExt)

    def removeFileName(self, addValue, targetFileExt = "js"):
        for i in glob.glob('*.' + targetFileExt):
            fileStruct = os.path.splitext(i)
            if (addValue in fileStruct[0] or "-" in fileStruct[0]):
                os.rename(i,fileStruct[0].replace(addValue, "").replace("-", "") +  "." + targetFileExt)

parser = argparse.ArgumentParser(
    prog="Renamer",
    description="to edit and modify filename"
)

parser.add_argument("FileTypeExt", help="target file type extension to add after name")
parser.add_argument("-a", "--AddAfterName", help="add string after filename without hyphen")
parser.add_argument("-ah", "--AddAfterNameWithHyphen", help="add string after filename with hyphen")
parser.add_argument("-r", "--removeAfterName", help="remove after name of specified type file")
args = parser.parse_args()

renamer = renamer()

if (args.AddAfterNameWithHyphen):
    AddAfterNameWithHyphen = "-" + args.AddAfterNameWithHyphen
    renamer.addFileName(AddAfterNameWithHyphen, args.FileTypeExt)
if (args.removeAfterName):
    renamer.removeFileName(args.removeAfterName, args.FileTypeExt)
if (args.AddAfterName):
    renamer.addFileName(args.AddAfterName, args.FileTypeExt)