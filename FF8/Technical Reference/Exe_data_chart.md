---
layout: default
title: Exe data
parent: Technical Reference
nav_order: 11
---

Here will be put all info on the exe editing. The base is version 2013 in english

1. TOC
{:toc}


# Limit
## Damage limit

```
0x091133: "No Damage Limit" Damage Bonus (0x0000C351 = 50,001)[dword]
0x091139: Normal Damage Cap (0x0000270F = 9,999)[dword]
```

## Maximum HP

```
0x095A1C: Maximum HP Cap (0x0000270F = 9,999)[dword] //Value to compare to. Setting this the 1 will set all characters to have the Maximum HP of 9999 all the time. This also gives the "Maximum HP" Achievment.
0x095A23: Maximum HP Cap (0x0000270F = 9,999)[dword] //Value to set to if exceeds previous check.
```

## Maximum draw

```
0x08FE00: Maximum In-Battle Draw Cap (0x09 = 9)[byte] //Value to compare to. Setting this to 1 will make you always Draw the maximum amount (in battle).
0x08FE04: Maximum In-Battle Draw Cap (0x00000009 = 9)[dword] //Value to set to if exceeds previous check.
```
