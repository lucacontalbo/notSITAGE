import instaloader as ig
from os import listdir, rename, getcwd
from os.path import isfile, join
from shutil import rmtree

L = ig.Instaloader()

profile = ig.Profile.from_username(L.context, "age.giovani").get_posts()
profile = list(profile)
for i in range(3):
	print(profile[i].caption)
	L.download_post(profile[i],"age.giovani")


path = join(getcwd(),"age.giovani")
pics = [join(path,pic) for pic in listdir(path) if isfile(join(path,pic)) and pic.endswith('.jpg')]
captions = [join(path,cap) for cap in listdir(path) if isfile(join(path,cap)) and cap.endswith('.txt')]

for i in range(3):
	rename(pics[i],join(getcwd(),"../public/ig",str(i)+"_ig.jpg"))
	rename(captions[i],join(getcwd(),"../public/ig",str(i)+"_ig.txt"))

rmtree(path)
