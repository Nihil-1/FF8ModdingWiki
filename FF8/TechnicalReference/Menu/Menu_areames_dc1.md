---
layout: default
parent: Menu
title: areames.dc1 File Format
permalink: /technicalreferencemenumenu-areames-dc1/
---

## Format

Same format as: **[Menu mngrp string section](../Menu_mngrp_strings_section)**

## Contents

Contains area strings. **Offsets\[Location number from save\]** gets the string that shows on the menu/load/save screens. The special character **0xE\#\#** is 2 bytes. Subtract **0xE20** and you get the desired in **[namedec.bin]({{site.baseurl}}/FF8/TechnicalReference/Main/Main_namedic)**.

### Example

**0xE22- Alcauld Plains**, **0xE22** becomes **Balamb**, so final string is **Balamb- Alcauld Plains**
