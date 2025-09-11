# DuelRequestListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/DuelRequestListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface DuelRequestListener
```

Represents a listener for duel requests

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onDuelRequest](#onDuelRequest(java.lang.String,java.lang.String))​(java.lang.String name,
java.lang.String message)` | Called when a duel request is received |

* + ### Method Detail

- #### onDuelRequest

```
void onDuelRequest​(java.lang.String name,
java.lang.String message)
```

Called when a duel request is received

Parameters:
`name` - the player name
`message` - the duel request message