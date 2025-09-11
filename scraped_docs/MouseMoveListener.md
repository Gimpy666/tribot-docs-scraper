# MouseMoveListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/MouseMoveListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface MouseMoveListener
```

Represents a listener for mouse movement

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[mouseMoved](#mouseMoved(java.awt.Point,boolean))​(java.awt.Point point,
boolean isBot)` | Called when the mouse is moved |

* + ### Method Detail

- #### mouseMoved

```
void mouseMoved​(java.awt.Point point,
boolean isBot)
```

Called when the mouse is moved

Parameters:
`point` - the point the mouse was moved to
`isBot` - true if the mouse was moved by the bot, false otherwise