# Options.Tab (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Options.Tab.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Options.Tab

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Options](Options.html "class in org.tribot.script.sdk")

---

```
public static enum Options.Tab
extends java.lang.Enum<[Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AUDIO](#AUDIO)` | |
| `[CONTROLS](#CONTROLS)` | |
| `[DISPLAY](#DISPLAY)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")` | `[getOpen](#getOpen())()` | Gets the currently opened options tab |
| `boolean` | `[isOpen](#isOpen())()` | Checks if this options tab is open |
| `boolean` | `[open](#open())()` | Attempts to open this options tab |
| `static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### CONTROLS

```
public static final [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk") CONTROLS
```
- #### AUDIO

```
public static final [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk") AUDIO
```
- #### DISPLAY

```
public static final [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk") DISPLAY
```

+ ### Method Detail

- #### values

```
public static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Options.Tab c : Options.Tab.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### isOpen

```
public boolean isOpen()
```

Checks if this options tab is open

Returns:
true if this tab is open, false otherwise
- #### open

```
public boolean open()
```

Attempts to open this options tab

Returns:
true if the options tab was opened, false otherwise
- #### getOpen

```
public static [Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk") getOpen()
```

Gets the currently opened options tab

Returns:
the currently opened options tab