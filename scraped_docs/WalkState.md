# WalkState (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/walking/WalkState.html

**Package:** Packageorg.tribot.script.sdk.walking

---

* java.lang.Object
* + java.lang.Enum<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")>
+ - org.tribot.script.sdk.walking.WalkState

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")>`

---

```
public enum WalkState
extends java.lang.Enum<[WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")>
```

Represents a walk state to be used as a walking condition. This is useful if we want to exit out of walking early.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CONTINUE](#CONTINUE)` | |
| `[FAILURE](#FAILURE)` | |
| `[SUCCESS](#SUCCESS)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### SUCCESS

```
public static final [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking") SUCCESS
```
- #### FAILURE

```
public static final [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking") FAILURE
```
- #### CONTINUE

```
public static final [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking") CONTINUE
```

+ ### Method Detail

- #### values

```
public static [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (WalkState c : WalkState.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [WalkState](WalkState.html "enum in org.tribot.script.sdk.walking") valueOf​(java.lang.String name)
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