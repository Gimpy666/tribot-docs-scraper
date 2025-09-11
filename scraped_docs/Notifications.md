# Notifications (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/Notifications.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.Notifications

* ---

```
public class Notifications
extends java.lang.Object
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Notifications](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[send](#send(java.lang.String))​(java.lang.String message)` | Sends a notification message to the discord webhook url specified by the user in the client. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Notifications

```
public Notifications()
```

+ ### Method Detail

- #### send

```
public static void send​(java.lang.String message)
```

Sends a notification message to the discord webhook url specified by the user in the client.
The user must have enabled script notifications or this will do nothing

Parameters:
`message` - the notification message to send