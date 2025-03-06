---
layout: default
title: Header
nav_order: 1
parent: Kernel
slug: header
permalink: /:categories/:slug/
---

## General

| Offset | Sections | Section Size |
|--------|----------|--------------|
| 0x0000 | 1        | 228 bytes    |

## Section Structure

| Offset | Length  | Description                                                                                                       |
|--------|---------|-------------------------------------------------------------------------------------------------------------------|
| 0x0000 | 4 bytes | Number of sections                                                                                                |
| 0x0004 | 4 bytes | Offset to [**Battle commands** section                              ](../Battle-commands)                         |
| 0x0008 | 4 bytes | Offset to [**Magic data** section                                   ](../Magic)                                   |
| 0x000C | 4 bytes | Offset to [**Junctionable GFs** section                             ](../Junctionable-GFs)                        |
| 0x0010 | 4 bytes | Offset to [**Enemy attacks** section                                ](../Enemy-attacks)                           |
| 0x0014 | 4 bytes | Offset to [**Weapons** section                                      ](../Weapons)                                 |
| 0x0018 | 4 bytes | Offset to [**Renzokuken finishers** section                         ](../Renzokuken-finishers)                    |
| 0x001C | 4 bytes | Offset to [**Characters** section                                   ](../Characters)                              |
| 0x0020 | 4 bytes | Offset to [**Battle items** section                                 ](../Battle-items)                            |
| 0x0024 | 4 bytes | Offset to [**Non-battle item name and description offsets** section ](../Non-battle-item-and-description-offsets) |
| 0x0028 | 4 bytes | Offset to [**Non-junctionable GF attacks** section                  ](../Non-junctionable-GF-attacks)             |
| 0x002C | 4 bytes | Offset to [**Command abilities in battle** section                  ](../Command-abilities-in-battle)             |
| 0x0030 | 4 bytes | Offset to [**Junction abilities** section                           ](../Junction-abilities)                      |
| 0x0034 | 4 bytes | Offset to [**Command abilities GF** section                         ](../Command-abilities-gf)                    |
| 0x0038 | 4 bytes | Offset to [**Stat percentage increasing abilities** section         ](../Stat-percentage-increasin-abilities)     |
| 0x003C | 4 bytes | Offset to [**Character abilities** section                          ](../Character-abilities)                     |
| 0x0040 | 4 bytes | Offset to [**Party abilities** section                              ](../Party-abilities)                         |
| 0x0044 | 4 bytes | Offset to [**GF abilities** section                                 ](../GF-abilities)                            |
| 0x0048 | 4 bytes | Offset to [**Menu abilities** section                               ](../Menu-abilities)                          |
| 0x004C | 4 bytes | Offset to [**Temporary character limit breaks** section             ](../Temporary-character-limit-breaks)        |
| 0x0050 | 4 bytes | Offset to [**Blue magic (Quistis limit break)** section             ](../Blue-magic)                              |
| 0x0054 | 4 bytes | Offset to [**Blue magic Parameters** section                        ](../Blue-magic-parameters)                   |
| 0x0058 | 4 bytes | Offset to [**Shot (Irvine limit break)** section                    ](../Shot-(irvine-limit-breaks))              |
| 0x005C | 4 bytes | Offset to [**Duel (Zell limit break)** section                      ](../Duel-(zell-limit-breaks))                |
| 0x0060 | 4 bytes | Offset to [**Duel Params** section                                  ](../Duel-params)                             |
| 0x0064 | 4 bytes | Offset to [**Rinoa limit breaks (part 1)** section                  ](../Rinoa-commands)                          |
| 0x0068 | 4 bytes | Offset to [**Rinoa limit breaks (part 2)** section                  ](../Rinoa-combine-limit-break)               |
| 0x006C | 4 bytes | Offset to [**Slots Array** section                                  ](../Slots-array)                             |
| 0x0070 | 4 bytes | Offset to [**Slots Sets** section                                   ](../Slots-seets)                             |
| 0x0074 | 4 bytes | Offset to [**Devour** section                                       ](../Devour)                                  |
| 0x0078 | 4 bytes | Offset to [**Misc** section                                         ](../Misc)                                    |
| 0x007C | 4 bytes | Offset to [**Misc text pointers** section                           ](../Misc-text-pointers)                      |
| 0x0080 | 4 bytes | Offset to **Battle command text** section                                                                         |
| 0x0084 | 4 bytes | Offset to **Magic text** section                                                                                  |
| 0x0088 | 4 bytes | Offset to **Junctionable GF text** section                                                                        |
| 0x008C | 4 bytes | Offset to **Enemy attack text** section                                                                           |
| 0x0090 | 4 bytes | Offset to **Weapon text** section                                                                                 |
| 0x0094 | 4 bytes | Offset to **Renzokuken finishers text** section                                                                   |
| 0x0098 | 4 bytes | Offset to **Character names** section                                                                             |
| 0x009C | 4 bytes | Offset to **Battle item names** section                                                                           |
| 0x00A0 | 4 bytes | Offset to **Non-battle item names** section                                                                       |
| 0x00A4 | 4 bytes | Offset to **Non-junctionable GF attack name** section                                                             |
| 0x00A8 | 4 bytes | Offset to **Junction abilities text** section                                                                     |
| 0x00AC | 4 bytes | Offset to **Command abilities text** section                                                                      |
| 0x00B0 | 4 bytes | Offset to **Stat percentage increasing abilities text** section                                                   |
| 0x00B4 | 4 bytes | Offset to **Character ability text** section                                                                      |
| 0x00B8 | 4 bytes | Offset to **Party ability text** section                                                                          |
| 0x00BC | 4 bytes | Offset to **GF ability text** section                                                                             |
| 0x00C0 | 4 bytes | Offset to **Menu ability text** section                                                                           |
| 0x00C4 | 4 bytes | Offset to **Temporary character limit break text** section                                                        |
| 0x00C8 | 4 bytes | Offset to **Blue magic text** section                                                                             |
| 0x00CC | 4 bytes | Offset to **Shot text** section                                                                                   |
| 0x00D0 | 4 bytes | Offset to **Duel text** section                                                                                   |
| 0x00D4 | 4 bytes | Offset to **Rinoa limit break (part 1) text** section                                                             |
| 0x00D8 | 4 bytes | Offset to **Rinoa limit break (part 2) text** section                                                             |
| 0x00DC | 4 bytes | Offset to **Devour text** section                                                                                 |
| 0x00E0 | 4 bytes | Offset to **Misc text** section                                                                                   |

