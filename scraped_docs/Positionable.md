# Positionable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Positionable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GraphicObject](../types/GraphicObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`, `[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types")`, `[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types")`

---

```
public interface Positionable
```

Represents an entity with a location on the game map

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `default int` | `[distance](#distance())()` | Determines the distance between this entity/tile and the local player |
| `default int` | `[distanceTo](#distanceTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Determines the distance between this entity/tile and the given entity/tile |
| `[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |

* + ### Method Detail

- #### getTile

```
[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Gets the WorldTile of this entity/position
- #### adjustCameraTo

```
boolean adjustCameraTo()
```

Moves the camera to a position where the given entity or position is in view. Takes into account distance.
Uses an algorithm to move both the angle and rotation of the camera simultaneously at pseudo-random intervals
to simulate human camera movement.

Returns:
True if the camera moved. False otherwise.
- #### distanceTo

```
default int distanceTo​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Determines the distance between this entity/tile and the given entity/tile
- #### distance

```
default int distance()
```

Determines the distance between this entity/tile and the local player