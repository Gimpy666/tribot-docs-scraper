# ServerMessageListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/ServerMessageListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface ServerMessageListener
```

Represents a listener for server/game messages. These are the black text messages in the chatbox.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onServerMessage](#onServerMessage(java.lang.String))​(java.lang.String message)` | Called when a server message is received |

* + ### Method Detail

- #### onServerMessage

```
void onServerMessage​(java.lang.String message)
```

Called when a server message is received

Parameters:
`message` - the server message