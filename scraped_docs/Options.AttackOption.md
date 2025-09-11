# Options.AttackOption (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Options.AttackOption.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Options.AttackOption

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Options](Options.html "class in org.tribot.script.sdk")

---

```
public static enum Options.AttackOption
extends java.lang.Enum<[Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ALWAYS\_RIGHT\_CLICK](#ALWAYS_RIGHT_CLICK)` | |
| `[DEPENDS\_ON\_COMBAT\_LEVEL](#DEPENDS_ON_COMBAT_LEVEL)` | |
| `[HIDDEN](#HIDDEN)` | |
| `[LEFT\_CLICK\_WHERE\_AVAILABLE](#LEFT_CLICK_WHERE_AVAILABLE)` | |
| `[RIGHT\_CLICK\_FOR\_CLAN\_MATES](#RIGHT_CLICK_FOR_CLAN_MATES)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")` | `[getNpcAttackOption](#getNpcAttackOption())()` | Gets the currently npc attack option |
| `static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")` | `[getPlayerAttackOption](#getPlayerAttackOption())()` | Gets the currently player attack option |
| `static boolean` | `[setNpcAttackOption](#setNpcAttackOption(org.tribot.script.sdk.Options.AttackOption))​([Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") attackOption)` | Set desired npc attack option |
| `static boolean` | `[setPlayerAttackOption](#setPlayerAttackOption(org.tribot.script.sdk.Options.AttackOption))​([Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") attackOption)` | Set desired player attack option |
| `static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### DEPENDS\_ON\_COMBAT\_LEVEL

```
public static final [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") DEPENDS_ON_COMBAT_LEVEL
```
- #### ALWAYS\_RIGHT\_CLICK

```
public static final [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") ALWAYS_RIGHT_CLICK
```
- #### LEFT\_CLICK\_WHERE\_AVAILABLE

```
public static final [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") LEFT_CLICK_WHERE_AVAILABLE
```
- #### HIDDEN

```
public static final [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") HIDDEN
```
- #### RIGHT\_CLICK\_FOR\_CLAN\_MATES

```
public static final [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") RIGHT_CLICK_FOR_CLAN_MATES
```

+ ### Method Detail

- #### values

```
public static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Options.AttackOption c : Options.AttackOption.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getPlayerAttackOption

```
public static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") getPlayerAttackOption()
```

Gets the currently player attack option

Returns:
the currently player attack option
- #### getNpcAttackOption

```
public static [Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") getNpcAttackOption()
```

Gets the currently npc attack option

Returns:
the currently npc attack option
- #### setNpcAttackOption

```
public static boolean setNpcAttackOption​([Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") attackOption)
```

Set desired npc attack option

Parameters:
`attackOption` - desired npc attack option
Returns:
true if the desired npc attack option is selected
- #### setPlayerAttackOption

```
public static boolean setPlayerAttackOption​([Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk") attackOption)
```

Set desired player attack option

Parameters:
`attackOption` - desired player attack option
Returns:
true if the desired player attack option is selected