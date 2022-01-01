# DeltaruneFileLoaders

# WORK IN PROGRESS 

Allows users to efficiently load save files from specific spots in Undertale and Deltarune  
TODO: allow for hacked equipment/rooms, boss rush?

## Instructions
1. Change USERNAME to your pc's user
2. Change NAME to the name you'd like your save file to be called
3. Change GAME to the game you'd like to load (e.g. UNDERTALE)
4. Change SELECTED the position you'd like to start at (e.g. genocide_sans)
5. Change BACKUP to your desired backup mode (see below)
6. run python main.py

## Features

### UNDERTALE Save Files
```
pacifist_napstablook    pacifist_muffet         pacifist_papyrus_date   genocide_toriel
pacifist_toriel         pacifist_mettaton       pacifist_undyne_date    genocide_papyrus
pacifist_papyrus        pacifist_asgore         pacifist_alphys_date    genocide_undyne
pacifist_mad_dummy      pacifist_omega_flowey   pacifist_asriel         genocide_sans
pacifist_undyne                                 pacifist_ending         genocide_ending
```
### DELTARUNE Save Files
```
ch1_field               ch2_cyber_world         ch2_mansion             snowgrave_start
ch1_forest              ch2_rollercoaster       ch2_acid_lake           snowgrave_mansion
ch1_castle              ch2_trash_zone          ch2_queen               snowgrave_spamton
ch1_king                ch2_berdly              ch2_queen_robot         snowgrave_ending
ch1_jevil               ch2_spamton             ch2_spamton_neo
```

### BACKUP functionality
'SAVE': Loads the files from your game into your BACKUP file  
'LOAD': Loads the files from the BACKUP file to your game  
OTHER : Loads SELECTED position as normal

## Acknowledgements/Resources:

#### Save Files:
[UNDERTALE](https://www.reddit.com/r/Undertale/comments/3szvui/my_undertale_save_files/) - u/HylianAngel  
[DELTARUNE Ch1](https://gamejolt.com/get/build?game=402285&build=679262) - @WarmColedavid  
[DELTARUNE Ch2](https://libredd.it/r/Deltarune/comments/pqx6y7/my_save_files_from_deltarune_chapter_2_theres/) - unknown

#### Save File Structure/IDs:
[UNDERTALE](https://pcy.ulyssis.be/undertale/) - @Mirrawrs  
[DELTARUNE](https://www.reddit.com/r/Underminers/comments/pw8xv3/dr_ch12_datamining_lists_items_encounters/?utm_source=share&utm_medium=ios_app&utm_name=iossmf) - u/santizhizi
