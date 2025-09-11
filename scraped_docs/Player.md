# Player (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Player.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Player

* All Implemented Interfaces:
`[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class Player
extends java.lang.Object
```

Represents a player (such as yourself, or another player)

See Also:
[`Query.players()`](../query/Query.html#players())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Player.OverheadIcon](Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")` | |
| `static class` | `[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")` | |

- ### Nested classes/interfaces inherited from interface org.tribot.script.sdk.interfaces.[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")

`[Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")`
- ### Nested classes/interfaces inherited from interface org.tribot.script.sdk.interfaces.[Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces")

`[Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `int` | `[getAnimation](#getAnimation())()` | Gets the character's current animation |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the character. |
| `java.util.List<java.lang.Integer>` | `[getEffects](#getEffects())()` | Gets the IDs representing the current effects applied to the player, or empty if none exist. |
| `java.util.List<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getEquipment](#getEquipment())()` | Gets the player's equipped items. |
| `java.util.Optional<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getEquippedItem](#getEquippedItem(org.tribot.script.sdk.Equipment.Slot))​([Equipment.Slot](../Equipment.Slot.html "enum in org.tribot.script.sdk") slot)` | Gets the item equipped in the specific slot. |
| `double` | `[getHealthBarPercent](#getHealthBarPercent())()` | Gets the current percent of the health bar that is green |
| `java.util.List<[Hitsplat](Hitsplat.html "class in org.tribot.script.sdk.types")>` | `[getHitsplats](#getHitsplats())()` | Gets the hitsplats currently displayed on this character |
| `int` | `[getIndex](#getIndex())()` | Gets the index of the entity. |
| `java.util.Optional<[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")>` | `[getInteractingCharacter](#getInteractingCharacter())()` | Gets the Character that this character is interacting with (attacking, following, etc). |
| `java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")>` | `[getModel](#getModel())()` | Gets the entity model |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |
| `java.util.Optional<[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")>` | `[getNextTile](#getNextTile())()` | Gets the next tile this character will be at, if it is moving |
| `[Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")` | `[getOrientation](#getOrientation())()` | Gets the orientation of this entity |
| `java.util.Optional<[Player.OverheadIcon](Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")>` | `[getOverheadIcon](#getOverheadIcon())()` | Gets the overhead icon on this player, such as protect from melee |
| `java.lang.String` | `[getOverheadMessage](#getOverheadMessage())()` | Gets the message displayed above this character, such as a public chat message |
| `java.util.Optional<[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")>` | `[getSkullIcon](#getSkullIcon())()` | Gets the skull icon above this player |
| `int` | `[getSpotAnimation](#getSpotAnimation())()` | Gets the ID representing the current spot animation of the player, or -1 if the player is not performing a
spot animation. |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |
| `java.util.Optional<[Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>` | `[getWalkingDirection](#getWalkingDirection())()` | Gets the direction this character is walking |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[isFacing](#isFacing(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Determines if this character is facing a given position. |
| `boolean` | `[isHealthBarVisible](#isHealthBarVisible())()` | Determines if the health bar interface is appearing over this character's head. |
| `boolean` | `[isInteracting](#isInteracting())()` | Determines if this character is interacting with any another character. |
| `boolean` | `[isInteractingWithMe](#isInteractingWithMe())()` | Determines if this character is interacting with the player. |
| `boolean` | `[isInteractingWithObject](#isInteractingWithObject(org.tribot.script.sdk.types.GameObject))​([GameObject](GameObject.html "class in org.tribot.script.sdk.types") object)` | Determines if an object is being interacted with by the player |
| `boolean` | `[isMoving](#isMoving())()` | Determines if the character is moving or not. |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `java.util.Optional<[Hiscores.Player](../Hiscores.Player.html "class in org.tribot.script.sdk")>` | `[lookupStats](#lookupStats())()` | Gets the stats of this player by checking the highscores. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")

`[isAnimating](../interfaces/Character.html#isAnimating()), [isHovering](../interfaces/Character.html#isHovering())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")

`[interact](../interfaces/Interactable.html#interact(java.lang.String)), [interact](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[distance](../interfaces/Positionable.html#distance()), [distanceTo](../interfaces/Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable))`

* + ### Method Detail

- #### getName

```
public java.lang.String getName()
```

Description copied from interface: `[Named](../interfaces/Named.html#getName())`
Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Returns:
The name of the entity
- #### getCombatLevel

```
public int getCombatLevel()
```

Description copied from interface: `[Character](../interfaces/Character.html#getCombatLevel())`
Gets the combat level of the character.
- #### getSkullIcon

```
public java.util.Optional<[Player.SkullIcon](Player.SkullIcon.html "enum in org.tribot.script.sdk.types")> getSkullIcon()
```

Gets the skull icon above this player

Returns:
the skull icon, or an empty optional if none
- #### getOverheadIcon

```
public java.util.Optional<[Player.OverheadIcon](Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")> getOverheadIcon()
```

Gets the overhead icon on this player, such as protect from melee

Returns:
the player's overhead icon, or an empty optional if none
- #### getEquipment

```
public java.util.List<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getEquipment()
```

Gets the player's equipped items. Note that due to how the game works, some items that aren't visible aren't sent to the client by the server such as rings.

Returns:
the player's equipped items
- #### getEquippedItem

```
public java.util.Optional<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getEquippedItem​([Equipment.Slot](../Equipment.Slot.html "enum in org.tribot.script.sdk") slot)
```

Gets the item equipped in the specific slot. Note that due to how the game works, some items that aren't visible aren't sent to the client by the server such as rings.

Parameters:
`slot` - the equipment slot
Returns:
the item in the specific slot
- #### lookupStats

```
public java.util.Optional<[Hiscores.Player](../Hiscores.Player.html "class in org.tribot.script.sdk")> lookupStats()
```

Gets the stats of this player by checking the highscores. Note this makes an http request and could take a few seconds.

Returns:
the player's stats
See Also:
[`Hiscores.lookup(String)`](../Hiscores.html#lookup(java.lang.String))
- #### getSpotAnimation

```
public int getSpotAnimation()
```

Gets the ID representing the current spot animation of the player, or -1 if the player is not performing a
spot animation.

Spot animations are usually animations done in place when no regular animation is being performed.

Returns:
The ID of the spot animation being performed or -1 if no animation is being performed.
- #### isInteractingWithObject

```
public boolean isInteractingWithObject​([GameObject](GameObject.html "class in org.tribot.script.sdk.types") object)
```

Determines if an object is being interacted with by the player
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
- #### getTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#getTile())`
Gets the WorldTile of this entity/position

Specified by:
`[getTile](../interfaces/Positionable.html#getTile())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
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