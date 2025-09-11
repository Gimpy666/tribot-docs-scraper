# Clickable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Clickable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`, `[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`, `[Widget](../types/Widget.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`, `[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types")`

---

```
public interface Clickable
```

Represents something that can be clicked, such as an in-game entity (object, npc, player) or interface entity (item,
interface).

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `default boolean` | `[hover](#hover(java.lang.String))​(java.lang.String action)` | Hovers the specified action on this entity. |
| `default boolean` | `[hoverMenu](#hoverMenu(java.lang.String))​(java.lang.String action)` | Hovers the specified action on this entity, always right-clicking and hovering over the menu |
| `boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |

* + ### Method Detail

- #### click

```
boolean click()
```

Interacts with the entity, with the first action available. This will generally perform a left-click, unless there is an action blocking in which case it will right click.

Returns:
true if the entity was clicked, false otherwise
- #### click

```
boolean click​(java.lang.String action)
```

Interacts with the entity, given a specific action. The "action" string is the part of the option that comes first.
For example, to attack an NPC, the action is "Attack". Case insensitive.

Returns:
If the entity was successfully clicked
- #### hover

```
boolean hover()
```

Moves the mouse to a human-randomized point on the entity.

Returns:
If the mouse successfully moved over the entity
- #### isVisible

```
boolean isVisible()
```

Determines if the entity is on the screen and able to be clicked.
- #### isHovering

```
boolean isHovering()
```

Checks if the mouse is currently over this entity

Returns:
true if the mouse if over this entity, false otherwise
- #### hover

```
default boolean hover​(java.lang.String action)
```

Hovers the specified action on this entity. This will right-click if it has to in order to hover the correct option.

Parameters:
`action` - the action to hover
Returns:
true if hovered successfully, false otherwise
- #### hoverMenu

```
default boolean hoverMenu​(java.lang.String action)
```

Hovers the specified action on this entity, always right-clicking and hovering over the menu

Parameters:
`action` - the action to hover
Returns:
true if hovered successfully, false otherwise