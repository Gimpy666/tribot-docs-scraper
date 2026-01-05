# IndexedSprite (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IndexedSprite.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface IndexedSprite
```

Represents an paletted sprite.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getHeight](#getHeight())()` | |
| `int` | `[getOffsetX](#getOffsetX())()` | |
| `int` | `[getOffsetY](#getOffsetY())()` | |
| `int` | `[getOriginalHeight](#getOriginalHeight())()` | |
| `int` | `[getOriginalWidth](#getOriginalWidth())()` | |
| `int[]` | `[getPalette](#getPalette())()` | The color palette in RGB. |
| `byte[]` | `[getPixels](#getPixels())()` | The bitmap of this sprite. |
| `int` | `[getWidth](#getWidth())()` | |
| `void` | `[setHeight](#setHeight(int))​(int height)` | |
| `void` | `[setOffsetX](#setOffsetX(int))​(int offsetX)` | |
| `void` | `[setOffsetY](#setOffsetY(int))​(int offsetY)` | |
| `void` | `[setOriginalHeight](#setOriginalHeight(int))​(int originalHeight)` | |
| `void` | `[setOriginalWidth](#setOriginalWidth(int))​(int originalWidth)` | |
| `void` | `[setPalette](#setPalette(int%5B%5D))​(int[] palette)` | |
| `void` | `[setPixels](#setPixels(byte%5B%5D))​(byte[] pixels)` | |
| `void` | `[setWidth](#setWidth(int))​(int width)` | |

* + ### Method Detail

- #### getPixels

```
byte[] getPixels()
```

The bitmap of this sprite. Each value is an index into [`getPalette()`](#getPalette()).
0 is transparent
- #### setPixels

```
void setPixels​(byte[] pixels)
```
- #### getPalette

```
int[] getPalette()
```

The color palette in RGB. The zero index is unused.
- #### setPalette

```
void setPalette​(int[] palette)
```
- #### getOffsetX

```
int getOffsetX()
```
- #### setOffsetX

```
void setOffsetX​(int offsetX)
```
- #### getOffsetY

```
int getOffsetY()
```
- #### setOffsetY

```
void setOffsetY​(int offsetY)
```
- #### getWidth

```
int getWidth()
```
- #### setWidth

```
void setWidth​(int width)
```
- #### getHeight

```
int getHeight()
```
- #### setHeight

```
void setHeight​(int height)
```
- #### getOriginalWidth

```
int getOriginalWidth()
```
- #### setOriginalWidth

```
void setOriginalWidth​(int originalWidth)
```
- #### getOriginalHeight

```
int getOriginalHeight()
```
- #### setOriginalHeight

```
void setOriginalHeight​(int originalHeight)
```