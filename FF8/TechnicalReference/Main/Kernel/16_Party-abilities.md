---
layout: default
title: Party abilities
nav_order: 17
parent: Kernel
permalink: /technical-reference/main/kernel/16-party-abilities/
---

## General

| Offset | Sections | Section Size |
|--------|----------|--------------|
| 0x4350 | 5        | 8 bytes      |

## Sections

| Offset | Ability   |
|--------|-----------|
| 0x4350 | Alert     |
| 0x4358 | Move-Find |
| 0x4360 | Enc-Half  |
| 0x4368 | Enc-None  |
| 0x4370 | Rare Item |

## Section Structure

| Offset | Length  | Description                   |
|--------|---------|-------------------------------|
| 0x0000 | 2 bytes | Offset to ability name        |
| 0x0002 | 2 bytes | Offset to ability description |
| 0x0004 | 1 byte  | AP Required to learn ability  |
| 0x0005 | 1 byte  | Flag                          |
| 0x0006 | 2 byte  | Unknown/Unused                |