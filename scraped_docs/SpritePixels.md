# SpritePixels (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/SpritePixels.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface SpritePixels
```

Represents data about the pixels of a sprite image.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[DEFAULT\_SHADOW\_COLOR](#DEFAULT_SHADOW_COLOR)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[drawAt](#drawAt(int,int))​(int x,
int y)` | Draws the pixels at the given coordinates on the canvas. |
| `int` | `[getHeight](#getHeight())()` | Gets the height of the sprite image in pixels. |
| `int` | `[getMaxHeight](#getMaxHeight())()` | Gets the max height of the sprite image in pixels. |
| `int` | `[getMaxWidth](#getMaxWidth())()` | Gets the max width of the sprite image in pixels. |
| `int` | `[getOffsetX](#getOffsetX())()` | Gets the x offset of the sprite image in pixels. |
| `int` | `[getOffsetY](#getOffsetY())()` | Gets the y offset of the sprite image in pixels. |
| `int[]` | `[getPixels](#getPixels())()` | Gets an array of all pixels data in the sprite. |
| `int` | `[getWidth](#getWidth())()` | Gets the width of the sprite image in pixels. |
| `void` | `[setMaxHeight](#setMaxHeight(int))​(int maxHeight)` | Sets the max height of the sprite image in pixels. |
| `void` | `[setMaxWidth](#setMaxWidth(int))​(int maxWidth)` | Sets the max width of the sprite image in pixels. |
| `void` | `[setOffsetX](#setOffsetX(int))​(int offsetX)` | Sets the x offset of the sprite image in pixels. |
| `void` | `[setOffsetY](#setOffsetY(int))​(int offsetY)` | Sets the y offset of the sprite image in pixels. |
| `[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image")` | `[toBufferedImage](#toBufferedImage())()` | Converts the sprite into a BufferedImage. |
| `void` | `[toBufferedImage](#toBufferedImage(java.awt.image.BufferedImage))​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") img)` | Writes the contents of the sprite to the given BufferedImage. |
| `[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image")` | `[toBufferedOutline](#toBufferedOutline(java.awt.Color))​([Color](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Color.html?is-external=true "class or interface in java.awt") color)` | Writes the contents of the SpritePixels with chosen outline to the BufferedImage |
| `void` | `[toBufferedOutline](#toBufferedOutline(java.awt.image.BufferedImage,int))​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") img,
int color)` | Writes the contents of the SpritePixels with chosen outline to the BufferedImage |

* + ### Field Detail

- #### DEFAULT\_SHADOW\_COLOR

```
static final int DEFAULT_SHADOW_COLOR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SpritePixels.DEFAULT_SHADOW_COLOR)

+ ### Method Detail

- #### drawAt

```
void drawAt​(int x,
int y)
```

Draws the pixels at the given coordinates on the canvas.

Parameters:
`x` - the x-axis coordinate
`y` - the y-axis coordinate
- #### getWidth

```
int getWidth()
```

Gets the width of the sprite image in pixels.

Returns:
the width
- #### getHeight

```
int getHeight()
```

Gets the height of the sprite image in pixels.

Returns:
the height
- #### getMaxWidth

```
int getMaxWidth()
```

Gets the max width of the sprite image in pixels.

Returns:
the width
- #### getMaxHeight

```
int getMaxHeight()
```

Gets the max height of the sprite image in pixels.

Returns:
the height
- #### getOffsetX

```
int getOffsetX()
```

Gets the x offset of the sprite image in pixels.

Returns:
the offset
- #### getOffsetY

```
int getOffsetY()
```

Gets the y offset of the sprite image in pixels.

Returns:
the offset
- #### setMaxWidth

```
void setMaxWidth​(int maxWidth)
```

Sets the max width of the sprite image in pixels.

Parameters:
`maxWidth` - the width
- #### setMaxHeight

```
void setMaxHeight​(int maxHeight)
```

Sets the max height of the sprite image in pixels.

Parameters:
`maxHeight` - the height
- #### setOffsetX

```
void setOffsetX​(int offsetX)
```

Sets the x offset of the sprite image in pixels.

Parameters:
`offsetX` - the offset
- #### setOffsetY

```
void setOffsetY​(int offsetY)
```

Sets the y offset of the sprite image in pixels.

Parameters:
`offsetY` - the offset
- #### getPixels

```
int[] getPixels()
```

Gets an array of all pixels data in the sprite.

Returns:
the pixel data
- #### toBufferedImage

```
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") toBufferedImage()
```

Converts the sprite into a BufferedImage.

Returns:
the resulting BufferedImage
- #### toBufferedImage

```
void toBufferedImage​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") img)
throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")
```

Writes the contents of the sprite to the given BufferedImage.

Parameters:
`img` - the passsed buffered image
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if the width or height do not match
- #### toBufferedOutline

```
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") toBufferedOutline​([Color](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Color.html?is-external=true "class or interface in java.awt") color)
```

Writes the contents of the SpritePixels with chosen outline to the BufferedImage

Parameters:
`color` - target color
- #### toBufferedOutline

```
void toBufferedOutline​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") img,
int color)
```

Writes the contents of the SpritePixels with chosen outline to the BufferedImage

Parameters:
`img` - target image
`color` - target color