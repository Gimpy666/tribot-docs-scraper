# LocalTile.Direction (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/LocalTile.Direction.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.LocalTile.Direction

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")

---

```
public static enum LocalTile.Direction
extends java.lang.Enum<[LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")>
```

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

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")` | `[getOpposite](#getOpposite())()` | |
| `boolean` | `[isCardinalDirection](#isCardinalDirection())()` | Checks if this is a cardinal direction (n/e/s/w) |
| `boolean` | `[isInterCardinalDirection](#isInterCardinalDirection())()` | Checks if this is not a cardinal direction, but an inter cardinal direction (made up of two cardinal directions, such as north-east) |
| `static [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### EAST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") EAST
```
- #### NORTH

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") NORTH
```
- #### WEST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") WEST
```
- #### SOUTH

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") SOUTH
```
- #### NORTH\_EAST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") NORTH_EAST
```
- #### NORTH\_WEST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") NORTH_WEST
```
- #### SOUTH\_EAST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") SOUTH_EAST
```
- #### SOUTH\_WEST

```
public static final [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") SOUTH_WEST
```

+ ### Method Detail

- #### values

```
public static [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (LocalTile.Direction c : LocalTile.Direction.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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
- #### isCardinalDirection

```
public boolean isCardinalDirection()
```

Checks if this is a cardinal direction (n/e/s/w)

Returns:
true if this is a cardinal direction, false otherwise
- #### isInterCardinalDirection

```
public boolean isInterCardinalDirection()
```

Checks if this is not a cardinal direction, but an inter cardinal direction (made up of two cardinal directions, such as north-east)

Returns:
true if this is an inter cardinal direction, false otherwise
- #### getOpposite

```
public [LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") getOpposite()
```