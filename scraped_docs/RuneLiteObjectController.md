# RuneLiteObjectController (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/RuneLiteObjectController.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.RuneLiteObjectController

* Direct Known Subclasses:
`[RuneLiteObject](RuneLiteObject.html "class in net.runelite.api")`

---

```
public abstract class RuneLiteObjectController
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[RuneLiteObjectController](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getLevel](#getLevel())()` | |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocation](#getLocation())()` | |
| `abstract [Model](Model.html "interface in net.runelite.api")` | `[getModel](#getModel())()` | Called every frame to get a model to render. |
| `int` | `[getOrientation](#getOrientation())()` | The object orientation |
| `int` | `[getRadius](#getRadius())()` | The radius is offset from the object position to form a 2d rectangle, and the tiles
the corners are in are used to determine the min and max scene x/y the object is on. |
| `int` | `[getWorldView](#getWorldView())()` | |
| `int` | `[getX](#getX())()` | |
| `int` | `[getY](#getY())()` | |
| `int` | `[getZ](#getZ())()` | |
| `boolean` | `[isDrawFrontTilesFirst](#isDrawFrontTilesFirst())()` | If true, the rectangle computed from the radius has 1 or 2 of its sides expanded by a full tile based on the
orientation the object is facing. |
| `void` | `[setDrawFrontTilesFirst](#setDrawFrontTilesFirst(boolean))​(boolean drawFrontTilesFirst)` | If true, the rectangle computed from the radius has 1 or 2 of its sides expanded by a full tile based on the
orientation the object is facing. |
| `void` | `[setLevel](#setLevel(int))​(int level)` | |
| `void` | `[setLocation](#setLocation(net.runelite.api.coords.LocalPoint,int))​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int level)` | Sets the location in the scene for the RuneLiteObjectController |
| `void` | `[setOrientation](#setOrientation(int))​(int orientation)` | The object orientation |
| `void` | `[setRadius](#setRadius(int))​(int radius)` | The radius is offset from the object position to form a 2d rectangle, and the tiles
the corners are in are used to determine the min and max scene x/y the object is on. |
| `void` | `[setWorldView](#setWorldView(int))​(int worldView)` | |
| `void` | `[setX](#setX(int))​(int x)` | |
| `void` | `[setY](#setY(int))​(int y)` | |
| `void` | `[setZ](#setZ(int))​(int z)` | |
| `void` | `[tick](#tick(int))​(int ticksSinceLastFrame)` | Called every frame the RuneLiteObject is registered and in the scene |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### RuneLiteObjectController

```
public RuneLiteObjectController()
```

+ ### Method Detail

- #### setLocation

```
public void setLocation​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int level)
```

Sets the location in the scene for the RuneLiteObjectController
- #### getLocation

```
public [LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocation()
```
- #### tick

```
public void tick​(int ticksSinceLastFrame)
```

Called every frame the RuneLiteObject is registered and in the scene

Parameters:
`ticksSinceLastFrame` - The number of client ticks since the last frame
- #### getModel

```
public abstract [Model](Model.html "interface in net.runelite.api") getModel()
```

Called every frame to get a model to render. The returned model is not modified and
can be a shared model.
- #### getX

```
public int getX()
```
- #### getY

```
public int getY()
```
- #### getZ

```
public int getZ()
```
- #### getWorldView

```
public int getWorldView()
```
- #### getLevel

```
public int getLevel()
```
- #### getRadius

```
public int getRadius()
```

The radius is offset from the object position to form a 2d rectangle, and the tiles
the corners are in are used to determine the min and max scene x/y the object is on. These tiles are then drawn
first prior to the object being drawn, so that the object renders correctly over top of each tile.
The default radius is 60, marginally less than 128/2, which works well for models the size of a single tile.
- #### isDrawFrontTilesFirst

```
public boolean isDrawFrontTilesFirst()
```

If true, the rectangle computed from the radius has 1 or 2 of its sides expanded by a full tile based on the
orientation the object is facing. This causes the tiles the object is facing to be drawn first, even if the
radius of the object would not place the object on that tile.
The default is false.
- #### getOrientation

```
public int getOrientation()
```

The object orientation

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### setX

```
public void setX​(int x)
```
- #### setY

```
public void setY​(int y)
```
- #### setZ

```
public void setZ​(int z)
```
- #### setWorldView

```
public void setWorldView​(int worldView)
```
- #### setLevel

```
public void setLevel​(int level)
```
- #### setRadius

```
public void setRadius​(int radius)
```

The radius is offset from the object position to form a 2d rectangle, and the tiles
the corners are in are used to determine the min and max scene x/y the object is on. These tiles are then drawn
first prior to the object being drawn, so that the object renders correctly over top of each tile.
The default radius is 60, marginally less than 128/2, which works well for models the size of a single tile.
- #### setDrawFrontTilesFirst

```
public void setDrawFrontTilesFirst​(boolean drawFrontTilesFirst)
```

If true, the rectangle computed from the radius has 1 or 2 of its sides expanded by a full tile based on the
orientation the object is facing. This causes the tiles the object is facing to be drawn first, even if the
radius of the object would not place the object on that tile.
The default is false.
- #### setOrientation

```
public void setOrientation​(int orientation)
```

The object orientation

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")