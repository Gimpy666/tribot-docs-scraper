# GraphicsObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GraphicsObject.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface GraphicsObject
extends [Renderable](Renderable.html "interface in net.runelite.api")
```

Represents a graphics object/spotanim.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `boolean` | `[finished](#finished())()` | Checks if this spotanim is done animating |
| `[Animation](Animation.html "interface in net.runelite.api")` | `[getAnimation](#getAnimation())()` | The animation of the spotanim |
| `int` | `[getAnimationFrame](#getAnimationFrame())()` | The frame of the current animation |
| `int` | `[getId](#getId())()` | The graphics object ID. |
| `int` | `[getLevel](#getLevel())()` | The plane the spotanim is on. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocation](#getLocation())()` | The location of the object. |
| `int` | `[getStartCycle](#getStartCycle())()` | Get the time this spotanim starts |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView())()` | Get the [`WorldEntity`](WorldEntity.html "interface in net.runelite.api") this spotanim is on. |
| `int` | `[getZ](#getZ())()` | Gets the z coordinate |
| `void` | `[setFinished](#setFinished(boolean))​(boolean finished)` | Set if this spotanim is done animating. |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView()
```

Get the [`WorldEntity`](WorldEntity.html "interface in net.runelite.api") this spotanim is on.

Returns:
- #### getId

```
int getId()
```

The graphics object ID.

Returns:
the ID
- #### getLocation

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocation()
```

The location of the object.

Returns:
the location
- #### getStartCycle

```
int getStartCycle()
```

Get the time this spotanim starts

Returns:
- #### getLevel

```
int getLevel()
```

The plane the spotanim is on.

Returns:
- #### getZ

```
int getZ()
```

Gets the z coordinate
- #### finished

```
boolean finished()
```

Checks if this spotanim is done animating

Returns:
- #### setFinished

```
void setFinished​(boolean finished)
```

Set if this spotanim is done animating. If finished, the spotanim will despawn next frame.

Parameters:
`finished` -
- #### getAnimation

```
@Nullable
[Animation](Animation.html "interface in net.runelite.api") getAnimation()
```

The animation of the spotanim

Returns:
- #### getAnimationFrame

```
int getAnimationFrame()
```

The frame of the current animation

Returns: