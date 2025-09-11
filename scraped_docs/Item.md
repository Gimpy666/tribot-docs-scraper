# Item (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Item.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Superinterfaces:
`[Actionable](Actionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Identifiable](Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces")`, `[ItemDefinable](ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Stackable](Stackable.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface Item
extends [Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces"), [Named](Named.html "interface in org.tribot.script.sdk.interfaces"), [Identifiable](Identifiable.html "interface in org.tribot.script.sdk.interfaces"), [Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces"), [Stackable](Stackable.html "interface in org.tribot.script.sdk.interfaces"), [ItemDefinable](ItemDefinable.html "interface in org.tribot.script.sdk.interfaces"), [Actionable](Actionable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents an item, such as an inventory item.

See Also:
[`to find items`](../query/Query.html "interface in org.tribot.script.sdk.query")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |
| `java.util.Optional<java.awt.Rectangle>` | `[getBounds](#getBounds())()` | Gets the bounds of the area |
| `default java.lang.String` | `[getName](#getName())()` | Gets the name of the Item. |
| `default boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `default java.util.Optional<java.lang.Integer>` | `[lookupPrice](#lookupPrice())()` | Looks up the price of the given itemId. |

- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[click](Clickable.html#click()), [click](Clickable.html#click(java.lang.String)), [hover](Clickable.html#hover()), [hover](Clickable.html#hover(java.lang.String)), [hoverMenu](Clickable.html#hoverMenu(java.lang.String)), [isVisible](Clickable.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Identifiable](Identifiable.html "interface in org.tribot.script.sdk.interfaces")

`[getId](Identifiable.html#getId())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Indexable](Indexable.html "interface in org.tribot.script.sdk.interfaces")

`[getIndex](Indexable.html#getIndex())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[ItemDefinable](ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")

`[getDefinition](ItemDefinable.html#getDefinition())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Stackable](Stackable.html "interface in org.tribot.script.sdk.interfaces")

`[getStack](Stackable.html#getStack())`

* + ### Method Detail

- #### getBounds

```
java.util.Optional<java.awt.Rectangle> getBounds()
```

Gets the bounds of the area

Returns:
the bounds of the area
- #### getName

```
default java.lang.String getName()
```

Gets the name of the Item.

Specified by:
`[getName](Named.html#getName())` in interface `[Named](Named.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The name of the entity
- #### lookupPrice

```
default java.util.Optional<java.lang.Integer> lookupPrice()
```

Looks up the price of the given itemId. Works on noted items.

Returns:
The price of the item. If the item is not found or cannot be looked up, empty Optional.
- #### getActions

```
default java.util.List<java.lang.String> getActions()
```

Gets the available actions for the entity, usually dependent on their definition.
Note this will attempt to provide the actions for the specific item type.
For example, if this is an equipment item it will provide the equipment actions.
To always get the general actions see {@link this#getDefinition()}.

Specified by:
`[getActions](Actionable.html#getActions())` in interface `[Actionable](Actionable.html "interface in org.tribot.script.sdk.interfaces")`
See Also:
[`ItemDefinition.getActions()`](../types/definitions/ItemDefinition.html#getActions())
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