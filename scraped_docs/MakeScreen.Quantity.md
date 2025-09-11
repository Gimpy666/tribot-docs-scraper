# MakeScreen.Quantity (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MakeScreen.Quantity.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.MakeScreen.Quantity

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[MakeScreen](MakeScreen.html "class in org.tribot.script.sdk")

---

```
public static enum MakeScreen.Quantity
extends java.lang.Enum<[MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ALL](#ALL)` | |
| `[FIVE](#FIVE)` | |
| `[ONE](#ONE)` | |
| `[TEN](#TEN)` | |
| `[X](#X)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ONE

```
public static final [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") ONE
```
- #### FIVE

```
public static final [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") FIVE
```
- #### TEN

```
public static final [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") TEN
```
- #### X

```
public static final [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") X
```
- #### ALL

```
public static final [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") ALL
```

+ ### Method Detail

- #### values

```
public static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (MakeScreen.Quantity c : MakeScreen.Quantity.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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