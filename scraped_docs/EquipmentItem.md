# EquipmentItem (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/EquipmentItem.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.EquipmentItem

* All Implemented Interfaces:
`[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`, `[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")`, `[ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class EquipmentItem
extends java.lang.Object
implements [Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")
```

Represents an equipped item

See Also:
[`Query.equipment()`](../query/Query.html#equipment())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |
| `java.util.Optional<java.awt.Rectangle>` | `[getBounds](#getBounds())()` | Gets the bounds of the area |
| `[ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")` | `[getDefinition](#getDefinition())()` | Gets the ItemDefinition for this item, which contains more details about the item. |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |
| `int` | `[getIndex](#getIndex())()` | Gets the index of the entity. |
| `[Equipment.Slot](../Equipment.Slot.html "enum in org.tribot.script.sdk")` | `[getSlot](#getSlot())()` | Gets the equipment slot of this item |
| `int` | `[getStack](#getStack())()` | Gets the stack of this item, which is how many of the item is occupying the item space. |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `boolean` | `[remove](#remove())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")

`[getName](../interfaces/Item.html#getName()), [isHovering](../interfaces/Item.html#isHovering()), [lookupPrice](../interfaces/Item.html#lookupPrice())`

* + ### Method Detail

- #### getId

```
public int getId()
```

Description copied from interface: `[Identifiable](../interfaces/Identifiable.html#getId())`
Gets the ID of the entity

Specified by:
`[getId](../interfaces/Identifiable.html#getId())` in interface `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getDefinition

```
public [ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions") getDefinition()
```

Description copied from interface: `[ItemDefinable](../interfaces/ItemDefinable.html#getDefinition())`
Gets the ItemDefinition for this item, which contains more details about the item.

Specified by:
`[getDefinition](../interfaces/ItemDefinable.html#getDefinition())` in interface `[ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getStack

```
public int getStack()
```

Description copied from interface: `[Stackable](../interfaces/Stackable.html#getStack())`
Gets the stack of this item, which is how many of the item is occupying the item space.

Specified by:
`[getStack](../interfaces/Stackable.html#getStack())` in interface `[Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getIndex

```
public int getIndex()
```

Description copied from interface: `[Indexable](../interfaces/Indexable.html#getIndex())`
Gets the index of the entity.

Specified by:
`[getIndex](../interfaces/Indexable.html#getIndex())` in interface `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getSlot

```
public [Equipment.Slot](../Equipment.Slot.html "enum in org.tribot.script.sdk") getSlot()
```

Gets the equipment slot of this item

Returns:
this item's equipment slot
- #### remove

```
public boolean remove()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`
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
- #### getBounds

```
public java.util.Optional<java.awt.Rectangle> getBounds()
```

Description copied from interface: `[Item](../interfaces/Item.html#getBounds())`
Gets the bounds of the area

Specified by:
`[getBounds](../interfaces/Item.html#getBounds())` in interface `[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the bounds of the area
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```

Description copied from interface: `[Item](../interfaces/Item.html#getActions())`
Gets the available actions for the entity, usually dependent on their definition.
Note this will attempt to provide the actions for the specific item type.
For example, if this is an equipment item it will provide the equipment actions.
To always get the general actions see {@link this#getDefinition()}.

Specified by:
`[getActions](../interfaces/Actionable.html#getActions())` in interface `[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`
Specified by:
`[getActions](../interfaces/Item.html#getActions())` in interface `[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")`
See Also:
[`ItemDefinition.getActions()`](definitions/ItemDefinition.html#getActions())