# Named (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Named.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`, `[Item](Item.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[EquipmentItem](../types/EquipmentItem.html "class in org.tribot.script.sdk.types")`, `[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[InventoryItem](../types/InventoryItem.html "class in org.tribot.script.sdk.types")`, `[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[NpcDefinition](../types/definitions/NpcDefinition.html "class in org.tribot.script.sdk.types.definitions")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`, `[WidgetItem](../types/WidgetItem.html "class in org.tribot.script.sdk.types")`

---

```
public interface Named
```

Represents something with an in-game name

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |

* + ### Method Detail

- #### getName

```
java.lang.String getName()
```

Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Returns:
The name of the entity