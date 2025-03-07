---
layout: default
title: Menu abilities
nav_order: 19
parent: Kernel
permalink: /technical-reference/main/kernel/menu-abilities/
---

## General

| Offset | Sections | Section Size |
|--------|----------|--------------|
| 0x43C0 | 24       | 8 bytes      |

## Sections

| Offset | Ability        |
|--------|----------------|
| 0x43C0 | Haggle         |
| 0x43C8 | Sell-High      |
| 0x43D0 | Familiar       |
| 0x43D8 | Call Shop      |
| 0x43E0 | Junk Shop      |
| 0x43E8 | T Mag-RF       |
| 0x43F0 | I Mag-RF       |
| 0x43F8 | F Mag-RF       |
| 0x4400 | L Mag-RF       |
| 0x4408 | Time Mag-RF    |
| 0x4410 | ST Mag-RF      |
| 0x4418 | Supt Mag-RF    |
| 0x4420 | Forbid Mag-RF  |
| 0x4428 | Recov Med-RF   |
| 0x4430 | ST Med-RF      |
| 0x4438 | Ammo-RF        |
| 0x4440 | Tool-RF        |
| 0x4448 | Forbid Med-RF  |
| 0x4450 | GFRecov Med-RF |
| 0x4458 | GFAbl Med-RF   |
| 0x4460 | Mid Mag-RF     |
| 0x4468 | High Mag-RF    |
| 0x4470 | Med LV Up      |
| 0x4780 | Card Mod       |

## Section Structure

| Offset | Length  | Description                                                                           |
|--------|---------|---------------------------------------------------------------------------------------|
| 0x0000 | 2 bytes | Offset to ability name                                                                |
| 0x0002 | 2 bytes | Offset to ability description                                                         |
| 0x0004 | 1 byte  | AP Required to learn ability                                                          |
| 0x0005 | 1 byte  | Index to m00X files in menu.fs <br/>_(first 3 sections are treated as special cases)_ |
| 0x0006 | 1 byte  | Start offset                                                                          |
| 0x0007 | 1 byte  | End offset                                                                            |