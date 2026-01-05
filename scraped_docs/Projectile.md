# Projectile (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Projectile.html

**Package:** Packagenet.runelite.api

**Description:** This value indicates how much arc the projectile can have. Projectiles
 with larger slopes have a more noticeable arc when thrown....

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface Projectile
extends [Renderable](Renderable.html "interface in net.runelite.api")
```

Represents a projectile entity. (ie. cannonball, arrow)

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `[Animation](Animation.html "interface in net.runelite.api")` | `[getAnimation](#getAnimation())()` | The animation of the projectile |
| `int` | `[getAnimationFrame](#getAnimationFrame())()` | The frame of the current animation |
| `int` | `[getEndCycle](#getEndCycle())()` | Gets the game cycle that the projectile will reach its target at. |
| `int` | `[getEndHeight](#getEndHeight())()` | Gets the ending height of the projectile. |
| `int` | `[getFloor](#getFloor())()` | Deprecated. |
| `int` | `[getHeight](#getHeight())()` | Deprecated. |
| `int` | `[getId](#getId())()` | Gets the ID of the projectile. |
| `default [Actor](Actor.html "interface in net.runelite.api")` | `[getInteracting](#getInteracting())()` | Deprecated. |
| `int` | `[getOrientation](#getOrientation())()` | Get the projectile orientation in JAU |
| `int` | `[getRemainingCycles](#getRemainingCycles())()` | Gets the remaining game cycles until the projectile reaches its
target and despawns. |
| `int` | `[getSlope](#getSlope())()` | Gets the slope of the projectile. |
| `[Actor](Actor.html "interface in net.runelite.api")` | `[getSourceActor](#getSourceActor())()` | Get the actor the projectile starts at. |
| `int` | `[getSourceLevel](#getSourceLevel())()` | Get the level the projectile starts on. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getSourcePoint](#getSourcePoint())()` | Get the point the projectile starts at. |
| `int` | `[getStartCycle](#getStartCycle())()` | Gets the game cycle that the projectile begun movement at. |
| `int` | `[getStartHeight](#getStartHeight())()` | Gets the starting height of the projectile. |
| `int` | `[getStartPos](#getStartPos())()` | Get the offset position from the start position where the projectile starts |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getTarget](#getTarget())()` | Deprecated. |
| `[Actor](Actor.html "interface in net.runelite.api")` | `[getTargetActor](#getTargetActor())()` | Get the actor the projectile ends at. |
| `int` | `[getTargetLevel](#getTargetLevel())()` | Get the level the projectile ends on. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getTargetPoint](#getTargetPoint())()` | Get the point the projectile ends at. |
| `double` | `[getX](#getX())()` | Gets the current x-axis coordinate of the projectile. |
| `int` | `[getX1](#getX1())()` | Deprecated. |
| `double` | `[getY](#getY())()` | Gets the current y-axis coordinate of the projectile. |
| `int` | `[getY1](#getY1())()` | Deprecated. |
| `double` | `[getZ](#getZ())()` | Gets the current z-axis coordinate of the projectile. |
| `void` | `[setEndCycle](#setEndCycle(int))​(int cycle)` | Sets the game cycle the projectile will reach its target at. |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getId

```
int getId()
```

Gets the ID of the projectile.

Returns:
the projectile ID
See Also:
`SpotanimID`
- #### getSourceLevel

```
int getSourceLevel()
```

Get the level the projectile starts on.

Returns:
- #### getSourcePoint

```
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getSourcePoint()
```

Get the point the projectile starts at.

Returns:
- #### getSourceActor

```
@Nullable
[Actor](Actor.html "interface in net.runelite.api") getSourceActor()
```

Get the actor the projectile starts at.

Returns:
- #### getTargetLevel

```
int getTargetLevel()
```

Get the level the projectile ends on.

Returns:
- #### getTargetPoint

```
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getTargetPoint()
```

Get the point the projectile ends at.

Returns:
- #### getTargetActor

```
@Nullable
[Actor](Actor.html "interface in net.runelite.api") getTargetActor()
```

Get the actor the projectile ends at.

Returns:
- #### getInteracting

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
default [Actor](Actor.html "interface in net.runelite.api") getInteracting()
```

Deprecated.
Gets the actor that is targeted by this projectile.

Returns:
the target actor, or null if this projectile is an AoE attack
- #### getTarget

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getTarget()
```

Deprecated.
Get the target point of the projectile. For projectiles with an actor target,
this is updated each frame to the actor position.

Returns:
- #### getX1

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getX1()
```

Deprecated.
Gets the original x-axis coordinate that this projectile started from.

Returns:
the original coordinate
- #### getY1

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getY1()
```

Deprecated.
Gets the original y-axis coordinate that this projectile started from.

Returns:
the original coordinate
- #### getFloor

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getFloor()
```

Deprecated.
Gets the plane that the projectile is on.

Returns:
the plane
- #### getHeight

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getHeight()
```

Deprecated.
Gets the height of the projectile.

Returns:
the height
- #### getEndHeight

```
int getEndHeight()
```

Gets the ending height of the projectile.

Returns:
the ending height
- #### getStartCycle

```
int getStartCycle()
```

Gets the game cycle that the projectile begun movement at.

Returns:
the start game cycle
- #### getEndCycle

```
int getEndCycle()
```

Gets the game cycle that the projectile will reach its target at.

Returns:
the end game cycle
- #### setEndCycle

```
void setEndCycle​(int cycle)
```

Sets the game cycle the projectile will reach its target at. The
projectile automatically despawns after this time, and setting the
end cycle to a time in the past is an effective way of removing the
projectile.

Parameters:
`cycle` -
- #### getRemainingCycles

```
int getRemainingCycles()
```

Gets the remaining game cycles until the projectile reaches its
target and despawns.

Returns:
the remaining game cycles
- #### getSlope

```
int getSlope()
```

Gets the slope of the projectile.

This value indicates how much arc the projectile can have. Projectiles
with larger slopes have a more noticeable arc when thrown.

Returns:
the slope of the projectile
- #### getStartPos

```
int getStartPos()
```

Get the offset position from the start position where the projectile starts

Returns:
- #### getStartHeight

```
int getStartHeight()
```

Gets the starting height of the projectile.

Returns:
the starting height
- #### getX

```
double getX()
```

Gets the current x-axis coordinate of the projectile.

Returns:
the x-axis coordinate
- #### getY

```
double getY()
```

Gets the current y-axis coordinate of the projectile.

Returns:
the y-axis coordinate
- #### getZ

```
double getZ()
```

Gets the current z-axis coordinate of the projectile.

Returns:
the z-axis coordinate
- #### getOrientation

```
int getOrientation()
```

Get the projectile orientation in JAU

Returns:
- #### getAnimation

```
@Nullable
[Animation](Animation.html "interface in net.runelite.api") getAnimation()
```

The animation of the projectile

Returns:
- #### getAnimationFrame

```
int getAnimationFrame()
```

The frame of the current animation

Returns: