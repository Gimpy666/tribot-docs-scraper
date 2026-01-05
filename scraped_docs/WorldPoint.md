# WorldPoint (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/coords/WorldPoint.html

**Package:** Packagenet.runelite.api.coords

**Description:** WorldPoints are immutable. Methods that modify the properties create a new
 instance....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.coords.WorldPoint

* ---

```
public final class WorldPoint
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A three-dimensional point representing the coordinate of a Tile.

WorldPoints are immutable. Methods that modify the properties create a new
instance.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[WorldPoint](#%3Cinit%3E(int,int,int))​(int x,
int y,
int plane)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `int` | `[distanceTo](#distanceTo(net.runelite.api.coords.WorldArea))​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Gets the shortest distance from this point to a WorldArea. |
| `int` | `[distanceTo](#distanceTo(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Gets the distance between this point and another. |
| `int` | `[distanceTo2D](#distanceTo2D(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Find the distance from this point to another point. |
| `[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[dx](#dx(int))​(int dx)` | Offsets the x-axis coordinate by the passed value. |
| `[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[dy](#dy(int))​(int dy)` | Offsets the y-axis coordinate by the passed value. |
| `[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[dz](#dz(int))​(int dz)` | Offsets the plane by the passed value. |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromCoord](#fromCoord(int))​(int c)` | Create a WorldPoint from a packed Jagex coordinate |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocal](#fromLocal(net.runelite.api.Client,int,int,int))​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y,
int plane)` | Deprecated. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocal](#fromLocal(net.runelite.api.Client,net.runelite.api.coords.LocalPoint))​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") local)` | Gets the coordinate of the tile that contains the passed local point. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocal](#fromLocal(net.runelite.api.Scene,int,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y,
int plane)` | Gets the coordinate of the tile that contains the passed local point. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocal](#fromLocal(net.runelite.api.WorldView,int,int,int))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y,
int plane)` | Gets the coordinate of the tile that contains the passed local point. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocalInstance](#fromLocalInstance(net.runelite.api.Client,net.runelite.api.coords.LocalPoint))​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint)` | Gets the coordinate of the tile that contains the passed local point,
accounting for instances. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocalInstance](#fromLocalInstance(net.runelite.api.Client,net.runelite.api.coords.LocalPoint,int))​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint,
int plane)` | Gets the coordinate of the tile that contains the passed local point,
accounting for instances. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromLocalInstance](#fromLocalInstance(net.runelite.api.Scene,net.runelite.api.coords.LocalPoint,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint,
int plane)` | Gets the coordinate of the tile that contains the passed local point,
accounting for instances. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromRegion](#fromRegion(int,int,int,int))​(int regionId,
int regionX,
int regionY,
int plane)` | Converts the passed region ID and coordinates to a world coordinate |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(net.runelite.api.Client,int,int,int))​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y,
int plane)` | Deprecated. |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(net.runelite.api.Scene,int,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y,
int plane)` | Converts the passed scene coordinates to a world space |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(net.runelite.api.WorldView,int,int,int))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y,
int plane)` | Converts the passed scene coordinates to a world space |
| `static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[getMirrorPoint](#getMirrorPoint(net.runelite.api.coords.WorldPoint,boolean))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint,
boolean toOverworld)` | Translate a coordinate either between overworld and real, or real and overworld |
| `int` | `[getPlane](#getPlane())()` | The plane level of the Tile, also referred as z-axis coordinate. |
| `int` | `[getRegionID](#getRegionID())()` | Gets the ID of the region containing this tile. |
| `int` | `[getRegionX](#getRegionX())()` | Gets the X-axis coordinate of the region coordinate |
| `int` | `[getRegionY](#getRegionY())()` | Gets the Y-axis coordinate of the region coordinate |
| `int` | `[getX](#getX())()` | X-axis coordinate. |
| `int` | `[getY](#getY())()` | Y-axis coordinate. |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isInArea](#isInArea(net.runelite.api.coords.WorldArea...))​([WorldArea](WorldArea.html "class in net.runelite.api.coords")... worldAreas)` | Checks whether this tile is located within any of the given areas. |
| `boolean` | `[isInArea2D](#isInArea2D(net.runelite.api.coords.WorldArea...))​([WorldArea](WorldArea.html "class in net.runelite.api.coords")... worldAreas)` | Checks whether this tile is located within any of the given areas, disregarding any plane differences. |
| `boolean` | `[isInScene](#isInScene(net.runelite.api.Client))​([Client](../Client.html "interface in net.runelite.api") client)` | Deprecated. |
| `static boolean` | `[isInScene](#isInScene(net.runelite.api.Client,int,int))​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y)` | Deprecated. |
| `static boolean` | `[isInScene](#isInScene(net.runelite.api.Scene,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y)` | Checks whether a tile is located in the current scene. |
| `static boolean` | `[isInScene](#isInScene(net.runelite.api.WorldView,int,int))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y)` | Checks whether a tile is located in the current scene. |
| `static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")>` | `[toLocalInstance](#toLocalInstance(net.runelite.api.Client,net.runelite.api.coords.WorldPoint))​([Client](../Client.html "interface in net.runelite.api") client,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Deprecated. |
| `static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")>` | `[toLocalInstance](#toLocalInstance(net.runelite.api.Scene,net.runelite.api.coords.WorldPoint))​([Scene](../Scene.html "interface in net.runelite.api") scene,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Deprecated. |
| `static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")>` | `[toLocalInstance](#toLocalInstance(net.runelite.api.WorldView,net.runelite.api.coords.WorldPoint))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Get occurrences of a tile on the scene, accounting for instances. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |
| `[WorldArea](WorldArea.html "class in net.runelite.api.coords")` | `[toWorldArea](#toWorldArea())()` | Retrieves an area consisting of only this point. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### WorldPoint

```
public WorldPoint​(int x,
int y,
int plane)
```

+ ### Method Detail

- #### dx

```
public [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") dx​(int dx)
```

Offsets the x-axis coordinate by the passed value.

Parameters:
`dx` - the offset
Returns:
new instance
- #### dy

```
public [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") dy​(int dy)
```

Offsets the y-axis coordinate by the passed value.

Parameters:
`dy` - the offset
Returns:
new instance
- #### dz

```
public [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") dz​(int dz)
```

Offsets the plane by the passed value.

Parameters:
`dz` - the offset
Returns:
new instance
- #### isInScene

```
public static boolean isInScene​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y)
```

Checks whether a tile is located in the current scene.

Parameters:
`scene` - the scene
`x` - the tiles x coordinate
`y` - the tiles y coordinate
Returns:
true if the tile is in the scene, false otherwise
- #### isInScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static boolean isInScene​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y)
```

Deprecated.
Checks whether a tile is located in the current scene.

Parameters:
`client` - the client
`x` - the tiles x coordinate
`y` - the tiles y coordinate
Returns:
true if the tile is in the scene, false otherwise
- #### isInScene

```
public static boolean isInScene​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y)
```

Checks whether a tile is located in the current scene.

Parameters:
`wv` - the client
`x` - the tiles x coordinate
`y` - the tiles y coordinate
Returns:
true if the tile is in the scene, false otherwise
- #### isInScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public boolean isInScene​([Client](../Client.html "interface in net.runelite.api") client)
```

Deprecated.
Checks whether this tile is located in the current scene.

Parameters:
`client` - the client
Returns:
true if this tile is in the scene, false otherwise
- #### fromLocal

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocal​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") local)
```

Gets the coordinate of the tile that contains the passed local point.

Parameters:
`client` - the client
`local` - the local coordinate
Returns:
the tile coordinate containing the local point
- #### fromLocal

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocal​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y,
int plane)
```

Gets the coordinate of the tile that contains the passed local point.

Parameters:
`wv` - the scene
`x` - the local x-axis coordinate
`y` - the local x-axis coordinate
`plane` - the plane
Returns:
the tile coordinate containing the local point
- #### fromLocal

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocal​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y,
int plane)
```

Gets the coordinate of the tile that contains the passed local point.

Parameters:
`scene` - the scene
`x` - the local x-axis coordinate
`y` - the local x-axis coordinate
`plane` - the plane
Returns:
the tile coordinate containing the local point
- #### fromLocal

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocal​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y,
int plane)
```

