# ItemDefinable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/ItemDefinable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface ItemDefinable
```

An entity that has an item definition

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")` | `[getDefinition](#getDefinition())()` | Gets the ItemDefinition for this item, which contains more details about the item. |

* + ### Method Detail

- #### getDefinition

```
[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions") getDefinition()
```

Gets the ItemDefinition for this item, which contains more details about the item.