# LocalWalking.Map (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/LocalWalking.Map.html

**Package:** Packageorg.tribot.script.sdk.walking

---

* java.lang.Object
* + org.tribot.script.sdk.walking.LocalWalking.Map

* Enclosing class:
[LocalWalking](LocalWalking.html "class in org.tribot.script.sdk.walking")

---

```
public static class LocalWalking.Map
extends java.lang.Object
```

Represents a mapped area from some source position.
This can be used to check if positions are reachable from the source position, generate paths, and get the path distance.

See Also:
[`LocalWalking.createMap()`](LocalWalking.html#createMap()),
[`LocalWalking.createMap(Positionable)`](LocalWalking.html#createMap(org.tribot.script.sdk.interfaces.Positionable))

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking")` | `[builder](#builder())()` | |
| `boolean` | `[canReach](#canReach(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Checks if the specified position is reachable from the source position |
| `int` | `[getDistance](#getDistance(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Gets the path distance to the specified position |
| `java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")>` | `[getPath](#getPath(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Generates a path to the position. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### canReach

```
public boolean canReach​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Checks if the specified position is reachable from the source position

Parameters:
`position` - the position to check
Returns:
true if the position is reachable, false otherwise
- #### getPath

```
public java.util.List<[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")> getPath​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Generates a path to the position.
This will attempt to generate a path to the closest nearby position to the destination position.

Parameters:
`position` - the position
Returns:
a path to the position, or an empty list if it or a nearby tile is not reachable
- #### getDistance

```
public int getDistance​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Gets the path distance to the specified position

Parameters:
`position` - the position
Returns:
the distance to the specified position, or `Integer.MAX_VALUE` if not reachable
- #### builder

```
public static [LocalWalking.Map.MapBuilder](LocalWalking.Map.MapBuilder.html "class in org.tribot.script.sdk.walking") builder()
```