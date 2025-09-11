# KeyEventOverrideListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/KeyEventOverrideListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface KeyEventOverrideListener
```

An interface to override key events from the user

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces")` | `[onKeyEvent](#onKeyEvent(java.awt.event.KeyEvent))​(java.awt.event.KeyEvent e)` | Overrides the global event blocking system for key events. |

* + ### Method Detail

- #### onKeyEvent

```
[EventOverride](EventOverride.html "enum in org.tribot.script.sdk.interfaces") onKeyEvent​(java.awt.event.KeyEvent e)
```

Overrides the global event blocking system for key events.

Parameters:
`e` - The key event.
Returns:
EventBlockingOverride.OVERRIDE\_RETURN.SEND to send the event, EventBlockingOverride.OVERRIDE\_RETURN
.DISMISS
to dismiss the event, and EventBlockingOverride.OVERRIDE\_RETURN.PROCESS to have the event processed by the
global
event blocking system.