# PlayerMessageListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/PlayerMessageListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface PlayerMessageListener
```

Represents a listener for public player messages in the chatbox

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onPlayerMessage](#onPlayerMessage(java.lang.String,java.lang.String))​(java.lang.String name,
java.lang.String message)` | Called when a public player message is received |

* + ### Method Detail

- #### onPlayerMessage

```
void onPlayerMessage​(java.lang.String name,
java.lang.String message)
```

Called when a public player message is received

Parameters:
`name` - the player name
`message` - the message sent