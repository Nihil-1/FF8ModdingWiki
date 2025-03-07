---
layout: default
parent: Field Opcodes
title: 013_PSHAC
permalink: /013-pshac/
---

-   Opcode: **0x013**
-   Short name: **PSHAC**
-   Long name: Push actor code???

#### Argument

ID of the entity to reference

#### Stack

none

#### Description

Push the entity ID of an actor onto the stack. This is always used before a call to [CTURN](090_CTURN) to set which character will be faced. IDK what happens when you try to use literals for CTURN or why this function is necessary.
