# DaxWalkerAdapter (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/adapter/DaxWalkerAdapter.html

**Package:** Packageorg.tribot.script.sdk.walking.adapter

---

* java.lang.Object
* + org.tribot.script.sdk.walking.adapter.DaxWalkerAdapter

* All Implemented Interfaces:
`[GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")`

---

```
public class DaxWalkerAdapter
extends java.lang.Object
implements [GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")
```

A walking adapter for using dax walker.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[DaxWalkerAdapter.Teleport](DaxWalkerAdapter.Teleport.html "enum in org.tribot.script.sdk.walking.adapter")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[DaxWalkerAdapter](#%3Cinit%3E(java.lang.String,java.lang.String))​(java.lang.String publicKey,
java.lang.String secretKey)` | Creates a new DaxWalkerAdapter |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `void` | `[setGlobalWalkingCondition](#setGlobalWalkingCondition(java.util.function.Supplier))​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> globalWalkingCondition)` | Sets the global walking condition. |
| `void` | `[setMoveCosts](#setMoveCosts(int))​(int moveCost)` | |
| `boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Walks to the specified position |
| `boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Walks to the specified position |
| `boolean` | `[walkToBank](#walkToBank())()` | Attempts to walk to the nearest bank |
| `boolean` | `[walkToBank](#walkToBank(java.util.function.Supplier))​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Attempts to walk to the nearest bank |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### DaxWalkerAdapter

```
public DaxWalkerAdapter​(java.lang.String publicKey,
java.lang.String secretKey)
```

Creates a new DaxWalkerAdapter

Parameters:
`publicKey` - the dax walker public api key
`secretKey` - the dax walker secret api key

+ ### Method Detail

- #### walkTo

```
public boolean walkTo​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Description copied from interface: `[GlobalWalkerAdapter](GlobalWalkerAdapter.html#walkTo(org.tribot.script.sdk.interfaces.Positionable))`
Walks to the specified position

Specified by:
`[walkTo](GlobalWalkerAdapter.html#walkTo(org.tribot.script.sdk.interfaces.Positionable))` in interface `[GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")`
Parameters:
`position` - the position to walk to
Returns:
true if walked successfully, false otherwise
- #### walkTo

```
public boolean walkTo​([Positionable](../../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Description copied from interface: `[GlobalWalkerAdapter](GlobalWalkerAdapter.html#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))`
Walks to the specified position

Specified by:
`[walkTo](GlobalWalkerAdapter.html#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))` in interface `[GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")`
Parameters:
`position` - the position to walk to
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
public boolean walkToBank()
```

Description copied from interface: `[GlobalWalkerAdapter](GlobalWalkerAdapter.html#walkToBank())`
Attempts to walk to the nearest bank

Specified by:
`[walkToBank](GlobalWalkerAdapter.html#walkToBank())` in interface `[GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")`
Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
public boolean walkToBank​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Description copied from interface: `[GlobalWalkerAdapter](GlobalWalkerAdapter.html#walkToBank(java.util.function.Supplier))`
Attempts to walk to the nearest bank

Specified by:
`[walkToBank](GlobalWalkerAdapter.html#walkToBank(java.util.function.Supplier))` in interface `[GlobalWalkerAdapter](GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter")`
Parameters:
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise
- #### setMoveCosts

```
public void setMoveCosts​(int moveCost)
```
- #### setGlobalWalkingCondition

```
public void setGlobalWalkingCondition​(java.util.function.Supplier<[WalkState](../WalkState.html "enum in org.tribot.script.sdk.walking")> globalWalkingCondition)
```

Sets the global walking condition. This is checked every time when walking with dax walker.

Parameters:
`globalWalkingCondition` - the walking condition