# LocalWalking (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/LocalWalking.html

**Package:** Packageorg.tribot.script.sdk.walking

---

* java.lang.Object
* + org.tribot.script.sdk.walking.LocalWalking

* ---

```
public class LocalWalking
extends java.lang.Object
```

Utilities for traversing and inspecting the 'local' area. This is a 104x104 area.

See Also:
[`for walking long distances`](GlobalWalking.html "class in org.tribot.script.sdk.walking")

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking")` | Represents a mapped area from some source position. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[LocalWalking](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking")` | `[createMap](#createMap())()` | Creates a local map with the player position as the source

return a local map |
| `static [LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking")` | `[createMap](#createMap(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)` | Creates a local map with the specified positionable as the source |
| `static boolean` | `[walkPath](#walkPath(java.util.List))​(java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> path)` | Walks the specified path |
| `static boolean` | `[walkPath](#walkPath(java.util.List,java.util.function.Supplier))​(java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> path,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkingCondition)` | Walks the specified path |
| `static boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") target)` | Walks to the target location, if it is in the local area |
| `static boolean` | `[walkTo](#walkTo(org.tribot.script.sdk.interfaces.Positionable,java.util.function.Supplier))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") target,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkingCondition)` | Walks to the target location, if it is in the local area |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### LocalWalking

```
public LocalWalking()
```

+ ### Method Detail

- #### createMap

```
public static [LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking") createMap()
```

Creates a local map with the player position as the source

return a local map
- #### createMap

```
public static [LocalWalking.Map](LocalWalking.Map.html "class in org.tribot.script.sdk.walking") createMap​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)
```

Creates a local map with the specified positionable as the source

Parameters:
`source` - the source of the map - all paths/reachable checks will be performed against this source
Returns:
a local map around the specified source
- #### walkTo

```
public static boolean walkTo​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") target)
```

Walks to the target location, if it is in the local area

Parameters:
`target` - the target tile
Returns:
true if walked successfully, false otherwise
- #### walkTo

```
public static boolean walkTo​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") target,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkingCondition)
```

Walks to the target location, if it is in the local area

Parameters:
`target` - the target tile
`walkingCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise
- #### walkPath

```
public static boolean walkPath​(java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> path)
```

Walks the specified path

Parameters:
`path` - the path to walk
Returns:
true if walked successfully, false otherwise
- #### walkPath

```
public static boolean walkPath​(java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> path,
java.util.function.Supplier<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")> walkingCondition)
```

Walks the specified path

Parameters:
`path` - the path to walk
`walkingCondition` - the walking condition to break out of walking early - this is checked often while walking
Returns:
true if walked successfully, false otherwise