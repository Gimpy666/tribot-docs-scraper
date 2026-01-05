# Perspective (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Perspective.html

**Package:** Packagenet.runelite.api

**Description:** Get the on-screen clickable area ofmodelas though it's for the
 object on the tile at (localX,localY) and rotated to
 angleorientation....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.Perspective

* ---

```
public class Perspective
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A utility class containing methods to help with conversion between
in-game features to canvas areas.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int[]` | `[COSINE](#COSINE)` | |
| `static int` | `[LOCAL\_COORD\_BITS](#LOCAL_COORD_BITS)` | |
| `static int` | `[LOCAL\_HALF\_TILE\_SIZE](#LOCAL_HALF_TILE_SIZE)` | |
| `static int` | `[LOCAL\_TILE\_SIZE](#LOCAL_TILE_SIZE)` | |
| `static int` | `[SCENE\_SIZE](#SCENE_SIZE)` | |
| `static int[]` | `[SINE](#SINE)` | |
| `static double` | `[UNIT](#UNIT)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Perspective](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static [Point](Point.html "class in net.runelite.api")` | `[getCanvasImageLocation](#getCanvasImageLocation(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,java.awt.image.BufferedImage,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image,
int zOffset)` | Calculates image position and centers depending on image size. |
| `static [Point](Point.html "class in net.runelite.api")` | `[getCanvasSpriteLocation](#getCanvasSpriteLocation(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,net.runelite.api.SpritePixels,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
[SpritePixels](SpritePixels.html "interface in net.runelite.api") sprite,
int zOffset)` | Calculates sprite position and centers depending on sprite size. |
| `static [Point](Point.html "class in net.runelite.api")` | `[getCanvasTextLocation](#getCanvasTextLocation(net.runelite.api.Client,java.awt.Graphics2D,net.runelite.api.coords.LocalPoint,java.lang.String,int))​([Client](Client.html "interface in net.runelite.api") client,
[Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int zOffset)` | Calculates text position and centers depending on string length. |
| `static [Point](Point.html "class in net.runelite.api")` | `[getCanvasTextMiniMapLocation](#getCanvasTextMiniMapLocation(net.runelite.api.Client,java.awt.Graphics2D,net.runelite.api.coords.LocalPoint,java.lang.String))​([Client](Client.html "interface in net.runelite.api") client,
[Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)` | Calculates text position and centers on minimap depending on string length. |
| `static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTileAreaPoly](#getCanvasTileAreaPoly(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int size)` | Returns a polygon representing an area. |
| `static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTileAreaPoly](#getCanvasTileAreaPoly(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int,int,int,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int sizeX,
int sizeY,
int level,
int heightOffset)` | Returns a polygon representing an area. |
| `static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTilePoly](#getCanvasTilePoly(net.runelite.api.Client,net.runelite.api.coords.LocalPoint))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation)` | Calculates a tile polygon from offset worldToScreen() points. |
| `static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTilePoly](#getCanvasTilePoly(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int zOffset)` | Calculates a tile polygon from offset worldToScreen() points. |
| `static [Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getClickbox](#getClickbox(net.runelite.api.Client,net.runelite.api.WorldView,net.runelite.api.Model,int,int,int,int))​([Client](Client.html "interface in net.runelite.api") client,
[WorldView](WorldView.html "interface in net.runelite.api") wv,
[Model](Model.html "interface in net.runelite.api") model,
int orientation,
int x,
int y,
int z)` | You don't want this. |
| `static int` | `[getFootprintTileHeight](#getFootprintTileHeight(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") p,
int level,
int footprintSize)` | |
| `static [Point](Point.html "class in net.runelite.api")` | `[getMiniMapImageLocation](#getMiniMapImageLocation(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,java.awt.image.BufferedImage))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image)` | Calculates image position and centers depending on image size. |
| `static int` | `[getTileHeight](#getTileHeight(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane)` | Calculates the above ground height of a tile point. |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToCanvas](#localToCanvas(net.runelite.api.Client,int,int,int))​([Client](Client.html "interface in net.runelite.api") client,
int x,
int y,
int z)` | Translates three-dimensional local coordinates within the 3D world to
their corresponding coordinates on the game screen. |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToCanvas](#localToCanvas(net.runelite.api.Client,int,int,int,int))​([Client](Client.html "interface in net.runelite.api") client,
int worldId,
int x,
int y,
int z)` | |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToCanvas](#localToCanvas(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane)` | Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the game screen. |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToCanvas](#localToCanvas(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane,
int heightOffset)` | Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the game screen. |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToMinimap](#localToMinimap(net.runelite.api.Client,net.runelite.api.coords.LocalPoint))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)` | Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the Minimap. |
| `static [Point](Point.html "class in net.runelite.api")` | `[localToMinimap](#localToMinimap(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](Client.html "interface in net.runelite.api") client,
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int distance)` | Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the Minimap. |
| `static void` | `[modelToCanvas](#modelToCanvas(net.runelite.api.Client,int,int,int,int,int,float%5B%5D,float%5B%5D,float%5B%5D,int%5B%5D,int%5B%5D))​([Client](Client.html "interface in net.runelite.api") client,
int end,
int x3dCenter,
int y3dCenter,
int z3dCenter,
int rotate,
float[] x3d,
float[] y3d,
float[] z3d,
int[] x2d,
int[] y2d)` | Deprecated. |
| `static void` | `[modelToCanvas](#modelToCanvas(net.runelite.api.Client,net.runelite.api.WorldView,int,int,int,int,int,float%5B%5D,float%5B%5D,float%5B%5D,int%5B%5D,int%5B%5D))​([Client](Client.html "interface in net.runelite.api") client,
[WorldView](WorldView.html "interface in net.runelite.api") wv,
int end,
int x3dCenter,
int y3dCenter,
int z3dCenter,
int rotate,
float[] x3d,
float[] y3d,
float[] z3d,
int[] x2d,
int[] y2d)` | Translates a model's vertices into 2d space. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### UNIT

