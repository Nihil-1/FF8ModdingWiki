---
layout: default
parent: Field File Format
title: Field Character Models
permalink: /technical-reference/field/field-file-format/field-character-models/
---

<small>Authors: [Koral](User:Koral "wikilink"), [JWP](http://forums.qhimm.com/index.php?topic=6961.msg86318#msg86318) and [Vehek](http://forums.qhimm.com/index.php?topic=13261.msg184344#msg184344)</small>

# MCH Field Character Models

Each MCH file contains a skinned-animated model representing a character on the field or world Maps. There appear to be multiple files of the same character representing differnt Level of Details.

They usually contain multiple TIM textures (standard PSX textures), mesh geometry, bones, skeleton heirarchy information and skinning information. The whereabouts of the Bone Animation data is currently unknown.

  

# Accessing MCH Files

<small>todo</small>

  

# MCH File Structure

## Header

`0x100 bytes [256 bytes]`  
  
`    DWORD: Offsets to multiple Texture-Data`  
`        Start: 0x00`  
`        Parse DWORDS until read value: 0xFFFFFFFF`  
  
`    DWORD: Offset to Model Data`  
`    `

  

## Texture-Data

[TIM format](../PSX/TIM_format)

`(for each Texture)`  
  
`    Standard [TIM] format textures`

  

## Model-Data

| Offset | Length  | Description                  |
|--------|---------|------------------------------|
| 0x00   | 4 bytes | Number of Skeleton Bones     |
| 0x04   | 4 bytes | Number of Vertices           |
| 0x08   | 4 bytes | Number of texture animations |
| 0x0C   | 4 bytes | Number of Faces              |
| 0x10   | 4 bytes | Number of Unknown data       |
| 0x14   | 4 bytes | Number of Skin objects       |
| 0x18   | 4 bytes | Unknown                      |
| 0x1C   | 2 bytes | Triangle count               |
| 0x1E   | 2 bytes | Quad count                   |
| 0x20   | 4 bytes | Offset of bones              |
| 0x24   | 4 bytes | Offset of vertices           |
| 0x28   | 4 bytes | Offset of texture animations |
| 0x2C   | 4 bytes | Offset of faces              |
| 0x30   | 4 bytes | Offset of unknown data       |
| 0x34   | 4 bytes | Offset of skin objects       |
| 0x38   | 4 bytes | Offset of animation data     |
| 0x3C   | 4 bytes | Unknown                      |

`    Skeleton Data: 0x40 bytes per bone, recurse through number of bones dictated in Header`  
`    (for each bone)`  
  
`        SHORT: parent bone (1-based)`  
`        SHORT: parent bone data offset (multiple of 64)`  
`        DWORD:   (unknown)`  
`        SHORT: bone length`  
`        DWORD * 15:   (unknown)`  
`          `

`    Vertex Data:`  
`    (for each vertex)`  
  
`        SHORT: Vertex X Position`  
`        SHORT: Vertex Y Position`  
`        SHORT: Vertex Z Position`  
`        SHORT:   (unknown)`  
`          `

`    UV_pair:`  
`struct`  
`{`  
`   BYTE: Coordinate 1`  
`   BYTE: Coordinate 2`
`};`

`    Texture-animations Data:`  
`struct`  
`{`  
`   BYTE: unknown`  
`   BYTE: Total textures`  
`   BYTE: unknown`
`   BYTE: uSize`  
`   BYTE: vSize`  
`   BYTE: Replacement coords count`  
`   UV_pair original_area_coords`  
`   byte unknown[2]`  
`   (UV_pair * Replacement coords count) Replacement Coordinates`  
`};`

`struct face {`  
`   u32 opcode; 0x07060125 = triangle, 0907012d = Quad`  
`   BYTE unk[4];`  
`   SHORT unknown; //When bit 0x04 is set, sets semitransparency`  
`   BYTE unk[2];`  
`   u16 verticies[4]; //vertex id's`  
`   u16 verticies1[4]; //Edge data???`  
`   u32 Vertex_Colours[4];`  
`   TextureMap TextureData[4]; // TextureMap = u16 with the first byte = u and the second byte = v`  
`   u16 Padding;`  
`   u16 Texture Index;`  
`   u32 Padding; `  
`   u32 Padding; `  
`};`

`    Unknown Data, Seems to split up the skin-objects, triangles, and quads:`  
`struct`  
`{`  
`   uint16 start_skinobject_index`  
`   uint16 skinobject_count`  
`   byte unknown[12]`  
`   uint16 start_triangle_index`  
`   uint16 triangle_count`  
`   uint16 start_quad_index`  
`   uint16 quad_count`  
`   byte unknown2[8]`  
`};`

`    Skin-Object Data: `  
`    (for each skin-object)`  
  
`        SHORT: index of first vertex`  
`        SHORT: number of vertices`  
`        SHORT: Bone ID (1-based)`  
`        SHORT:   (unknown)`  
`        `

  

`    Animations Header ("offset of animation data" above): `  
`        uint16: number_of_animations`  
`        Animation: Animation Object[number_of_animations]  
`        `


`    Animation:
`        uint16: frame_count`  
`        uint16: bone_count`  
`        Frame: Frame Object[frame_count]  
`        `

`    Frame:
`        uint16: x location transform`  
`        uint16: y location transform`  
`        uint16: z location transform`  
`        Pose: Pose Object[bone_count]  
`        `

`    Pose:
`        uint8: byte1`  
`        uint8: byte2`  
`        uint8: byte3`  
`        uint8: byte4`
`        `

# MCH Model File List

<small>todo</small>