00000000 struct FF8KernelHeader // sizeof=0xE4
00000000 {   // XREF: .data:KERNEL_HEADER/r
00000000     DWORD numSections;
00000004     DWORD offsetBattleCommands; // XREF: sub_4ACB70+2A2/r
00000004     // sub_4D45D0+137/r
00000008     DWORD offsetMagicData;
0000000C     DWORD offsetJunctionableGFs;
00000010     DWORD offsetEnemyAttacks;
00000014     DWORD offsetWeapons;
00000018     DWORD offsetRenzokukenFinishers;
0000001C     DWORD offsetCharacters;
00000020     DWORD offsetBattleItems;
00000024     DWORD offsetNonBattleItemNameDesc;
00000028     DWORD offsetNonJunctionableGFAttacks;
0000002C     DWORD offsetCommandAbilitiesGF;
00000030     DWORD offsetJunctionAbilities;
00000034     DWORD offsetCommandAbilitiesInBattle;
00000038     DWORD offsetStatPercentageAbilities;
0000003C     DWORD offsetCharacterAbilities;
00000040     DWORD offsetPartyAbilities;
00000044     DWORD offsetGFAbilities;
00000048     DWORD offsetMenuAbilities;
0000004C     DWORD offsetTempCharLimitBreaks;
00000050     DWORD offsetBlueMagic;
00000054     DWORD offsetBlueMagicParams;
00000058     DWORD offsetShot;
0000005C     DWORD offsetDuel;
00000060     DWORD offsetDuelParams;
00000064     DWORD offsetRinoaLimitBreaksPart1;
00000068     DWORD offsetRinoaLimitBreaksPart2;
0000006C     DWORD offsetSlotsArray;
00000070     DWORD offsetSlotsSets;
00000074     DWORD offsetDevour;
00000078     DWORD offsetMisc;
0000007C     DWORD offsetMiscTextPointers;
00000080     DWORD offsetBattleCommandText;
00000080     // XREF: getAddressTextCommand:loc_47EBE8/r sub_47EC00:loc_47EC18/r
00000084     DWORD offsetMagicText; // XREF: RELATED_TO_MAGIC_ID:loc_47E993/r
00000084     // sub_47E9C0:loc_47E9E3/r
00000088     DWORD offsetJunctionableGFText; // XREF: sub_47E9C0:loc_47EA14/r
00000088     // getAddressTextGfAttack_sub_495070/r
0000008C     DWORD offsetEnemyAttackText; // XREF: sub_4950A0/r
00000090     DWORD offsetWeaponText; // XREF: sub_47EBA0:loc_47EBBB/r
00000094     DWORD offsetRenzokukenFinishersText;
00000094     // XREF: getRenzokukenFinisherText:loc_47E60B/r
00000094     // sub_47E620:loc_47E63B/r
00000098     DWORD offsetCharacterNames;
00000098     // XREF: getAddressTextCharacter:loc_47EB39/r
00000098     // sub_47EB50:loc_47EB80/r
0000009C     DWORD offsetBattleItemNames; // XREF: getTextBattleItem:loc_47EA50/r
0000009C     // sub_47EA90:loc_47EAB0/r
000000A0     DWORD offsetNonBattleItemNames;
000000A0     // XREF: getTextBattleItem:loc_47EA77/r sub_47EA90:loc_47EAD7/r
000000A4     DWORD offsetNonJunctionableGFAttackName;
000000A4     // XREF: getAddressTextNonJGF/r
000000A8     DWORD offsetJunctionAbilitiesText; // XREF: sub_47E710:loc_47E72D/r
000000A8     // sub_47E840:loc_47E85D/r
000000AC     DWORD offsetCommandAbilitiesText; // XREF: sub_47E710:loc_47E759/r
000000AC     // sub_47E840:loc_47E889/r
000000B0     DWORD offsetStatPercentageAbilitiesText;
000000B0     // XREF: sub_47E710:loc_47E785/r sub_47E840:loc_47E8B5/r
000000B4     DWORD offsetCharacterAbilityText; // XREF: sub_47E710:loc_47E7B1/r
000000B4     // sub_47E840:loc_47E8E1/r
000000B8     DWORD offsetPartyAbilityText; // XREF: sub_47E710:loc_47E7DD/r
000000B8     // sub_47E840:loc_47E90D/r
000000BC     DWORD offsetGFAbilityText; // XREF: sub_47E710:loc_47E809/r
000000BC     // sub_47E840:loc_47E939/r
000000C0     DWORD offsetMenuAbilityText; // XREF: sub_47E710:loc_47E828/r
000000C0     // sub_47E840:loc_47E958/r
000000C4     DWORD offsetTempCharLimitBreakText; // XREF: sub_47E6B0:loc_47E6CB/r
000000C4     // sub_47E6E0:loc_47E6FB/r
000000C8     DWORD offsetBlueMagicText; // XREF: sub_47E650:loc_47E66A/r
000000C8     // sub_47E680:loc_47E69A/r
000000CC     DWORD offsetShotText; // XREF: getAddressTextShot:loc_47E5AB/r
000000CC     // sub_47E5C0:loc_47E5DB/r
000000D0     DWORD offsetDuelText; // XREF: sub_47E530:loc_47E54A/r
000000D0     // sub_47E560:loc_47E57A/r
000000D4     DWORD offsetRinoaLimitBreakTextPart1;
000000D4     // XREF: getTextRinoa1:loc_47E512/r sub_4952D0+4/r
000000D8     DWORD offsetRinoaLimitBreakTextPart2; // XREF: sub_47E4C0:loc_47E4DB/r
000000DC     DWORD offsetDevourText; // XREF: Battle_DamageGettingRelated+46A/r
000000E0     DWORD offsetMiscText; // XREF: .text:0047EC4D/r
000000E0     // getAddressTextMisc:loc_47EC88/r
000000E4 };

