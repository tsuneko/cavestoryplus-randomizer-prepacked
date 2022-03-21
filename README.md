# cavestoryplus-randomizer-prepacked
Working pre-packaged copy of [duncathan's CaveStoryRandomizer v2.1](https://github.com/cave-story-randomizer/cave-story-randomizer/releases/tag/v2.1-RC2), and [Kaitlyn's CS+ rando mod](https://cdn.discordapp.com/attachments/558603545008537604/686288099134799965/rando_but_cs_plus.zip) with duncathan's modified [ArmsItem.tsc](https://cdn.discordapp.com/attachments/558603545008537604/686331261131948162/ArmsItem.tsc), with a python script to automatically copy the required directory trees into your CS+ mods directory, and randomize seasonal tilesets and sprites.

All provided files belong to their respective owners and I do not claim any right over them.

This mod package has been created purely for ease of access, since CS+ is not officially supported by the randomizer mod.

This mod package utilises Windows binaries provided by duncathan's CSR. Since CSR is written for the Love2D engine, it may be possible to port it to Mac/Linux by unpacking the .exe as a .zip and re-compiling for the respective platform. See this [page](https://love2d.org/wiki/Game_Distribution) for more information. The provided python script should be platform-independent.

# Installation

Extract latest [release](https://github.com/tsuneko/cavestoryplus-randomizer-prepacked/files/8318636/cavestoryplus-randomizer-prepacked.zip) into `CaveStory+\data\`

Ensure that [Python3](https://www.python.org/downloads/) is installed.

# Usage

Run `randomizer_csplus.py` and follow the instructions.

To prevent randomization of tilesets and/or player sprite, edit these variables to be `False`:
- `enable_random_tileset = True`
- `enable_random_sprite = True`

Randomizer is only able to use the "New" tilesets, most likely due to a limitation related to CS+ modding.
