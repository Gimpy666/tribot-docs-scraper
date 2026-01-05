# Rasterizer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Rasterizer.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface Rasterizer
```

Jagex 2D and 3D drawing utilities.
Similar to AWT's [`Graphics2D`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt")

See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[fillRectangle](#fillRectangle(int,int,int,int,int))​(int x,
int y,
int w,
int h,
int rgb)` | Draws a filled rectangle onto the rasterizer buffer at full opacity |
| `int` | `[getHeight](#getHeight())()` | Height of [`getPixels()`](#getPixels()) |
| `int[]` | `[getPixels](#getPixels())()` | Gets the back buffer of the rasterizer

ARGB or RGB depending on [`Client.isGpu()`](Client.html#isGpu()) |
| `int` | `[getWidth](#getWidth())()` | Width of [`getPixels()`](#getPixels()) |
| `void` | `[rasterFlat](#rasterFlat(int,int,int,int,int,int,int))​(int y0,
int y1,
int y2,
int x0,
int x1,
int x2,
int rgb)` | Draws a filled triangle onto the rasterizer buffer at rasterizer opacity |
| `void` | `[rasterGouraud](#rasterGouraud(int,int,int,int,int,int,int,int,int))​(int y0,
int y1,
int y2,
int x0,
int x1,
int x2,
int hsl0,
int hsl1,
int hsl2)` | Draws a gouraud shaded filled triangle onto the rasterizer buffer at rasterizer opacity |
| `void` | `[resetRasterClipping](#resetRasterClipping())()` | |
| `void` | `[setDrawRegion](#setDrawRegion(int,int,int,int))​(int x0,
int y0,
int x1,
int x2)` | |
| `void` | `[setRasterGouraudLowRes](#setRasterGouraudLowRes(boolean))​(boolean lowRes)` | Sets if [`rasterGouraud(int, int, int, int, int, int, int, int, int)`](#rasterGouraud(int,int,int,int,int,int,int,int,int)) uses a faster shading algorithm |

* + ### Method Detail

- #### getPixels

```
int[] getPixels()
```

Gets the back buffer of the rasterizer

ARGB or RGB depending on [`Client.isGpu()`](Client.html#isGpu())
- #### getWidth

```
int getWidth()
```

Width of [`getPixels()`](#getPixels())
- #### getHeight

```
int getHeight()
```

Height of [`getPixels()`](#getPixels())
- #### fillRectangle

```
void fillRectangle​(int x,
int y,
int w,
int h,
int rgb)
```

Draws a filled rectangle onto the rasterizer buffer at full opacity
- #### rasterFlat

```
void rasterFlat​(int y0,
int y1,
int y2,
int x0,
int x1,
int x2,
int rgb)
```

Draws a filled triangle onto the rasterizer buffer at rasterizer opacity
- #### setRasterGouraudLowRes

```
void setRasterGouraudLowRes​(boolean lowRes)
```

Sets if [`rasterGouraud(int, int, int, int, int, int, int, int, int)`](#rasterGouraud(int,int,int,int,int,int,int,int,int)) uses a faster shading algorithm
- #### rasterGouraud

```
void rasterGouraud​(int y0,
int y1,
int y2,
int x0,
int x1,
int x2,
int hsl0,
int hsl1,
int hsl2)
```

Draws a gouraud shaded filled triangle onto the rasterizer buffer at rasterizer opacity
- #### setDrawRegion

```
void setDrawRegion​(int x0,
int y0,
int x1,
int x2)
```
- #### resetRasterClipping

```
void resetRasterClipping()
```