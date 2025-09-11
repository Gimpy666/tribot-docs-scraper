# GameTab.SwitchPreference (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GameTab.SwitchPreference.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.GameTab.SwitchPreference

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[GameTab](GameTab.html "enum in org.tribot.script.sdk")

---

```
public static enum GameTab.SwitchPreference
extends java.lang.Enum<[GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")>
```

*Default* - Tab switching will be either done by keys or mouse, depending on antiban props.
*Mouse* - Tab switching will be done with mouse clicks.
*Keys* - Tab switching will be done by keyboard keys if enabled in game.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DEFAULT](#DEFAULT)` | |
| `[KEYS](#KEYS)` | |
| `[MOUSE](#MOUSE)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### DEFAULT

```
public static final [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") DEFAULT
```
- #### MOUSE

```
public static final [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") MOUSE
```
- #### KEYS

```
public static final [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") KEYS
```

+ ### Method Detail

- #### values

```
public static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GameTab.SwitchPreference c : GameTab.SwitchPreference.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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