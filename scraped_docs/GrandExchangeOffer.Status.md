# GrandExchangeOffer.Status (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/GrandExchangeOffer.Status.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.GrandExchangeOffer.Status

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[GrandExchangeOffer](GrandExchangeOffer.html "class in org.tribot.script.sdk.types")

---

```
public static enum GrandExchangeOffer.Status
extends java.lang.Enum<[GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CANCELLED](#CANCELLED)` | |
| `[COMPLETED](#COMPLETED)` | |
| `[EMPTY](#EMPTY)` | |
| `[IN\_PROGRESS](#IN_PROGRESS)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### CANCELLED

```
public static final [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") CANCELLED
```
- #### COMPLETED

```
public static final [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") COMPLETED
```
- #### EMPTY

```
public static final [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") EMPTY
```
- #### IN\_PROGRESS

```
public static final [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") IN_PROGRESS
```

+ ### Method Detail

- #### values

```
public static [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GrandExchangeOffer.Status c : GrandExchangeOffer.Status.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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