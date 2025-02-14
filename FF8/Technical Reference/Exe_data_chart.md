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

[Original Qhimm post](https://forums.qhimm.com/index.php?topic=15211.0)

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

# Command
## Cover Command

```
0x091091: Cover Damage Reduction (D1 EE - Take half damage while covering)
```

## Darkside Command

```
0x0905AF: HP Cost (C1 FA 02 - 10% HP Cost) //Determines how much HP% Darkside costs to use
0x091069: Damage Modifier (8D 34 76 - *3 Damage) //Determines how much bonus damage Darkside inflicts
```

## Kamikaze Command

```
0x092D72: Kamikaze Damage Modifier (8D 04 80 - Damage = *6 of user's maximum HP)
```


# Others 
## Crisis Level 

```
0x0941F0: Crisis Level checks start here

0x0942E7: Random MOD for variance in Crisis Level (0x000000FF - 255) //Adjusting this value can shrink variance in Crisis Level
0x0942F2: Fixed +160 added to Random MOD value (0x000000A0 - 160)
```
