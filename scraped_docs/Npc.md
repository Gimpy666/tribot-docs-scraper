# Npc (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Npc.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Npc

* All Implemented Interfaces:
`[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class Npc
extends java.lang.Object
implements [Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces"), [Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents a non-player-character

See Also:
[`Query.npcs()`](../query/Query.html#npcs())

* + ### Nested Class Summary

- ### Nested classes/interfaces inherited from interface org.tribot.script.sdk.interfaces.[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")

`[Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")`
- ### Nested classes/interfaces inherited from interface org.tribot.script.sdk.interfaces.[Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces")

`[Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")`

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Npc](#%3Cinit%3E(org.tribot.api2007.types.RSNPC))​(org.tribot.api2007.types.RSNPC npc)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |
| `int` | `[getAnimation](#getAnimation())()` | Gets the character's current animation |
| `[Area](Area.html "class in org.tribot.script.sdk.types")` | `[getArea](#getArea())()` | Gets the area that this npc occupies. |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the character. |
| `java.util.List<java.lang.Integer>` | `[getEffects](#getEffects())()` | Gets the IDs representing the current effects applied to the player, or empty if none exist. |
| `double` | `[getHealthBarPercent](#getHealthBarPercent())()` | Gets the current percent of the health bar that is green |
| `java.util.List<[Hitsplat](Hitsplat.html "class in org.tribot.script.sdk.types")>` | `[getHitsplats](#getHitsplats())()` | Gets the hitsplats currently displayed on this character |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |
| `int` | `[getIndex](#getIndex())()` | Gets the index of the entity. |
| `java.util.Optional<[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")>` | `[getInteractingCharacter](#getInteractingCharacter())()` | Gets the Character that this character is interacting with (attacking, following, etc). |
| `java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")>` | `[getModel](#getModel())()` | Gets the entity model |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |
| `java.util.Optional<[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")>` | `[getNextTile](#getNextTile())()` | Gets the next tile this character will be at, if it is moving |
| `[Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")` | `[getOrientation](#getOrientation())()` | Gets the orientation of this entity |
| `java.util.Optional<[Player.OverheadIcon](Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")>` | `[getOverheadIcon](#getOverheadIcon())()` | |
| `java.lang.String` | `[getOverheadMessage](#getOverheadMessage())()` | Gets the message displayed above this character, such as a public chat message |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |
| `java.util.Optional<[Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>` | `[getWalkingDirection](#getWalkingDirection())()` | Gets the direction this character is walking |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[interact](#interact(java.lang.String))​(java.lang.String action)` | Attempts to interact with the entity using the given action. |
| `boolean` | `[interact](#interact(java.lang.String,java.util.function.BooleanSupplier))​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)` | Attempts to interact with the entity using the given action. |
| `boolean` | `[isFacing](#isFacing(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Determines if this character is facing a given position. |
| `boolean` | `[isHealthBarVisible](#isHealthBarVisible())()` | Determines if the health bar interface is appearing over this character's head. |
| `boolean` | `[isInteracting](#isInteracting())()` | Determines if this character is interacting with any another character. |
| `boolean` | `[isInteractingWithMe](#isInteractingWithMe())()` | Determines if this character is interacting with the player. |
| `boolean` | `[isMoving](#isMoving())()` | Determines if the character is moving or not. |
| `boolean` | `[isValid](#isValid())()` | Checks if this npc still exists in the game. |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")

`[isAnimating](../interfaces/Character.html#isAnimating()), [isHovering](../interfaces/Character.html#isHovering())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[distance](../interfaces/Positionable.html#distance()), [distanceTo](../interfaces/Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable))`

* + ### Constructor Detail

- #### Npc

```
public Npc​(org.tribot.api2007.types.RSNPC npc)
```

+ ### Method Detail

- #### getTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#getTile())`
Gets the WorldTile of this entity/position

Specified by:
`[getTile](../interfaces/Positionable.html#getTile())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getOverheadIcon

```
public java.util.Optional<[Player.OverheadIcon](Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")> getOverheadIcon()
```

Specified by:
`[getOverheadIcon](../interfaces/Character.html#getOverheadIcon())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
- #### getName

```
public java.lang.String getName()
```

Description copied from interface: `[Named](../interfaces/Named.html#getName())`
Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Specified by:
`[getName](../interfaces/Named.html#getName())` in interface `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The name of the entity
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```

Description copied from interface: `[Actionable](../interfaces/Actionable.html#getActions())`
Gets the available actions for the entity, usually dependent on their definition.

Specified by:
`[getActions](../interfaces/Actionable.html#getActions())` in interface `[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getId

```
public int getId()
```

Description copied from interface: `[Identifiable](../interfaces/Identifiable.html#getId())`
Gets the ID of the entity

Specified by:
`[getId](../interfaces/Identifiable.html#getId())` in interface `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`
- #### isValid

```
public boolean isValid()
```

Checks if this npc still exists in the game. This can generally be used to check if an npc is dead.

Returns:
true if this npc still exists in the game client, false otherwise
- #### getCombatLevel

```
public int getCombatLevel()
```

Description copied from interface: `[Character](../interfaces/Character.html#getCombatLevel())`
Gets the combat level of the character.

Specified by:
`[getCombatLevel](../interfaces/Character.html#getCombatLevel())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
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
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`
- #### getArea

```
public [Area](Area.html "class in org.tribot.script.sdk.types") getArea()
```

Gets the area that this npc occupies. Every npc in the game takes up a square of tiles.
For normal, single tile npcs, this will be an area that takes up a single tile.
Larger npcs will have larger areas.

Returns:
the area that this npc occupies
- #### interact

```
public boolean interact​(java.lang.String action)
```

Description copied from interface: `[Interactable](../interfaces/Interactable.html#interact(java.lang.String))`
Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Specified by:
`[interact](../interfaces/Interactable.html#interact(java.lang.String))` in interface `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`
Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
Returns:
True if the entity was clicked, false otherwise
- #### interact

```
public boolean interact​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)
```

Description copied from interface: `[Interactable](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Specified by:
`[interact](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))` in interface `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`
Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
`interruptCondition` - a condition to interrupt the interaction attempt - if this condition is ever true, when checked, the interaction attempt with return early with a result of false
Returns:
True if the entity was clicked, false otherwise
- #### getIndex

```
public int getIndex()
```

Description copied from interface: `[Indexable](../interfaces/Indexable.html#getIndex())`
Gets the index of the entity.

Specified by:
`[getIndex](../interfaces/Indexable.html#getIndex())` in interface `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getNextTile

```
public java.util.Optional<[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")> getNextTile()
```

Description copied from interface: `[Character](../interfaces/Character.html#getNextTile())`
Gets the next tile this character will be at, if it is moving

Specified by:
`[getNextTile](../interfaces/Character.html#getNextTile())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the next tile this character will be at, if it is moving
- #### isMoving

```
public boolean isMoving()
```

Description copied from interface: `[Character](../interfaces/Character.html#isMoving())`
Determines if the character is moving or not.

Specified by:
`[isMoving](../interfaces/Character.html#isMoving())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if moving. False otherwise.
- #### isHealthBarVisible

```
public boolean isHealthBarVisible()
```

Description copied from interface: `[Character](../interfaces/Character.html#isHealthBarVisible())`
Determines if the health bar interface is appearing over this character's head. This bar usually appears when a
character takes a hit that could damage them, and disappears after a few seconds of not taking such a hit.

Specified by:
`[isHealthBarVisible](../interfaces/Character.html#isHealthBarVisible())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the bar is visible. False otherwise.
- #### isInteractingWithMe

```
public boolean isInteractingWithMe()
```

Description copied from interface: `[Character](../interfaces/Character.html#isInteractingWithMe())`
Determines if this character is interacting with the player.

Specified by:
`[isInteractingWithMe](../interfaces/Character.html#isInteractingWithMe())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
- #### getInteractingCharacter

```
public java.util.Optional<[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")> getInteractingCharacter()
```

Description copied from interface: `[Character](../interfaces/Character.html#getInteractingCharacter())`
Gets the Character that this character is interacting with (attacking, following, etc). Does NOT return characters
that are not in the loaded region, even if this character is interacting with them.

Specified by:
`[getInteractingCharacter](../interfaces/Character.html#getInteractingCharacter())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The character that is being interacted with. Empty optional if this character is not interacting with another.
- #### isInteracting

```
public boolean isInteracting()
```

Description copied from interface: `[Character](../interfaces/Character.html#isInteracting())`
Determines if this character is interacting with any another character. Includes interaction with a character not
in the loaded region.

Specified by:
`[isInteracting](../interfaces/Character.html#isInteracting())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if interacting with another character. False otherwise.
- #### isFacing

```
public boolean isFacing​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Description copied from interface: `[Character](../interfaces/Character.html#isFacing(org.tribot.script.sdk.interfaces.Positionable))`
Determines if this character is facing a given position.

Specified by:
`[isFacing](../interfaces/Character.html#isFacing(org.tribot.script.sdk.interfaces.Positionable))` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Parameters:
`position` - The position to check if this character is facing.
Returns:
True if the character is facing the position. False otherwise.
- #### click

```
public boolean click​(java.lang.String action)
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click(java.lang.String))`
Interacts with the entity, given a specific action. The "action" string is the part of the option that comes first.
For example, to attack an NPC, the action is "Attack". Case insensitive.

Specified by:
`[click](../interfaces/Clickable.html#click(java.lang.String))` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the entity was successfully clicked
- #### click

```
public boolean click()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click())`
Interacts with the entity, with the first action available. This will generally perform a left-click, unless there is an action blocking in which case it will right click.

Specified by:
`[click](../interfaces/Clickable.html#click())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the entity was clicked, false otherwise
- #### hover

```
public boolean hover()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#hover())`
Moves the mouse to a human-randomized point on the entity.

Specified by:
`[hover](../interfaces/Clickable.html#hover())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the mouse successfully moved over the entity
- #### isVisible

```
public boolean isVisible()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#isVisible())`
Determines if the entity is on the screen and able to be clicked.

Specified by:
`[isVisible](../interfaces/Clickable.html#isVisible())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
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
- #### getAnimation

```
public int getAnimation()
```

Description copied from interface: `[Character](../interfaces/Character.html#getAnimation())`
Gets the character's current animation

Specified by:
`[getAnimation](../interfaces/Character.html#getAnimation())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the character's current animation
- #### getHealthBarPercent

```
public double getHealthBarPercent()
```

Description copied from interface: `[Character](../interfaces/Character.html#getHealthBarPercent())`
Gets the current percent of the health bar that is green

Specified by:
`[getHealthBarPercent](../interfaces/Character.html#getHealthBarPercent())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the current percent of the health bar that is green, or 1 if the health bar isn't visible
- #### getOrientation

```
public [Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces") getOrientation()
```

Description copied from interface: `[Orientable](../interfaces/Orientable.html#getOrientation())`
Gets the orientation of this entity

Specified by:
`[getOrientation](../interfaces/Orientable.html#getOrientation())` in interface `[Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the orientation
- #### getWalkingDirection

```
public java.util.Optional<[Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")> getWalkingDirection()
```

Description copied from interface: `[Character](../interfaces/Character.html#getWalkingDirection())`
Gets the direction this character is walking

Specified by:
`[getWalkingDirection](../interfaces/Character.html#getWalkingDirection())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the direction this character is walking, or an empty optional if not walking
- #### getOverheadMessage

```
public java.lang.String getOverheadMessage()
```

Description copied from interface: `[Character](../interfaces/Character.html#getOverheadMessage())`
Gets the message displayed above this character, such as a public chat message

Specified by:
`[getOverheadMessage](../interfaces/Character.html#getOverheadMessage())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the message displayed above this character
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
- #### getHitsplats

```
public java.util.List<[Hitsplat](Hitsplat.html "class in org.tribot.script.sdk.types")> getHitsplats()
```

Description copied from interface: `[Character](../interfaces/Character.html#getHitsplats())`
Gets the hitsplats currently displayed on this character

Specified by:
`[getHitsplats](../interfaces/Character.html#getHitsplats())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the hitsplats on this character
- #### getEffects

```
public java.util.List<java.lang.Integer> getEffects()
```

Description copied from interface: `[Character](../interfaces/Character.html#getEffects())`
Gets the IDs representing the current effects applied to the player, or empty if none exist.

Specified by:
`[getEffects](../interfaces/Character.html#getEffects())` in interface `[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`