# Texture (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Texture.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface Texture
extends [Node](Node.html "interface in net.runelite.api")
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getAnimationDirection](#getAnimationDirection())()` | |
| `int` | `[getAnimationSpeed](#getAnimationSpeed())()` | |
| `int[]` | `[getPixels](#getPixels())()` | |
| `float` | `[getU](#getU())()` | |
| `float` | `[getV](#getV())()` | |
| `boolean` | `[isLoaded](#isLoaded())()` | |
| `void` | `[setU](#setU(float))​(float u)` | |
| `void` | `[setV](#setV(float))​(float v)` | |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getPixels

```
int[] getPixels()
```
- #### getAnimationDirection

```
int getAnimationDirection()
```
- #### getAnimationSpeed

```
int getAnimationSpeed()
```
- #### isLoaded

```
boolean isLoaded()
```
- #### getU

```
float getU()
```
- #### setU

```
void setU​(float u)
```
- #### getV

```
float getV()
```
- #### setV

```
void setV​(float v)
```