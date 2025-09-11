# MouseDragListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/MouseDragListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface MouseDragListener
```

Represents a listener for mouse dragging

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[mouseDragged](#mouseDragged(java.awt.Point,int,boolean))​(java.awt.Point point,
int mouseButton,
boolean isBot)` | Called when the mouse is dragged |

* + ### Method Detail

- #### mouseDragged

```
void mouseDragged​(java.awt.Point point,
int mouseButton,
boolean isBot)
```

Called when the mouse is dragged

Parameters:
`point` - the point the mouse is dragged to
`mouseButton` - the held mouse button
`isBot` - true if the mouse was dragged by the bot, false otherwise