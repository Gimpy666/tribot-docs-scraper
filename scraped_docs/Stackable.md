# Stackable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Stackable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface Stackable
```

Represents a stackable entity (an entity that has a stack)

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getStack](#getStack())()` | Gets the stack of this item, which is how many of the item is occupying the item space. |

* + ### Method Detail

- #### getStack

```
int getStack()
```

Gets the stack of this item, which is how many of the item is occupying the item space.