# TextureProvider (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/TextureProvider.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface TextureProvider
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `double` | `[getBrightness](#getBrightness())()` | |
| `int` | `[getDefaultColor](#getDefaultColor(int))​(int textureID)` | Get the HSL color used when the texture isn't loaded yet |
| `[Texture](Texture.html "interface in net.runelite.api")[]` | `[getTextures](#getTextures())()` | Get all textures |
| `int[]` | `[load](#load(int))​(int textureId)` | Get the pixels for a texture |
| `void` | `[setBrightness](#setBrightness(double))​(double brightness)` | Set the brightness for textures, clearing the texture cache. |

* + ### Method Detail

- #### getBrightness

```
double getBrightness()
```
- #### setBrightness

```
void setBrightness​(double brightness)
```

Set the brightness for textures, clearing the texture cache.

.9 is the darkest value available in the standard options
.6 is the brightest value
- #### getTextures

```
[Texture](Texture.html "interface in net.runelite.api")[] getTextures()
```

Get all textures
- #### load

```
int[] load​(int textureId)
```

Get the pixels for a texture
- #### getDefaultColor

```
int getDefaultColor​(int textureID)
```

Get the HSL color used when the texture isn't loaded yet