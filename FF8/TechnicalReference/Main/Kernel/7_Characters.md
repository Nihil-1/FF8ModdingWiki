---
layout: default
title: Characters
nav_order: 8
parent: Kernel
permalink: /technical-reference/main/kernel/7-characters/
---

## General

| Offset | Sections | Section Size |
|--------|----------|--------------|
| 0x37A4 | 11       | 36 bytes     |

## Sections

| Offset | Character |
|--------|-----------|
| 0x37A4 | Squall    |
| 0x37C8 | Zell      |
| 0x37EC | Irvine    |
| 0x3810 | Quistis   |
| 0x3834 | Rinoa     |
| 0x3858 | Selphie   |
| 0x387C | Seifer    |
| 0x38A0 | Edea      |
| 0x38C4 | Laguna    |
| 0x38E8 | Kiros     |
| 0x390C | Ward      |

## Section Structure

| Offset | Length  | Description                                                                                                                                            |
|--------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0000 | 2 bytes | Offset to character name<br/><br/>  _Squall and Rinoa have name offsets of 0xFFFF because their name is in the save game data rather than kernel.bin._ |
| 0x0002 | 1 byte  | Crisis level hp multiplier                                                                                                                             |
| 0x0003 | 1 byte  | Gender<br/><br/> 0x00 - Male<br/> 0x01 - Female                                                                                                        |
| 0x0004 | 1 byte  | Limit Break ID                                                                                                                                         |
| 0x0005 | 1 byte  | Limit Break Param<br/><br/> _used for the power of each renzokuken hit before finisher_                                                                |
| 0x0006 | 2 bytes | EXP modifier                                                                                                                                           |
| 0x0008 | 4 bytes | HP                                                                                                                                                     |
| 0x000C | 4 bytes | STR                                                                                                                                                    |
| 0x0010 | 4 bytes | VIT                                                                                                                                                    |
| 0x0014 | 4 bytes | MAG                                                                                                                                                    |
| 0x0018 | 4 bytes | SPR                                                                                                                                                    |
| 0x001C | 4 bytes | SPD                                                                                                                                                    |
| 0x0020 | 4 bytes | LUCK                                                                                                                                                   |