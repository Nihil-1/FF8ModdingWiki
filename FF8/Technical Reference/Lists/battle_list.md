---
layout: default
title: Battle
parent: List
---


# Encounter data

| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| 0x0   | Regular battle.                                                      |
| 0x1   | No escape?                                                           |
| 0x2   | Disable victory fanfare (battle music keeps playing after win/loss). |
| 0x4   | Inherit countdown timer from field.                                  |
| 0x8   | No Item/XP Gain?                                                     |
| 0x10  | Use current music as battle music.                                   |
| 0x20  | Force preemptive attack.                                             |
| 0x40  | Force back attack.                                                   |
| 0x80  | Unknown.                                                             |

# Monster info byte flag


## Byte 0

| Bit Position | Flag (Hex) | Description |
|--------------|------------|-------------|
| 0 (LSB)      | 0x01       | UNKNOWN0    |
| 1            | 0x02       | UNKNOWN1    |
| 2            | 0x04       | UNKNOWN2    |
| 3            | 0x08       | UNKNOWN3    |
| 4            | 0x10       | UNKNOWN4    |
| 5            | 0x20       | UNKNOWN5    |
| 6            | 0x40       | UNKNOWN6    |
| 7 (MSB)      | 0x80       | UNKNOWN7    |


## Byte 1

| Bit Position | Flag (Hex) | Description           |
|--------------|------------|-----------------------|
| 0 (LSB)      | 0x01       | Zombie                |
| 1            | 0x02       | Fly                   |
| 2            | 0x04       | zz1                   |
| 3            | 0x08       | LvUp-Down Immunity    |
| 4            | 0x10       | HP Hidden             |
| 5            | 0x20       | Auto-Reflect          |
| 6            | 0x40       | Auto-Shell            |
| 7 (MSB)      | 0x80       | Auto-Protect          |

## Byte 2

| Bit Position | Flag (Hex) | Description           |
|--------------|------------|-----------------------|
| 0 (LSB)      | 0x01       | zz1                   |
| 1            | 0x02       | zz2                   |
| 2            | 0x04       | unused                |
| 3            | 0x08       | unused                |
| 4            | 0x10       | unused                |
| 5            | 0x20       | unused                |
| 6            | 0x40       | Gravity Immunity      |
| 7 (MSB)      | 0x80       | Always obtains card   |

# Attack flag

| ID   | Meaning          |
|------|------------------|
| 0x01 | Shelled          |
| 0x02 | ?                |
| 0x04 | ?                |
| 0x08 | BreakDamageLimit |
| 0x10 | Reflected        |
| 0x20 | ?                |
| 0x40 | ?                |
| 0x80 | Revive?          |


enum MonsterInfoByteFlags0
{
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN0 = 0x1,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN1 = 0x2,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN2 = 0x4,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN3 = 0x8,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN4= 0x10,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN5= 0x20,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN6= 0x40,
  MONSTER_INFO_BYTE_FLAG0_UNKNOWN7= 0x80,
};
