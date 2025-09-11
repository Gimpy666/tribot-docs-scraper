# Projectile (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Projectile.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Projectile

* All Implemented Interfaces:
`[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class Projectile
extends java.lang.Object
implements [Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces"), [Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents a projectile in the air, such as an arrow or a spell

See Also:
[`Query.projectiles()`](../query/Query.html#projectiles())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getDestination](#getDestination())()` | Gets the expected destination tile of this projectile. |
| `int` | `[getGraphicId](#getGraphicId())()` | |
| `org.tribot.api2007.types.RSProjectile` | `[getLegacyProjectile](#getLegacyProjectile())()` | |
| `java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")>` | `[getModel](#getModel())()` | Gets the entity model |
| `int` | `[getOrientation](#getOrientation())()` | |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getStart](#getStart())()` | Gets the start tile of this projectile |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isMoving](#isMoving())()` | |
| `boolean` | `[isTargetingMe](#isTargetingMe())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[distance](../interfaces/Positionable.html#distance()), [distanceTo](../interfaces/Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable))`

* + ### Method Detail

- #### getLegacyProjectile

```
public org.tribot.api2007.types.RSProjectile getLegacyProjectile()
```
- #### getOrientation

```
public int getOrientation()
```
- #### getGraphicId

```
public int getGraphicId()
```
- #### isMoving

```
public boolean isMoving()
```
- #### isTargetingMe

```
public boolean isTargetingMe()
```
- #### getTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#getTile())`
Gets the WorldTile of this entity/position

Specified by:
`[getTile](../interfaces/Positionable.html#getTile())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getStart

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getStart()
```

Gets the start tile of this projectile

Returns:
the start tile of this projectile
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### getDestination

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getDestination()
```

Gets the expected destination tile of this projectile. For AoE attacks, this will generally be some tile.
For projectiles targeting a player or NPC, this will generally be the position of that target.

Returns:
the expected destination tile of this projectile
- #### adjustCameraTo

```
public boolean adjustCameraTo()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#adjustCameraTo())`
Moves the camera to a position where the given entity or position is in view. Takes into account distance.
Uses an algorithm to move both the angle and rotation of the camera simultaneously at pseudo-random intervals
to simulate human camera movement.

Specified by:
`[adjustCameraTo](../interfaces/Positionable.html#adjustCameraTo())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the camera moved. False otherwise.
- #### getModel

```
public java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")> getModel()
```

Description copied from interface: `[Modellable](../interfaces/Modellable.html#getModel())`
Gets the entity model

Specified by:
`[getModel](../interfaces/Modellable.html#getModel())` in interface `[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the entity model, or an empty optional if the model could not be obtained (ex. not visible on screen)
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`