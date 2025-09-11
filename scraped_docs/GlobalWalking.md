# GlobalWalking (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/GlobalWalking.html

**Package:** Packageorg.tribot.script.sdk.walking

---

* java.lang.Object
* + org.tribot.script.sdk.walking.GlobalWalking

* ---

```
public class GlobalWalking
extends java.lang.Object
```

Utilities for walking across the entire game

See Also:
[`for walking short distances`](LocalWalking.html "class in org.tribot.script.sdk.walking")

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[GlobalWalking](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[setEngine](#setEngine(org.tribot.script.sdk.walking.adapter.GlobalWalkerAdapter))​([GlobalWalkerAdapter](adapter/GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter") adapter)` | Sets the walker engine adapter |
| `static boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Walks to the specified position |
| `static boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Walks to the specified position |
| `static boolean` | `[walkToBank](#walkToBank())()` | Attempts to walk to the nearest bank |
| `static boolean` | `[walkToBank](#walkToBank(java.util.function.Supplier))​(java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)` | Attempts to walk to the nearest bank |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### GlobalWalking

```
public GlobalWalking()
```

+ ### Method Detail

- #### setEngine

```
public static void setEngine​([GlobalWalkerAdapter](adapter/GlobalWalkerAdapter.html "interface in org.tribot.script.sdk.walking.adapter") adapter)
```

Sets the walker engine adapter

Parameters:
`adapter` - the walking engine adapter
See Also:
[`DaxWalkerAdapter`](adapter/DaxWalkerAdapter.html "class in org.tribot.script.sdk.walking.adapter")
- #### walkTo

```
public static boolean walkTo​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Walks to the specified position

Parameters:
`position` - the position to walk to
Returns:
true if walked successfully, false otherwise
- #### walkTo

```
public static boolean walkTo​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Walks to the specified position

Parameters:
`position` - the position to walk to
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
public static boolean walkToBank()
```

Attempts to walk to the nearest bank

Returns:
true if walked successfully, false otherwise
- #### walkToBank

```
public static boolean walkToBank​(java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkCondition)
```

Attempts to walk to the nearest bank

Parameters:
`walkCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise