# Preferences (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Preferences.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface Preferences
```

Stores the clients persisting preferences.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getAreaSoundEffectVolume](#getAreaSoundEffectVolume())()` | Gets the area sound effect volume |
| `boolean` | `[getHideUsername](#getHideUsername())()` | Gets if the login name should be replaced with asterisks |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getRememberedUsername](#getRememberedUsername())()` | Gets the remembered login username. |
| `int` | `[getSoundEffectVolume](#getSoundEffectVolume())()` | Gets the sound effect volume |
| `void` | `[setAreaSoundEffectVolume](#setAreaSoundEffectVolume(int))​(int volume)` | Sets the area sound effect volume |
| `void` | `[setRememberedUsername](#setRememberedUsername(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") username)` | Sets the remembered login username. |
| `void` | `[setSoundEffectVolume](#setSoundEffectVolume(int))​(int volume)` | Sets the sound effect volume |

* + ### Method Detail

- #### getRememberedUsername

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getRememberedUsername()
```

Gets the remembered login username.

Returns:
the remembered username
- #### setRememberedUsername

```
void setRememberedUsername​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") username)
```

Sets the remembered login username.

Parameters:
`username` - the new remembered username
- #### getSoundEffectVolume

```
int getSoundEffectVolume()
```

Gets the sound effect volume

Returns:
volume 0-127 inclusive
- #### setSoundEffectVolume

```
void setSoundEffectVolume​(int volume)
```

Sets the sound effect volume

Parameters:
`volume` - 0-127 inclusive
- #### getAreaSoundEffectVolume

```
int getAreaSoundEffectVolume()
```

Gets the area sound effect volume

Returns:
volume 0-127 inclusive
- #### setAreaSoundEffectVolume

```
void setAreaSoundEffectVolume​(int volume)
```

Sets the area sound effect volume

Parameters:
`volume` - 0-127 inclusive
- #### getHideUsername

```
boolean getHideUsername()
```

Gets if the login name should be replaced with asterisks