# WorldEntity (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/WorldEntity.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`

---

```
public interface WorldEntity
extends [CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[OWNER\_TYPE\_NOT\_PLAYER](#OWNER_TYPE_NOT_PLAYER)` | |
| `static int` | `[OWNER\_TYPE\_OTHER\_PLAYER](#OWNER_TYPE_OTHER_PLAYER)` | |
| `static int` | `[OWNER\_TYPE\_SELF\_PLAYER](#OWNER_TYPE_SELF_PLAYER)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[WorldEntityConfig](WorldEntityConfig.html "interface in net.runelite.api")` | `[getConfig](#getConfig())()` | |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocalLocation](#getLocalLocation())()` | Get the location of this world entity in the top level world. |
| `int` | `[getOrientation](#getOrientation())()` | Get the orientation of this world entity in the top level world. |
| `int` | `[getOwnerType](#getOwnerType())()` | |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getTargetLocation](#getTargetLocation())()` | Get the destination that the WorldEntity is moving toward. |
| `int` | `[getTargetOrientation](#getTargetOrientation())()` | Get the target orientation of this world entity in the top level world. |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView())()` | |
| `boolean` | `[isHiddenForOverlap](#isHiddenForOverlap())()` | Return true if this worldentity is overlapped |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[transformToMainWorld](#transformToMainWorld(net.runelite.api.coords.LocalPoint))​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)` | Transform a point within the world entity to the overworld |

- ### Methods inherited from interface net.runelite.api.[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")

`[getCameraFocus](CameraFocusableEntity.html#getCameraFocus())`

* + ### Field Detail

- #### OWNER\_TYPE\_NOT\_PLAYER

```
static final int OWNER_TYPE_NOT_PLAYER
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.WorldEntity.OWNER_TYPE_NOT_PLAYER)
- #### OWNER\_TYPE\_OTHER\_PLAYER

```
static final int OWNER_TYPE_OTHER_PLAYER
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.WorldEntity.OWNER_TYPE_OTHER_PLAYER)
- #### OWNER\_TYPE\_SELF\_PLAYER

```
static final int OWNER_TYPE_SELF_PLAYER
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.WorldEntity.OWNER_TYPE_SELF_PLAYER)

+ ### Method Detail

- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView()
```

Specified by:
`[getWorldView](CameraFocusableEntity.html#getWorldView())` in interface `[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`
- #### getLocalLocation

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocalLocation()
```

Get the location of this world entity in the top level world.

Returns:
- #### getOrientation

```
int getOrientation()
```

Get the orientation of this world entity in the top level world.

Returns:
- #### getTargetLocation

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getTargetLocation()
```

Get the destination that the WorldEntity is moving toward.
After receiving a destination from the server, the client will
interpolate movement along this route until the next game tick
(with some added buffer for lag compensation).

Returns:
The target [`LocalPoint`](coords/LocalPoint.html "class in net.runelite.api.coords") in the top-level [`WorldView`](WorldView.html "interface in net.runelite.api").
- #### getTargetOrientation

```
int getTargetOrientation()
```

Get the target orientation of this world entity in the top level world.

Returns:
See Also:
[`getTargetLocation()`](#getTargetLocation())
- #### transformToMainWorld

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") transformToMainWorld​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)
```

Transform a point within the world entity to the overworld

Parameters:
`point` -
Returns:
- #### isHiddenForOverlap

```
boolean isHiddenForOverlap()
```

Return true if this worldentity is overlapped

Returns:
- #### getConfig

```
[WorldEntityConfig](WorldEntityConfig.html "interface in net.runelite.api") getConfig()
```
- #### getOwnerType

```
int getOwnerType()
```