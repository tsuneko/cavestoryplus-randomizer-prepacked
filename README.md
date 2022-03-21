# cavestoryplus-randomizer-prepacked
Working pre-packaged copy of [duncathan's CaveStoryRandomizer v2.1](https://github.com/cave-story-randomizer/cave-story-randomizer/releases/tag/v2.1-RC2), and [Kaitlyn's CS+ rando mod](https://cdn.discordapp.com/attachments/558603545008537604/686288099134799965/rando_but_cs_plus.zip) with duncathan's modified [ArmsItem.tsc](https://cdn.discordapp.com/attachments/558603545008537604/686331261131948162/ArmsItem.tsc), with a python script to automatically copy the required directory trees into your CS+ mods directory, and randomize seasonal tilesets and sprites.

# Installation

Extract latest release into `CaveStory+\data\`

Ensure that [Python3](https://www.python.org/downloads/) is installed.

# Usage

Run `randomizer_csplus.py` and follow the instructions.

To prevent randomization of tilesets and/or player sprite, edit these variables to be `False`:
- `enable_random_tileset = True`
- `enable_random_sprite = True`
