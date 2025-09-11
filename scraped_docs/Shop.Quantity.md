# Shop.Quantity (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Shop.Quantity.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Shop.Quantity

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Shop](Shop.html "class in org.tribot.script.sdk")

---

```
public static enum Shop.Quantity
extends java.lang.Enum<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")>
```

Represents a quantity that can be bought/sold at a shop

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[FIFTY](#FIFTY)` | |
| `[FIVE](#FIVE)` | |
| `[ONE](#ONE)` | |
| `[TEN](#TEN)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")>` | `[getClosestAbove](#getClosestAbove(int))​(int target)` | Gets the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is greater than or equal to the specified amount |
| `static java.util.Optional<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")>` | `[getClosestBelow](#getClosestBelow(int))​(int target)` | Gets the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is less than or equal to the specified amount |
| `int` | `[getQuantity](#getQuantity())()` | |
| `static [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ONE

```
public static final [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") ONE
```
- #### FIVE

```
public static final [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") FIVE
```
- #### TEN

```
public static final [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") TEN
```
- #### FIFTY

```
public static final [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") FIFTY
```

+ ### Method Detail

- #### values

```
public static [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Shop.Quantity c : Shop.Quantity.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getClosestBelow

```
public static java.util.Optional<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")> getClosestBelow​(int target)
```

Gets the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is less than or equal to the specified amount

Parameters:
`target` - the target value
Returns:
the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is less than or equal to the specified amount, or an empty optional if none
- #### getClosestAbove

```
public static java.util.Optional<[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")> getClosestAbove​(int target)
```

Gets the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is greater than or equal to the specified amount

Parameters:
`target` - the target value
Returns:
the closest [`Shop.Quantity`](Shop.Quantity.html "enum in org.tribot.script.sdk") whose numeric value is greater than or equal to the specified amount, or an empty optional if none
- #### getQuantity

```
public int getQuantity()
```