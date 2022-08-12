import Augmentor

p = Augmentor.Pipeline("./data/images")

##Features
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)
p.crop_random(probability=1, percentage_area=0.5)
p.resize(probability=1.0, width=360, height=240)

##Sample output
p.sample(100)