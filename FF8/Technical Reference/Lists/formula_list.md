---
layout: default
title: Formula
parent: List
---

Here you'll find all formula as found in the game

# Magic

## Classic

Damage = AttackerMag + Power  
Damage = Damage * (265 - TargetSpr) / 4  
Damage = Damage * Power / 256  
Damage = Damage * ([0..32] + 240) / 256   

$$
\text{Damage} = \left( \left( \left( \text{AttackerMag} + \text{Power} \right) \times \frac{265 - \text{TargetSpr}}{4} \right) \times \frac{\text{Power}}{256} \right) \times \frac{[0..32] + 240}{256}
$$

## Demi, Percent

Damage = AttackPower * TargetCurrentHP / 16

$$
\text{Damage} = \frac{\text{AttackPower} \times \text{TargetCurrentHP}}{16}
$$

{: .note }
Demi power = 4
Percent = 15

# GF

## Classic damage:

Damage = LevelMod * Level / 10 + Power + PowerMod  
Damage = Damage * (265 - TargetSpr) / 8  
Damage = Damage * Power / 256  
Damage = Damage * Boost / 100  
Damage = Damage * (100 + SummonMagBonus) / 100  
Damage = Damage * ([0..32] + 240) / 256   

$$
\text{Damage} = \left( \left( \left( \left( \left( \left( \text{LevelMod} \times 
\frac{\text{Level}}{10} + \text{Power} + \text{PowerMod} \right) \times \frac{265 - 
\text{TargetSpr}}{8} \right) \times \frac{\text{Power}}{256} \right) \times \frac{\text{Boost}}{100} 
\right) \times \frac{100 + \text{SummonMagBonus}}{100} \right) \times \frac{[0..32] + 240}{256}
$$

### Modifiers

#### Monsters
If monster: 
Damage = Damage / 2

#### Elem
If elem:
Damage = Damage * (900 - ElemDef) / 100

#### Protective magic:
If Shell:
Damage = Damage / 2

## Diablos

Damage = TargetMaxHP * Level / (PowerMod - LevelMod + 100)





