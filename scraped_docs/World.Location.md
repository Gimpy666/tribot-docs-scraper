# World.Location (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/World.Location.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[World.Location](World.Location.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.World.Location

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[World.Location](World.Location.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[World](World.html "class in org.tribot.script.sdk.types")

---

```
public static enum World.Location
extends java.lang.Enum<[World.Location](World.Location.html "enum in org.tribot.script.sdk.types")>
```

Represents the location that a world can have. This is where the world server is located.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AUSTRALIA](#AUSTRALIA)` | |
| `[GERMANY](#GERMANY)` | |
| `[UNITED\_KINGDOM](#UNITED_KINGDOM)` | |
| `[UNITED\_STATES](#UNITED_STATES)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [World.Location](World.Location.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [World.Location](World.Location.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### UNITED\_STATES

```
public static final [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") UNITED_STATES
```
- #### UNITED\_KINGDOM

```
public static final [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") UNITED_KINGDOM
```
- #### AUSTRALIA

```
public static final [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") AUSTRALIA
```
- #### GERMANY

```
public static final [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") GERMANY
```

+ ### Method Detail

- #### values

```
public static [World.Location](World.Location.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (World.Location c : World.Location.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [World.Location](World.Location.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
`java.lang.NullPointerException` - if the argument is null