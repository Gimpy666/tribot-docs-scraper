# NpcOverrides (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/NpcOverrides.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface NpcOverrides
```

Dynamically applied NPC effects

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `short[]` | `[getColorToReplaceWith](#getColorToReplaceWith())()` | Replaces this NPC's recolor values. |
| `int[]` | `[getModelIds](#getModelIds())()` | Entirely replaces this NPC's models |
| `short[]` | `[getTextureToReplaceWith](#getTextureToReplaceWith())()` | |
| `boolean` | `[useLocalPlayer](#useLocalPlayer())()` | Causes this NPC to use the model of the local player instead |

* + ### Method Detail

- #### getModelIds

```
@Nullable
int[] getModelIds()
```

Entirely replaces this NPC's models
- #### getColorToReplaceWith

```
@Nullable
short[] getColorToReplaceWith()
```

Replaces this NPC's recolor values. Does not replace it's keys, which must be set statically
in the cache
- #### getTextureToReplaceWith

```
@Nullable
short[] getTextureToReplaceWith()
```
- #### useLocalPlayer

```
boolean useLocalPlayer()
```

Causes this NPC to use the model of the local player instead