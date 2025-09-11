# Hiscores.ActivityRanking (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Hiscores.ActivityRanking.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Hiscores.ActivityRanking

* All Implemented Interfaces:
`[Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")`

Enclosing class:
[Hiscores](Hiscores.html "class in org.tribot.script.sdk")

---

```
public static final class Hiscores.ActivityRanking
extends java.lang.Object
implements [Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ActivityRanking](#%3Cinit%3E(org.tribot.script.sdk.Hiscores.Activity,int,int))​([Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk") activity,
int rank,
int score)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `[Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk")` | `[getActivity](#getActivity())()` | |
| `int` | `[getRank](#getRank())()` | |
| `int` | `[getScore](#getScore())()` | |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

- #### ActivityRanking

```
public ActivityRanking​([Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk") activity,
int rank,
int score)
```

+ ### Method Detail

- #### getActivity

```
public [Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk") getActivity()
```
- #### getRank

```
public int getRank()
```

Specified by:
`[getRank](Hiscores.CategoryRanking.html#getRank())` in interface `[Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")`
- #### getScore

```
public int getScore()
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