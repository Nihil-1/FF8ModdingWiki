---
layout: default
parent: Battle
title: Opcode Type List
author: nihil, hobbitdur
---

# Type list

## int

This type take literally the value of the parameter.
If the parameter is more than 1 byte, the int is in little endian

## unused

Means the value is not used and could be changed by any value without any impact on the game

## Comparator

| Opcode int | Opcode hex | Comparator pretty | Comparator IfritAI |
|------------|------------|-------------------|--------------------|
| 0          | 0x00       | ==                | ==                 |
| 1          | 0x01       | <                 | <                  |
| 2          | 0x02       | \>                | \>                 |
| 3          | 0x03       | ≠                 | !=                 |
| 4          | 0x04       | ≤                 | <=                 |
| 5          | 0x05       | ≥                 | \>=                |

## Target advanced specific

| Opcode int | Opcode hex | Text          |
|------------|------------|---------------|
| 200        | 0xC8       | SELF          |
| 203        | 0xCB       | LAST ATTACKER |

## Target advanced generic

| Opcode int | Opcode hex | Text       |
|------------|------------|------------|
| 200        | 0xC8       | ENEMY TEAM |
| 201        | 0xC9       | ALLY TEAM  |
