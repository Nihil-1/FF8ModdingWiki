---
title: FF8 Home
layout: home
nav_order: 1
permalink: /
---


This wiki will be divided in 3 main sections:
- [Modding user guide](FF8/UserGuide)
- [Modding technical reference](#modding-technical)
- [FAQ](faq)

# Modding user guide
This part can contains any guide the community wanna share on how to mod the game.
[]




### Game engine
-   [Final Fantasy VIII's Engine](FF8/TechnicalReference/Engine/Engine)
-   [Array of Battle files](FF8/TechnicalReference/Engine/BattleFiles)

### Details of the Game

-   [Final Fantasy VIII's Kernel](FF8/TechnicalReference/Main/Kernel) Empty file for the moment
-   [Game variables used in scripting](FF8/TechnicalReference/Miscellaneous/Variables)
-   [World map camera](FF8/TechnicalReference/WorldMap/WorldMapCamera)
-   [Battle encounters list](FF8/TechnicalReference/Battle/Encounter_Codes)

  For String encoding, you can  find the info on the wiki of the [ShumiTranslator](https://github.com/HobbitDur/ShumiTranslator/wiki/FF8_char) tool done by HobbitDur which detail the following file (link is kept here to the old wiki for archive purpose):
-   [String Encoding](FF8/TechnicalReference/Miscellaneous/String_Encoding)

### Media Formats

-   [Final Fantasy VIII PS1](FF8/TechnicalReference/Miscellaneous/PlaystationMedia) media information.
-   [Final Fantasy VIII PC](FF8/TechnicalReference/Miscellaneous/PC_Media) media information.
-   [Final Fantasy VIII Save data](FF8/TechnicalReference/Miscellaneous/GameSaveFormat)

  
## File formats

### Movie Files

-   [\[PAK](FF8/TechnicalReference/Field/FileFormat/FileFormat_PAK)\] Movie Archives

### Sound Files

-   [\[FMT](FF8/TechnicalReference/Field/FileFormat/FileFormat_FMT)\] Sound Archives

### Battle files

-   [\[X](FF8/TechnicalReference/Battle/FileFormat_X)\] Battle Fields
-   [\[DAT](FF8/TechnicalReference/Battle/FileFormat_DAT)\] Battle Models
-   [Scene.out](FF8/TechnicalReference/Battle/BattleStructure) Battle encounter data
-   [r0win.dat](FF8/TechnicalReference/Battle/FileFormat_r0win) Winning sequence
-   [b0wave.dat](FF8/TechnicalReference/Battle/FileFormat_b0wave)
-   [a9btlfnt.bft](FF8/TechnicalReference/Field/FileFormat/FileFormat_TDW)
-   [.mag files](FF8/TechnicalReference/Field/FileFormat/FileFormat_magfiles) - MAG files

### Field files

-   [Opcodes](FF8/TechnicalReference/Field/Opcodes/Opcodes) Field script opcodes
-   [\[MCH](FF8/TechnicalReference/Field/FileFormat/FileFormat_MCH)\] Field Character Models
-   [\[ONE](FF8/TechnicalReference/Field/FileFormat/FileFormat_ONE)\] Field Character Models Container
-   [\[MIM](FF8/TechnicalReference/Field/FileFormat/FileFormat_MIM)\] Field Background Image Data
-   [\[MAP](FF8/TechnicalReference/Field/FileFormat/FileFormat_MAP)\] Field Background Tile Data
-   [\[JSM](FF8/TechnicalReference/Field/FileFormat/FileFormat_JSM)\] Field Scripts
-   [\[SYM](FF8/TechnicalReference/Field/FileFormat/FileFormat_SYM)\] Script entity
-   [\[MSD](FF8/TechnicalReference/Field/FileFormat/FileFormat_MSD)\] Field Dialogs
-   [\[INF](FF8/TechnicalReference/Field/FileFormat/FileFormat_INF)\] Field Gateways
-   [\[ID](FF7/Field/Walkmesh)\] Walkmesh field (from FF7)
-   [\[CA](FF8/TechnicalReference/Field/FileFormat/FileFormat_CA)\] Field Camera
-   [\[TDW](FF8/TechnicalReference/Field/FileFormat/FileFormat_TDW)\] Extra font
-   [\[MSK](FF8/TechnicalReference/Field/FileFormat/FileFormat_MSK)\] Mask files
-   [\[RAT](FF8/TechnicalReference/Field/FileFormat/FileFormat_RAT_MRT) & \[MRT\]\] Battle related
-   [\[PMD](FF8/FileFormat_PMD)\] Particle Info
-   [\[PMP](FF8/TechnicalReference/Field/FileFormat/FileFormat_PMP)\] Particle Image Data
-   PVP (No info on this wiki)
-   [\[SFX](FF8/TechnicalReference/Field/FileFormat/FileFormat_SFX)\] Sound IDs

### World map files

-   [music0.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [music1.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [music2.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [music3.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [music4.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [music5.obj](FF8/TechnicalReference/WorldMap/WorldMap_music)
-   [rail.obj](FF8/TechnicalReference/WorldMap/WorldMap_rail)
-   [texl.obj](FF8/TechnicalReference/WorldMap/WorldMap_texl)
-   [wmset.obj](FF8/TechnicalReference/WorldMap/WorldMap_wmset)
-   [wmsetXX.obj](FF8/TechnicalReference/WorldMap/WorldMap_wmsetxx)
-   [wmx.obj](FF8/TechnicalReference/WorldMap/WorldMap_wmx)
-   [chara.one](FF8/TechnicalReference/WorldMap/WorldMap_charaone)

### Main
  For kernel data, there is a dedicated wiki in the [Doomtrain](https://github.com/DarkShinryu/doomtrain/wiki) tool done by Maki which detail the kernel.bin
  
  For namedic, you can also find the info on the wiki of the [ShumiTranslator](https://github.com/HobbitDur/ShumiTranslator/wiki/Namedic_bin) tool done by HobbitDur which detail the following file (link is kept here to the old wiki for archive purpose):
  -   [namedic.bin](FF8/TechnicalReference/Main/Main_namedic)

  For others:
-   [wm2field.tbl](FF8/TechnicalReference/Main/Main_wm2) 
-   [harata.cnf](FF8/TechnicalReference/Main/Main_harata)
-   [init.out](FF8/Main_init) 


### Menu
For text menu, there is a dedicated wiki in the [ShumiTranslator](https://github.com/HobbitDur/ShumiTranslator/wiki) tool done by HobbitDur which detail the following files (link are kept here to the old wiki for archive purpose):
-   [mngrphd.bin](FF8/TechnicalReference/Menu/Menu_mngrphd_bin)
-   [mngrp.bin](FF8/TechnicalReference/Menu/Menu_mngrp_bin)
-   [tkmnmes\*.bin](FF8/TechnicalReference/Menu/Menu_tkmnmes)
-   [mngrp strings](FF8/TechnicalReference/Menu/Menu_mngrp_strings_locations)
-   [mngrp complex strings](FF8/TechnicalReference/Menu/Menu_mngrp_complex_strings)
-   [m00\*.bin and m00\*.msg](FF8/TechnicalReference/Menu/Menu_m000_m004)

For shop, you can also find the info on the wiki of the [TonberryShop](https://github.com/HobbitDur/TonberryShop/wiki) tool done by HobbitDur which detail the following file (link is kept here to the old wiki for archive purpose):
-   [shop.bin](https://github.com/HobbitDur/TonberryShop/wiki)

For others files
-   [mag\*.tex](FF8/Menu_mag_textures)
-   [\*.sp1/\*.sp2](FF8/TechnicalReference/Menu/Menu_sp2)
-   [areames.dc1](FF8/TechnicalReference/Menu/Menu_areames_dc1)
-   [price.bin](FF8/TechnicalReference/Menu/Menu_price_bin)


# Tools and Patches

-   [Tools and Patches](FF8/TechnicalReference/Tools.md)

