# Hiscores (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Hiscores.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Hiscores

* ---

```
public class Hiscores
extends java.lang.Object
```

Utility for grabbing data from the game highscores

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Hiscores.Activity](Hiscores.Activity.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Hiscores.ActivityRanking](Hiscores.ActivityRanking.html "class in org.tribot.script.sdk")` | |
| `static interface` | `[Hiscores.CategoryRanking](Hiscores.CategoryRanking.html "interface in org.tribot.script.sdk")` | |
| `static class` | `[Hiscores.Player](Hiscores.Player.html "class in org.tribot.script.sdk")` | |
| `static class` | `[Hiscores.Skill](Hiscores.Skill.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Hiscores.SkillRanking](Hiscores.SkillRanking.html "class in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Hiscores](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[Hiscores.Player](Hiscores.Player.html "class in org.tribot.script.sdk")>` | `[lookup](#lookup(java.lang.String))​(java.lang.String player)` | Attempts to look up the specified player name on the hiscores |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Hiscores

```
public Hiscores()
```

+ ### Method Detail

- #### lookup

```
public static java.util.Optional<[Hiscores.Player](Hiscores.Player.html "class in org.tribot.script.sdk")> lookup​(java.lang.String player)
```

Attempts to look up the specified player name on the hiscores

Parameters:
`player` - the player name
Returns:
the player data on the hiscores, or an empty optional if there was an issue getting the data