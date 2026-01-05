# Prayer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Prayer.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[Prayer](Prayer.html "enum in net.runelite.api")>
+ - net.runelite.api.Prayer

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Prayer](Prayer.html "enum in net.runelite.api")>`

---

```
public enum Prayer
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[Prayer](Prayer.html "enum in net.runelite.api")>
```

An enumeration of prayers.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AUGURY](#AUGURY)` | Augury (Level 77, Magic/Magic Def./Defence). |
| `[BURST\_OF\_STRENGTH](#BURST_OF_STRENGTH)` | Burst of Strength (Level 4, Strength). |
| `[CHIVALRY](#CHIVALRY)` | Chivalry (Level 60, Defence/Strength/Attack). |
| `[CLARITY\_OF\_THOUGHT](#CLARITY_OF_THOUGHT)` | Clarity of Thought (Level 7, Attack). |
| `[DEADEYE](#DEADEYE)` | Deadeye (Level 62, Ranging/Damage/Defence). |
| `[EAGLE\_EYE](#EAGLE_EYE)` | Eagle Eye (Level 44, Ranging). |
| `[HAWK\_EYE](#HAWK_EYE)` | Hawk Eye (Level 26, Ranging). |
| `[IMPROVED\_REFLEXES](#IMPROVED_REFLEXES)` | Improved Reflexes (Level 16, Attack). |
| `[INCREDIBLE\_REFLEXES](#INCREDIBLE_REFLEXES)` | Incredible Reflexes (Level 34, Attack). |
| `[MYSTIC\_LORE](#MYSTIC_LORE)` | Mystic Lore (Level 27, Magic). |
| `[MYSTIC\_MIGHT](#MYSTIC_MIGHT)` | Mystic Might (Level 45, Magic). |
| `[MYSTIC\_VIGOUR](#MYSTIC_VIGOUR)` | Mystic Vigour (Level 63, Magic/Magic Def./Defence). |
| `[MYSTIC\_WILL](#MYSTIC_WILL)` | Mystic Will (Level 9, Magic). |
| `[PIETY](#PIETY)` | Piety (Level 70, Defence/Strength/Attack). |
| `[PRESERVE](#PRESERVE)` | Preserve (Level 55). |
| `[PROTECT\_FROM\_MAGIC](#PROTECT_FROM_MAGIC)` | Protect from Magic (Level 37). |
| `[PROTECT\_FROM\_MELEE](#PROTECT_FROM_MELEE)` | Protect from Melee (Level 43). |
| `[PROTECT\_FROM\_MISSILES](#PROTECT_FROM_MISSILES)` | Protect from Missiles (Level 40). |
| `[PROTECT\_ITEM](#PROTECT_ITEM)` | Protect Item (Level 25). |
| `[RAPID\_HEAL](#RAPID_HEAL)` | Rapid Heal (Level 22, Hitpoints). |
| `[RAPID\_RESTORE](#RAPID_RESTORE)` | Rapid Restore (Level 19, Stats). |
| `[REDEMPTION](#REDEMPTION)` | Redemption (Level 49). |
| `[RETRIBUTION](#RETRIBUTION)` | Retribution (Level 46). |
| `[RIGOUR](#RIGOUR)` | Rigour (Level 74, Ranging/Damage/Defence). |
| `[ROCK\_SKIN](#ROCK_SKIN)` | Rock Skin (Level 10, Defence). |
| `[RP\_ANCIENT\_SIGHT](#RP_ANCIENT_SIGHT)` | Ruinous Powers Ancient Sight (Level 62). |
| `[RP\_ANCIENT\_STRENGTH](#RP_ANCIENT_STRENGTH)` | Ruinous Powers Ancient Strength (Level 61). |
| `[RP\_ANCIENT\_WILL](#RP_ANCIENT_WILL)` | Ruinous Powers Ancient Will (Level 63). |
| `[RP\_ANNIHILATE](#RP_ANNIHILATE)` | Ruinous Powers Annihilate (Level 84). |
| `[RP\_BERSERKER](#RP_BERSERKER)` | Ruinous Powers Berserker (Level 74). |
| `[RP\_CRUORS\_VOW](#RP_CRUORS_VOW)` | Ruinous Powers Cruor's Vow (Level 89). |
| `[RP\_DAMPEN\_MAGIC](#RP_DAMPEN_MAGIC)` | Ruinous Powers Dampen Magic (Level 67). |
| `[RP\_DAMPEN\_MELEE](#RP_DAMPEN_MELEE)` | Ruinous Powers Dampen Melee (Level 71). |
| `[RP\_DAMPEN\_RANGED](#RP_DAMPEN_RANGED)` | Ruinous Powers Dampen Ranged (Level 69). |
| `[RP\_DECIMATE](#RP_DECIMATE)` | Ruinous Powers Decimate (Level 82). |
| `[RP\_FUMUS\_VOW](#RP_FUMUS_VOW)` | Ruinous Powers Fumus' Vow (Level 87). |
| `[RP\_GLACIES\_VOW](#RP_GLACIES_VOW)` | Ruinous Powers Glacies' Vow (Level 90). |
| `[RP\_INTENSIFY](#RP_INTENSIFY)` | Ruinous Powers Intensify (Level 92). |
| `[RP\_METABOLISE](#RP_METABOLISE)` | Ruinous Powers Metabolise (Level 77). |
| `[RP\_PROTECT\_ITEM](#RP_PROTECT_ITEM)` | Ruinous Powers Protect Item (Level 65). |
| `[RP\_PURGE](#RP_PURGE)` | Ruinous Powers Purge (Level 75). |
| `[RP\_REBUKE](#RP_REBUKE)` | Ruinous Powers Rebuke (Level 78). |
| `[RP\_REJUVENATION](#RP_REJUVENATION)` | Ruinous Powers Rejuvenation (Level 60). |
| `[RP\_RUINOUS\_GRACE](#RP_RUINOUS_GRACE)` | Ruinous Powers Ruinous Grace (Level 66). |
| `[RP\_TRINITAS](#RP_TRINITAS)` | Ruinous Powers Trinitas (Level 72). |
| `[RP\_UMBRA\_VOW](#RP_UMBRA_VOW)` | Ruinous Powers Umbra's Vow (Level 88). |
| `[RP\_VAPORISE](#RP_VAPORISE)` | Ruinous Powers Vaporise (Level 86). |
| `[RP\_VINDICATION](#RP_VINDICATION)` | Ruinous Powers Vindication (Level 80). |
| `[RP\_WRATH](#RP_WRATH)` | Ruinous Powers Wrath (Level 91). |
| `[SHARP\_EYE](#SHARP_EYE)` | Sharp Eye (Level 8, Ranging). |
| `[SMITE](#SMITE)` | Smite (Level 52). |
| `[STEEL\_SKIN](#STEEL_SKIN)` | Steel Skin (Level 28, Defence). |
| `[SUPERHUMAN\_STRENGTH](#SUPERHUMAN_STRENGTH)` | Superhuman Strength (Level 13, Strength). |
| `[THICK\_SKIN](#THICK_SKIN)` | Thick Skin (Level 1, Defence). |
| `[ULTIMATE\_STRENGTH](#ULTIMATE_STRENGTH)` | Ultimate Strength (Level 31, Strength). |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getVarbit](#getVarbit())()` | Gets the varbit that stores whether the prayer is active or not. |
| `static [Prayer](Prayer.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [Prayer](Prayer.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### THICK\_SKIN

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") THICK_SKIN
```

Thick Skin (Level 1, Defence).
- #### BURST\_OF\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") BURST_OF_STRENGTH
```

Burst of Strength (Level 4, Strength).
- #### CLARITY\_OF\_THOUGHT

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") CLARITY_OF_THOUGHT
```

Clarity of Thought (Level 7, Attack).
- #### SHARP\_EYE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") SHARP_EYE
```

Sharp Eye (Level 8, Ranging).
- #### MYSTIC\_WILL

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") MYSTIC_WILL
```

Mystic Will (Level 9, Magic).
- #### ROCK\_SKIN

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") ROCK_SKIN
```

Rock Skin (Level 10, Defence).
- #### SUPERHUMAN\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") SUPERHUMAN_STRENGTH
```

Superhuman Strength (Level 13, Strength).
- #### IMPROVED\_REFLEXES

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") IMPROVED_REFLEXES
```

Improved Reflexes (Level 16, Attack).
- #### RAPID\_RESTORE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RAPID_RESTORE
```

Rapid Restore (Level 19, Stats).
- #### RAPID\_HEAL

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RAPID_HEAL
```

Rapid Heal (Level 22, Hitpoints).
- #### PROTECT\_ITEM

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PROTECT_ITEM
```

Protect Item (Level 25).
- #### HAWK\_EYE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") HAWK_EYE
```

Hawk Eye (Level 26, Ranging).
- #### MYSTIC\_LORE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") MYSTIC_LORE
```

Mystic Lore (Level 27, Magic).
- #### STEEL\_SKIN

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") STEEL_SKIN
```

Steel Skin (Level 28, Defence).
- #### ULTIMATE\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") ULTIMATE_STRENGTH
```

Ultimate Strength (Level 31, Strength).
- #### INCREDIBLE\_REFLEXES

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") INCREDIBLE_REFLEXES
```

Incredible Reflexes (Level 34, Attack).
- #### PROTECT\_FROM\_MAGIC

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PROTECT_FROM_MAGIC
```

Protect from Magic (Level 37).
- #### PROTECT\_FROM\_MISSILES

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PROTECT_FROM_MISSILES
```

Protect from Missiles (Level 40).
- #### PROTECT\_FROM\_MELEE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PROTECT_FROM_MELEE
```

Protect from Melee (Level 43).
- #### EAGLE\_EYE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") EAGLE_EYE
```

Eagle Eye (Level 44, Ranging).
- #### MYSTIC\_MIGHT

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") MYSTIC_MIGHT
```

Mystic Might (Level 45, Magic).
- #### RETRIBUTION

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RETRIBUTION
```

Retribution (Level 46).
- #### REDEMPTION

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") REDEMPTION
```

Redemption (Level 49).
- #### SMITE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") SMITE
```

Smite (Level 52).
- #### CHIVALRY

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") CHIVALRY
```

Chivalry (Level 60, Defence/Strength/Attack).
- #### DEADEYE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") DEADEYE
```

Deadeye (Level 62, Ranging/Damage/Defence).
- #### MYSTIC\_VIGOUR

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") MYSTIC_VIGOUR
```

Mystic Vigour (Level 63, Magic/Magic Def./Defence).
- #### PIETY

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PIETY
```

Piety (Level 70, Defence/Strength/Attack).
- #### PRESERVE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") PRESERVE
```

Preserve (Level 55).
- #### RIGOUR

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RIGOUR
```

Rigour (Level 74, Ranging/Damage/Defence).
- #### AUGURY

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") AUGURY
```

Augury (Level 77, Magic/Magic Def./Defence).
- #### RP\_REJUVENATION

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_REJUVENATION
```

Ruinous Powers Rejuvenation (Level 60).
- #### RP\_ANCIENT\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_ANCIENT_STRENGTH
```

Ruinous Powers Ancient Strength (Level 61).
- #### RP\_ANCIENT\_SIGHT

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_ANCIENT_SIGHT
```

Ruinous Powers Ancient Sight (Level 62).
- #### RP\_ANCIENT\_WILL

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_ANCIENT_WILL
```

Ruinous Powers Ancient Will (Level 63).
- #### RP\_PROTECT\_ITEM

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_PROTECT_ITEM
```

Ruinous Powers Protect Item (Level 65).
- #### RP\_RUINOUS\_GRACE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_RUINOUS_GRACE
```

Ruinous Powers Ruinous Grace (Level 66).
- #### RP\_DAMPEN\_MAGIC

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_DAMPEN_MAGIC
```

Ruinous Powers Dampen Magic (Level 67).
- #### RP\_DAMPEN\_RANGED

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_DAMPEN_RANGED
```

Ruinous Powers Dampen Ranged (Level 69).
- #### RP\_DAMPEN\_MELEE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_DAMPEN_MELEE
```

Ruinous Powers Dampen Melee (Level 71).
- #### RP\_TRINITAS

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_TRINITAS
```

Ruinous Powers Trinitas (Level 72).
- #### RP\_BERSERKER

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_BERSERKER
```

Ruinous Powers Berserker (Level 74).
- #### RP\_PURGE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_PURGE
```

Ruinous Powers Purge (Level 75).
- #### RP\_METABOLISE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_METABOLISE
```

Ruinous Powers Metabolise (Level 77).
- #### RP\_REBUKE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_REBUKE
```

Ruinous Powers Rebuke (Level 78).
- #### RP\_VINDICATION

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_VINDICATION
```

Ruinous Powers Vindication (Level 80).
- #### RP\_DECIMATE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_DECIMATE
```

Ruinous Powers Decimate (Level 82).
- #### RP\_ANNIHILATE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_ANNIHILATE
```

Ruinous Powers Annihilate (Level 84).
- #### RP\_VAPORISE

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_VAPORISE
```

Ruinous Powers Vaporise (Level 86).
- #### RP\_FUMUS\_VOW

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_FUMUS_VOW
```

Ruinous Powers Fumus' Vow (Level 87).
- #### RP\_UMBRA\_VOW

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_UMBRA_VOW
```

Ruinous Powers Umbra's Vow (Level 88).
- #### RP\_CRUORS\_VOW

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_CRUORS_VOW
```

Ruinous Powers Cruor's Vow (Level 89).
- #### RP\_GLACIES\_VOW

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_GLACIES_VOW
```

Ruinous Powers Glacies' Vow (Level 90).
- #### RP\_WRATH

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_WRATH
```

Ruinous Powers Wrath (Level 91).
- #### RP\_INTENSIFY

```
public static final [Prayer](Prayer.html "enum in net.runelite.api") RP_INTENSIFY
```

Ruinous Powers Intensify (Level 92).

+ ### Method Detail

- #### values

```
public static [Prayer](Prayer.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Prayer c : Prayer.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Prayer](Prayer.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if this enum type has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if the argument is null
- #### getVarbit

```
[@Varbit](annotations/Varbit.html "annotation in net.runelite.api.annotations")
public int getVarbit()
```

Gets the varbit that stores whether the prayer is active or not.

Returns:
the prayer active varbit