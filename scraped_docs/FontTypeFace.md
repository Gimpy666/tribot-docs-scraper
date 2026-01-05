# FontTypeFace (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/FontTypeFace.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface FontTypeFace
```

A bitmap Font in Jagex's format

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[drawWidgetText](#drawWidgetText(java.lang.String,int,int,int,int,int,int,int,int,int,int))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int x,
int y,
int width,
int height,
int rgb,
int shadowRGB,
int alpha,
int xTextAlignment,
int yTextAlignment,
int lineHeight)` | |
| `int` | `[getBaseline](#getBaseline())()` | |
| `int` | `[getTextWidth](#getTextWidth(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)` | |

* + ### Method Detail

- #### getTextWidth

```
int getTextWidth​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)
```
- #### getBaseline

```
int getBaseline()
```
- #### drawWidgetText

```
void drawWidgetText​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int x,
int y,
int width,
int height,
int rgb,
int shadowRGB,
int alpha,
int xTextAlignment,
int yTextAlignment,
int lineHeight)
```