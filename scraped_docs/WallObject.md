# WallObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/WallObject.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[TileObject](TileObject.html "interface in net.runelite.api")`

---

```
public interface WallObject
extends [TileObject](TileObject.html "interface in net.runelite.api")
```

Represents one or two walls on a tile

* + ### Field Summary

- ### Fields inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[HASH\_PLANE\_SHIFT](TileObject.html#HASH_PLANE_SHIFT)`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getConfig](#getConfig())()` | A bitfield containing various flags: |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getConvexHull](#getConvexHull())()` | Gets the convex hull of the objects model. |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getConvexHull2](#getConvexHull2())()` | |
| `int` | `[getOrientationA](#getOrientationA())()` | A bitfield with the orientation of the first wall
1 = West
2 = North
4 = East
8 = South
16 = North-west
32 = North-east
64 = South-east
128 = South-west |
| `int` | `[getOrientationB](#getOrientationB())()` | A bitfield with the orientation of the second wall
1 = West
2 = North
4 = East
8 = South
16 = North-west
32 = North-east
64 = South-east
128 = South-west |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getRenderable1](#getRenderable1())()` | |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getRenderable2](#getRenderable2())()` | |

- ### Methods inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[getCanvasLocation](TileObject.html#getCanvasLocation()), [getCanvasLocation](TileObject.html#getCanvasLocation(int)), [getCanvasTextLocation](TileObject.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](TileObject.html#getCanvasTilePoly()), [getClickbox](TileObject.html#getClickbox()), [getHash](TileObject.html#getHash()), [getId](TileObject.html#getId()), [getLocalLocation](TileObject.html#getLocalLocation()), [getMinimapLocation](TileObject.html#getMinimapLocation()), [getOpOverride](TileObject.html#getOpOverride(int)), [getPlane](TileObject.html#getPlane()), [getWorldLocation](TileObject.html#getWorldLocation()), [getWorldView](TileObject.html#getWorldView()), [getX](TileObject.html#getX()), [getY](TileObject.html#getY()), [getZ](TileObject.html#getZ()), [isOpShown](TileObject.html#isOpShown(int))`

* + ### Method Detail

- #### getOrientationA

```
int getOrientationA()
```

A bitfield with the orientation of the first wall
1 = West
2 = North
4 = East
8 = South
16 = North-west
32 = North-east
64 = South-east
128 = South-west
- #### getOrientationB

```
int getOrientationB()
```

A bitfield with the orientation of the second wall
1 = West
2 = North
4 = East
8 = South
16 = North-west
32 = North-east
64 = South-east
128 = South-west
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
- #### getConvexHull

```
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getConvexHull()
```

Gets the convex hull of the objects model.

Returns:
the convex hull
See Also:
[`Jarvis`](model/Jarvis.html "class in net.runelite.api.model")
- #### getConvexHull2

```
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getConvexHull2()
```
- #### getRenderable1

```
[Renderable](Renderable.html "interface in net.runelite.api") getRenderable1()
```
- #### getRenderable2

```
[Renderable](Renderable.html "interface in net.runelite.api") getRenderable2()
```