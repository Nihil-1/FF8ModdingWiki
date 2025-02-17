---
layout: default
title: Exe data
parent: ExeData
author: SegaChief, HobbitDur
---

Here will be put all info on the exe editing. The base is version 2013 in english.  
The goal will be to put the value in the .exe reference, but for the moment there is a mix of RAM reference and EXE reference.  
The RAM data start at +0x400000, so it's just a matter of shift.  
Keep in mind the values are in little endian, so when writing hext files, you need to write byte in the opposite order.  
In lots of cases, 0x9090 value is used, it's because 0x90 is a nop,  
so if there is a computation that take 2 bytes and you want to cancel it, you replace it with 2 nop (0x9090)

1. TOC
{:toc}


# Limit

[Original Qhimm post](https://forums.qhimm.com/index.php?topic=15211.0)

## Damage limit
There is 2 values, the normal damage cap and the bonus damage cap for damage that can break the limit (Eden for example)  
So for example, if the max damage limit is 9999, and the bonus damage is 50,001; the max damage limit for Eden is 60 000

| Offset   | Size | Default value | Name                           |
|----------|------|---------------|--------------------------------|
| 0x091133 | 4    | 0x0000C351    | "No Damage Limit" Damage Bonus |
| 0x091139 | 4    | 0x0000270F    | Normal Damage Cap              |

## Maximum HP

### Party

The first offset (0x095A1C) is the value to compare to. Setting this to 1 will set all characters to have the Maximum HP of 9999 all the time. This also gives the "Maximum HP" Achievement.  
The second offset (0x095A23) is the value that will be set if it exceed the previous value set at offset 0x095A1C.  
It is to be noted than when putting value > 9999, the game has strange behavior: value above 9999 start from 0 (so character don't really have 10000 HP).  
The menu and battle text can't handle it also.

| Offset   | Size | Default value | Name                                              |
|----------|------|---------------|---------------------------------------------------|
| 0x095A1C | 4    | 0x0000270F    | Maximum HP Cap limit value                        |
| 0x095A23 | 4    | 0x0000270F    | Maximum HP Cap value set if currenthp > cap value |

### GF
The first offset (0x095E6F) is the value to compare to. Setting this to 1 will set all GF to have the Maximum HP of 9999 all the time (this part to be confirmed).
The second offset (0x095E76) is the value that will be set if it exceed the previous value set at offset 0x095E6F.
It is to be noted than when putting value > 9999, the game has strange behavior: value above 9999 start from 0 (so character don't really have 10000 HP).
The menu and battle text can't handle it also.

| Offset   | Size | Default value | Name                                              |
|----------|------|---------------|---------------------------------------------------|
| 0x095E6F | 4    | 0x0000270F    | Maximum HP Cap limit value                        |
| 0x095E76 | 4    | 0x0000270F    | Maximum HP Cap value set if currenthp > cap value |

## Maximum draw

The first offset (0x08FE00) is the value to compare to. Setting this to 1 will make you always Draw the maximum amount (in battle).
The second offset (0x08FE04) is the value that will be set if it exceed the previous value set at offset 0x08FE00.

| Offset   | Size | Default value | Name                                            |
|----------|------|---------------|-------------------------------------------------|
| 0x08FE00 | 1    | 0x09          | Maximum Draw limit value                        |
| 0x08FE04 | 4    | 0x00000009    | Maximum Draw value set if drawvalue > cap value |

Example:
```
8FE00 =  
09 7E 05 B8 09 (Default: 9 max per draw)  
01 7E 05 B8 64 (Draw 100 so long as 1+ is drawn)  
09 7D 05 B8 09 (Draw minimum of 9, no upper cap - changes jump type to greater/equal, Sets a minimum draw but with no upper cap so that your magic stat can influence how many you get)   
```

## Limitless magic

I don't know how it works, but here what seems to work:

### In Battle

| Offset   | Size | Default value | Name                                              |
|----------|------|---------------|---------------------------------------------------|
| 0x086B0C | 2    | 0xC9FE        | Limitless magic in battle                         |

Replace value by 0x9090 for limitless magic in battle


#### In Field

| Offset   | Size | Default value | Name                     |
|----------|------|---------------|--------------------------|
| 0x0F3027 | 2    | 0xCBFE        | Limitless magic in field |

Replace value by 0x9090 for limitless magic in field (using curaga on menu for example)

# Command
[Qhimm post](https://forums.qhimm.com/index.php?topic=17098.0)
## Cover Command
At 0xD1EE there is a shift value  `v3 = (unsigned int)v3 >> 1;` means divided by 2
This is used to compute the reduce damage.
If replaced by 2 nop (0x9090), this avoid computing the damage.

| Offset   | Size | Default value | Name                   |
|----------|------|---------------|------------------------|
| 0x091091 | 2    | 0xD1EE (/2)   | Cover damage reduction |

## Darkside Command

This command has 2 part, the damage taken, and the damage modifier.

### Damage taken

The damage taken percentage is computed by 2 function:
- A magic number 0x0905A3 = 0x66666667 that allow to do a division by 10
- A shift call of 3 byte at 0x0905AF by 34 (SAR EDX, 2) that shift this magical number to obtain the division by 10

So in order to change the percentage, both those values need to be modified.

| Offset   | Size | Default value | Name                                                |
|----------|------|---------------|-----------------------------------------------------|
| 0x0905A3 | 4    | 0x66666667    | Magic number for how much HP% Darkside costs to use |
| 0x0905B1 | 1    | 0x02          | Shift for how much HP% Darkside costs to use        |

If you need any percentage (e.g., 7%, 33%, etc.), follow these steps:
- Compute the divisor:
`D = 100 / (desired percentage)`
- Compute the magic constant:
`Magic = floor(2^32 / D) + 1`
- Find the shift amount:
  - Start with `log2(D) - 1` as a rule of thumb.
  - Experiment with rounding correction.

Here a table with some interesting value (you need the magic number and shift amount):

| Percentage | Divisor (D) | Magic Number (Hex) | Shift Amount (SAR) |
|------------|-------------|--------------------|--------------------|
| 0%         | ∞           | 0x00000000         | N/A                |
| 10%        | 10          | 0x66666667         | 2                  |
| 20%        | 5           | 0x33333333         | 2                  |
| 30%        | 3.33_       | 0x2AAAAAAB         | 1                  |
| 40%        | 2.5         | 0x1999999A         | 1                  |
| 50%        | 2           | 0x80000001         | 0                  |
| 60%        | 1.66_       | 0xAAAAAAAB         | 0                  |
| 70%        | 1.428571    | 0xBA2E8BA3         | 0                  |
| 80%        | 1.25        | 0xCCCCCCCD         | 0                  |
| 90%        | 1.11_       | 0xE38E38E4         | 0                  |
| 100%       | 1           | 0xFFFFFFFF         | 0                  |


### Damage modifier

Determines how much bonus damage Darkside inflicts
At offset 0x091069, there is a LEA instruction with the third byte having 2 bit that allow to multiply.

| Offset   | Size | Default value | Name            |
|----------|------|---------------|-----------------|
| 0x09106B | 2    | 0x76          | Damage modifier |

| Possible values | Result |
|-----------------|--------|
| 0x36            | x2     |
| 0x76            | x3     |
| 0xB6            | x5     |
| 0xF6            | x9     |


## Kamikaze Command
By default, the command kamikaze is x5 damage of the user's maximum HP  
At offset 0x92D72, 0x8D0480 correspond to this instruction:
 - 0x8D: Opcode for LEA r32,m
 - 0x04: Byte ModR/M (MOD = 00, REG = 00, R/M=100)
 - 0x80: Byte SIB (Scale-Index-Base), where the 2 first bit are for the scale

The multiplier is link to the scale which is on 2 bit, so we can have the following SIB multiplier: 1, 2, 4, 8  
which give the following address multiplier: 2, 3, 5, 9

| Offset  | Size | Default value | Name                       |
|---------|------|---------------|----------------------------|
| 0x92D74 | 1    | 0x80          | Kamikaze damage multiplier |

| Possible values | Result |
|-----------------|--------|
| 0x00            | x2     |
| 0x40            | x3     |
| 0x80            | x5     |
| 0xC0            | x9     |

# SeeD rank salary

[Qhimm post](https://forums.qhimm.com/index.php?topic=18496.0)  
Array starts at offset 0x78E474. Each SeeD Rank salary is determined by two bytes, and each value gets multiplied by 10 before being shown in-game.

| S-Rank | Offset  | Value  |
|--------|---------|--------|
| 01     | 78E476  | 32 00  |
| 02     | 78E478  | 64 00  |
| 03     | 78E47A  | 96 00  |
| 04     | 78E47C  | C8 00  |
| 05     | 78E47E  | 2C 01  |
| 06     | 78E480  | 90 01  |
| 07     | 78E482  | F4 01  |
| 08     | 78E484  | 58 02  |
| 09     | 78E486  | BC 02  |
| 10     | 78E488  | 20 03  |
| 11     | 78E48A  | 84 03  |
| 12     | 78E48C  | E8 03  |
| 13     | 78E48E  | 4C 04  |
| 14     | 78E490  | B0 04  |
| 15     | 78E492  | E2 04  |
| 16     | 78E494  | 14 05  |
| 17     | 78E496  | 46 05  |
| 18     | 78E498  | 78 05  |
| 19     | 78E49A  | AA 05  |
| 20     | 78E49C  | DC 05  |
| 21     | 78E49E  | 0E 06  |
| 22     | 78E4A0  | 40 06  |
| 23     | 78E4A2  | 72 06  |
| 24     | 78E4A4  | A4 06  |
| 25     | 78E4A6  | D6 06  |
| 26     | 78E4A8  | 08 07  |
| 27     | 78E4AA  | 3A 07  |
| 28     | 78E4AC  | 6C 07  |
| 29     | 78E4AE  | 9E 07  |
| 30     | 78E4B0  | D0 07  |
| 31     | 78E4B2  | B8 0B  |

# Cheat function
Fkey, to be tested. [Qhimm post](https://forums.qhimm.com/index.php?topic=18426.0)

# Junction
## Junction at max even with 1 magic

Here, the function computing the quantity of magic is directly replaced by a mov, 100 (0x64) followed by nop

### HP
963CB = B3 64 90 90 90 90 90

### Primary Stats
966E5 = B2 64 90 90 90 90 90

### Secondary Stats
96788 = B2 64 90 90 90 90 90

### Elemental Attack
969D1 = B0 64 90 90 90 90 90

### Elemental Defence
96AAE = B1 64 90 90 90 90 90

### Status Attack
96BC1 = B0 64 90 90 90 90 90

### Status Defence
96C9D = B1 64 90 90 90 90 90

## Junction depending on level
*Likely JWP is the author of this

Assembly modifications so that Level determines the 'stock' of
stat-junction bonuses. So if you junction Curaga, the stock is
irrelevant and it uses your level instead. If you're Level 50,
you get an equivalent boost of 50x Curaga for instance.

Address: 0x004966E5
From:    8A 14 4D F9 E0 CF 01 
To:      8A 54 24 1C 90 90 90

Code: [Select]
Address: 0x00496788
From:    8A 14 4D F9 E0 CF 01
To:      8A 54 24 1C 90 90 90

Code: [Select]
Address: 0x004963CB
From:    8A 1C 45 F9 E0 CF 01
To:      8A 5C 24 14 90 90 90

The way this works is that the following functions:
Code: [Select]
0x496310: GetCharacterHP (int lvl, int char_id)
0x496440: GetCharacterStat (int lvl, int char_id, int stat)

are called with the character level as a parameter and it's easy to pull this off the stack when it tries to get the value for the junctioned magic amount.

Hit and Eva are calculated in the following functions:
Code: [Select]
0x4967C0: GetCharacterHit (int char_id)
0x4968A0: GetCharacterEva (int char_id, int unk1)

# Others 
## Crisis Level 

#Random MOD 0-255 + 160 (Set to 0 for no variance)
942E7 = 83 E1 00 90 90 90
#Default: +160, Current = 255
942F2 = 81 C1 FF 00 00 00
#Change this to EB 09 (or JMP 494329) to set 'fixed' crisis level proc
#or deactivate limits altogether with 0
#49431E

#494329 - Where crisis level 4 checked for, can be changed to any level or 0
```
0x0941F0: Crisis Level checks start here

0x0942E7: Random MOD for variance in Crisis Level (0x000000FF - 255) //Adjusting this value can shrink variance in Crisis Level
0x0942F2: Fixed +160 added to Random MOD value (0x000000A0 - 160)
```

## Add VIT0 resist
#Author - JWP
#Adds check for 20th status resist byte [VIT0] for enemies
#Called 'prcnt' in ifrit editor
#USE AT OWN RISK

#Default: B90A 0A0A 0A
#8BEE8 = E9A8 0000 00

#Default: 9090 9090 9090 9090
#8BF95 = 8A87 7B01 0000 EB77

#Default: 9090 9090 9090 9090 9090 90
#8C014 = 8886 C07B D201 E912 0100 00

#Default: 9090 9090 9090 9090 9090
#8C131 = B90A 0A0A 0AE9 B2FD FFFF

## Add new attack
#Author - JWP
#The space in the jump table - around 0x492AB8 (0x92AB8 in exe).
#There's room for 1 more attack type without any major changes.
#New Attack Type: Offence, removes statuses

#Default: 11
#91C19 = 12

#Default: E8 7B 00 00
#92010: E9 1F 69 6D

#Default: 90
#9208A: 00

#Default: 24
#922D9 = 25

#Default: 90 90 90 90
#92AB8 = 5E 89 B6 00

#Default: All 0s
#768934 = 80 7C E4 38 12 74 07 E8 50 97 92 FF EB 17 FF 35 34 A2 D2 01 66 A1 3E #A2 D2 01 50 55 51 E8 CA 8E 92 FF 83 C4 10 E9 B7 96 92 FF 6A 12 8B 4C 24 30 8B #54 24 28 51 56 52 E8 60 91 92 FF 83 C4 10 8B F8 E9 58 9C 92 FF

#if (magic_attack_type != 0x12) {
#inflict_status_function(caster_id, target_id, 1) - 1 means it's a magic attack, 0 is for physical attacks
#}
#else {
#cure_status_function(target_id, spell_power, status_word, status_dword)
#}

## Disable flash

#For disabling certain flashes like critical attacks
1067BC = 90:5

#Disable all battle flashes
1712C0 = C3

#Hextlaunch addresses for flash disable (when game is running)
Code: [Select]
#For certain flashes like critical attacks
5067BC = 90:5

#Disable all battle flashes
5712C0 = C3


## Angel wing
The spell used under Angel Wing is decided in function 0x483D60.

From your post, it looks like you want the following weightings:
Code: [Select]
Firaga - 11
Blizzaga - 11
Thundaga - 10
Water - 6
Bio - 6
Pain - 6
Meltdown - 6
Demi - 6
Tornado - 32
Quake - 32
Flare - 48
Holy - 48
Meteor - 16
Ultima - 18

0x483D67 - does the lookup
e8 b4 b2 00 00 25 ff 00 00 00 b3 40 31 c9 31 d2 02 91 86 3D 48 00 41 39 c2 7e f5 89 c8 eb 74

0x483D86 - spell table
00 00 0B 00 00 0B 00 00 0A 06
00 06 06 30 30 10 20 20 12 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 06 00 00 00 06 00
00 00 00 00 00 00

0x483E09 - patch to ignore a jump
90 90

0x48D819 - hacky patch that needs to be improved
EB 25