00000000 struct FF8KernelBattleCommand // sizeof=0x8
00000000 {   // XREF: .data:K_BATTLE_COMMAND_NAME_OFFSET/r
00000000     WORD offsetAbilityName; // XREF: getAddressTextCommand+4/r
00000002     WORD offsetAbilityDescription; // XREF: sub_47EC00+4/r
00000004     BYTE abilityDataID; // XREF: getText+239/r getText+108A/r ...
00000005     BYTE unknownFlags; // XREF: sub_48CAE0+1A/r
00000005     // ParseBattleCharacter+233/r ...
00000006     BYTE target; // XREF: sub_48C920+17/r sub_48CAE0+2C/r ...
00000007     BYTE unknownUnused;
00000008 };

00000000 struct FF8KernelMagicData // sizeof=0x3C
00000000 {   // XREF: .data:K_MAGIC_NAME_OFFSET/r
00000000     WORD offsetSpellName; // XREF: RELATED_TO_MAGIC_ID+F/r
00000002     WORD offsetSpellDescription; // XREF: sub_47E9C0+F/r
00000004     WORD magicID; // XREF: sub_482950+A8/r getText+537/r ...
00000006     BYTE animationTriggered; // XREF: Battle_DamageRelated+BA9/r
00000006     // Battle_DamageRelated+C7E/r
00000007     BYTE attackType; // XREF: Battle_DamageRelated+BBF/r
00000007     // Battle_DamageRelated+C94/r ...
00000008     BYTE spellPower; // XREF: Battle_DamageRelated+BB7/r
00000008     // Battle_DamageRelated+C8C/r
00000009     BYTE unknown1; // XREF: sub_48CAE0+49/r sub_4954B0+70/r
0000000A     BYTE defaultTarget; // XREF: sub_4838C0+D/r sub_4838C0+62/r ...
0000000B     BYTE attackFlags; // XREF: sub_48CAE0+58/r
0000000B     // Battle_DamageRelated+B91/r ...
0000000C     BYTE drawResist; // XREF: getHowManyDraw+96/r
0000000D     BYTE hitCount; // XREF: getText+531/r getText+5B9/r ...
0000000E     BYTE element; // XREF: Battle_DamageRelated+299/r
0000000F     BYTE unknown2;
00000010     DWORD statuses1; // XREF: Battle_DamageRelated+2BC/r
00000014     WORD statuses0; // XREF: Battle_DamageRelated+2AF/r
00000016     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+2A4/r
00000017     BYTE hpJunctionValue; // XREF: GetCharacterHP+77/r
00000018     BYTE strJunctionValue; // XREF: GetCharacterStat+61/r
00000019     BYTE vitJunctionValue; // XREF: GetCharacterStat+E9/r
0000001A     BYTE magJunctionValue; // XREF: GetCharacterStat+11D/r
0000001B     BYTE sprJunctionValue; // XREF: GetCharacterStat+151/r
0000001C     BYTE spdJunctionValue; // XREF: GetCharacterStat+182/r
0000001D     BYTE evaJunctionValue; // XREF: GetCharacterEva+23/r
0000001E     BYTE hitJunctionValue; // XREF: GetCharacterHit+23/r
0000001F     BYTE luckJunctionValue; // XREF: GetCharacterStat+1B3/r
00000020     BYTE jElemAttack; // XREF: sub_496930+1B/r
00000021     BYTE jElemAttackValue; // XREF: sub_496960+23/r
00000022     BYTE jElemDefense; // XREF: sub_4969E0+43/r
00000023     BYTE jElemDefenseValue; // XREF: sub_4969E0+4D/r
00000024     BYTE jStatusAttackValue; // XREF: sub_496B50+23/r
00000025     BYTE jStatusDefenseValue; // XREF: sub_496BD0+4E/r
00000026     WORD jStatusesAttack; // XREF: sub_496AC0+19/r sub_496AF0+1D/r
00000028     WORD jStatusesDefend; // XREF: sub_496BD0+41/r
0000002A     BYTE quezacoltCompatibility; // XREF: getText+574/o getText+6A4/o
0000002B     BYTE shivaCompatibility;
0000002C     BYTE ifritCompatibility;
0000002D     BYTE sirenCompatibility;
0000002E     BYTE brothersCompatibility;
0000002F     BYTE diablosCompatibility;
00000030     BYTE carbuncleCompatibility;
00000031     BYTE leviathanCompatibility;
00000032     BYTE pandemonaCompatibility;
00000033     BYTE cerberusCompatibility;
00000034     BYTE alexanderCompatibility;
00000035     BYTE doomtrainCompatibility;
00000036     BYTE bahamutCompatibility;
00000037     BYTE cactuarCompatibility;
00000038     BYTE tonberryCompatibility;
00000039     BYTE edenCompatibility;
0000003A     WORD unknown3;
0000003C };

