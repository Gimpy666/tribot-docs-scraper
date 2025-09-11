# Quest.State (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Quest.State.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Quest.State](Quest.State.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Quest.State

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Quest.State](Quest.State.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Quest](Quest.html "enum in org.tribot.script.sdk")

---

```
public static enum Quest.State
extends java.lang.Enum<[Quest.State](Quest.State.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[COMPLETE](#COMPLETE)` | |
| `[IN\_PROGRESS](#IN_PROGRESS)` | |
| `[NOT\_STARTED](#NOT_STARTED)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Quest.State](Quest.State.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Quest.State](Quest.State.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### NOT\_STARTED

```
public static final [Quest.State](Quest.State.html "enum in org.tribot.script.sdk") NOT_STARTED
```
- #### IN\_PROGRESS

```
public static final [Quest.State](Quest.State.html "enum in org.tribot.script.sdk") IN_PROGRESS
```
- #### COMPLETE

```
public static final [Quest.State](Quest.State.html "enum in org.tribot.script.sdk") COMPLETE
```

+ ### Method Detail

- #### values

```
public static [Quest.State](Quest.State.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Quest.State c : Quest.State.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Quest.State](Quest.State.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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