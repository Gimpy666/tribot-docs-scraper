# GameObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GameObject.html

**Package:** Packagenet.runelite.api

**Description:** Most object in the RuneScape world are considered as game objects. Things
 such as trees, anvils, boxes, etc are all game objects....

---

* All Superinterfaces:
`[TileObject](TileObject.html "interface in net.runelite.api")`

---

```
public interface GameObject
extends [TileObject](TileObject.html "interface in net.runelite.api")
```

Represents a game object.

Most object in the RuneScape world are considered as game objects. Things
such as trees, anvils, boxes, etc are all game objects.

* + ### Field Summary

- ### Fields inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[HASH\_PLANE\_SHIFT](TileObject.html#HASH_PLANE_SHIFT)`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getConfig](#getConfig())()` | A bitfield containing various flags: |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getConvexHull](#getConvexHull())()` | Gets the convex hull of the object's model. |
| `int` | `[getModelOrientation](#getModelOrientation())()` | Gets the orientation of the model in JAU. |
| `int` | `[getOrientation](#getOrientation())()` | Get the orientation of the object |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getRenderable](#getRenderable())()` | |
| `[Point](Point.html "class in net.runelite.api")` | `[getSceneMaxLocation](#getSceneMaxLocation())()` | Gets the maximum x and y scene coordinate pair for this game object. |
| `[Point](Point.html "class in net.runelite.api")` | `[getSceneMinLocation](#getSceneMinLocation())()` | Gets the minimum x and y scene coordinate pair for this game object. |
| `int` | `[sizeX](#sizeX())()` | Get the size of this object, in tiles, on the x axis |
| `int` | `[sizeY](#sizeY())()` | Get the size of this object, in tiles, on the y axis |

- ### Methods inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[getCanvasLocation](TileObject.html#getCanvasLocation()), [getCanvasLocation](TileObject.html#getCanvasLocation(int)), [getCanvasTextLocation](TileObject.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](TileObject.html#getCanvasTilePoly()), [getClickbox](TileObject.html#getClickbox()), [getHash](TileObject.html#getHash()), [getId](TileObject.html#getId()), [getLocalLocation](TileObject.html#getLocalLocation()), [getMinimapLocation](TileObject.html#getMinimapLocation()), [getOpOverride](TileObject.html#getOpOverride(int)), [getPlane](TileObject.html#getPlane()), [getWorldLocation](TileObject.html#getWorldLocation()), [getWorldView](TileObject.html#getWorldView()), [getX](TileObject.html#getX()), [getY](TileObject.html#getY()), [getZ](TileObject.html#getZ()), [isOpShown](TileObject.html#isOpShown(int))`

* + ### Method Detail

- #### sizeX

```
int sizeX()
```

Get the size of this object, in tiles, on the x axis

Returns:
- #### sizeY

```
int sizeY()
```

Get the size of this object, in tiles, on the y axis

Returns:
- #### getSceneMinLocation

```
[Point](Point.html "class in net.runelite.api") getSceneMinLocation()
```

Gets the minimum x and y scene coordinate pair for this game object.

Returns:
the minimum scene coordinate
- #### getSceneMaxLocation

```
[Point](Point.html "class in net.runelite.api") getSceneMaxLocation()
```

Gets the maximum x and y scene coordinate pair for this game object.

This value differs from [`getSceneMinLocation()`](#getSceneMinLocation()) when the size
of the object is more than 1 tile.

Returns:
the maximum scene coordinate
- #### getConvexHull

```
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getConvexHull()
```

Gets the convex hull of the object's model.

Returns:
the convex hull
See Also:
[`Jarvis`](model/Jarvis.html "class in net.runelite.api.model")
- #### getOrientation

```
int getOrientation()
```

Get the orientation of the object

Returns:
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getRenderable

```
[Renderable](Renderable.html "interface in net.runelite.api") getRenderable()
```
- #### getModelOrientation

```
int getModelOrientation()
```

Gets the orientation of the model in JAU.
This is typically 0 for non-actors, since
most object's models are oriented prior to
lighting during scene loading. See [`getOrientation()`](#getOrientation())
instead for object orientation.

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getConfig

```
int getConfig()
```

A bitfield containing various flags:

```

object type = bits & 31
orientation = bits >>> 6 & 3
supports items = bits >>> 8 & 1

```