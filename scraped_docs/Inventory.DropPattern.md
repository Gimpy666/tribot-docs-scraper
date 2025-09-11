# Inventory.DropPattern (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Inventory.DropPattern.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Inventory.DropPattern

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Inventory](Inventory.html "class in org.tribot.script.sdk")

---

```
public static enum Inventory.DropPattern
extends java.lang.Enum<[Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")>
```

A pattern, or order, to drop items in

See Also:
[`Inventory.drop(List)`](Inventory.html#drop(java.util.List))

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[LEFT\_TO\_RIGHT](#LEFT_TO_RIGHT)` | |
| `[TOP\_TO\_BOTTOM](#TOP_TO_BOTTOM)` | |
| `[TOP\_TO\_BOTTOM\_ZIGZAG](#TOP_TO_BOTTOM_ZIGZAG)` | |
| `[ZIGZAG](#ZIGZAG)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int[]` | `[getDropList](#getDropList())()` | |
| `static [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### LEFT\_TO\_RIGHT

```
public static final [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk") LEFT_TO_RIGHT
```
- #### TOP\_TO\_BOTTOM

```
public static final [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk") TOP_TO_BOTTOM
```
- #### ZIGZAG

```
public static final [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk") ZIGZAG
```
- #### TOP\_TO\_BOTTOM\_ZIGZAG

```
public static final [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk") TOP_TO_BOTTOM_ZIGZAG
```

+ ### Method Detail

- #### values

```
public static [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Inventory.DropPattern c : Inventory.DropPattern.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getDropList

```
public int[] getDropList()
```