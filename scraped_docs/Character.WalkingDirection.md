# Character.WalkingDirection (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Character.WalkingDirection.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* java.lang.Object
* + java.lang.Enum<[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>
+ - org.tribot.script.sdk.interfaces.Character.WalkingDirection

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>`

Enclosing interface:
[Character](Character.html "interface in org.tribot.script.sdk.interfaces")

---

```
public static enum Character.WalkingDirection
extends java.lang.Enum<[Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[EAST](#EAST)` | |
| `[NORTH](#NORTH)` | |
| `[NORTHEAST](#NORTHEAST)` | |
| `[NORTHWEST](#NORTHWEST)` | |
| `[SOUTH](#SOUTH)` | |
| `[SOUTHEAST](#SOUTHEAST)` | |
| `[SOUTHWEST](#SOUTHWEST)` | |
| `[WEST](#WEST)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `org.tribot.api2007.types.RSCharacter.DIRECTION` | `[getLegacyDirection](#getLegacyDirection())()` | |
| `static [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### WEST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") WEST
```
- #### NORTHWEST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") NORTHWEST
```
- #### NORTHEAST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") NORTHEAST
```
- #### SOUTHEAST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") SOUTHEAST
```
- #### SOUTH

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") SOUTH
```
- #### EAST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") EAST
```
- #### NORTH

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") NORTH
```
- #### SOUTHWEST

```
public static final [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") SOUTHWEST
```

+ ### Method Detail

- #### values

```
public static [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Character.WalkingDirection c : Character.WalkingDirection.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Character.WalkingDirection](Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces") valueOf​(java.lang.String name)
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
- #### getLegacyDirection

```
public org.tribot.api2007.types.RSCharacter.DIRECTION getLegacyDirection()
```