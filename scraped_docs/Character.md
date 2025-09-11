# Character (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Character.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Superinterfaces:
`[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Modellable](Modellable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Orientable](Orientable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`

---

```
public interface Character
extends [Modellable](Modellable.html "interface in org.tribot.script.sdk.interfaces"), [Named](Named.html "interface in org.tribot.script.sdk.interfaces"), [Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces"), [Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces"), [Orientable](Orientable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents a player or npc entity

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Interface | Description |
| `static class` | `[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")` | |

- ### Nested classes/interfaces inherited from interface org.tribot.script.sdk.interfaces.[Orientable](Orientable.html "interface in org.tribot.script.sdk.interfaces")

`[Orientable.Orientation](Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")`

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `int` | `[getAnimation](#getAnimation())()` | Gets the character's current animation |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the character. |
| `java.util.List<java.lang.Integer>` | `[getEffects](#getEffects())()` | Gets the IDs representing the current effects applied to the player, or empty if none exist. |
| `double` | `[getHealthBarPercent](#getHealthBarPercent())()` | Gets the current percent of the health bar that is green |
| `java.util.List<[Hitsplat](../types/Hitsplat.html "class in org.tribot.script.sdk.types")>` | `[getHitsplats](#getHitsplats())()` | Gets the hitsplats currently displayed on this character |
| `java.util.Optional<[Character](Character.html "interface in org.tribot.script.sdk.interfaces")>` | `[getInteractingCharacter](#getInteractingCharacter())()` | Gets the Character that this character is interacting with (attacking, following, etc). |
| `java.util.Optional<[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")>` | `[getNextTile](#getNextTile())()` | Gets the next tile this character will be at, if it is moving |
| `java.util.Optional<[Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")>` | `[getOverheadIcon](#getOverheadIcon())()` | |
| `java.lang.String` | `[getOverheadMessage](#getOverheadMessage())()` | Gets the message displayed above this character, such as a public chat message |
| `java.util.Optional<[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>` | `[getWalkingDirection](#getWalkingDirection())()` | Gets the direction this character is walking |
| `default boolean` | `[isAnimating](#isAnimating())()` | Checks if the character is currently animating |
| `boolean` | `[isFacing](#isFacing(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Determines if this character is facing a given position. |
| `boolean` | `[isHealthBarVisible](#isHealthBarVisible())()` | Determines if the health bar interface is appearing over this character's head. |
| `default boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `boolean` | `[isInteracting](#isInteracting())()` | Determines if this character is interacting with any another character. |
| `boolean` | `[isInteractingWithMe](#isInteractingWithMe())()` | Determines if this character is interacting with the player. |
| `boolean` | `[isMoving](#isMoving())()` | Determines if the character is moving or not. |

- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[click](Clickable.html#click()), [click](Clickable.html#click(java.lang.String)), [hover](Clickable.html#hover()), [hover](Clickable.html#hover(java.lang.String)), [hoverMenu](Clickable.html#hoverMenu(java.lang.String)), [isVisible](Clickable.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces")

`[getIndex](Indexable.html#getIndex())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")

`[interact](Interactable.html#interact(java.lang.String)), [interact](Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Modellable](Modellable.html "interface in org.tribot.script.sdk.interfaces")

`[getModel](Modellable.html#getModel())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Named](Named.html "interface in org.tribot.script.sdk.interfaces")

`[getName](Named.html#getName())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Orientable](Orientable.html "interface in org.tribot.script.sdk.interfaces")

`[getOrientation](Orientable.html#getOrientation())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[adjustCameraTo](Positionable.html#adjustCameraTo()), [distance](Positionable.html#distance()), [distanceTo](Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable)), [getTile](Positionable.html#getTile())`

* + ### Method Detail

- #### getCombatLevel

```
int getCombatLevel()
```

Gets the combat level of the character.
- #### isMoving

```
boolean isMoving()
```

Determines if the character is moving or not.

Returns:
True if moving. False otherwise.
- #### isHealthBarVisible

```
boolean isHealthBarVisible()
```

Determines if the health bar interface is appearing over this character's head. This bar usually appears when a
character takes a hit that could damage them, and disappears after a few seconds of not taking such a hit.

Returns:
True if the bar is visible. False otherwise.
- #### getHealthBarPercent

```
double getHealthBarPercent()
```

Gets the current percent of the health bar that is green

Returns:
the current percent of the health bar that is green, or 1 if the health bar isn't visible
- #### isInteracting

```
boolean isInteracting()
```

Determines if this character is interacting with any another character. Includes interaction with a character not
in the loaded region.

Returns:
True if interacting with another character. False otherwise.
- #### isInteractingWithMe

```
boolean isInteractingWithMe()
```

Determines if this character is interacting with the player.
- #### getInteractingCharacter

```
java.util.Optional<[Character](Character.html "interface in org.tribot.script.sdk.interfaces")> getInteractingCharacter()
```

Gets the Character that this character is interacting with (attacking, following, etc). Does NOT return characters
that are not in the loaded region, even if this character is interacting with them.

Returns:
The character that is being interacted with. Empty optional if this character is not interacting with another.
- #### isFacing

```
boolean isFacing​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Determines if this character is facing a given position.

Parameters:
`position` - The position to check if this character is facing.
Returns:
True if the character is facing the position. False otherwise.
- #### getAnimation

```
int getAnimation()
```

Gets the character's current animation

Returns:
the character's current animation
- #### getNextTile

```
java.util.Optional<[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")> getNextTile()
```

Gets the next tile this character will be at, if it is moving

Returns:
the next tile this character will be at, if it is moving
- #### getOverheadMessage

```
java.lang.String getOverheadMessage()
```

Gets the message displayed above this character, such as a public chat message

Returns:
the message displayed above this character
- #### getWalkingDirection

```
java.util.Optional<[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")> getWalkingDirection()
```

Gets the direction this character is walking

Returns:
the direction this character is walking, or an empty optional if not walking
- #### getHitsplats

```
java.util.List<[Hitsplat](../types/Hitsplat.html "class in org.tribot.script.sdk.types")> getHitsplats()
```

Gets the hitsplats currently displayed on this character

Returns:
the hitsplats on this character
- #### getOverheadIcon

```
java.util.Optional<[Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")> getOverheadIcon()
```
- #### getEffects

```
java.util.List<java.lang.Integer> getEffects()
```

Gets the IDs representing the current effects applied to the player, or empty if none exist.
- #### isAnimating

```
default boolean isAnimating()
```

Checks if the character is currently animating

Returns:
true if the character is animating, false otherwise
- #### isHovering

```
default boolean isHovering()
```

Description copied from interface: `[Clickable](Clickable.html#isHovering())`
Checks if the mouse is currently over this entity

Specified by:
`[isHovering](Clickable.html#isHovering())` in interface `[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the mouse if over this entity, false otherwise