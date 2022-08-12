import Augmentor
import os

p = Augmentor.Pipeline("./drowsy")

##Features
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.5)
p.resize(probability=1.0, width=480, height=480)

##Sample output
p.sample(100)

##Move files from source to destination
destination = "./drowsy/"
source = "./drowsy/output/"

allfiles = os.listdir(source)

for f in allfiles:
    os.rename(source + f, destination + f)
