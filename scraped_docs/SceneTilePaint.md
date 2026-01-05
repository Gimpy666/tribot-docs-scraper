# SceneTilePaint (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/SceneTilePaint.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface SceneTilePaint
```

Represents the paint of a tile in the current scene.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getBufferLen](#getBufferLen())()` | |
| `int` | `[getBufferOffset](#getBufferOffset())()` | |
| `int` | `[getNeColor](#getNeColor())()` | Gets the color of the north-east corner of the tile. |
| `int` | `[getNwColor](#getNwColor())()` | Gets the color of the north-west corner of the tile. |
| `int` | `[getRBG](#getRBG())()` | Gets the RGB value of the paint. |
| `int` | `[getSeColor](#getSeColor())()` | Gets the color of the south-east corner of the tile. |
| `int` | `[getSwColor](#getSwColor())()` | Gets the color of the south-west corner of the tile. |
| `int` | `[getTexture](#getTexture())()` | Gets the texture to be rendered for the tile. |
| `int` | `[getUvBufferOffset](#getUvBufferOffset())()` | |
| `boolean` | `[isFlat](#isFlat())()` | |
| `void` | `[setBufferLen](#setBufferLen(int))​(int bufferLen)` | |
| `void` | `[setBufferOffset](#setBufferOffset(int))​(int bufferOffset)` | |
| `void` | `[setNeColor](#setNeColor(int))​(int color)` | Sets the color of the north-east corner of the tile. |
| `void` | `[setNwColor](#setNwColor(int))​(int color)` | Sets the color of the north-west corner of the tile. |
| `void` | `[setSeColor](#setSeColor(int))​(int color)` | Sets the color of the south-east corner of the tile. |
| `void` | `[setSwColor](#setSwColor(int))​(int color)` | Sets the color of the south-west corner of the tile. |
| `void` | `[setTexture](#setTexture(int))​(int texture)` | Sets the texture to be rendered for the tile. |
| `void` | `[setUvBufferOffset](#setUvBufferOffset(int))​(int bufferOffset)` | |

* + ### Method Detail

- #### getRBG

```
int getRBG()
```

Gets the RGB value of the paint.

Returns:
the paint RGB
- #### getSwColor

```
int getSwColor()
```

Gets the color of the south-west corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Returns:
the south-west corner of the tile
- #### setSwColor

```
void setSwColor​(int color)
```

Sets the color of the south-west corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Parameters:
`color` - the new color for the south-west corner of the tile
- #### getSeColor

```
int getSeColor()
```

Gets the color of the south-east corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Returns:
the south-east corner of the tile
- #### setSeColor

```
void setSeColor​(int color)
```

Sets the color of the south-east corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Parameters:
`color` - the new color for the south-east corner of the tile
- #### getNwColor

```
int getNwColor()
```

Gets the color of the north-west corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Returns:
the north-west corner of the tile
- #### setNwColor

```
void setNwColor​(int color)
```

Sets the color of the north-west corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Parameters:
`color` - the new color for the north-west corner of the tile
- #### getNeColor

```
int getNeColor()
```

Gets the color of the north-east corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Returns:
the north-east corner of the tile
- #### setNeColor

```
void setNeColor​(int color)
```

Sets the color of the north-east corner of the tile.
Used to render a Gouraud-shaded gradient along the tile plane in the scene.

Parameters:
`color` - the new color for the north-east corner of the tile
- #### getTexture

```
int getTexture()
```

Gets the texture to be rendered for the tile.
When set, the texture will be drawn instead of a 4-point color gradient.

Returns:
the texture id to draw on the tile
- #### setTexture

```
void setTexture​(int texture)
```

Sets the texture to be rendered for the tile.
When set, the texture will be drawn instead of a 4-point color gradient.

Parameters:
`texture` - the texture id to be drawn on the tile
- #### isFlat

```
boolean isFlat()
```
- #### getBufferOffset

```
int getBufferOffset()
```
- #### setBufferOffset

```
void setBufferOffset​(int bufferOffset)
```
- #### getUvBufferOffset

```
int getUvBufferOffset()
```
- #### setUvBufferOffset

```
void setUvBufferOffset​(int bufferOffset)
```
- #### getBufferLen

```
int getBufferLen()
```
- #### setBufferLen

```
void setBufferLen​(int bufferLen)
```