Deprecated.
Gets the coordinate of the tile that contains the passed local point.

Parameters:
`client` - the client
`x` - the local x-axis coordinate
`y` - the local x-axis coordinate
`plane` - the plane
Returns:
the tile coordinate containing the local point
- #### fromLocalInstance

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocalInstance​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint)
```

Gets the coordinate of the tile that contains the passed local point,
accounting for instances.

Parameters:
`client` - the client
`localPoint` - the local coordinate
Returns:
the tile coordinate containing the local point
- #### fromLocalInstance

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocalInstance​([Client](../Client.html "interface in net.runelite.api") client,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint,
int plane)
```

Gets the coordinate of the tile that contains the passed local point,
accounting for instances.

Parameters:
`client` - the client
`localPoint` - the local coordinate
`plane` - the plane the localpoint is on
Returns:
the tile coordinate containing the local point
- #### fromLocalInstance

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromLocalInstance​([Scene](../Scene.html "interface in net.runelite.api") scene,
[LocalPoint](LocalPoint.html "class in net.runelite.api.coords") localPoint,
int plane)
```

Gets the coordinate of the tile that contains the passed local point,
accounting for instances.

Parameters:
`scene` - the scene
`localPoint` - the local coordinate
`plane` - the plane for the returned point, if it is not an instance
Returns:
the tile coordinate containing the local point
- #### toLocalInstance

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> toLocalInstance​([Client](../Client.html "interface in net.runelite.api") client,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Deprecated.
Get occurrences of a tile on the scene, accounting for instances. There may be
more than one if the same template chunk occurs more than once on the scene.
- #### toLocalInstance

```
public static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> toLocalInstance​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Get occurrences of a tile on the scene, accounting for instances. There may be
more than one if the same template chunk occurs more than once on the scene.
- #### toLocalInstance

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> toLocalInstance​([Scene](../Scene.html "interface in net.runelite.api") scene,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Deprecated.
Get occurrences of a tile on the scene, accounting for instances. There may be
more than one if the same template chunk occurs more than once on the scene.
- #### distanceTo

```
public int distanceTo​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Gets the shortest distance from this point to a WorldArea.

Parameters:
`other` - the world area
Returns:
the shortest distance
- #### distanceTo

```
public int distanceTo​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Gets the distance between this point and another.

If the other point is not on the same plane, this method will return
[`Integer.MAX_VALUE`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true#MAX_VALUE "class or interface in java.lang"). If ignoring the plane is wanted, use the
[`distanceTo2D(WorldPoint)`](#distanceTo2D(net.runelite.api.coords.WorldPoint)) method.

Parameters:
`other` - other point
Returns:
the distance
- #### distanceTo2D

```
public int distanceTo2D​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Find the distance from this point to another point.

This method disregards the plane value of the two tiles and returns
the simple distance between the X-Z coordinate pairs.

Parameters:
`other` - other point
Returns:
the distance
- #### fromScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromScene​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y,
int plane)
```

Deprecated.
- #### fromScene

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromScene​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y,
int plane)
```

Converts the passed scene coordinates to a world space
- #### fromScene

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromScene​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y,
int plane)
```

Converts the passed scene coordinates to a world space
- #### getRegionID

```
public int getRegionID()
```

Gets the ID of the region containing this tile.

Returns:
the region ID
- #### fromRegion

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromRegion​(int regionId,
int regionX,
int regionY,
int plane)
```

Converts the passed region ID and coordinates to a world coordinate
- #### getRegionX

```
public int getRegionX()
```

Gets the X-axis coordinate of the region coordinate
- #### getRegionY

```
public int getRegionY()
```

Gets the Y-axis coordinate of the region coordinate
- #### getMirrorPoint

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") getMirrorPoint​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint,
boolean toOverworld)
```

Translate a coordinate either between overworld and real, or real and overworld

Parameters:
`worldPoint` -
`toOverworld` - whether to convert to overworld coordinates, or to real coordinates
Returns:
- #### isInArea

```
public boolean isInArea​([WorldArea](WorldArea.html "class in net.runelite.api.coords")... worldAreas)
```

Checks whether this tile is located within any of the given areas.

Parameters:
`worldAreas` - areas to check within
Returns:
`true` if any area contains this point, `false` otherwise.
- #### isInArea2D

```
public boolean isInArea2D​([WorldArea](WorldArea.html "class in net.runelite.api.coords")... worldAreas)
```

Checks whether this tile is located within any of the given areas, disregarding any plane differences.

Parameters:
`worldAreas` - areas to check within
Returns:
`true` if any area contains this point, `false` otherwise.
- #### toWorldArea

```
public [WorldArea](WorldArea.html "class in net.runelite.api.coords") toWorldArea()
```

Retrieves an area consisting of only this point.

Returns:
A [`WorldArea`](WorldArea.html "class in net.runelite.api.coords") of width and height 1, encompassing only this point.
- #### fromCoord

```
public static [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") fromCoord​(int c)
```

Create a WorldPoint from a packed Jagex coordinate
- #### getX

```
public int getX()
```

X-axis coordinate.
- #### getY

```
public int getY()
```

Y-axis coordinate.
- #### getPlane

```
public int getPlane()
```

The plane level of the Tile, also referred as z-axis coordinate.
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`