00000000 struct FF8KernelJunctionableGFAbilityData // sizeof=0x4
00000000 {   // XREF: FF8KernelJunctionableGF/r
00000000     BYTE abilityUnlocker;
00000001     BYTE unknown1;
00000002     BYTE ability; // XREF: battle_mode5_RelatedToLvlIncrase?+3D6/o
00000003     BYTE unknown2;
00000004 };

00000000 struct FF8KernelJunctionableGF // sizeof=0x84
00000000 {   // XREF: .data:K_GF_ATTACK_NAME/r
00000000     WORD offsetGFAttackName;
00000000     // XREF: getAddressTextGfAttack_sub_495070+14/r
00000002     WORD offsetGFAttackDescription; // XREF: sub_47E9C0+40/r
00000004     WORD magicID; // XREF: getText+83E/r
00000006     BYTE attackType; // XREF: Battle_DamageRelated+1105/r
00000007     BYTE gfPower; // XREF: Battle_DamageRelated+10FD/r
00000008     WORD unknown1; // XREF: sub_48F2C0+12/r ParseBattleCharacter+19E/o
0000000A     BYTE attackFlags; // XREF: Battle_DamageRelated+10C9/r
0000000B     BYTE unknown2; // XREF: Battle_DamageRelated+10EF/r
0000000C     BYTE hitCount; // XREF: getText+834/r
0000000D     BYTE element; // XREF: Battle_DamageRelated+218/r
0000000E     WORD statuses0; // XREF: Battle_DamageRelated+22E/r
00000010     DWORD statuses1; // XREF: Battle_DamageRelated+23B/r
00000014     BYTE gfHPModifier; // XREF: sub_496120+2D/r
00000015     BYTE unknown3[6]; // XREF: sub_496080+15/r sub_496080+2C/r ...
0000001B     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+223/r
0000001C     FF8KernelJunctionableGFAbilityData abilityData[21];
0000001C     // XREF: battle_mode5_RelatedToLvlIncrase?+3D6/o
00000070     BYTE quezacoltCompatibility; // XREF: getText+84E/o
00000071     BYTE shivaCompatibility;
00000072     BYTE ifritCompatibility;
00000073     BYTE sirenCompatibility;
00000074     BYTE brothersCompatibility;
00000075     BYTE diablosCompatibility;
00000076     BYTE carbuncleCompatibility;
00000077     BYTE leviathanCompatibility;
00000078     BYTE pandemonaCompatibility;
00000079     BYTE cerberusCompatibility;
0000007A     BYTE alexanderCompatibility;
0000007B     BYTE doomtrainCompatibility;
0000007C     BYTE bahamutCompatibility;
0000007D     BYTE cactuarCompatibility;
0000007E     BYTE tonberryCompatibility;
0000007F     BYTE edenCompatibility;
00000080     WORD unknown40; // XREF: pre_computeGFBoost?+1C/r
00000082     BYTE powerMod; // XREF: Battle_DamageRelated+109F/r
00000083     BYTE levelMod; // XREF: Battle_DamageRelated+10A5/r
00000084 };

00000000 struct FF8KernelEnemyAttack // sizeof=0x14
00000000 {   // XREF: .data:K_ENEMY_ATTACK_NAME/r
00000000     WORD offsetAttackName; // XREF: sub_4950A0+D/r
00000002     WORD magicID; // XREF: sub_482950:loc_4829D2/r getText+E6B/r
00000004     BYTE cameraChange; // XREF: sub_482950+89/r getText+E7F/r
00000005     BYTE animationTriggered; // XREF: Battle_DamageRelated+1048/r
00000006     BYTE attackType; // XREF: Battle_DamageRelated+105E/r
00000007     BYTE attackPower; // XREF: Battle_DamageRelated+1056/r
00000008     BYTE attackFlags; // XREF: MonsterAI+219A/r sub_48EB90+4A/r ...
00000009     BYTE unknown; // XREF: sub_482950+64/r getText+E4D/r ...
0000000A     BYTE attackElement; // XREF: Battle_DamageRelated+48B/r
0000000A     // battle_mode5_RelatedToLvlIncrase?+5BF/o
0000000B     BYTE attackCritBonus; // XREF: Battle_DamageRelated+4C4/r
0000000C     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+496/r
0000000D     BYTE attackParameter; // XREF: Battle_DamageRelated+4B9/r
0000000E     WORD status0; // XREF: Battle_DamageRelated+4A1/r
00000010     DWORD status1; // XREF: Battle_DamageRelated+4AE/r
00000014 };

