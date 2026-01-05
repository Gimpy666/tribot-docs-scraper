# WorldArea (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/coords/WorldArea.html

**Package:** Packagenet.runelite.api.coords

**Description:** Melee distance is exactly 1 tile, so this method computes and returns
 whether the shortest distance to the passed area is directly
 on the outside of this areas edge....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.coords.WorldArea

* ---

```
public class WorldArea
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Represents an area on the world.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[WorldArea](#%3Cinit%3E(int,int,int,int,int))​(int x,
int y,
int width,
int height,
int plane)` | |
| `[WorldArea](#%3Cinit%3E(net.runelite.api.coords.WorldPoint,int,int))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") location,
int width,
int height)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[canTravelInDirection](#canTravelInDirection(net.runelite.api.WorldView,int,int))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int dx,
int dy)` | Determines if the area can travel in one of the 9 directions
by using the standard collision detection algorithm. |
| `boolean` | `[canTravelInDirection](#canTravelInDirection(net.runelite.api.WorldView,int,int,java.util.function.Predicate))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int dx,
int dy,
[Predicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Predicate.html?is-external=true "class or interface in java.util.function")<? super [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> extraCondition)` | Determines if the area can travel in one of the 9 directions
by using the standard collision detection algorithm. |
| `boolean` | `[contains](#contains(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Checks whether a tile is contained within the area and in the same plane. |
| `boolean` | `[contains2D](#contains2D(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Checks whether a tile is contained within the area while ignoring the plane. |
| `int` | `[distanceTo](#distanceTo(net.runelite.api.coords.WorldArea))​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Computes the shortest distance to another area. |
| `int` | `[distanceTo](#distanceTo(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Computes the shortest distance to a world coordinate. |
| `int` | `[distanceTo2D](#distanceTo2D(net.runelite.api.coords.WorldArea))​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Computes the shortest distance to another area while ignoring the plane. |
| `int` | `[distanceTo2D](#distanceTo2D(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Computes the shortest distance to a world coordinate. |
| `int` | `[getHeight](#getHeight())()` | The height of the area. |
| `int` | `[getPlane](#getPlane())()` | The plane the area is on. |
| `int` | `[getWidth](#getWidth())()` | The width of the area. |
| `int` | `[getX](#getX())()` | The western most point of the area. |
| `int` | `[getY](#getY())()` | The southern most point of the area. |
| `boolean` | `[hasLineOfSightTo](#hasLineOfSightTo(net.runelite.api.WorldView,net.runelite.api.coords.WorldArea))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Determine if this WorldArea has line of sight to another WorldArea. |
| `boolean` | `[hasLineOfSightTo](#hasLineOfSightTo(net.runelite.api.WorldView,net.runelite.api.coords.WorldPoint))​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Determine if this WorldArea has line of sight to another WorldArea. |
| `boolean` | `[intersectsWith](#intersectsWith(net.runelite.api.coords.WorldArea))​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Checks whether this area intersects with another. |
| `boolean` | `[isInMeleeDistance](#isInMeleeDistance(net.runelite.api.coords.WorldArea))​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)` | Checks whether this area is within melee distance of another. |
| `boolean` | `[isInMeleeDistance](#isInMeleeDistance(net.runelite.api.coords.WorldPoint))​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)` | Checks whether a coordinate is within melee distance of this area. |
| `[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")` | `[toWorldPoint](#toWorldPoint())()` | Retrieves the southwestern most point of this WorldArea. |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")>` | `[toWorldPointList](#toWorldPointList())()` | Accumulates all the WorldPoints that this WorldArea contains and returns them as a list |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### WorldArea

```
public WorldArea​(int x,
int y,
int width,
int height,
int plane)
```
- #### WorldArea

```
public WorldArea​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") location,
int width,
int height)
```

+ ### Method Detail

- #### distanceTo

```
public int distanceTo​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Computes the shortest distance to another area.

Parameters:
`other` - the passed area
Returns:
the distance, or [`Integer.MAX_VALUE`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true#MAX_VALUE "class or interface in java.lang") if the planes differ
- #### distanceTo

```
public int distanceTo​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Computes the shortest distance to a world coordinate.

Parameters:
`other` - the passed coordinate
Returns:
the distance, or [`Integer.MAX_VALUE`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html?is-external=true#MAX_VALUE "class or interface in java.lang") if the planes differ
- #### distanceTo2D

```
public int distanceTo2D​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Computes the shortest distance to another area while ignoring the plane.

Parameters:
`other` - the passed area
Returns:
the distance
- #### distanceTo2D

```
public int distanceTo2D​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Computes the shortest distance to a world coordinate.

Parameters:
`other` - the passed coordinate
Returns:
the distance
- #### contains

```
public boolean contains​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Checks whether a tile is contained within the area and in the same plane.

Returns:
`true` if the tile is contained within the bounds of this area, `false` otherwise.
- #### contains2D

```
public boolean contains2D​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Checks whether a tile is contained within the area while ignoring the plane.

Returns:
`true` if the tile is contained within the bounds of this area regardless of plane, `false` otherwise.
- #### isInMeleeDistance

```
public boolean isInMeleeDistance​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Checks whether this area is within melee distance of another.

Melee distance is exactly 1 tile, so this method computes and returns
whether the shortest distance to the passed area is directly
on the outside of this areas edge.

Parameters:
`other` - the other area
Returns:
true if in melee distance, false otherwise
- #### isInMeleeDistance

```
public boolean isInMeleeDistance​([WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Checks whether a coordinate is within melee distance of this area.

Parameters:
`other` - the coordinate
Returns:
true if in melee distance, false otherwise
See Also:
[`isInMeleeDistance(WorldArea)`](#isInMeleeDistance(net.runelite.api.coords.WorldArea))
- #### intersectsWith

```
public boolean intersectsWith​([WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Checks whether this area intersects with another.

Parameters:
`other` - the other area
Returns:
true if the areas intersect, false otherwise
- #### canTravelInDirection

```
public boolean canTravelInDirection​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int dx,
int dy)
```

Determines if the area can travel in one of the 9 directions
by using the standard collision detection algorithm.

Note that this method does not consider other actors as
a collision, but most non-boss NPCs do check for collision
with some actors. For actor collision checking, use the
[`canTravelInDirection(WorldView, int, int, Predicate)`](#canTravelInDirection(net.runelite.api.WorldView,int,int,java.util.function.Predicate)) method.

Parameters:
`dx` - the x-axis direction to travel (-1, 0, or 1)
`dy` - the y-axis direction to travel (-1, 0, or 1)
Returns:
true if the area can travel in the specified direction
- #### canTravelInDirection

```
public boolean canTravelInDirection​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
int dx,
int dy,
[Predicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Predicate.html?is-external=true "class or interface in java.util.function")<? super [WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> extraCondition)
```

Determines if the area can travel in one of the 9 directions
by using the standard collision detection algorithm.

The passed x and y axis directions indicate the direction to
travel in.

Note that this method does not normally consider other actors
as a collision, but most non-boss NPCs do check for collision
with some actors. However, using the `extraCondition` param
it is possible to implement this check manually.

Parameters:
`dx` - the x-axis direction to travel (-1, 0, or 1)
`dy` - the y-axis direction to travel (-1, 0, or 1)
`extraCondition` - an additional condition to perform when checking valid tiles,
such as performing a check for un-passable actors
Returns:
true if the area can travel in the specified direction
- #### hasLineOfSightTo

```
public boolean hasLineOfSightTo​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldArea](WorldArea.html "class in net.runelite.api.coords") other)
```

Determine if this WorldArea has line of sight to another WorldArea.

Note that the reverse isn't necessarily true, meaning this can return true
while the other WorldArea does not have line of sight to this WorldArea.

Parameters:
`other` - The other WorldArea to compare with
Returns:
Returns true if this WorldArea has line of sight to the other
- #### hasLineOfSightTo

```
public boolean hasLineOfSightTo​([WorldView](../WorldView.html "interface in net.runelite.api") wv,
[WorldPoint](WorldPoint.html "class in net.runelite.api.coords") other)
```

Determine if this WorldArea has line of sight to another WorldArea.

Note that the reverse isn't necessarily true, meaning this can return true
while the other WorldArea does not have line of sight to this WorldArea.

Parameters:
`other` - The other WorldPoint to compare with
Returns:
Returns true if this WorldPoint has line of sight to the WorldPoint
- #### toWorldPoint

```
public [WorldPoint](WorldPoint.html "class in net.runelite.api.coords") toWorldPoint()
```

Retrieves the southwestern most point of this WorldArea.

Returns:
Returns the southwestern most WorldPoint in the area
- #### toWorldPointList

```
public [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WorldPoint](WorldPoint.html "class in net.runelite.api.coords")> toWorldPointList()
```

Accumulates all the WorldPoints that this WorldArea contains and returns them as a list

Returns:
Returns the WorldPoints in this WorldArea
- #### getX

```
public int getX()
```

The western most point of the area.
- #### getY

```
public int getY()
```

The southern most point of the area.
- #### getWidth

```
public int getWidth()
```

The width of the area.
- #### getHeight

```
public int getHeight()
```

The height of the area.
- #### getPlane

```
public int getPlane()
```

The plane the area is on.