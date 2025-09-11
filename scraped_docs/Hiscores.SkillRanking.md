# Hiscores.SkillRanking (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Hiscores.SkillRanking.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Hiscores.SkillRanking

* All Implemented Interfaces:
`[Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")`

Enclosing class:
[Hiscores](Hiscores.html "class in org.tribot.script.sdk")

---

```
public static final class Hiscores.SkillRanking
extends java.lang.Object
implements [Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[SkillRanking](#%3Cinit%3E(org.tribot.script.sdk.Hiscores.Skill,int,int,long))​([Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk") skill,
int rank,
int level,
long experience)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `long` | `[getExperience](#getExperience())()` | |
| `int` | `[getLevel](#getLevel())()` | |
| `int` | `[getRank](#getRank())()` | |
| `[Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk")` | `[getSkill](#getSkill())()` | |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

- #### SkillRanking

```
public SkillRanking​([Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk") skill,
int rank,
int level,
long experience)
```

+ ### Method Detail

- #### getSkill

```
public [Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk") getSkill()
```
- #### getRank

```
public int getRank()
```

Specified by:
`[getRank](Hiscores.CategoryRanking.html#getRank())` in interface `[Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")`
- #### getLevel

```
public int getLevel()
```
- #### getExperience

```
public long getExperience()
```
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`