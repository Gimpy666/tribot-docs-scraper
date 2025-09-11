# Interactable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Interactable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Superinterfaces:
`[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")`

All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`, `[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types")`

---

```
public interface Interactable
extends [Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces"), [Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents an "interactable" entity. This is an entity that is both positionable (has a position), and clickable.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default boolean` | `[interact](#interact(java.lang.String))​(java.lang.String action)` | Attempts to interact with the entity using the given action. |
| `default boolean` | `[interact](#interact(java.lang.String,java.util.function.BooleanSupplier))​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)` | Attempts to interact with the entity using the given action. |

- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[click](Clickable.html#click()), [click](Clickable.html#click(java.lang.String)), [hover](Clickable.html#hover()), [hover](Clickable.html#hover(java.lang.String)), [hoverMenu](Clickable.html#hoverMenu(java.lang.String)), [isHovering](Clickable.html#isHovering()), [isVisible](Clickable.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[adjustCameraTo](Positionable.html#adjustCameraTo()), [distance](Positionable.html#distance()), [distanceTo](Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable)), [getTile](Positionable.html#getTile())`

* + ### Method Detail

- #### interact

```
default boolean interact​(java.lang.String action)
```

Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
Returns:
True if the entity was clicked, false otherwise
- #### interact

```
default boolean interact​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)
```

Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
`interruptCondition` - a condition to interrupt the interaction attempt - if this condition is ever true, when checked, the interaction attempt with return early with a result of false
Returns:
True if the entity was clicked, false otherwise