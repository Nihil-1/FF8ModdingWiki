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

## GF/ Magic Type damage

| Value | Description      |
|-------|------------------|
| 0x00  |                  |
| 0x01  | % Current HP     |
| 0x02  |                  |
| 0x04  | Diablos damage   |
| 0x05  | GF damage        |
| 0x06  | Magic ignore SPR |
| 0x0A  | Magic damage     |
| 0x11  |                  |









