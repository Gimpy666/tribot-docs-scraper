# LocalPoint (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/coords/LocalPoint.html

**Package:** Packagenet.runelite.api.coords

**Description:** Local points are immutable, however since the local coordinate space moves,
 it is not safe to keep a LocalPoint after a loading zone.The unit of a LocalPoint is 1/128th of a tile....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.coords.LocalPoint

* ---

```
public final class LocalPoint
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A two-dimensional point in the local coordinate space.

Local points are immutable, however since the local coordinate space moves,
it is not safe to keep a LocalPoint after a loading zone.

The unit of a LocalPoint is 1/128th of a tile.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[LocalPoint](#%3Cinit%3E(int,int))​(int x,
int y)` | Deprecated. |
| `[LocalPoint](#%3Cinit%3E(int,int,int))​(int x,
int y,
int worldView)` | |
| `[LocalPoint](#%3Cinit%3E(int,int,net.runelite.api.WorldView))​(int x,
int y,
[WorldView](../WorldView.html "interface in net.runelite.api") wv)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `int` | `[distanceTo](#distanceTo(net.runelite.api.coords.LocalPoint))​([LocalPoint](LocalPoint.html "class in net.runelite.api.coords") other)` | Gets the distance between this point and another. |
| `[LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[dx](#dx(int))​(int dx)` | |
| `[LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[dy](#dy(int))​(int dy)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(int,int))​(int x,
int y)` | Deprecated. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(int,int,net.runelite.api.Scene))​(int x,
int y,
[Scene](../Scene.html "interface in net.runelite.api") scene)` | Gets the coordinate at the center of the passed tile. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromScene](#fromScene(int,int,net.runelite.api.WorldView))​(int x,
int y,
[WorldView](../WorldView.html "interface in net.runelite.api") wv)` | Gets the coordinate at the center of the passed tile. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromWorld](#fromWorld(net.runelite.api.Client,int,int))​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y)` | Deprecated. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromWorld](#fromWorld(net.runelite.api.Client,net.runelite.api.coords.WorldPoint))​([Client](../Client.html "interface in net.runelite.api") client,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") point)` | |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromWorld](#fromWorld(net.runelite.api.Scene,int,int))​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y)` | Gets the local coordinate at the center of the passed tile. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromWorld](#fromWorld(net.runelite.api.WorldView,int,int))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y)` | Gets the local coordinate at the center of the passed tile. |
| `static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[fromWorld](#fromWorld(net.runelite.api.WorldView,net.runelite.api.coords.WorldPoint))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") world)` | Gets the local coordinate at the center of the passed tile. |
| `int` | `[getSceneX](#getSceneX())()` | Gets the x-axis coordinate in scene space (tiles). |
| `int` | `[getSceneY](#getSceneY())()` | Gets the y-axis coordinate in scene space (tiles). |
| `int` | `[getWorldView](#getWorldView())()` | |
| `int` | `[getX](#getX())()` | X and Y axis coordinates. |
| `int` | `[getY](#getY())()` | |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isInScene](#isInScene())()` | Deprecated. |
| `[LocalPoint](LocalPoint.html "class in net.runelite.api.coords")` | `[plus](#plus(int,int))​(int dx,
int dy)` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### LocalPoint

```
public LocalPoint​(int x,
int y,
[WorldView](../WorldView.html "interface in net.runelite.api") wv)
```
- #### LocalPoint

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public LocalPoint​(int x,
int y)
```

Deprecated.
- #### LocalPoint

```
public LocalPoint​(int x,
int y,
int worldView)
```

+ ### Method Detail

- #### fromWorld

```
@Nullable
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromWorld​([Client](../Client.html "interface in net.runelite.api") client,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") point)
```
- #### fromWorld

```
@Nullable
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromWorld​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") world)
```

Gets the local coordinate at the center of the passed tile.

Returns:
coordinate if the tile is in the world view, otherwise null
- #### fromWorld

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
@Nullable
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromWorld​([Client](../Client.html "interface in net.runelite.api") client,
int x,
int y)
```

Deprecated.
- #### fromWorld

```
@Nullable
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromWorld​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int x,
int y)
```

Gets the local coordinate at the center of the passed tile.

Parameters:
`wv` - the scene
`x` - x-axis coordinate of the tile
`y` - y-axis coordinate of the tile
Returns:
coordinate if the tile is in the current scene, otherwise null
- #### fromWorld

```
@Nullable
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromWorld​([Scene](../Scene.html "interface in net.runelite.api") scene,
int x,
int y)
```

Gets the local coordinate at the center of the passed tile.

Parameters:
`scene` - the scene
`x` - x-axis coordinate of the tile
`y` - y-axis coordinate of the tile
Returns:
coordinate if the tile is in the current scene, otherwise null
- #### distanceTo

```
public int distanceTo​([LocalPoint](LocalPoint.html "class in net.runelite.api.coords") other)
```

Gets the distance between this point and another.

Parameters:
`other` - other point
Returns:
the distance
- #### isInScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public boolean isInScene()
```

Deprecated.
Test if this point is in the basic 104x104 tile scene.

Returns:
- #### fromScene

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromScene​(int x,
int y)
```

Deprecated.
Gets the coordinate at the center of the passed tile.

Parameters:
`x` - x-axis coordinate of the tile in Scene coords
`y` - y-axis coordinate of the tile in Scene coords
Returns:
true coordinate of the tile
- #### fromScene

```
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromScene​(int x,
int y,
[Scene](../Scene.html "interface in net.runelite.api") scene)
```

Gets the coordinate at the center of the passed tile.

Parameters:
`x` - x-axis coordinate of the tile in Scene coords
`y` - y-axis coordinate of the tile in Scene coords
`scene` - scene containing the tile
Returns:
true coordinate of the tile
- #### fromScene

```
public static [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") fromScene​(int x,
int y,
[WorldView](../WorldView.html "interface in net.runelite.api") wv)
```

Gets the coordinate at the center of the passed tile.

Parameters:
`x` - x-axis coordinate of the tile in Scene coords
`y` - y-axis coordinate of the tile in Scene coords
`wv` - wv containing the tile
Returns:
true coordinate of the tile
- #### getSceneX

```
public int getSceneX()
```

Gets the x-axis coordinate in scene space (tiles).

Returns:
x-axis coordinate
- #### getSceneY

```
public int getSceneY()
```

Gets the y-axis coordinate in scene space (tiles).

Returns:
y-axis coordinate
- #### dx

```
public [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") dx​(int dx)
```
- #### dy

```
public [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") dy​(int dy)
```
- #### plus

```
public [LocalPoint](LocalPoint.html "class in net.runelite.api.coords") plus​(int dx,
int dy)
```
- #### getX

```
public int getX()
```

X and Y axis coordinates.
- #### getY

```
public int getY()
```
- #### getWorldView

```
public int getWorldView()
```
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