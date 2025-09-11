# GlobalWalkerAdapter (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/adapter/GlobalWalkerAdapter.html

**Package:** Packageorg.tribot.script.sdk.walking.adapter

---

* All Known Implementing Classes:
`[DaxWalkerAdapter](DaxWalkerAdapter.html "class in org.tribot.script.sdk.walking.adapter")`

---

```
public interface GlobalWalkerAdapter
```

Provides a definition for a webwalker that can be set as the engine of the GlobalWalker API

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Walks to the specified position |
| `boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Walks to the specified position |
| `boolean` | `[walkToBank](#walkToBank())()` | Attempts to walk to the nearest bank |
| `boolean` | `[walkToBank](#walkToBank(java.util.function.Supplier))​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Attempts to walk to the nearest bank |

* + ### Method Detail

- #### walkTo

```
boolean walkTo​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Walks to the specified position

Parameters:
`position` - the position to walk to
Returns:
true if walked successfully, false otherwise
- #### walkTo

```
boolean walkTo​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Walks to the specified position

Parameters:
`position` - the position to walk to
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
boolean walkToBank()
```

Attempts to walk to the nearest bank

Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
boolean walkToBank​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Attempts to walk to the nearest bank

Parameters:
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise