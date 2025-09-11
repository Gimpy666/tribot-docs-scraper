# World (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/World.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.World

* ---

```
public class World
extends java.lang.Object
```

Represents a world in the list of worlds available

See Also:
[`Query.worlds()`](../query/Query.html#worlds())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[World.Location](World.Location.html "enum in org.tribot.script.sdk.types")` | Represents the location that a world can have. |
| `static class` | `[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")` | Represents the types that a world can have. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[World](#%3Cinit%3E(org.tribot.api2007.types.RSServer))​(org.tribot.api2007.types.RSServer server)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.Optional<java.lang.String>` | `[getActivity](#getActivity())()` | Gets the name of the activity of this world |
| `java.lang.String` | `[getHostAddress](#getHostAddress())()` | Gets the host domain address (ex. |
| `[World.Location](World.Location.html "enum in org.tribot.script.sdk.types")` | `[getLocation](#getLocation())()` | Gets the world [`World.Location`](World.Location.html "enum in org.tribot.script.sdk.types") |
| `java.util.Optional<java.lang.Integer>` | `[getPing](#getPing())()` | Attempts to calculate the ping for this world. |
| `int` | `[getPlayerCount](#getPlayerCount())()` | Gets the number of players listed in this world |
| `int` | `[getTotalLevelRequirement](#getTotalLevelRequirement())()` | Gets the total level requirement for this world |
| `java.util.Set<[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")>` | `[getTypes](#getTypes())()` | Gets all the types of this world. |
| `int` | `[getWorldNumber](#getWorldNumber())()` | Gets the number of this world, ex. |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isDangerous](#isDangerous())()` | Checks if this world has some alternative combat rules or form of items lost on death. |
| `boolean` | `[isLowPing](#isLowPing())()` | Checks if this world has low ping relative to other worlds. |
| `boolean` | `[isMainGame](#isMainGame())()` | Checks if this world is a part of the 'main' game, not some secondary game mode |
| `boolean` | `[isMembers](#isMembers())()` | Checks if this world is a members world |
| `boolean` | `[isRequirementsMet](#isRequirementsMet())()` | Checks if this world can be entered, the best it can with the information available. |
| `boolean` | `[isType](#isType(org.tribot.script.sdk.types.World.Type...))​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Checks if this world matches all the specified types |
| `boolean` | `[isTypesAny](#isTypesAny(org.tribot.script.sdk.types.World.Type...))​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Checks if this world matches any of the specified types |
| `boolean` | `[isTypesExactly](#isTypesExactly(org.tribot.script.sdk.types.World.Type...))​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Checks if this world matches the specified types exactly. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

- #### World

```
public World​(org.tribot.api2007.types.RSServer server)
```

+ ### Method Detail

- #### getWorldNumber

```
public int getWorldNumber()
```

Gets the number of this world, ex. 301

Returns:
the world number
- #### getActivity

```
public java.util.Optional<java.lang.String> getActivity()
```

Gets the name of the activity of this world

Returns:
the name of the activity of this world
- #### getPlayerCount

```
public int getPlayerCount()
```

Gets the number of players listed in this world

Returns:
the number of players listed in this world
- #### getHostAddress

```
public java.lang.String getHostAddress()
```

Gets the host domain address (ex. oldschool93.runescape.com)

Returns:
the host domain address, never null
- #### getLocation

```
public [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") getLocation()
```

Gets the world [`World.Location`](World.Location.html "enum in org.tribot.script.sdk.types")

Returns:
the world location, never null
- #### getTypes

```
public java.util.Set<[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")> getTypes()
```

Gets all the types of this world. It may have multiple types.

Returns:
the types of this world
- #### isType

```
public boolean isType​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Checks if this world matches all the specified types

Parameters:
`types` - the types to check
Returns:
true if this world is all of the specified types, false otherwise
- #### isTypesAny

```
public boolean isTypesAny​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Checks if this world matches any of the specified types

Parameters:
`types` - the types to check
Returns:
true if this world matches any of the specified types, false otherwise
- #### isTypesExactly

```
public boolean isTypesExactly​([World.Type](World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Checks if this world matches the specified types exactly.
This means that this world contains no other types other then the specified types.

Parameters:
`types` - the types to check
Returns:
true if this world matches the specified types exactly, false otherwise
- #### isMembers

```
public boolean isMembers()
```

Checks if this world is a members world

Returns:
true if this is a members world, false otherwise
- #### getPing

```
public java.util.Optional<java.lang.Integer> getPing()
```

Attempts to calculate the ping for this world. It will time how long it takes to connect a socket to the world's host address.
The resulting ping is cached for up to 15 minutes to avoid repeated connections. This can take up to two seconds (it will time out and fail after two seconds).

Note that this may not be the 'true' ping but is generally an accurate estimation in most cases.

Returns:
the ping to this world, or an empty optional if there was an issue getting the ping
- #### isLowPing

```
public boolean isLowPing()
```

Checks if this world has low ping relative to other worlds.

Note that this operation could take a while, it has to get the ping of all other worlds.

Returns:
true if this world has low ping relative to other worlds, false otherwise
- #### isMainGame

```
public boolean isMainGame()
```

Checks if this world is a part of the 'main' game, not some secondary game mode

Returns:
true if this is the 'main' game and false if it is a secondary game mode
- #### getTotalLevelRequirement

```
public int getTotalLevelRequirement()
```

Gets the total level requirement for this world

Returns:
the total level requirement for this world, 0 if none
- #### isDangerous

```
public boolean isDangerous()
```

Checks if this world has some alternative combat rules or form of items lost on death.
For example, PvP worlds and high-risk worlds are considered dangerous.

Returns:
true if this is a dangerous world according to the above criteria, false otherwise
- #### isRequirementsMet

```
public boolean isRequirementsMet()
```

Checks if this world can be entered, the best it can with the information available.
Some things like play-time aren't available and can't be checked for bounty hunter.

Returns:
true if the player can enter this world, false otherwise
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`