# Worlds (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Worlds.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Worlds

* ---

```
public class Worlds
extends java.lang.Object
```

Contains utility methods for accessing worlds

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Worlds](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.List<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getAll](#getAll())()` | Gets a list of all worlds |
| `static java.util.List<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getAll](#getAll(java.util.function.Predicate))​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)` | Gets a list of all worlds matching the specified filter |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getCurrent](#getCurrent())()` | Gets the current world |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getFirst](#getFirst(int...))​(int... worldNumber)` | Gets the first world with one of the specified world numbers |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getFirst](#getFirst(java.util.function.Predicate))​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)` | Gets the first world matching the specified filter |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getRandom](#getRandom(int...))​(int... worldNumber)` | Gets a random world with one of the specified world numbers |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getRandom](#getRandom(java.util.function.Predicate))​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)` | Gets a random world that matches the specified filter |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getRandomMembers](#getRandomMembers())()` | Gets a random members world, where the worlds types is exactly [`World.Type.MEMBERS`](types/World.Type.html#MEMBERS) (won't match pvp worlds and so on) |
| `static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")>` | `[getRandomNonMembers](#getRandomNonMembers())()` | Gets a random non members world, where the world has exactly no types (won't match pvp worlds and so on) |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Worlds

```
public Worlds()
```

+ ### Method Detail

- #### getAll

```
public static java.util.List<[World](types/World.html "class in org.tribot.script.sdk.types")> getAll()
```

Gets a list of all worlds

Returns:
all worlds
- #### getAll

```
public static java.util.List<[World](types/World.html "class in org.tribot.script.sdk.types")> getAll​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)
```

Gets a list of all worlds matching the specified filter

Parameters:
`filter` - the world filter
Returns:
all worlds matching the specified filter
- #### getFirst

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getFirst​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)
```

Gets the first world matching the specified filter

Parameters:
`filter` - the world filter
Returns:
the first world matching the specified filter
- #### getFirst

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getFirst​(int... worldNumber)
```

Gets the first world with one of the specified world numbers

Parameters:
`worldNumber` - the world numbers
Returns:
the first world with one of the specified world numbers
- #### getRandom

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getRandom​(java.util.function.Predicate<[World](types/World.html "class in org.tribot.script.sdk.types")> filter)
```

Gets a random world that matches the specified filter

Parameters:
`filter` - the world filter
Returns:
a random world matching the specified filter
- #### getRandom

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getRandom​(int... worldNumber)
```

Gets a random world with one of the specified world numbers

Parameters:
`worldNumber` - the world numbers
Returns:
a random world with one of the specified world numbers
- #### getCurrent

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getCurrent()
```

Gets the current world

Returns:
the current world
- #### getRandomMembers

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getRandomMembers()
```

Gets a random members world, where the worlds types is exactly [`World.Type.MEMBERS`](types/World.Type.html#MEMBERS) (won't match pvp worlds and so on)

Returns:
a random members world
- #### getRandomNonMembers

```
public static java.util.Optional<[World](types/World.html "class in org.tribot.script.sdk.types")> getRandomNonMembers()
```

Gets a random non members world, where the world has exactly no types (won't match pvp worlds and so on)

Returns:
a random non members world