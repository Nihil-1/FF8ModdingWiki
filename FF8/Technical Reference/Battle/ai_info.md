---
layout: default
parent: Battle
title: Battle Scripts
author: nihil, hobbitdur
---

FF8 monster battle scripts are divided into 5 sections, **init**, **turn**, **counter**, **death** and **pre-counter**.
Each section contains code that is executed at different times during the battle.
- Init: executes once when the monster is loaded into battle.
- Turn: executes once the monster's ATB bar fills. This happens after the monsters turn counter is incremented.
- Counter: executes when the monster is targeted by a battle command.
- Death: executes when the monster’s HP reaches 0 or it is afflicted with the *Death* status.  (Eject may not trigger this section - this needs further testing.)
- Pre-Counter: similar to counter but executed before it. Needs further testing. Seems to be used mostly for checking if the monster has the *Death* status and then change its animation. Ifs, variable assignments and stat changes can also be used. Launching an attack from this section crashes the game.

The order of execution when a monster is attacked is: **pre-counter** -> **death** (if killed) -> **counter**
Note: **pre-counter** code will **ONLY** be executed after an attack that kills a monster if the monster's **death** section has code in it (apart from "return").
Note: if the **death** section is empty, it will function like a **_die_** opcode.
Note: if the **death** section is empty, it is mandatory for it to eventually execute a **_die_** opcode, otherwise the monster will continue, even on 0 HP, making the battle unwinnable for the player and forcing them to run. If running is not an option, this results in a soft locked.


1. TOC
{:toc}

# Opcodes

Monster AI sections are composed of one-byte opcodes, each followed by a variable number of the bytes used as parameters.
These opcodes define the monster's behaviour in battle.
Note: descriptions are written from the monster's perspective, so "opposing party" refers to the party of playable characters.

## Opcode 0x00 (0) - return

### Summary

| Opcode | IfritAI name | Size | Short Description  |
|--------|--------------|------|--------------------|
| 0x00   | return       | 1    | End monster's turn |

This opcode is used to end the monster's turn, preventing further execution of code.
It is mandatory for every battle script section to end with a **_return_**.

### Parameters

None

---

## Opcode 0x01 (1) - print

### Summary

| Opcode | IfritAI name | Size | Short Description   |
|--------|--------------|------|---------------------|
| 0x01   | print        | 2    | Print text          |

### Parameters

