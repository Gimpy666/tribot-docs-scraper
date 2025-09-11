# MouseReleaseListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/MouseReleaseListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface MouseReleaseListener
```

Represents a listener for when the mouse is released

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[mouseReleased](#mouseReleased(java.awt.Point,int,boolean))​(java.awt.Point point,
int mouseButton,
boolean isBot)` | Called when the mouse is released after a click |

* + ### Method Detail

- #### mouseReleased

```
void mouseReleased​(java.awt.Point point,
int mouseButton,
boolean isBot)
```

Called when the mouse is released after a click

Parameters:
`point` - the point the mouse was released
`mouseButton` - the released mouse button
`isBot` - true if the mouse was clicked by the bot, false otherwise