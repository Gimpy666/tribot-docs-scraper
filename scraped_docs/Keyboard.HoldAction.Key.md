# Keyboard.HoldAction.Key (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Keyboard.HoldAction.Key.html

**Package:** Packageorg.tribot.script.sdk.input

---

* java.lang.Object
* + java.lang.Enum<[Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")>
+ - org.tribot.script.sdk.input.Keyboard.HoldAction.Key

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")>`

Enclosing class:
[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")

---

```
public static enum Keyboard.HoldAction.Key
extends java.lang.Enum<[Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")>
```

Represents a key that can be held. This provides a more intuitive way to specify a key to hold.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CTRL](#CTRL)` | |
| `[SHIFT](#SHIFT)` | |
| `[SPACE](#SPACE)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### SHIFT

```
public static final [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") SHIFT
```
- #### CTRL

```
public static final [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") CTRL
```
- #### SPACE

```
public static final [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") SPACE
```

+ ### Method Detail

- #### values

```
public static [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Keyboard.HoldAction.Key c : Keyboard.HoldAction.Key.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") valueOf​(java.lang.String name)
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