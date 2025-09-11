# MouseClickListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/MouseClickListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface MouseClickListener
```

Represents a listener for mouse clicking

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[mouseClicked](#mouseClicked(java.awt.Point,int,boolean))​(java.awt.Point point,
int mouseButton,
boolean isBot)` | Called when the mouse is clicked |

* + ### Method Detail

- #### mouseClicked

```
void mouseClicked​(java.awt.Point point,
int mouseButton,
boolean isBot)
```

Called when the mouse is clicked

Parameters:
`point` - the point the mouse clicked
`mouseButton` - the clicked mouse button
`isBot` - true if the mouse was clicked by the bot, false otherwise