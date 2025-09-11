# ClanMessageListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/ClanMessageListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface ClanMessageListener
```

Represents a listener for clan chat (or friends chat) messages

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onClanMessage](#onClanMessage(java.lang.String,java.lang.String))​(java.lang.String name,
java.lang.String message)` | Called when a clan message is received |

* + ### Method Detail

- #### onClanMessage

```
void onClanMessage​(java.lang.String name,
java.lang.String message)
```

Called when a clan message is received

Parameters:
`name` - the player name
`message` - the message sent