00000000 struct FF8KernelWeapon // sizeof=0xC
00000000 {   // XREF: .data:K_WEAPON_NAME_OFFSET/r
00000000     WORD offsetWeaponName; // XREF: sub_47EBA0+7/r
00000002     BYTE renzokukenFinishers; // XREF: getText+C78/r sub_4CCBF0+50/r ...
00000003     BYTE unknown1;
00000004     BYTE characterID; // XREF: sub_4EA4D0+5F/o sub_4EA4D0+B1/o
00000005     BYTE attackType; // XREF: Battle_DamageRelated+ABD/r
00000006     BYTE attackPower; // XREF: Battle_DamageRelated+AB4/r
00000006     // Battle_DamageRelated+11D3/r
00000007     BYTE attackParameter; // XREF: GetCharacterHit+9E/r sub_4EB670+3B/r ...
00000008     BYTE strBonus; // XREF: GetCharacterStat+B1/r
00000009     BYTE weaponTier; // XREF: sub_48B9A0+20/r
0000000A     BYTE critBonus; // XREF: Battle_DamageRelated+5F7/r
0000000B     BYTE isMeleeWeapon; // XREF: sub_48B5F0+71/r
0000000C };

00000000 struct FF8KernelRenzokukenFinisher // sizeof=0x18
00000000 {   // XREF: .data:K_RENZOKUKEN_FINISHER_NAME_OFFSET/r
00000000     WORD offsetLimitName; // XREF: getRenzokukenFinisherText+7/r
00000002     WORD offsetLimitDescription; // XREF: sub_47E620+7/r
00000004     WORD magicID; // XREF: getText+99A/r
00000006     BYTE attackType; // XREF: Battle_DamageRelated+1173/r
00000007     BYTE unknown1;
00000008     BYTE attackPower; // XREF: Battle_DamageRelated+116B/r
00000009     BYTE unknown2; // XREF: Battle_DamageRelated+115D/r
0000000A     BYTE targetInfo; // XREF: relatedToRenzokukenFinisher+10/r
0000000A     // relatedToRenzokukenFinisher+22/r
0000000B     BYTE attackFlags; // XREF: Battle_DamageRelated+1142/r
0000000C     BYTE hitCount; // XREF: getText+994/r ComputeRenzokukenDamage+13/r
0000000D     BYTE elementAttack; // XREF: Battle_DamageRelated+560/r
0000000E     BYTE elementAttackPercent; // XREF: Battle_DamageRelated+555/r
0000000F     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+56B/r
00000010     WORD unknown3;
00000012     WORD status0; // XREF: Battle_DamageRelated+576/r
00000014     DWORD status1; // XREF: Battle_DamageRelated+583/r
00000018 };

00000000 struct FF8KernelCharacter // sizeof=0x24
00000000 {   // XREF: .data:K_CHARACTER_NAME_OFFSET/r
00000000     WORD offsetCharacterName; // XREF: getAddressTextCharacter+35/r
00000000     // sub_47EB50+1C/r
00000002     BYTE crisisLevelHPMultiplier; // XREF: sub_4941F0+30/r
00000003     BYTE gender; // XREF: sub_48B5F0+94/r
00000004     BYTE limitBreakID; // XREF: ParseBattleCharacter+31E/r
00000005     BYTE limitBreakParam; // XREF: Battle_DamageRelated+11AE/r
00000006     WORD expModifier; // XREF: sub_496170+28/r sub_496170+3F/r ...
00000008     BYTE hp[4]; // XREF: GetCharacterHP+62/r GetCharacterHP+8B/r ...
0000000C     BYTE str[4];
00000010     BYTE vit[4];
00000014     BYTE mag[4];
00000018     BYTE spr[4];
0000001C     BYTE spd[4];
00000020     BYTE luck[4];
00000024 };

00000000 struct FF8KernelBattleItem // sizeof=0x18
00000000 {   // XREF: .data:K_ITEM_NAME/r
00000000     WORD offsetItemName; // XREF: getTextBattleItem+C/r
00000002     WORD offsetItemDescription; // XREF: sub_47EA90+C/r
00000004     WORD magicID; // XREF: getText:loc_48D2FF/r getText+968/r
00000006     BYTE attackType; // XREF: getText+68/r Battle_DamageRelated+E48/r
00000007     BYTE attackPower; // XREF: Battle_DamageRelated+E40/r
00000008     BYTE unknown1; // XREF: sub_48C670+55/r
00000009     BYTE targetInfo; // XREF: findTarget?+1F1/r findTarget?+23D/r ...
0000000A     BYTE unknown2; // XREF: sub_48C670+12/r sub_48C670+26/r ...
0000000B     BYTE attackFlags; // XREF: Battle_DamageRelated+E32/r
0000000C     BYTE unknown3; // XREF: getTextBattleItem:loc_47EA63/r
0000000D     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+455/r
0000000E     WORD status0; // XREF: sub_47EA90:loc_47EAC3/r
0000000E     // Battle_DamageRelated+460/r
00000010     DWORD status1; // XREF: Battle_DamageRelated+46D/r
00000014     BYTE attackParam; // XREF: Battle_DamageRelated+43F/r
00000015     BYTE unknown4; // XREF: sub_483CA0+21/r sub_483CA0+62/r
00000016     BYTE hitCount; // XREF: getText+95E/r
00000017     BYTE element; // XREF: Battle_DamageRelated+44A/r
00000018 };

