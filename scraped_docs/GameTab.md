# GameTab (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GameTab.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[GameTab](GameTab.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.GameTab

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[GameTab](GameTab.html "enum in org.tribot.script.sdk")>`

---

```
public enum GameTab
extends java.lang.Enum<[GameTab](GameTab.html "enum in org.tribot.script.sdk")>
```

A game tab available in the side-panel widgets

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")` | *Default* - Tab switching will be either done by keys or mouse, depending on antiban props. |

+ ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ACCOUNT](#ACCOUNT)` | |
| `[CLAN](#CLAN)` | |
| `[COMBAT](#COMBAT)` | |
| `[EMOTES](#EMOTES)` | |
| `[EQUIPMENT](#EQUIPMENT)` | |
| `[FRIENDS](#FRIENDS)` | |
| `[IGNORE](#IGNORE)` | |
| `[INVENTORY](#INVENTORY)` | |
| `[LOGOUT](#LOGOUT)` | |
| `[MAGIC](#MAGIC)` | |
| `[MUSIC](#MUSIC)` | |
| `[NULL](#NULL)` | |
| `[OPTIONS](#OPTIONS)` | |
| `[PRAYER](#PRAYER)` | |
| `[QUESTS](#QUESTS)` | |
| `[SKILLS](#SKILLS)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getFKey](#getFKey())()` | Gets the custom functional key to open a game tab. |
| `static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk")` | `[getSwitchPreference](#getSwitchPreference())()` | Gets the preferred game tab switch preference |
| `boolean` | `[isOpen](#isOpen())()` | Checks whether or not the game tab is open. |
| `boolean` | `[open](#open())()` | Opens the game tab. |
| `static void` | `[setSwitchPreference](#setSwitchPreference(org.tribot.script.sdk.GameTab.SwitchPreference))​([GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") pref)` | Sets the preferred gametab switch preference |
| `static [GameTab](GameTab.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [GameTab](GameTab.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### COMBAT

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") COMBAT
```
- #### SKILLS

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") SKILLS
```
- #### QUESTS

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") QUESTS
```
- #### INVENTORY

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") INVENTORY
```
- #### EQUIPMENT

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") EQUIPMENT
```
- #### PRAYER

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") PRAYER
```
- #### MAGIC

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") MAGIC
```
- #### CLAN

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") CLAN
```
- #### FRIENDS

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") FRIENDS
```
- #### IGNORE

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") IGNORE
```
- #### ACCOUNT

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") ACCOUNT
```
- #### LOGOUT

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") LOGOUT
```
- #### OPTIONS

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") OPTIONS
```
- #### EMOTES

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") EMOTES
```
- #### MUSIC

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") MUSIC
```
- #### NULL

```
public static final [GameTab](GameTab.html "enum in org.tribot.script.sdk") NULL
```

+ ### Method Detail

- #### values

```
public static [GameTab](GameTab.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (GameTab c : GameTab.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [GameTab](GameTab.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getFKey

```
public int getFKey()
```

Gets the custom functional key to open a game tab.

Returns:
int, the functional key (F1-F12) or KeyEvent.VK\_ESC
- #### open

```
public boolean open()
```

Opens the game tab.

Returns:
True if the tab was successfully opened; false otherwise.
- #### isOpen

```
public boolean isOpen()
```

Checks whether or not the game tab is open.

Returns:
True if open; false otherwise.
- #### getSwitchPreference

```
public static [GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") getSwitchPreference()
```

Gets the preferred game tab switch preference

Returns:
the preferred game tab switch preference
- #### setSwitchPreference

```
public static void setSwitchPreference​([GameTab.SwitchPreference](GameTab.SwitchPreference.html "enum in org.tribot.script.sdk") pref)
```

Sets the preferred gametab switch preference

Parameters:
`pref` - the game tab switch preference