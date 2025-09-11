# Actionable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Actionable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Widget](../types/Widget.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface Actionable
```

Represents an entity whose definition contains "actions" that can be performed on the entity.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |

* + ### Method Detail

- #### getActions

```
java.util.List<java.lang.String> getActions()
```

Gets the available actions for the entity, usually dependent on their definition.