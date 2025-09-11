# Identifiable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Identifiable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GraphicObject](../types/GraphicObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[NpcDefinition](../types/definitions/NpcDefinition.html "class in org.tribot.script.sdk.types.definitions")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface Identifiable
```

Represents anything with an in-game ID

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |

* + ### Method Detail

- #### getId

```
int getId()
```

Gets the ID of the entity