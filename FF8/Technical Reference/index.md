---
title: Technical Reference
layout: default
nav_order: 3
---

The game data is hold by archive files (.fs files), and this wiki is organized following this logic.



struct ff8_kernel_header
{
  DWORD numSections;
  DWORD offsetBattleCommands;
  DWORD offsetMagicData;
  DWORD offsetJunctionableGFs;
  DWORD offsetEnemyAttacks;
  DWORD offsetWeapons;
  DWORD offsetRenzokukenFinishers;
  DWORD offsetCharacters;
  DWORD offsetBattleItems;
  DWORD offsetNonBattleItemNameDesc;
  DWORD offsetNonJunctionableGFAttacks;
  DWORD offsetCommandAbilitiesGF;
  DWORD offsetJunctionAbilities;
  DWORD offsetCommandAbilitiesInBattle;
  DWORD offsetStatPercentageAbilities;
  DWORD offsetCharacterAbilities;
  DWORD offsetPartyAbilities;
  DWORD offsetGFAbilities;
  DWORD offsetMenuAbilities;
  DWORD offsetTempCharLimitBreaks;
  DWORD offsetBlueMagic;
  DWORD offsetBlueMagicParams;
  DWORD offsetShot;
  DWORD offsetDuel;
  DWORD offsetDuelParams;
  DWORD offsetRinoaLimitBreaksPart1;
  DWORD offsetRinoaLimitBreaksPart2;
  DWORD offsetSlotsArray;
  DWORD offsetSlotsSets;
  DWORD offsetDevour;
  DWORD offsetMisc;
  DWORD offsetMiscTextPointers;
  DWORD offsetBattleCommandText;
  DWORD offsetMagicText;
  DWORD offsetJunctionableGFText;
  DWORD offsetEnemyAttackText;
  DWORD offsetWeaponText;
  DWORD offsetRenzokukenFinishersText;
  DWORD offsetCharacterNames;
  DWORD offsetBattleItemNames;
  DWORD offsetNonBattleItemNames;
  DWORD offsetNonJunctionableGFAttackName;
  DWORD offsetJunctionAbilitiesText;
  DWORD offsetCommandAbilitiesText;
  DWORD offsetStatPercentageAbilitiesText;
  DWORD offsetCharacterAbilityText;
  DWORD offsetPartyAbilityText;
  DWORD offsetGFAbilityText;
  DWORD offsetMenuAbilityText;
  DWORD offsetTempCharLimitBreakText;
  DWORD offsetBlueMagicText;
  DWORD offsetShotText;
  DWORD offsetDuelText;
  DWORD offsetRinoaLimitBreakTextPart1;
  DWORD offsetRinoaLimitBreakTextPart2;
  DWORD offsetDevourText;
  DWORD offsetMiscText;
};
