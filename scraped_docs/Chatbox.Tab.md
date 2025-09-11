# Chatbox.Tab (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Chatbox.Tab.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Chatbox.Tab

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Chatbox](Chatbox.html "class in org.tribot.script.sdk")

---

```
public static enum Chatbox.Tab
extends java.lang.Enum<[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ALL](#ALL)` | |
| `[CHANNEL](#CHANNEL)` | |
| `[CLAN](#CLAN)` | |
| `[GAME](#GAME)` | |
| `[GROUP](#GROUP)` | |
| `[PRIVATE](#PRIVATE)` | |
| `[PUBLIC](#PUBLIC)` | |
| `[TRADE](#TRADE)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")>` | `[getOpen](#getOpen())()` | Gets the currently open tab |
| `boolean` | `[isOpen](#isOpen())()` | Checks if this tab is currently open |
| `boolean` | `[open](#open())()` | Attempts to open this tab |
| `static [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ALL

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") ALL
```
- #### GAME

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") GAME
```
- #### PUBLIC

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") PUBLIC
```
- #### PRIVATE

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") PRIVATE
```
- #### CHANNEL

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") CHANNEL
```
- #### CLAN

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") CLAN
```
- #### TRADE

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") TRADE
```
- #### GROUP

```
public static final [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") GROUP
```

+ ### Method Detail

- #### values

```
public static [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Chatbox.Tab c : Chatbox.Tab.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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

Checks if this tab is currently open

Returns:
true if this tab is open, false otherwise
- #### open

```
public boolean open()
```

Attempts to open this tab

Returns:
true if this tab is open, false otherwise
- #### getOpen

```
public static java.util.Optional<[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")> getOpen()
```

Gets the currently open tab

Returns:
the currently open tab, or an empty optional if the chatbox is hidden