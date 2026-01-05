# TileObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/TileObject.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[DecorativeObject](DecorativeObject.html "interface in net.runelite.api")`, `[GameObject](GameObject.html "interface in net.runelite.api")`, `[GroundObject](GroundObject.html "interface in net.runelite.api")`, `[ItemLayer](ItemLayer.html "interface in net.runelite.api")`, `[WallObject](WallObject.html "interface in net.runelite.api")`

---

```
public interface TileObject
```

Represents an object on a Tile

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[HASH\_PLANE\_SHIFT](#HASH_PLANE_SHIFT)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasLocation](#getCanvasLocation())()` | Calculates the position of the center of this tile on the canvas |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasLocation](#getCanvasLocation(int))​(int zOffset)` | Calculates the position of the center of this tile on the canvas |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasTextLocation](#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int))​([Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int zOffset)` | Calculates the canvas point to center `text` above the tile this object is on. |
| `[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTilePoly](#getCanvasTilePoly())()` | Creates a polygon outlining the tile this object is on |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getClickbox](#getClickbox())()` | Calculate the on-screen clickable area of the object. |
| `long` | `[getHash](#getHash())()` | A bitfield containing various flags: |
| `int` | `[getId](#getId())()` | Gets the ID of the object. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocalLocation](#getLocalLocation())()` | Get the local location for this object. |
| `[Point](Point.html "class in net.runelite.api")` | `[getMinimapLocation](#getMinimapLocation())()` | Gets a point on the canvas of where this objects mini-map indicator
should appear. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getOpOverride](#getOpOverride(int))​(int index)` | Get the text override for a certain action |
| `int` | `[getPlane](#getPlane())()` | Gets the plane of the tile that the object is on. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getWorldLocation](#getWorldLocation())()` | Get the world location for this object. |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView())()` | Gets the WorldView this TileObject is a part of. |
| `int` | `[getX](#getX())()` | Gets the x-axis coordinate of the object in local context. |
| `int` | `[getY](#getY())()` | Gets the y-axis coordinate of the object in local context. |
| `int` | `[getZ](#getZ())()` | Gets the vertical coordinate of this object |
| `boolean` | `[isOpShown](#isOpShown(int))​(int index)` | Gets if an action is shown in the minimenu. |

* + ### Field Detail

- #### HASH\_PLANE\_SHIFT

```
static final int HASH_PLANE_SHIFT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.TileObject.HASH_PLANE_SHIFT)

+ ### Method Detail

- #### getHash

```
long getHash()
```

A bitfield containing various flags:

```

worldView = bits >> 52 & 4095
id = bits >> 20 & 0xffffffff
wall = bits >> 19 & 1
type = bits >> 16 & 7
plane = bits >> 14 & 3
scene y = bits >> 7 & 127
scene x = bits >> 0 & 127

```

Type 0 = player, 1 = npc, 2 = game object, 3 = item, 4 = world entity
- #### getX

```
int getX()
```

Gets the x-axis coordinate of the object in local context.

See Also:
[`LocalPoint`](coords/LocalPoint.html "class in net.runelite.api.coords")
- #### getY

```
int getY()
```

Gets the y-axis coordinate of the object in local context.

See Also:
[`LocalPoint`](coords/LocalPoint.html "class in net.runelite.api.coords")
- #### getZ

```
int getZ()
```

Gets the vertical coordinate of this object
- #### getPlane

```
int getPlane()
```

Gets the plane of the tile that the object is on.
- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView()
```

Gets the WorldView this TileObject is a part of.
- #### getId

```
int getId()
```

Gets the ID of the object.

See Also:
`ObjectID`
- #### getWorldLocation

```
@Nonnull
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getWorldLocation()
```

Get the world location for this object. For objects which are larger than 1 tile, this is the
center most tile, rounded to the south-west.

Returns:
- #### getLocalLocation

```
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocalLocation()
```

Get the local location for this object. This point is the center point of the object.

Returns:
- #### getCanvasLocation

```
@Nullable
[Point](Point.html "class in net.runelite.api") getCanvasLocation()
```

Calculates the position of the center of this tile on the canvas
- #### getCanvasLocation

```
@Nullable
[Point](Point.html "class in net.runelite.api") getCanvasLocation​(int zOffset)
```

Calculates the position of the center of this tile on the canvas

Parameters:
`zOffset` - Vertical offset to apply before projection
- #### getCanvasTilePoly

```
@Nullable
[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTilePoly()
```

Creates a polygon outlining the tile this object is on
- #### getCanvasTextLocation

```
@Nullable
[Point](Point.html "class in net.runelite.api") getCanvasTextLocation​([Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int zOffset)
```

Calculates the canvas point to center `text` above the tile this object is on.

Parameters:
`graphics` - the graphics to use for font size calculation
`zOffset` - Vertical offset to apply before projection
Returns:
the canvas point to draw the text at
- #### getMinimapLocation

```
@Nullable
[Point](Point.html "class in net.runelite.api") getMinimapLocation()
```

Gets a point on the canvas of where this objects mini-map indicator
should appear.

Returns:
mini-map location on canvas
- #### getClickbox

```
@Nullable
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getClickbox()
```

Calculate the on-screen clickable area of the object.
- #### getOpOverride

```
@Nullable
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getOpOverride​(int index)
```

Get the text override for a certain action
- #### isOpShown

```
boolean isOpShown​(int index)
```

Gets if an action is shown in the minimenu. If an action is `null` it
will not be shown even if this method returns `true`