# TileItem (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/TileItem.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface TileItem
extends [Renderable](Renderable.html "interface in net.runelite.api")
```

Represents an item inside an [`ItemLayer`](ItemLayer.html "interface in net.runelite.api").

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[OWNERSHIP\_GROUP](#OWNERSHIP_GROUP)` | |
| `static int` | `[OWNERSHIP\_NONE](#OWNERSHIP_NONE)` | |
| `static int` | `[OWNERSHIP\_OTHER](#OWNERSHIP_OTHER)` | |
| `static int` | `[OWNERSHIP\_SELF](#OWNERSHIP_SELF)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getDespawnTime](#getDespawnTime())()` | Get the time, in server ticks, when the item despawns |
| `int` | `[getId](#getId())()` | |
| `int` | `[getOwnership](#getOwnership())()` | Get the item ownership |
| `int` | `[getQuantity](#getQuantity())()` | |
| `int` | `[getVisibleTime](#getVisibleTime())()` | Get the time, in server ticks, when the item becomes visible to other players |
| `boolean` | `[isPrivate](#isPrivate())()` | Test whether the item is private |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Field Detail

- #### OWNERSHIP\_NONE

```
static final int OWNERSHIP_NONE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.TileItem.OWNERSHIP_NONE)
- #### OWNERSHIP\_SELF

```
static final int OWNERSHIP_SELF
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.TileItem.OWNERSHIP_SELF)
- #### OWNERSHIP\_OTHER

```
static final int OWNERSHIP_OTHER
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.TileItem.OWNERSHIP_OTHER)
- #### OWNERSHIP\_GROUP

```
static final int OWNERSHIP_GROUP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.TileItem.OWNERSHIP_GROUP)

+ ### Method Detail

- #### getId

```
int getId()
```

Returns:
the ID of the item
See Also:
`ItemID`
- #### getQuantity

```
int getQuantity()
```
- #### getVisibleTime

```
int getVisibleTime()
```

Get the time, in server ticks, when the item becomes visible to other players

Returns:
See Also:
[`Client.getTickCount()`](Client.html#getTickCount())
- #### getDespawnTime

```
int getDespawnTime()
```

Get the time, in server ticks, when the item despawns

Returns:
See Also:
[`Client.getTickCount()`](Client.html#getTickCount())
- #### getOwnership

```
int getOwnership()
```

Get the item ownership

Returns:
- #### isPrivate

```
boolean isPrivate()
```

Test whether the item is private

Returns: