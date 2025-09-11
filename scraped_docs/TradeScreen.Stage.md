# TradeScreen.Stage (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/TradeScreen.Stage.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.TradeScreen.Stage

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[TradeScreen](TradeScreen.html "class in org.tribot.script.sdk")

---

```
public static enum TradeScreen.Stage
extends java.lang.Enum<[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")>
```

The trade window stage

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[FIRST\_WINDOW](#FIRST_WINDOW)` | |
| `[SECOND\_WINDOW](#SECOND_WINDOW)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### FIRST\_WINDOW

```
public static final [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk") FIRST_WINDOW
```
- #### SECOND\_WINDOW

```
public static final [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk") SECOND_WINDOW
```

+ ### Method Detail

- #### values

```
public static [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (TradeScreen.Stage c : TradeScreen.Stage.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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