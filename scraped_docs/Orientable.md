# Orientable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Orientable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`

---

```
public interface Orientable
```

Represents an entity with an orientation

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Interface | Description |
| `static class` | `[Orientable.Orientation](Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")` | Represents the orientation of an entity |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Orientable.Orientation](Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")` | `[getOrientation](#getOrientation())()` | Gets the orientation of this entity |

* + ### Method Detail

- #### getOrientation

```
[Orientable.Orientation](Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces") getOrientation()
```

Gets the orientation of this entity

Returns:
the orientation