# Skill (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Skill.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Skill](Skill.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Skill

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Skill](Skill.html "enum in org.tribot.script.sdk")>`

---

```
public enum Skill
extends java.lang.Enum<[Skill](Skill.html "enum in org.tribot.script.sdk")>
```

A skill listed in the skills tab

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AGILITY](#AGILITY)` | |
| `[ATTACK](#ATTACK)` | |
| `[CONSTRUCTION](#CONSTRUCTION)` | |
| `[COOKING](#COOKING)` | |
| `[CRAFTING](#CRAFTING)` | |
| `[DEFENCE](#DEFENCE)` | |
| `[FARMING](#FARMING)` | |
| `[FIREMAKING](#FIREMAKING)` | |
| `[FISHING](#FISHING)` | |
| `[FLETCHING](#FLETCHING)` | |
| `[HERBLORE](#HERBLORE)` | |
| `[HITPOINTS](#HITPOINTS)` | |
| `[HUNTER](#HUNTER)` | |
| `[MAGIC](#MAGIC)` | |
| `[MINING](#MINING)` | |
| `[PRAYER](#PRAYER)` | |
| `[RANGED](#RANGED)` | |
| `[RUNECRAFT](#RUNECRAFT)` | |
| `[SLAYER](#SLAYER)` | |
| `[SMITHING](#SMITHING)` | |
| `[STRENGTH](#STRENGTH)` | |
| `[THIEVING](#THIEVING)` | |
| `[WOODCUTTING](#WOODCUTTING)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getActualLevel](#getActualLevel())()` | Gets the actual skill level based on exp, not including boosts/stat changes |
| `int` | `[getCurrentLevel](#getCurrentLevel())()` | Gets the current skill level, accounting for boosts/stat changes |
| `int` | `[getCurrentXpToNextLevel](#getCurrentXpToNextLevel())()` | Gets the exp needed to reach the next level |
| `int` | `[getTotalXpToNextLevel](#getTotalXpToNextLevel())()` | Gets the total exp to the next level (the exp for the next level - the exp for the current level) |
| `int` | `[getXp](#getXp())()` | Gets the current exp gained in this skill |
| `int` | `[getXpPercentToNextLevel](#getXpPercentToNextLevel())()` | Gets the percent until the next level |
| `boolean` | `[hover](#hover())()` | Hovers the skill in the skills tab |
| `boolean` | `[isMembersOnly](#isMembersOnly())()` | |
| `static [Skill](Skill.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Skill](Skill.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ATTACK

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") ATTACK
```
- #### STRENGTH

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") STRENGTH
```
- #### DEFENCE

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") DEFENCE
```
- #### RANGED

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") RANGED
```
- #### PRAYER

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") PRAYER
```
- #### MAGIC

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") MAGIC
```
- #### RUNECRAFT

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") RUNECRAFT
```
- #### CONSTRUCTION

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") CONSTRUCTION
```
- #### HITPOINTS

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") HITPOINTS
```
- #### AGILITY

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") AGILITY
```
- #### HERBLORE

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") HERBLORE
```
- #### THIEVING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") THIEVING
```
- #### CRAFTING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") CRAFTING
```
- #### FLETCHING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") FLETCHING
```
- #### SLAYER

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") SLAYER
```
- #### HUNTER

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") HUNTER
```
- #### MINING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") MINING
```
- #### SMITHING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") SMITHING
```
- #### FISHING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") FISHING
```
- #### COOKING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") COOKING
```
- #### FIREMAKING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") FIREMAKING
```
- #### WOODCUTTING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") WOODCUTTING
```
- #### FARMING

```
public static final [Skill](Skill.html "enum in org.tribot.script.sdk") FARMING
```

+ ### Method Detail

- #### values

```
public static [Skill](Skill.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Skill c : Skill.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Skill](Skill.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### isMembersOnly

```
public boolean isMembersOnly()
```
- #### getXp

```
public int getXp()
```

Gets the current exp gained in this skill

Returns:
the current exp
- #### getCurrentXpToNextLevel

```
public int getCurrentXpToNextLevel()
```

Gets the exp needed to reach the next level

Returns:
the exp needed to reach the next level
- #### getXpPercentToNextLevel

```
public int getXpPercentToNextLevel()
```

Gets the percent until the next level

Returns:
the percent until the next level
- #### getTotalXpToNextLevel

```
public int getTotalXpToNextLevel()
```

Gets the total exp to the next level (the exp for the next level - the exp for the current level)

Returns:
the total exp to the next level
- #### getActualLevel

```
public int getActualLevel()
```

Gets the actual skill level based on exp, not including boosts/stat changes

Returns:
the actual skill level based on exp
- #### getCurrentLevel

```
public int getCurrentLevel()
```

Gets the current skill level, accounting for boosts/stat changes

Returns:
the current skill level, accounting for boosts/stat changes
- #### hover

```
public boolean hover()
```

Hovers the skill in the skills tab

Returns:
true if hovered successfully, false otherwise