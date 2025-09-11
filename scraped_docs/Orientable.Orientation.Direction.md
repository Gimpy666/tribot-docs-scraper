# Orientable.Orientation.Direction (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Orientable.Orientation.Direction.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* java.lang.Object
* + java.lang.Enum<[Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")>
+ - org.tribot.script.sdk.interfaces.Orientable.Orientation.Direction

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")>`

Enclosing class:
[Orientable.Orientation](Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")

---

```
public static enum Orientable.Orientation.Direction
extends java.lang.Enum<[Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")>
```

Represents a cardinal direction (and the four inter-cardinal directions)

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[EAST](#EAST)` | |
| `[NORTH](#NORTH)` | |
| `[NORTH\_EAST](#NORTH_EAST)` | |
| `[NORTH\_WEST](#NORTH_WEST)` | |
| `[SOUTH](#SOUTH)` | |
| `[SOUTH\_EAST](#SOUTH_EAST)` | |
| `[SOUTH\_WEST](#SOUTH_WEST)` | |
| `[WEST](#WEST)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### SOUTH

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") SOUTH
```
- #### SOUTH\_WEST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") SOUTH_WEST
```
- #### WEST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") WEST
```
- #### NORTH\_WEST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") NORTH_WEST
```
- #### NORTH

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") NORTH
```
- #### NORTH\_EAST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") NORTH_EAST
```
- #### EAST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") EAST
```
- #### SOUTH\_EAST

```
public static final [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") SOUTH_EAST
```

+ ### Method Detail

- #### values

```
public static [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Orientable.Orientation.Direction c : Orientable.Orientation.Direction.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") valueOf​(java.lang.String name)
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