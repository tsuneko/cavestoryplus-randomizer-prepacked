import os
import subprocess
from distutils.dir_util import copy_tree
from shutil import rmtree, copyfile
import random

randomizer_files_dir = "randomizer_files"
csr_dir = randomizer_files_dir + "\\CSR-v2.1-RC2"
csr_file = "CaveStoryRandomizer.exe"
randomizer_dir = "Randomizer"
randomizer_mod_dir = randomizer_dir + "\\mod"
mod_dir = "Randomizer_files\\mod"
sprites_dir = "Randomizer_files\\sprites"

enable_random_tileset = True
enable_random_sprite = True

tilesets = ["Default", "Halloween", "Christmas"]
sprites = ["Quote", "Curly", "QuoteAlt", "QuoteAlt2", "Halloween", "Christmas"]

if os.path.exists(csr_dir + "\\" + csr_file) and os.path.exists(mod_dir):
    print("Please ensure that you have added the following line to your mods.txt!")
    print("XX R+   P01 /Randomizer/mod/")
    print("Replace XX with the next number in the list eg. 07")
    print()
    print("Usage: set desired Settings, and then click Randomize!")
    print()
    print("Following this, press [Esc] in the randomizer to close the window")
    print("and continue this script")
    print()
    os.chdir(csr_dir)
    subprocess.call([csr_file])
else:
    print("Error: could not find randomizer files")
    exit(-1)

print("Press [Enter] to continue or [Ctrl+C] to exit")
input()

os.chdir("..")
os.chdir("..")

if os.path.exists(randomizer_dir):
    rmtree(randomizer_dir, ignore_errors=True)

os.mkdir(randomizer_dir)

copy_tree(mod_dir, randomizer_mod_dir)
copy_tree(csr_dir + "\\data", randomizer_mod_dir)
copyfile(mod_dir + "\\MyChar.bmp", randomizer_mod_dir + "\\MyChar.bmp")

if enable_random_tileset or enable_random_sprite:
    rng = random.Random()

    # use randomizer hash as seed
    if os.path.exists(randomizer_mod_dir + "\\hash.txt"):
        with open(randomizer_mod_dir + "\\hash.txt") as f:
            rng = random.Random(f.read())

    if enable_random_tileset:
        tileset = random.choice(tilesets)
        if tileset != "Default":
            copy_tree(tileset + "\\season", randomizer_mod_dir)
        print("Selected the " + tileset + " tileset.")

    if enable_random_sprite:
        sprite = random.choice(sprites)
        if sprite != "Quote":
            copy_tree(sprites_dir + "\\" + sprite, randomizer_mod_dir)
        print("Playing as " + sprite + ".")

print()
print("Ready!")
