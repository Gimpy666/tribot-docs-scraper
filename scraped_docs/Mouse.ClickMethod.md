# Mouse.ClickMethod (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Mouse.ClickMethod.html

**Package:** Packageorg.tribot.script.sdk.input

---

* java.lang.Object
* + java.lang.Enum<[Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")>
+ - org.tribot.script.sdk.input.Mouse.ClickMethod

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")>`

Enclosing class:
[Mouse](Mouse.html "class in org.tribot.script.sdk.input")

---

```
public static enum Mouse.ClickMethod
extends java.lang.Enum<[Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")>
```

Represents an entity clicking method

See Also:
[`Mouse.setClickMethod(ClickMethod)`](Mouse.html#setClickMethod(org.tribot.script.sdk.input.Mouse.ClickMethod)),
[`Mouse.getClickMethod()`](Mouse.html#getClickMethod())

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ACCURATE\_MOUSE](#ACCURATE_MOUSE)` | |
| `[TOUCH\_SCREEN](#TOUCH_SCREEN)` | |
| `[TRIBOT](#TRIBOT)` | |
| `[TRIBOT\_DYNAMIC](#TRIBOT_DYNAMIC)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### TRIBOT

```
public static final [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") TRIBOT
```
- #### ACCURATE\_MOUSE

```
public static final [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") ACCURATE_MOUSE
```
- #### TOUCH\_SCREEN

```
public static final [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") TOUCH_SCREEN
```
- #### TRIBOT\_DYNAMIC

```
public static final [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") TRIBOT_DYNAMIC
```

+ ### Method Detail

- #### values

```
public static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Mouse.ClickMethod c : Mouse.ClickMethod.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") valueOf​(java.lang.String name)
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