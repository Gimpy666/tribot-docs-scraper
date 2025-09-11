# MouseEventOverrideListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/MouseEventOverrideListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface MouseEventOverrideListener
```

An interface to override mouse events from the user

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")` | `[onMouseEvent](#onMouseEvent(java.awt.event.MouseEvent))​(java.awt.event.MouseEvent e)` | Overrides the global event blocking system for mouse events. |

* + ### Method Detail

- #### onMouseEvent

```
[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") onMouseEvent​(java.awt.event.MouseEvent e)
```

Overrides the global event blocking system for mouse events.

Parameters:
`e` - The mouse event.
Returns:
EventBlockingOverride.OVERRIDE\_RETURN.SEND to send the event, EventBlockingOverride.OVERRIDE\_RETURN
.DISMISS
to dismiss the event, and EventBlockingOverride.OVERRIDE\_RETURN.PROCESS to have the event processed by the
global
event blocking system.