00000000 struct FF8KernelNonBattleItemNameAndOffset // sizeof=0x4
00000000 {   // XREF: .data:K_NON_BATTLE_ITEM/r
00000000     WORD offsetToItemName;
00000002     WORD offsetToItemDescription;
00000004 };

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelNonJGF // sizeof=0x14
00000000 {   // XREF: .data:K_NONJ_GF_ATTACK_NAME_OFFSET/r
00000000     WORD offsetGFAttackName; // XREF: getAddressTextNonJGF+D/r
00000002     WORD magicID; // XREF: getText+930/r
00000004     BYTE attackType; // XREF: Battle_DamageRelated+F05/r
00000005     BYTE gfPower; // XREF: Battle_DamageRelated+EFD/r
00000006     BYTE statusAttackEnabler; // XREF: Battle_DamageRelated+1CC/r
00000007     BYTE unknown1; // XREF: pre_MonsterAI+48C/r pre_MonsterAI+49E/r
00000008     BYTE statusFlags; // XREF: Battle_DamageRelated+ED1/r
00000009     WORD unknown2; // XREF: getText+92A/r Battle_DamageRelated+EEF/r
0000000B     BYTE element; // XREF: Battle_DamageRelated+1C1/r
0000000C     BYTE status1; // XREF: Battle_DamageRelated+1E4/r
0000000D     BYTE status2;
0000000E     BYTE status3;
0000000F     BYTE status4;
00000010     BYTE status5; // XREF: Battle_DamageRelated+1D7/r
00000011     BYTE unknown3;
00000012     BYTE powerMod; // XREF: Battle_DamageRelated+EB5/r
00000013     BYTE levelMod; // XREF: Battle_DamageRelated+1B6/r
00000013     // Battle_DamageRelated+EAF/r
00000014 };
00000014 #pragma pack(pop)

