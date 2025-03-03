---
layout: default
title: Angel Gilgamesh Odin
parent: List
---

## Angel Gilgamesh Odin Flags

| Flag | Meaning                              |
|------|--------------------------------------|
| 0x01 | In Laguna dream                      |
| 0x02 | Possess odin                         |
| 0x04 |                                      |
| 0x08 | Possess Gilgamesh                    |
| 0x10 |                                      |
| 0x20 | Rinoa alternate limit break unlocked |
| 0x40 |                                      |
| 0x80 |                                      |

Note:
Rinoa alternate limit break Unlocked: This is only called once in the whole game - the first time you enter the Ragnarok in space.<br/> It unlocks Rinoa's alternate limit break after she becomes a sorceress.


enum SpecialByteFlag {
    SPECIAL_BYTE_FLAG_IN_LAGUNA_DREAM = 0x01,                     // In Laguna dream
    SPECIAL_BYTE_FLAG_POSSESS_ODIN = 0x02,                        // Possess Odin
    SPECIAL_BYTE_FLAG_UNKNOWN_04 = 0x04,                           // UNKNOWN
    SPECIAL_BYTE_FLAG_POSSESS_GILGAMESH = 0x08,                   // Possess Gilgamesh
    SPECIAL_BYTE_FLAG_UNKNOWN_10 = 0x10,                           // UNKNOWN
    SPECIAL_BYTE_FLAG_RINOA_ALTERNATE_LIMIT_BREAK_UNLOCKED = 0x20, // Rinoa alternate limit break unlocked
    SPECIAL_BYTE_FLAG_UNKNOWN_40 = 0x40,                           // UNKNOWN
    SPECIAL_BYTE_FLAG_UNKNOWN_80 = 0x80                            // UNKNOWN
};