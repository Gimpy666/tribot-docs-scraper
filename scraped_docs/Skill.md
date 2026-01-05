# Skill (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Skill.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[Skill](Skill.html "enum in net.runelite.api")>
+ - net.runelite.api.Skill

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Skill](Skill.html "enum in net.runelite.api")>`

---

```
public enum Skill
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[Skill](Skill.html "enum in net.runelite.api")>
```

An enumeration of skills that a player can level.

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
| `[SAILING](#SAILING)` | |
| `[SLAYER](#SLAYER)` | |
| `[SMITHING](#SMITHING)` | |
| `[STRENGTH](#STRENGTH)` | |
| `[THIEVING](#THIEVING)` | |
| `[WOODCUTTING](#WOODCUTTING)` | |

+ ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static [Skill](Skill.html "enum in net.runelite.api")` | `[OVERALL](#OVERALL)` | Deprecated. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the skill. |
| `static [Skill](Skill.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [Skill](Skill.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### ATTACK

```
public static final [Skill](Skill.html "enum in net.runelite.api") ATTACK
```
- #### DEFENCE

```
public static final [Skill](Skill.html "enum in net.runelite.api") DEFENCE
```
- #### STRENGTH

```
public static final [Skill](Skill.html "enum in net.runelite.api") STRENGTH
```
- #### HITPOINTS

```
public static final [Skill](Skill.html "enum in net.runelite.api") HITPOINTS
```
- #### RANGED

```
public static final [Skill](Skill.html "enum in net.runelite.api") RANGED
```
- #### PRAYER

```
public static final [Skill](Skill.html "enum in net.runelite.api") PRAYER
```
- #### MAGIC

```
public static final [Skill](Skill.html "enum in net.runelite.api") MAGIC
```
- #### COOKING

```
public static final [Skill](Skill.html "enum in net.runelite.api") COOKING
```
- #### WOODCUTTING

```
public static final [Skill](Skill.html "enum in net.runelite.api") WOODCUTTING
```
- #### FLETCHING

```
public static final [Skill](Skill.html "enum in net.runelite.api") FLETCHING
```
- #### FISHING

```
public static final [Skill](Skill.html "enum in net.runelite.api") FISHING
```
- #### FIREMAKING

```
public static final [Skill](Skill.html "enum in net.runelite.api") FIREMAKING
```
- #### CRAFTING

```
public static final [Skill](Skill.html "enum in net.runelite.api") CRAFTING
```
- #### SMITHING

```
public static final [Skill](Skill.html "enum in net.runelite.api") SMITHING
```
- #### MINING

```
public static final [Skill](Skill.html "enum in net.runelite.api") MINING
```
- #### HERBLORE

```
public static final [Skill](Skill.html "enum in net.runelite.api") HERBLORE
```
- #### AGILITY

```
public static final [Skill](Skill.html "enum in net.runelite.api") AGILITY
```
- #### THIEVING

```
public static final [Skill](Skill.html "enum in net.runelite.api") THIEVING
```
- #### SLAYER

```
public static final [Skill](Skill.html "enum in net.runelite.api") SLAYER
```
- #### FARMING

```
public static final [Skill](Skill.html "enum in net.runelite.api") FARMING
```
- #### RUNECRAFT

```
public static final [Skill](Skill.html "enum in net.runelite.api") RUNECRAFT
```
- #### HUNTER

```
public static final [Skill](Skill.html "enum in net.runelite.api") HUNTER
```
- #### CONSTRUCTION

```
public static final [Skill](Skill.html "enum in net.runelite.api") CONSTRUCTION
```
- #### SAILING

```
public static final [Skill](Skill.html "enum in net.runelite.api") SAILING
```

+ ### Field Detail

- #### OVERALL

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [Skill](Skill.html "enum in net.runelite.api") OVERALL
```

Deprecated.

+ ### Method Detail

- #### values

```
public static [Skill](Skill.html "enum in net.runelite.api")[] values()
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
public static [Skill](Skill.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### getName

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the skill.

Returns:
the skill name