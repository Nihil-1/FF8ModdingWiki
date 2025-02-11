---
layout: default
parent: Battle
title: Opcode List
author: nihil
---

This section will list all opcode of the game, with a type list of parameters

1. TOC
{:toc}

# Opcode list

## Opcode 0x00 (0) - return

### Summary

| Opcode | IfritAI name | Short Description         |
|--------|--------------|---------------------------|
| 0x00   | return       | Exit the AI for this turn |

This function will stop the code execution and leave the AI turn.  
It can be used to either stop in a condition or used at the end of the AI code.  
It is mandatory to have one **_return_** for every end of execution.

### Parameters

None



---

## Opcode 0x01 (1) - print

### Summary

| Opcode | IfritAI name | Short Description |
|--------|--------------|-------------------|
| 0x01   | print        | Print text        |

### Parameters

| Parameter position | Parameter name | Parameter type | Short Description     |
|--------------------|----------------|----------------|-----------------------|
| 1                  | **TextID**     | [int](#int)    | The index of the text |

Text in combat are defined in [section 7](../FileFormat_DAT#section-7-informations--stats) of c0mxxx.dat files.  
Each text as an ID starting from 0 to the number of text - 1.  
**TextID** correspond to this ID

---

## Opcode 0x02 (2) - If/Else Statement (7 args)

### IfritAI name: if

If and else jump

### General Structure:

- **Byte #1:** Condition Type
- **Byte #2:** Target / Parameter
- **Byte #3:** Comparison Operator
- **Byte #4:** Comparison Value
- **Byte #5:** Always 0x00
- **Byte #6 and #7:** Bytes to jump if condition is false
    - **Byte #6:** (Bytes to Jump % 256)
    - **Byte #7:** (Bytes to Jump // 256)

### Condition Types:

### 1. **Remaining HP Check**

- **Byte #1:** 0x00 (Self / Last command user) or 0x01 (Any ally / opponent)
- **Byte #2:**
    - 0xC8 (200): Own HP / Any opponent's HP
    - 0xC9 (201): Unused / Any ally's HP
    - 0xCB (203): Last command user's HP (persists across battles) / Unused
- **Byte #4:** Remaining HP percentage
    - 0x0A (10) = 100%
    - 0x09 (9)  = 90%
    - . . .

### 2. **Random Number Check**

- **Byte #1:** 0x02
- **Byte #2:** Exclusive upper bound of range (0 to this value - 1)
- **Byte #4:** Number to compare against

### 3. **Status Check**

### At least 1 member:

- **Byte #1:** 0x04 (Self / Last command user) or 0x05 (Any ally / opponent)
- **Byte #2:**
    - 0xC8 (200): Self / Any opponent
    - 0xC9 (201): Unused / Any ally
    - 0xCB (203): Last command user / Unused
- **Byte #4:** Status ID

  ### All members of party:
- **Byte #1:** 0x14 (20)
- **Byte #2:**
    - 0xC8 (200): Opposing part
    - 0xC9 (201): Own party
- **Byte #4:** Status ID

### 4. **Alive Count Check**

- **Byte #1:** 0x06
- **Byte #2:**
    - 0xC8 (200): Opposing party
    - 0xC9 (201): Own party
- **Byte #4:** Number to compare against

### 5. **Specific Entity Alive Check**

- **Byte #1:** 0x09
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Entity ID

### 6. **Last Action / Turn Count Check**

- **Byte #1:** 0x0A (10)
- **Byte #2:**
    - 0x00: Damage Type (Byte #4: 0x00 = Physical, 0x01 = Magical)
    - 0x01: Last command user ID (Byte #4 = Entity ID)
    - 0x02: Turn Counter that increases as soon as the ATB bar is full (Byte #4 = Number)
    - 0x03: Command (Byte #4: 0x01 = Attack, 0x02 = Magic, 0x04 = Item, 0x06 = Draw, 0xFE = GF)
    - 0x04: ID (Byte #4: Magic/Item/GF ID)
    - 0x05: Element (Byte #4 = Element ID)
    - 0xCB (203): Last command user party (Byte #4: 0xC8 = Own part, 0xC9 = Opposing party)  **TO BE TESTED**

### 7. **Entity Alive Check (In specific slot)**

- **Byte #1:** 0x0F (15)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Target slot + 3 (e.g., 0x03 for slot 0)

### 8. **Sex check**

- **Byte #1:** 0x10 (16)
- **Byte #4:**
    - 0xCA (202): Male
    - 0xCB (203): Female

### 9. **GF Check (Not yet obtained)**

- **Byte #1:** 0x11 (17)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** 0xCC (204)

### 10. **Odin Acquisition Check (true if obtained)**

- **Byte #1:** 0x12 (18)
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** 0x00 / 0x01 (true / false)

### 11. **Timer Check**

- **Byte #1:** 0x13 (19)
- **Byte #2:** 0xC8 (Unused?)

### 12. **Variable Check**

- **Byte #1:** Variable ID
- **Byte #2:** 0xC8 (Unused?)
- **Byte #4:** Value to compare against

---

## Opcode 0x04 (4) - IfritAI name: target (1 arg)

Defines target of battle ability

- **Byte #1:** Basic target

---

## Opcode 0x0B (11) - IfritAI name: useRandom (3 arg)

Picks one of 3 abilities to use randomly, then uses it

- **Byte #1 - Byte #3:** Monster ability ID (from the dat file)

---

## Opcode 0x0C (12) - IfritAI name: use (1 arg)

Uses ability

- **Byte #1:** Monster ability ID (from the dat file)

---

## Opcode 0x0E (14) - IfritAI name: var (2 args)

Sets local variable (accessible by this monster)

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to assign

---

## Opcode 0x0F (15) - IfritAI name: gvar (2 args)

Sets global variable (accessible by all monsters)

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to assign

---

## Opcode 0x11 (17) - IfritAI name: svar (2 args)

Sets savefile variable

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to assign

---

## Opcode 0x12 (18) - IfritAI name: add (2 args)

Adds value to local variable (accessible by this monster)

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to add

---

## Opcode 0x13 (19) - IfritAI name: gadd (2 args)

Adds value to battle variable (accessible by all monsters)

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to add

---

## Opcode 0x15 (21) - IfritAI name: sadd (2 args)

Adds value to savefile variable

- **Byte #1:** Variable
- **Byte #2:** Unsigned byte value to add

---

## Opcode 0x16 (22) - IfritAI name: recover

Sets remaining HP to max HP

---

## Opcode 0x17 (23) - IfritAI name: setEscape (1 arg)

Sets ability to escape true / false

- **Byte #1:** Boolean value

---

# Opcode 0x2E (46) - IfritAI name: blowAway

Makes previous ability blow away magic from target (use after opcode 0x0B or 0x0C, useRandom or use)

---

# Type list

## int

This type take literally the value of the parameter
