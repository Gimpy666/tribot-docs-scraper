# EventOverride (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/EventOverride.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* java.lang.Object
* + java.lang.Enum<[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")>
+ - org.tribot.script.sdk.interfaces.EventOverride

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")>`

---

```
public enum EventOverride
extends java.lang.Enum<[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DISMISS](#DISMISS)` | |
| `[PROCESS](#PROCESS)` | |
| `[SEND](#SEND)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `org.tribot.script.interfaces.EventBlockingOverride.OVERRIDE_RETURN` | `[getLegacyOverride](#getLegacyOverride())()` | |
| `static [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### SEND

```
public static final [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") SEND
```
- #### DISMISS

```
public static final [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") DISMISS
```
- #### PROCESS

```
public static final [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") PROCESS
```

+ ### Method Detail

- #### values

```
public static [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (EventOverride c : EventOverride.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") valueOf​(java.lang.String name)
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
- #### getLegacyOverride

```
public org.tribot.script.interfaces.EventBlockingOverride.OVERRIDE_RETURN getLegacyOverride()
```