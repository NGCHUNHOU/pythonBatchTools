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

    def addAfterFileName(self, addValue, targetFileExt = "js"):
        for i in glob.glob('*.' + targetFileExt):
            fileStruct = os.path.splitext(i)
            if (addValue not in fileStruct[0]):
                os.rename(i,fileStruct[0] + addValue + "." + targetFileExt)

    def addBeforeFileName(self, addValue, targetFileExt = "js"):
        for i in glob.glob('*.' + targetFileExt):
            fileStruct = os.path.splitext(i)
            if (addValue not in fileStruct[0]):
                os.rename(i,addValue + fileStruct[0] + "." + targetFileExt)

    def removeFileName(self, addValue, targetFileExt = "js"):
        for i in glob.glob('*.' + targetFileExt):
            fileStruct = os.path.splitext(i)
            if (addValue in fileStruct[0] or "-" in fileStruct[0]):
                os.rename(i,fileStruct[0].replace(addValue, "").replace("-", "") +  "." + targetFileExt)

parser = argparse.ArgumentParser(
    prog="renamer",
    description="to edit and modify filename"
)

parser.add_argument("FileTypeExt", help="target file type extension to add after name")
parser.add_argument("-af", "--AddAfterName", help="add string after filename")
parser.add_argument("-afh", "--AddAfterNameWithHyphen", help="add string after filename with hyphen")
parser.add_argument("-ab", "--AddBeforeName", help="add string before filename")
parser.add_argument("-abh", "--AddBeforeNameWithHyphen", help="add string before filename with hyphen")
parser.add_argument("-r", "--removeAfterName", help="remove after name of specified type file")
args = parser.parse_args()

renamer = renamer()

if (args.AddAfterNameWithHyphen):
    AddAfterNameWithHyphen = "-" + args.AddAfterNameWithHyphen
    renamer.addAfterFileName(AddAfterNameWithHyphen, args.FileTypeExt)
if (args.AddBeforeName):
    AddBeforeName = args.AddBeforeName
    renamer.addBeforeFileName(AddBeforeName, args.FileTypeExt)
if (args.AddBeforeNameWithHyphen):
    AddBeforeNameWithHyphen = args.AddBeforeNameWithHyphen + "-"
    renamer.addBeforeFileName(AddBeforeNameWithHyphen, args.FileTypeExt)
if (args.removeAfterName):
    renamer.removeFileName(args.removeAfterName, args.FileTypeExt)
if (args.AddAfterName):
    renamer.addAfterFileName(args.AddAfterName, args.FileTypeExt)