```
public static final double UNIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Perspective.UNIT)
- #### LOCAL\_COORD\_BITS

```
public static final int LOCAL_COORD_BITS
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Perspective.LOCAL_COORD_BITS)
- #### LOCAL\_TILE\_SIZE

```
public static final int LOCAL_TILE_SIZE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Perspective.LOCAL_TILE_SIZE)
- #### LOCAL\_HALF\_TILE\_SIZE

```
public static final int LOCAL_HALF_TILE_SIZE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Perspective.LOCAL_HALF_TILE_SIZE)
- #### SCENE\_SIZE

```
public static final int SCENE_SIZE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Perspective.SCENE_SIZE)
- #### SINE

```
public static final int[] SINE
```
- #### COSINE

```
public static final int[] COSINE
```

+ ### Constructor Detail

- #### Perspective

```
public Perspective()
```

+ ### Method Detail

- #### localToCanvas

```
@Nullable
public static [Point](Point.html "class in net.runelite.api") localToCanvas​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane)
```

Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the game screen.

Parameters:
`client` - the game client
`point` - ground coordinate
`plane` - ground plane on the z axis
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the position in
3D-space
- #### localToCanvas

```
@Nullable
public static [Point](Point.html "class in net.runelite.api") localToCanvas​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane,
int heightOffset)
```

Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the game screen.

Parameters:
`client` - the game client
`point` - ground coordinate
`plane` - ground plane on the z axis
`heightOffset` - distance from ground on the z axis
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the position in
3D-space
- #### localToCanvas

```
public static [Point](Point.html "class in net.runelite.api") localToCanvas​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
int x,
int y,
int z)
```

Translates three-dimensional local coordinates within the 3D world to
their corresponding coordinates on the game screen.

Parameters:
`client` - the game client
`x` - ground coordinate on the x axis
`y` - ground coordinate on the y axis
`z` -
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the position in
3D-space
- #### localToCanvas

```
public static [Point](Point.html "class in net.runelite.api") localToCanvas​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
int worldId,
int x,
int y,
int z)
```
- #### modelToCanvas

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static void modelToCanvas​([Client](Client.html "interface in net.runelite.api") client,
int end,
int x3dCenter,
int y3dCenter,
int z3dCenter,
int rotate,
float[] x3d,
float[] y3d,
float[] z3d,
int[] x2d,
int[] y2d)
```

Deprecated.
- #### modelToCanvas

```
public static void modelToCanvas​([Client](Client.html "interface in net.runelite.api") client,
[WorldView](WorldView.html "interface in net.runelite.api") wv,
int end,
int x3dCenter,
int y3dCenter,
int z3dCenter,
int rotate,
float[] x3d,
float[] y3d,
float[] z3d,
int[] x2d,
int[] y2d)
```

Translates a model's vertices into 2d space.
- #### localToMinimap

```
@Nullable
public static [Point](Point.html "class in net.runelite.api") localToMinimap​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)
```

Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the Minimap.

Parameters:
`client` - the game client
`point` - ground coordinate
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the position in
3D-space
- #### localToMinimap

```
@Nullable
public static [Point](Point.html "class in net.runelite.api") localToMinimap​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int distance)
```

Translates two-dimensional ground coordinates within the 3D world to
their corresponding coordinates on the Minimap.

Parameters:
`client` - the game client
`point` - ground coordinate
`distance` - max distance from local player to minimap point
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the position in
3D-space
- #### getTileHeight

