# Combat.AttackStyle (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Combat.AttackStyle.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Combat.AttackStyle

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Combat](Combat.html "class in org.tribot.script.sdk")

---

```
public static enum Combat.AttackStyle
extends java.lang.Enum<[Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")>
```

An attack style that is selectable on the combat tab

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[ACCURATE](#ACCURATE)` | |
| `[AGGRESSIVE](#AGGRESSIVE)` | |
| `[CASTING](#CASTING)` | |
| `[CONTROLLED](#CONTROLLED)` | |
| `[DEFENSIVE](#DEFENSIVE)` | |
| `[DEFENSIVE\_CASTING](#DEFENSIVE_CASTING)` | |
| `[LONGRANGE](#LONGRANGE)` | |
| `[OTHER](#OTHER)` | |
| `[RANGED\_ACCURATE](#RANGED_ACCURATE)` | |
| `[RAPID](#RAPID)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `java.util.List<[Skill](Skill.html "enum in org.tribot.script.sdk")>` | `[getSkills](#getSkills())()` | |
| `static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### ACCURATE

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") ACCURATE
```
- #### AGGRESSIVE

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") AGGRESSIVE
```
- #### DEFENSIVE

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") DEFENSIVE
```
- #### CONTROLLED

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") CONTROLLED
```
- #### RANGED\_ACCURATE

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") RANGED_ACCURATE
```
- #### RAPID

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") RAPID
```
- #### LONGRANGE

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") LONGRANGE
```
- #### CASTING

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") CASTING
```
- #### DEFENSIVE\_CASTING

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") DEFENSIVE_CASTING
```
- #### OTHER

```
public static final [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") OTHER
```

+ ### Method Detail

- #### values

```
public static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Combat.AttackStyle c : Combat.AttackStyle.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getSkills

```
public java.util.List<[Skill](Skill.html "enum in org.tribot.script.sdk")> getSkills()
```