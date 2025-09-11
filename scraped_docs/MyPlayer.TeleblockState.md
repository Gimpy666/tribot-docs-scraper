# MyPlayer.TeleblockState (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MyPlayer.TeleblockState.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.MyPlayer.TeleblockState

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[MyPlayer](MyPlayer.html "class in org.tribot.script.sdk")

---

```
public static enum MyPlayer.TeleblockState
extends java.lang.Enum<[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")>
```

The various states of teleblock
0 = not currently active
0 - 100 = not active, but immune
100 - 600 = currently active

See Also:
[`MyPlayer.getTeleblockState()`](MyPlayer.html#getTeleblockState())

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ACTIVE](#ACTIVE)` | |
| `[IMMUNE](#IMMUNE)` | |
| `[NOT\_ACTIVE](#NOT_ACTIVE)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### NOT\_ACTIVE

```
public static final [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk") NOT_ACTIVE
```
- #### IMMUNE

```
public static final [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk") IMMUNE
```
- #### ACTIVE

```
public static final [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk") ACTIVE
```

+ ### Method Detail

- #### values

```
public static [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (MyPlayer.TeleblockState c : MyPlayer.TeleblockState.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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