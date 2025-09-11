# GroundItem.OwnerType (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/GroundItem.OwnerType.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.GroundItem.OwnerType

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[GroundItem](GroundItem.html "class in org.tribot.script.sdk.types")

---

```
public static enum GroundItem.OwnerType
extends java.lang.Enum<[GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[GROUP](#GROUP)` | |
| `[NONE](#NONE)` | |
| `[OTHER](#OTHER)` | |
| `[SELF](#SELF)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### NONE

```
public static final [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") NONE
```
- #### SELF

```
public static final [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") SELF
```
- #### OTHER

```
public static final [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") OTHER
```
- #### GROUP

```
public static final [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") GROUP
```

+ ### Method Detail

- #### values

```
public static [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GroundItem.OwnerType c : GroundItem.OwnerType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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