# ActorSpotAnim (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ActorSpotAnim.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface ActorSpotAnim
extends [Node](Node.html "interface in net.runelite.api")
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getCycle](#getCycle())()` | Get the frame cycle. |
| `int` | `[getFrame](#getFrame())()` | Get the spotanim frame |
| `int` | `[getHeight](#getHeight())()` | Get the spotanim height |
| `int` | `[getId](#getId())()` | Get the spotanim id |
| `void` | `[setCycle](#setCycle(int))​(int cycle)` | Set the frame cycle. |
| `void` | `[setFrame](#setFrame(int))​(int frame)` | Set the spotanim frame |
| `void` | `[setHeight](#setHeight(int))​(int height)` | Set the spotanim height |
| `void` | `[setId](#setId(int))​(int id)` | Set the spotanim id |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getId

```
int getId()
```

Get the spotanim id

Returns:
See Also:
`SpotanimID`
- #### setId

```
void setId​(int id)
```

Set the spotanim id

Parameters:
`id` -
See Also:
`SpotanimID`
- #### getHeight

```
int getHeight()
```

Get the spotanim height

Returns:
- #### setHeight

```
void setHeight​(int height)
```

Set the spotanim height

Parameters:
`height` -
- #### getFrame

```
int getFrame()
```

Get the spotanim frame

Returns:
- #### setFrame

```
void setFrame​(int frame)
```

Set the spotanim frame

Parameters:
`frame` -
- #### getCycle

```
int getCycle()
```

Get the frame cycle. The number of ticks the client has been on this frame.

Returns:
- #### setCycle

```
void setCycle​(int cycle)
```

Set the frame cycle.

Parameters:
`cycle` -