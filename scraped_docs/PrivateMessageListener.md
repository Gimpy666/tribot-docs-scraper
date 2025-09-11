# PrivateMessageListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/PrivateMessageListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface PrivateMessageListener
```

Represents a listener for private messages from other players

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onPrivateMessage](#onPrivateMessage(java.lang.String,java.lang.String))​(java.lang.String name,
java.lang.String message)` | Called when a private message is received |

* + ### Method Detail

- #### onPrivateMessage

```
void onPrivateMessage​(java.lang.String name,
java.lang.String message)
```

Called when a private message is received

Parameters:
`name` - the player name
`message` - the message sent