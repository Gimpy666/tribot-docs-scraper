# AmbientSoundEffect (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/AmbientSoundEffect.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface AmbientSoundEffect
```

An ambient sound effect. These are loaded only at scene load and are used to play ambient
sound effects that are purely client side and not sent from the server.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int[]` | `[getBackgroundSoundEffectIds](#getBackgroundSoundEffectIds())()` | The background sound effect ids. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getMaxPosition](#getMaxPosition())()` | The max x/y position of the area this sound effect is at |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getMinPosition](#getMinPosition())()` | The min x/y position of the area this sound effect is at. |
| `int` | `[getPlane](#getPlane())()` | The plane the sound effect is on |
| `int` | `[getSoundEffectId](#getSoundEffectId())()` | The id of the sound effect |

* + ### Method Detail

- #### getSoundEffectId

```
int getSoundEffectId()
```

The id of the sound effect

Returns:
See Also:
[`SoundEffectID`](SoundEffectID.html "class in net.runelite.api")
- #### getBackgroundSoundEffectIds

```
@Nullable
int[] getBackgroundSoundEffectIds()
```

The background sound effect ids. One sound effect is picked from this at random.

Returns:
See Also:
[`SoundEffectID`](SoundEffectID.html "class in net.runelite.api")
- #### getPlane

```
int getPlane()
```

The plane the sound effect is on

Returns:
- #### getMinPosition

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getMinPosition()
```

The min x/y position of the area this sound effect is at.

Returns:
- #### getMaxPosition

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getMaxPosition()
```

The max x/y position of the area this sound effect is at

Returns: