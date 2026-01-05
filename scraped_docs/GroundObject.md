# GroundObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GroundObject.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[TileObject](TileObject.html "interface in net.runelite.api")`

---

```
public interface GroundObject
extends [TileObject](TileObject.html "interface in net.runelite.api")
```

Represents an object on the ground of a tile.

* + ### Field Summary

- ### Fields inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[HASH\_PLANE\_SHIFT](TileObject.html#HASH_PLANE_SHIFT)`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getConfig](#getConfig())()` | A bitfield containing various flags: |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getConvexHull](#getConvexHull())()` | Gets the convex hull of the objects model. |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getRenderable](#getRenderable())()` | |

- ### Methods inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[getCanvasLocation](TileObject.html#getCanvasLocation()), [getCanvasLocation](TileObject.html#getCanvasLocation(int)), [getCanvasTextLocation](TileObject.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](TileObject.html#getCanvasTilePoly()), [getClickbox](TileObject.html#getClickbox()), [getHash](TileObject.html#getHash()), [getId](TileObject.html#getId()), [getLocalLocation](TileObject.html#getLocalLocation()), [getMinimapLocation](TileObject.html#getMinimapLocation()), [getOpOverride](TileObject.html#getOpOverride(int)), [getPlane](TileObject.html#getPlane()), [getWorldLocation](TileObject.html#getWorldLocation()), [getWorldView](TileObject.html#getWorldView()), [getX](TileObject.html#getX()), [getY](TileObject.html#getY()), [getZ](TileObject.html#getZ()), [isOpShown](TileObject.html#isOpShown(int))`

* + ### Method Detail

- #### getRenderable

```
[Renderable](Renderable.html "interface in net.runelite.api") getRenderable()
```
- #### getConvexHull

```
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getConvexHull()
```

Gets the convex hull of the objects model.

Returns:
the convex hull
See Also:
[`Jarvis`](model/Jarvis.html "class in net.runelite.api.model")
- #### getConfig

```
int getConfig()
```

A bitfield containing various flags:

```

object type id = bits & 0x20
orientation (0-3) = bits >>> 6 & 3
supports items = bits >>> 8 & 1

```