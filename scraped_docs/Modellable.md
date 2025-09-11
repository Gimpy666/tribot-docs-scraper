# Modellable (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Modellable.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Known Subinterfaces:
`[Character](Character.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[GameObject](../types/GameObject.html "class in org.tribot.script.sdk.types")`, `[GroundItem](../types/GroundItem.html "class in org.tribot.script.sdk.types")`, `[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")`, `[Player](../types/Player.html "class in org.tribot.script.sdk.types")`, `[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types")`

---

```
public interface Modellable
```

An entity with a model

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `java.util.Optional<[Model](../types/Model.html "class in org.tribot.script.sdk.types")>` | `[getModel](#getModel())()` | Gets the entity model |

* + ### Method Detail

- #### getModel

```
java.util.Optional<[Model](../types/Model.html "class in org.tribot.script.sdk.types")> getModel()
```

Gets the entity model

Returns:
the entity model, or an empty optional if the model could not be obtained (ex. not visible on screen)