00000000 struct FF8KernelCommandAbilityGF // sizeof=0x8
00000000 {
00000000     WORD AbilityNameOffset;
00000002     WORD AbilityDescriptionOffset;
00000004     BYTE APRequired;
00000005     BYTE BattleCommandIndex;
00000006     WORD Unknown;
00000008 };

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelJunctionAbility // sizeof=0x8
00000000 {
00000000     WORD AbilityNameOffset;
00000002     WORD AbilityDescriptionOffset;
00000004     BYTE APRequired;
00000005     BYTE JFlag[3];
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelCommandBattleAbility // sizeof=0x10
00000000 {
00000000     WORD MagicID;
00000002     BYTE Unknown;
00000003     BYTE AnimationTriggered;
00000004     BYTE AttackType;
00000005     BYTE AttackPower;
00000006     BYTE AttackFlags;
00000007     BYTE HitCount;
00000008     BYTE Element;
00000009     BYTE StatusAttackEnabler;
0000000A     BYTE Statuses[6];
00000010 };
00000010 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelStatPercentIncreaseAbility // sizeof=0x8
00000000 {
00000000     WORD AbilityNameOffset;
00000002     WORD AbilityDescriptionOffset;
00000004     BYTE APNeeded;
00000005     BYTE StatToIncrease;
00000006     BYTE IncreaseValue;
00000007     BYTE Unknown;
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelCharacterAbility // sizeof=0x8
00000000 {
00000000     WORD AbilityNameOffset;
00000002     WORD AbilityDescriptionOffset;
00000004     BYTE APRequired;
00000005     BYTE Flags[3];
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelPartyAbility // sizeof=0x8
00000000 {
00000000     WORD AbilityNameOffset;
00000002     WORD AbilityDescriptionOffset;
00000004     BYTE APRequired;
00000005     BYTE Flag;
00000006     WORD Unknown;
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelTempCharaLimitBreak // sizeof=0x18
00000000 {   // XREF: .data:K_TEMP_CHAR_LIMIT_NAME_OFFSET/r
00000000     WORD LimitNameOffset; // XREF: sub_47E6B0+7/r
00000002     WORD LimitDescriptionOffset; // XREF: sub_47E6E0+7/r
00000004     WORD MagicID; // XREF: getText+AE6/r
00000006     BYTE AttackType; // XREF: Battle_DamageRelated+D64/r
00000007     BYTE AttackPower; // XREF: Battle_DamageRelated+D5C/r
00000008     WORD Unknown1; // XREF: sub_48CCE0:loc_48CEBB/r
00000008     // sub_48CCE0:loc_48CEF5/r ...
0000000A     BYTE TargetInfo; // XREF: sub_48CCE0+1E1/r sub_48CCE0+21B/r ...
0000000B     BYTE AttackFlags; // XREF: sub_48CCE0+1EF/r sub_48CCE0+229/r ...
0000000C     BYTE HitCount; // XREF: getText+AE0/r
0000000D     BYTE ElementAttack; // XREF: Battle_DamageRelated+32F/r
0000000E     BYTE ElementAttackPercent; // XREF: Battle_DamageRelated+324/r
0000000F     BYTE StatusAttackEnabler; // XREF: Battle_DamageRelated+33A/r
00000010     WORD Status0; // XREF: Battle_DamageRelated+345/r
00000012     WORD Unknown2;
00000014     DWORD Status1; // XREF: Battle_DamageRelated+352/r
00000018 };
00000018 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelQuistisLimitAbility // sizeof=0x10
00000000 {   // XREF: .data:K_BLUE_MAGIC_NAME_OFFSET/r
00000000     WORD LimitNameOffset; // XREF: sub_47E650+7/r
00000002     WORD LimitDescriptionOffset; // XREF: sub_47E680+7/r
00000004     WORD MagicID; // XREF: getText+B1A/r
00000006     BYTE Unknown1; // XREF: Battle_DamageRelated+DCC/r
00000007     BYTE AttackType; // XREF: Battle_DamageRelated+DE6/r
00000008     WORD Unknown2; // XREF: sub_48CCE0+134/o
0000000A     BYTE AttackFlags; // XREF: Battle_DamageRelated+D9D/r
0000000B     BYTE Unknown3; // XREF: getText+B14/r
0000000C     BYTE Element; // XREF: Battle_DamageRelated+36F/r
0000000D     BYTE StatusAttack; // XREF: Battle_DamageRelated+375/r
0000000E     BYTE CritBonus; // XREF: Battle_DamageRelated+3B0/r
0000000E     // Battle_DamageRelated+DD8/r
0000000F     BYTE Unknown4;
00000010 };
00000010 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelQuistisLimitParam // sizeof=0x8
00000000 {   // XREF: .data:K_BLUE_MAGIC_PARAM_STATUS_8_39/r
00000000     DWORD Status1; // XREF: sub_48CCE0+171/o Battle_DamageRelated+39B/r
00000004     WORD Status0; // XREF: Battle_DamageRelated+3A2/r
00000006     BYTE AttackPower;
00000007     BYTE AttackParam; // XREF: Battle_DamageRelated+3BC/r
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelIrvineLimitShot // sizeof=0x18
00000000 {   // XREF: .data:K_SHOT_NAME_OFFSET/r
00000000     WORD LimitNameOffset; // XREF: getAddressTextShot+7/r
00000002     WORD LimitDescriptionOffset; // XREF: sub_47E5C0+7/r
00000004     WORD MagicID; // XREF: getText+A86/r
00000006     BYTE AttackType; // XREF: Battle_DamageRelated+FFB/r
00000007     BYTE AttackPower; // XREF: Battle_DamageRelated+FE1/r
00000008     WORD Unknown; // XREF: Battle_DamageRelated+F6F/r
00000008     // Battle_DamageRelated+FE7/r
0000000A     BYTE TargetInfo; // XREF: RelatedToShotIrvineLimit+D/r
0000000B     BYTE AttackFlags; // XREF: Battle_DamageRelated+FB2/r
0000000C     BYTE HitCount; // XREF: getText+A80/r
0000000D     BYTE ElementAttack; // XREF: Battle_DamageRelated+3F8/r
0000000E     BYTE ElementAttackPercent; // XREF: Battle_DamageRelated+3ED/r
0000000F     BYTE StatusAttackEnabler; // XREF: Battle_DamageRelated+403/r
00000010     WORD Status0; // XREF: Battle_DamageRelated+40E/r
00000012     BYTE UsedItemIndex; // XREF: sub_4C0AD0+A/o sub_4CFA00+1B/o
00000013     BYTE CritIncrease; // XREF: Battle_DamageRelated+426/r
00000014     DWORD Status1; // XREF: Battle_DamageRelated+41B/r
00000018 };
00000018 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelZellLimitDuell // sizeof=0x20
00000000 {   // XREF: .data:K_DUEL_NAME_OFFSET/r
00000000     WORD LimitNameOffset; // XREF: sub_47E530+7/r
00000002     WORD LimitDescriptionOffset; // XREF: sub_47E560+7/r
00000004     WORD MagicID; // XREF: getText+D29/r getText+DD5/r ...
00000006     BYTE AttackType; // XREF: Battle_DamageRelated+84A/r
00000007     BYTE AttackPower; // XREF: Battle_DamageRelated+842/r
00000008     BYTE AttackFlags; // XREF: Battle_DamageRelated+82B/r
00000009     BYTE Unknown1;
0000000A     BYTE TargetInfo; // XREF: sub_48F220+B/r sub_48F220+11/o
0000000B     BYTE Unknown2; // XREF: Battle_DamageRelated+818/r
0000000C     BYTE HitCount; // XREF: getText+DCB/r getText+E1C/r
0000000D     BYTE ElementAttack; // XREF: Battle_DamageRelated+16F/r
0000000E     BYTE ElementAttackPercent; // XREF: Battle_DamageRelated:loc_48FF84/r
0000000F     BYTE StatusAttackEnabler; // XREF: Battle_DamageRelated+17A/r
00000010     WORD SequenceButton1; // XREF: sub_4B0280+64/o sub_4CD190+62/o ...
00000012     WORD SequenceButton2;
00000014     WORD SequenceButton3;
00000016     WORD SequenceButton4;
00000018     WORD SequenceButton5; // XREF: sub_4AF840+112/o
0000001A     WORD Status0; // XREF: Battle_DamageRelated+185/r
0000001C     DWORD Status1; // XREF: Battle_DamageRelated+192/r
00000020 };
00000020 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct DuelMoves // sizeof=0x4
00000000 {   // XREF: FF8KernelZellLimitDuelParam/r
00000000     BYTE StartMove0; // XREF: sub_4852B0+6C/r getText+D12/r ...
00000001     BYTE NextSequence01;
00000002     BYTE NextSequence02;
00000003     BYTE NextSequence03;
00000004 };
00000004 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelZellLimitDuelParam // sizeof=0x64
00000000 {   // XREF: .data:K_DUEL_PARAM/r
00000000     DuelMoves duelMoves[25]; // XREF: sub_4852B0+6C/r getText+D12/r ...
00000064 };
00000064 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelRinoaLimitPart1 // sizeof=0x8
00000000 {   // XREF: .data:K_RIONA_LIMIT_PART_1/r
00000000     WORD AbilityNameOffset; // XREF: getTextRinoa1:loc_47E4FE/r
00000002     WORD AbilityDescriptionOffset; // XREF: sub_4952D0+A/r
00000004     BYTE UnknownFlags; // XREF: sub_48CFB0+1A/r
00000005     BYTE Target; // XREF: sub_48CFB0+21/r
00000006     BYTE AbilityDataID;
00000007     BYTE UnknownUnused;
00000008 };
00000008 #pragma pack(pop)

00000000 #pragma pack(push, 1)
00000000 struct FF8KernelRinoaLimitPart2 // sizeof=0x14
00000000 {   // XREF: .data:K_RINOA_LIMIT_PART_2/r
00000000     WORD LimitNameOffset; // XREF: sub_47E4C0+7/r
00000002     WORD MagicID; // XREF: getText+AB6/r
00000004     BYTE AttackType; // XREF: Battle_DamageRelated+CFB/r
00000005     BYTE AttackPower; // XREF: Battle_DamageRelated+CF3/r
00000006     BYTE AttackFlags; // XREF: Battle_DamageRelated+CE5/r
00000007     BYTE Unknown1;
00000008     BYTE TargetInfo; // XREF: sub_484D20+11F/r sub_484D20+13E/r
00000009     BYTE Unknown2; // XREF: Battle_DamageRelated+CCA/r
0000000A     BYTE HitCount; // XREF: getText+AAC/r
0000000B     BYTE ElementAttack; // XREF: Battle_DamageRelated+2E3/r
0000000C     BYTE ElementAttackPercent; // XREF: Battle_DamageRelated+2D8/r
0000000D     BYTE StatusAttackEnabler; // XREF: Battle_DamageRelated+2EE/r
0000000E     WORD Status0; // XREF: Battle_DamageRelated+2F9/r
00000010     DWORD Status1; // XREF: Battle_DamageRelated+306/r
00000014 };
00000014 #pragma pack(pop)

#pragma pack(push, 1)
struct FF8KernelDevour // sizeof=0xC
{   // XREF: .data:K_DEVOUR_DESCRIPTION_OFFSET/r
    WORD DevourDescriptionOffset;
    // XREF: Battle_DamageGettingRelated+487/r
    BYTE DamageOrHealFlag; // XREF: Battle_DamageRelated+671/r
    BYTE HPHealDMGQuantityFlag; // XREF: Battle_DamageRelated+65C/r
    DWORD Status1; // XREF: Battle_DamageRelated+506/r
    WORD Status0; // XREF: Battle_DamageRelated+4FF/r
    BYTE RaisedStatFlag; // XREF: sub_492220+11/r
    BYTE RaisedStatHPQuantity; // XREF: sub_492220+79/r
};
#pragma pack(pop)
#pragma pack(push, 1)
struct FF8KernelMisc // sizeof=0x3C
{   // XREF: .data:K_MISC/r
    BYTE SleepTimer; // XREF: sub_4832F0+20/r
    BYTE HasteTimer;
    BYTE SlowTimer;
    BYTE StopTimer;
    BYTE RegenTimer;
    BYTE ProtectTimer;
    BYTE ShellTimer;
    BYTE ReflectTimer;
    BYTE AuraTimer;
    BYTE CurseTimer;
    BYTE DoomTimer;
    BYTE InvincibleTimer;
    BYTE PetrifyingTimer;
    BYTE FloatTimer;
    BYTE ATBSpeedMultiplier; // XREF: sub_4842B0+FF/r
    BYTE DeadTimer; // XREF: sub_482F70/r sub_482F80:loc_48312B/r ...
    BYTE DeathLimitEffect; // XREF: sub_4941F0+80/r
    BYTE PoisonLimitEffect;
    BYTE PetrifyLimitEffect;
    BYTE DarknessLimitEffect;
    BYTE SilenceLimitEffect;
    BYTE BerserkLimitEffect;
    BYTE ZombieLimitEffect;
    BYTE UnknownStatusLimitEffect1;
    BYTE SleepLimitEffect; // XREF: sub_4941F0+A3/r
    BYTE HasteLimitEffect;
    BYTE SlowLimitEffect;
    BYTE StopLimitEffect;
    BYTE RegenLimitEffect;
    BYTE ProtectLimitEffect;
    BYTE ShellLimitEffect;
    BYTE ReflectLimitEffect;
    BYTE AuraLimitEffect;
    BYTE CurseLimitEffect;
    BYTE DoomLimitEffect;
    BYTE InvincibleLimitEffect;
    BYTE PetrifyingLimitEffect;
    BYTE FloatLimitEffect;
    BYTE ConfusionLimitEffect;
    BYTE DrainLimitEffect;
    BYTE EjectLimitEffect;
    BYTE DoubleLimitEffect;
    BYTE TripleLimitEffect;
    BYTE DefendLimitEffect;
    BYTE UnknownStatusLimitEffect2;
    BYTE UnknownStatusLimitEffect3;
    BYTE ChargedLimitEffect; // XREF: sub_48E5A0+22/r
    BYTE BackAttackLimitEffect; // XREF: getText+D02/r
    BYTE DuelStartSeqCrisis1;
    BYTE DuelTimerCrisis1;
    BYTE DuelStartSeqCrisis2;
    BYTE DuelTimerCrisis2;
    BYTE DuelStartSeqCrisis3;
    BYTE DuelTimerCrisis3;
    BYTE DuelStartSeqCrisis4;
    BYTE DuelTimerCrisis4; // XREF: RelatedToShotIrvineLimit+3C/r
    BYTE ShotTimerCrisis1;
    BYTE ShotTimerCrisis2;
    BYTE ShotTimerCrisis3;
    BYTE ShotTimerCrisis4;
};
#pragma pack(pop)
#pragma pack(push, 1)
struct FF8KernelMiscTextPointer // sizeof=0x100
{   // XREF: .data:K_MISC_TEXT_POINTER/r
    WORD Offset[128]; // XREF: .text:0047EC31/r getAddressTextMisc+4/r
};
#pragma pack(pop)
