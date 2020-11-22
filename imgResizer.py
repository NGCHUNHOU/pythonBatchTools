from PIL import Image
import os, glob, sys
import argparse


def resizeImage(nameAfter: str = "", size: tuple = (200,200), targetDirectory: str = "./resized/") -> None:
    """
    Main resize function to resize a batch of images with given directory
    nameAfter: a addon-name after every image filename 
    size: image resolution size
    targetDirectory: the target folder where resized images should put into
    return: none
    """
    if (os.path.isdir(targetDirectory) == False):
        os.mkdir("resized") 

    types = ("*.jpg", "*.png")
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))

    for file in files_grabbed:
        image = Image.open(file)
        image.thumbnail(size)
        myfile = os.path.splitext(file) 
        mfile = myfile[0] + nameAfter + myfile[1]
        image.save(targetDirectory+mfile)
        print(mfile)

# CLI documentation script 
# use -h flag to see documentation
parser = argparse.ArgumentParser(
    prog="image resizer",
    description="to resize a batch of images with given directory"
)
parser.add_argument("-s", "--size", type=int, nargs='+', help="image resolution size exp: 1200 800")
parser.add_argument("-n", "--nameAfter", type=str, help="filename-<nameAfter> a addon-name after every image  exp: thumbnail")
args = parser.parse_args()

# example how to use resizeImage def
# resizeImage("-200", (400,400))
if __name__ == "__main__":
    size =  tuple(args.size)
    postfix = '-' + args.nameAfter
    resizeImage(postfix, size)