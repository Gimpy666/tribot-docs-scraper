# Hiscores.Player (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Hiscores.Player.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Hiscores.Player

* Enclosing class:
[Hiscores](Hiscores.html "class in org.tribot.script.sdk")

---

```
public static class Hiscores.Player
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​(java.lang.Object other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.Optional<[Hiscores.ActivityRanking](Hiscores.ActivityRanking.html "class in org.tribot.script.sdk")>` | `[getActivity](#getActivity(org.tribot.script.sdk.Hiscores.Activity))​([Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk") activity)` | |
| `java.util.Optional<[Hiscores.SkillRanking](Hiscores.SkillRanking.html "class in org.tribot.script.sdk")>` | `[getSkill](#getSkill(org.tribot.script.sdk.Hiscores.Skill))​([Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk") skill)` | |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### getSkill

```
public java.util.Optional<[Hiscores.SkillRanking](Hiscores.SkillRanking.html "class in org.tribot.script.sdk")> getSkill​([Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk") skill)
```
- #### getActivity

```
public java.util.Optional<[Hiscores.ActivityRanking](Hiscores.ActivityRanking.html "class in org.tribot.script.sdk")> getActivity​([Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk") activity)
```
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### canEqual

```
protected boolean canEqual​(java.lang.Object other)
```
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