# ItemLayer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ItemLayer.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[TileObject](TileObject.html "interface in net.runelite.api")`

---

```
public interface ItemLayer
extends [TileObject](TileObject.html "interface in net.runelite.api")
```

Represents a pile of items held by a tile.

* + ### Field Summary

- ### Fields inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[HASH\_PLANE\_SHIFT](TileObject.html#HASH_PLANE_SHIFT)`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getBottom](#getBottom())()` | Gets the item at the bottom of the pile. |
| `int` | `[getHeight](#getHeight())()` | Gets the height of the layer. |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getMiddle](#getMiddle())()` | Gets the item at the middle of the pile. |
| `[Renderable](Renderable.html "interface in net.runelite.api")` | `[getTop](#getTop())()` | Gets the item at the top of the pile. |

- ### Methods inherited from interface net.runelite.api.[TileObject](TileObject.html "interface in net.runelite.api")

`[getCanvasLocation](TileObject.html#getCanvasLocation()), [getCanvasLocation](TileObject.html#getCanvasLocation(int)), [getCanvasTextLocation](TileObject.html#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int)), [getCanvasTilePoly](TileObject.html#getCanvasTilePoly()), [getClickbox](TileObject.html#getClickbox()), [getHash](TileObject.html#getHash()), [getId](TileObject.html#getId()), [getLocalLocation](TileObject.html#getLocalLocation()), [getMinimapLocation](TileObject.html#getMinimapLocation()), [getOpOverride](TileObject.html#getOpOverride(int)), [getPlane](TileObject.html#getPlane()), [getWorldLocation](TileObject.html#getWorldLocation()), [getWorldView](TileObject.html#getWorldView()), [getX](TileObject.html#getX()), [getY](TileObject.html#getY()), [getZ](TileObject.html#getZ()), [isOpShown](TileObject.html#isOpShown(int))`

* + ### Method Detail

- #### getHeight

```
int getHeight()
```

Gets the height of the layer.

Returns:
the height
- #### getBottom

```
[Renderable](Renderable.html "interface in net.runelite.api") getBottom()
```

Gets the item at the bottom of the pile.

Returns:
the bottom item
- #### getMiddle

```
[Renderable](Renderable.html "interface in net.runelite.api") getMiddle()
```

Gets the item at the middle of the pile.

Returns:
the middle item
- #### getTop

```
[Renderable](Renderable.html "interface in net.runelite.api") getTop()
```

Gets the item at the top of the pile.

Returns:
the top item