```
public static int getTileHeight​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int plane)
```

Calculates the above ground height of a tile point.

Parameters:
`client` - the game client
`point` - the local ground coordinate
`plane` - the client plane/ground level
Returns:
the offset from the ground of the tile
- #### getFootprintTileHeight

```
public static int getFootprintTileHeight​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") p,
int level,
int footprintSize)
```
- #### getCanvasTilePoly

```
public static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTilePoly​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation)
```

Calculates a tile polygon from offset worldToScreen() points.

Parameters:
`client` - the game client
`localLocation` - local location of the tile
Returns:
a [`Polygon`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") on screen corresponding to the given
localLocation.
- #### getCanvasTilePoly

```
public static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTilePoly​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int zOffset)
```

Calculates a tile polygon from offset worldToScreen() points.

Parameters:
`client` - the game client
`localLocation` - local location of the tile
`zOffset` - offset from ground plane
Returns:
a [`Polygon`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") on screen corresponding to the given
localLocation.
- #### getCanvasTileAreaPoly

```
public static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTileAreaPoly​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int size)
```

Returns a polygon representing an area.

Parameters:
`client` - the game client
`localLocation` - the center location of the AoE
`size` - the size of the area (ie. 3x3 AoE evaluates to size 3)
Returns:
a polygon representing the tiles in the area
- #### getCanvasTileAreaPoly

```
public static [Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTileAreaPoly​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
int sizeX,
int sizeY,
int level,
int heightOffset)
```

Returns a polygon representing an area.

Parameters:
`client` - the game client
`localLocation` - the center location of the AoE
`sizeX` - the size of the area in tiles on the x axis
`sizeY` - the size of the area in tiles on the z axis
`level` - the level of the area
`heightOffset` - offset from ground level
Returns:
a polygon representing the tiles in the area
- #### getCanvasTextLocation

```
public static [Point](Point.html "class in net.runelite.api") getCanvasTextLocation​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
@Nullable
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int zOffset)
```

Calculates text position and centers depending on string length.

Parameters:
`client` - the game client
`graphics` - the game graphics
`localLocation` - local location of the tile
`text` - string for width measurement
`zOffset` - offset from ground plane
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the given
localLocation.
- #### getCanvasImageLocation

```
public static [Point](Point.html "class in net.runelite.api") getCanvasImageLocation​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
@Nonnull
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image,
int zOffset)
```

Calculates image position and centers depending on image size.

Parameters:
`client` - the game client
`localLocation` - local location of the tile
`image` - image for size measurement
`zOffset` - offset from ground plane
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the given
localLocation.
- #### getMiniMapImageLocation

```
public static [Point](Point.html "class in net.runelite.api") getMiniMapImageLocation​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
@Nonnull
[BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image)
```

Calculates image position and centers depending on image size.

Parameters:
`client` - the game client
`localLocation` - local location of the tile
`image` - image for size measurement
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the given
localLocation.
- #### getCanvasSpriteLocation

```
public static [Point](Point.html "class in net.runelite.api") getCanvasSpriteLocation​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
@Nonnull
[SpritePixels](SpritePixels.html "interface in net.runelite.api") sprite,
int zOffset)
```

Calculates sprite position and centers depending on sprite size.

Parameters:
`client` - the game client
`localLocation` - local location of the tile
`sprite` - SpritePixel for size measurement
`zOffset` - offset from ground plane
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the given localLocation.
- #### getClickbox

```
@Nullable
@Internal
public static [Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getClickbox​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
[WorldView](WorldView.html "interface in net.runelite.api") wv,
[Model](Model.html "interface in net.runelite.api") model,
int orientation,
int x,
int y,
int z)
```

You don't want this. Use [`TileObject.getClickbox()`](TileObject.html#getClickbox()) instead.

Get the on-screen clickable area of `model` as though it's for the
object on the tile at (`localX`, `localY`) and rotated to
angle `orientation`.

Parameters:
`client` - the game client
`wv` - the worldview
`model` - the model to calculate a clickbox for
`orientation` - the orientation of the model (0-2048, where 0 is north)
`x` - x coord in local space
`z` - y coord in local space
Returns:
the clickable area of the model
- #### getCanvasTextMiniMapLocation

```
public static [Point](Point.html "class in net.runelite.api") getCanvasTextMiniMapLocation​(@Nonnull
[Client](Client.html "interface in net.runelite.api") client,
@Nonnull
[Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
@Nonnull
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") localLocation,
@Nonnull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)
```

Calculates text position and centers on minimap depending on string length.

Parameters:
`client` - the game client
`graphics` - the game graphics
`localLocation` - local location of the tile
`text` - string for width measurement
Returns:
a [`Point`](Point.html "class in net.runelite.api") on screen corresponding to the given
localLocation.