| Position | Size | Name       | Type                     | Short Description     |
|----------|------|------------|--------------------------|-----------------------|
| 1        | 1    | **TextID** | [int](../OpCodeType#int) | The index of the text |

Texts are defined in [section 7](../FileFormat_DAT#section-7-informations--stats) of c0mxxx.dat files.  
Each text has an ID, starting from 0 and incrementing with each subsequent text.  
**TextID** correspond to this ID.

---

## Opcode 0x02 (2) - if

### Summary

The if opcode allow to execute code only on certain condition

| Opcode | IfritAI name | Size | Short Description |
|--------|--------------|------|-------------------|
| 0x02   | if           | 1    | Define condition  |

### Parameters

The if opcode is a really complex one with lots of different possibilities.  
It is composed of a subject that define how the other parameters are used.  
Then it uses 3 parameters for the condition: the left part of the condition, the right part, and the comparator.  
So it does something like this: \[ConditionLeftPart\] \[Comparator\] \[ConditionRightPart\], for ex: COMBAT SCENE == 76  
Then there is a jump param to define the jump size if the condition is not met

| Position | Size | Name                   | Type                                   | Short Description                                    |
|----------|------|------------------------|----------------------------------------|------------------------------------------------------|
| 1        | 1    | **SubjectID**          | [SubjectID](#subjectid)                | Define what the if will be about                     |
| 2        | 1    | **ConditionLeftPart**  | Vary                                   | The left condition                                   |
| 3        | 1    | **Comparator**         | [Comparator](../OpCodeType#comparator) | The comparator of the condition                      |
| 4        | 1    | **ConditionRightPart** | Vary                                   | The right condition                                  |
| 5        | 1    | **Padding**            | [Unused](../OpCodeType#unused)         | Always 0x00 (changing it has no impact)              |
| 6        | 2    | **Jump**               | [int](../OpCodeType#int)               | The number of byte to jump if the condition is false |

### SubjectID

#### General info

The **SubjectID** defines what will be the type of the left part and right part of the condition  
The _Short text_ is a description of the subject id.  
The _Left text_ is the meaning of the **ConditionLeftPart**. {} is to be replaced with the value hold by **ConditionLeftPart** depending of _Param left type_  
The _Param left type_ define the type to use to translate the **ConditionLeftPart**  
Same logic for the **ConditionRightPart**  
The _Param list_ can feed the param type with additional info.

#### Subject list

| SubjectID | Short text                | Left text                           | Param left type                                                    | Right text     | Param right type         | Param list |
|-----------|---------------------------|-------------------------------------|--------------------------------------------------------------------|----------------|--------------------------|------------|
| 0         | HP OF SPECIFIC TARGET     | HP_SPE of {}                        | [target_advanced_specific](../OpCodeType#target-advanced-specific) |                | percent                  |            |
| 1         | HP OF GENERIC TARGET      | HP_GEN of {}                        | [target_advanced_generic](../OpCodeType#target-advanced-generic)   |                | percent                  |            |
| 2         | RANDOM VALUE              | RANDOM VALUE BETWEEN 0 AND {}       | int_shift                                                          |                | int                      | [-1]       |
| 3         | COMBAT SCENE              | COMBAT SCENE                        |                                                                    |                | int                      |            |
| 4         | STATUS OF SPECIFIC TARGET | STATUS_SPE OF {}                    | target_advanced_specific                                           |                | status_ai                |            |
| 5         | STATUS OF GENERIC TARGET  | STATUS_GEN OF {}                    | target_advanced_generic                                            |                | status_ai                |            |
| 6         | NUMBER OF MEMBER          | NUMBER OF MEMBER OF {}              | target_advanced_generic                                            |                | int                      |            |
| 9         | ALIVE                     | ALIVE                               |                                                                    |                | target_advanced_specific |            |
| 10        | ATTACKER                  | ATTACKER                            | subject10                                                          |                | complex                  |            |
| 14        | GROUP LEVEL               | GROUP LEVEL OF {}                   | target_advanced_generic                                            |                | int                      |            |
| 15        | ALIVE IN SLOT             | ALLY IN SLOT {}                     | int_right                                                          | ALIVE          | alive                    |            |
| 16        | GENDER CHECK              | AT LEAST ONE ENEMY ALIVE HAS GENDER |                                                                    |                | gender                   |            |
| 17        | GFORCE OBTAINED           | Gforce to be stolen                 | const                                                              | Not yet stolen | const                    | [200, 204] |
| 18        | ODIN OBTAINED             | {} POSSESS ODIN                     | target_advanced_generic                                            |                | int                      |            |
| 19        | COUNTDOWN                 | COUNTDOWN                           |                                                                    |                | int                      |            |
| 20        | STATUS OF ALL IN TEAM     | STATUS OF ALL IN {}                 | target_advanced_generic                                            |                | status_ai                |            |
| \>20      | Var                       | var                                 | var_name                                                           |                | int                      |            |

If the **SubjectID** is > 20, it means the subject is of type var, the **ConditionLeftPart** is the ID of the var and the **ConditionRightPart** the value of the var to be compared

#### Additional info:

Here are additional info for some values

##### HP OF SPECIFIC TARGET

The **ConditionLeftPart** 0xCB (203) is persists across battles

- **Byte #1:** 0x00 (Self / Last command user) or 0x01 (Any ally / opponent)
- **Byte #2:**
    - 0xC8 (200): Own HP / Any opponent's HP
    - 0xC9 (201): Unused / Any ally's HP
    - 0xCB (203): Last command user's HP (persists across battles) / Unused
- **Byte #4:** Remaining HP percentage
    - 0x0A (10) = 100%
    - 0x09 (9)  = 90%
    - . . .

##### 2. **Random Number Check**

- **Byte #1:** 0x02
- **Byte #2:** Exclusive upper bound of range (0 to this value - 1)
- **Byte #4:** Number to compare against

##### 3. **Status Check**

###### At least 1 member:

- **Byte #1:** 0x04 (Self / Last command user) or 0x05 (Any ally / opponent)
- **Byte #2:**
    - 0xC8 (200): Self / Any opponent
    - 0xC9 (201): Unused / Any ally
    - 0xCB (203): Last command user / Unused
- **Byte #4:** Status ID

###### All members of party:
- **Byte #1:** 0x14 (20)
- **Byte #2:**
    - 0xC8 (200): Opposing part
    - 0xC9 (201): Own party
- **Byte #4:** Status ID

##### 4. **Alive Count Check**

- **Byte #1:** 0x06
- **Byte #2:**
    - 0xC8 (200): Opposing party
    - 0xC9 (201): Own party
- **Byte #4:** Number to compare against

##### 5. **Specific Entity Alive Check**

- **Byte #1:** 0x09
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Entity ID

##### 6. **Last Action / Turn Count Check**

- **Byte #1:** 0x0A (10)
- **Byte #2:**
    - 0x00: Damage Type (Byte #4: 0x00 = Physical, 0x01 = Magical)
    - 0x01: Last command user ID (Byte #4 = Entity ID)
    - 0x02: Turn Counter that increases as soon as the ATB bar is full (Byte #4 = Number)
    - 0x03: Command (Byte #4: 0x01 = Attack, 0x02 = Magic, 0x04 = Item, 0x06 = Draw, 0xFE = GF)
    - 0x04: ID (Byte #4: Magic/Item/GF ID)
    - 0x05: Element (Byte #4 = Element ID)
    - 0xCB (203): Last command user party (Byte #4: 0xC8 = Own part, 0xC9 = Opposing party)  **TO BE TESTED**

##### 7. **Entity Alive Check (In specific slot)**

- **Byte #1:** 0x0F (15)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Target slot + 3 (e.g., 0x03 for slot 0)

##### 8. **Sex check**

- **Byte #1:** 0x10 (16)
- **Byte #4:**
    - 0xCA (202): Male
    - 0xCB (203): Female

##### 9. **GF Check (Not yet obtained)**

- **Byte #1:** 0x11 (17)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** 0xCC (204)

##### 10. **Odin Acquisition Check (true if obtained)**

- **Byte #1:** 0x12 (18)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** 0x00 / 0x01 (true / false)

##### 11. **Timer Check**

- **Byte #1:** 0x13 (19)
- **Byte #2:** 0xC8 (Unused?)

##### 12. **Variable Check**

- **Byte #1:** Variable ID
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Value to compare against

---

## Opcode 0x04 (4) - target

### Summary

This opcode defines a target, it must be used before any opcode that requires a target (like launching an ability).

| Opcode | IfritAI name | Size | Short Description |
|--------|--------------|------|-------------------|
| 0x04   | target       | 2    | Print text        |

### Parameters

| Position | Size | Name            | Type                                      | Short Description |
|----------|------|-----------------|-------------------------------------------|-------------------|
| 1        | 1    | **Target** | [TargetBasic](../OpCodeType#target-basic) | The target        |

---

## Opcode 0x0B (11) - useRandom

### Summary

Picks one of 3 abilities to use randomly, then uses it

| Opcode | IfritAI name | Size | Short Description            |
|--------|--------------|------|------------------------------|
| 0x0B   | useRandom    | 4    | Use random ability between 3 |

### Parameters

| Position | Size | Name                    | Type                                                     | Short Description       |
|----------|------|-------------------------|----------------------------------------------------------|-------------------------|
| 1        | 1    | **MonsterLineAbilit1** | [MonsterLineAbility](../OpCodeType#monster-line-ability) | The first ability line  |
| 2        | 1    | **MonsterLineAbilit2**  | [MonsterLineAbility](../OpCodeType#monster-line-ability) | The second ability line |
| 3        | 1    | **MonsterLineAbility3** | [MonsterLineAbility](../OpCodeType#monster-line-ability) | The third ability line  |

---

## Opcode 0x0C (12) - use

### Summary

Use one ability

| Opcode | IfritAI name | Size | Short Description |
|--------|--------------|------|-------------------|
| 0x0C   | use          | 2    | Use one ability   |

### Parameters

| Position | Size | Name                   | Type                                                     | Short Description |
|----------|------|------------------------|----------------------------------------------------------|-------------------|
| 1        | 1    | **MonsterLineAbility** | [MonsterLineAbility](../OpCodeType#monster-line-ability) | The ability line  |

---

## Opcode 0x0E (14) - var

### Summary

Sets local variable that will be only accessible by this monster during the battle

| Opcode | IfritAI name | Size | Short Description               |
|--------|--------------|------|---------------------------------|
| 0x0E   | var          | 3    | Set local var to specific value |

### Parameters

| Position | Size | Name      | Type                                | Short Description             |
|----------|------|-----------|-------------------------------------|-------------------------------|
| 1        | 1    | **Var**   | [LocalVar](../OpCodeType#local-var) | The var to store the data     |
| 1        | 1    | **Value** | [int](../OpCodeType#int)            | The value to set the var with |

---

## Opcode 0x0F (15) - gvar

Sets global variable (accessible by all monsters)

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to assign

### Summary

Sets global variable (accessible by all monsters)

| Opcode | IfritAI name | Size | Short Description       |
|--------|--------------|------|-------------------------|
| 0x0F   | gvar         | 3    | Set global var to value |

### Parameters

| Position | Size | Name      | Type                                 | Short Description             |
|----------|------|-----------|--------------------------------------|-------------------------------|
| 1        | 1    | **Var**   | [LocalVar](../OpCodeType#global-var) | The var to store the data     |
| 1        | 1    | **Value** | [int](../OpCodeType#int)             | The value to set the var with |

---

## Opcode 0x11 (17) - svar

### Summary

Sets savemap variable (not sure how it it stored)

| Opcode | IfritAI name | Size | Short Description        |
|--------|--------------|------|--------------------------|
| 0x11   | svar         | 3    | Set savemap var to value |

### Parameters

| Position | Size | Name      | Type                                    | Short Description             |
|----------|------|-----------|-----------------------------------------|-------------------------------|
| 1        | 1    | **Var**   | [SavemapVar](../OpCodeType#savemap-var) | The var to store the data     |
| 1        | 1    | **Value** | [int](../OpCodeType#int)                | The value to set the var with |

---

## Opcode 0x12 (18) - add (2 args)

### Summary

Adds value to local variable that will be only accessible by this monster during the battle

| Opcode | IfritAI name | Size | Short Description      |
|--------|--------------|------|------------------------|
| 0x12   | add          | 3    | Add value to local var |

### Parameters

| Position | Size | Name      | Type                                | Short Description           |
|----------|------|-----------|-------------------------------------|-----------------------------|
| 1        | 1    | **Var**   | [LocalVar](../OpCodeType#local-var) | The var to store the data   |
| 1        | 1    | **Value** | [int](../OpCodeType#int)            | The value to add to the var |

---

## Opcode 0x13 (19) - gadd

### Summary

Adds value to global var (accessible by all monsters)

| Opcode | IfritAI name | Size | Short Description       |
|--------|--------------|------|-------------------------|
| 0x13   | gadd         | 3    | Add value to global var |

### Parameters

| Position | Size | Name      | Type                                  | Short Description           |
|----------|------|-----------|---------------------------------------|-----------------------------|
| 1        | 1    | **Var**   | [GlobalVar](../OpCodeType#global-var) | The var to store the data   |
| 1        | 1    | **Value** | [int](../OpCodeType#int)              | The value to add to the var |

---

## Opcode 0x15 (21) - sadd

### Summary

Adds value to savemap var (not sure where it is stored)

| Opcode | IfritAI name | Size | Short Description        |
|--------|--------------|------|--------------------------|
| 0x15   | sadd         | 3    | Add value to savemap var |

### Parameters

| Position | Size | Name      | Type                                    | Short Description           |
|----------|------|-----------|-----------------------------------------|-----------------------------|
| 1        | 1    | **Var**   | [SavemapVar](../OpCodeType#savemap-var) | The var to store the data   |
| 1        | 1    | **Value** | [int](../OpCodeType#int)                | The value to add to the var |

---

## Opcode 0x16 (22) - IfritAI name: recover

### Summary

Sets remaining HP to max HP

| Opcode | IfritAI name | Size | Short Description           |
|--------|--------------|------|-----------------------------|
| 0x16   | recover      | 1    | Sets remaining HP to max HP |

### Parameters

None

---

## Opcode 0x17 (23) - setEscape
### Summary


| Opcode | IfritAI name | Size | Short Description      |
|--------|--------------|------|------------------------|
| 0x17   | setEscape    | 2    | Sets ability to escape |

### Parameters

| Position | Size | Name                | Type                       | Short Description                         |
|----------|------|---------------------|----------------------------|-------------------------------------------|
| 1        | 1    | **EscapeActivated** | [Bool](../OpCodeType#bool) | True to allow escape, False to deactivate |


---

## Opcode 0x2E - blowAway
### Summary

Makes previous ability blow away magic from target (use after opcode 0x0B or 0x0C, useRandom or use).
Note that blown away magic is removed from junctions too.

| Opcode | IfritAI name | Size | Short Description |
|--------|------------|------|------------------|
| 0x2E   | blowAway   | 1    | Blow away magic  |

### Parameters

None

---

