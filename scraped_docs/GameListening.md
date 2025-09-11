# GameListening (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GameListening.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.GameListening

* ---

```
public class GameListening
extends java.lang.Object
```

Contains listeners for game events. These are scoped to the script and are removed when it ends.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[GameListening](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[addGameTickListener](#addGameTickListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run when a game server tick processes |
| `static void` | `[removeGameTickListener](#removeGameTickListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes a game tick listener |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### GameListening

```
public GameListening()
```

+ ### Method Detail

- #### addGameTickListener

```
public static void addGameTickListener​(java.lang.Runnable listener)
```

Adds a listener that will run when a game server tick processes

Parameters:
`listener` - the game tick listener
- #### removeGameTickListener

```
public static void removeGameTickListener​(java.lang.Runnable listener)
```

Removes a game tick listener

Parameters:
`listener` - the listener to remove