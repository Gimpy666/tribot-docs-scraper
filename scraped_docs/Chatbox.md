# Chatbox (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Chatbox.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Chatbox

* ---

```
public class Chatbox
extends java.lang.Object
```

Contains methods for inspecting and interacting with the chatbox screen (the box that contains chat messages from players for example)

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Chatbox.Tab](Chatbox.Tab.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Chatbox](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[acceptTradeRequest](#acceptTradeRequest())()` | Accepts the most recent trade request |
| `static boolean` | `[acceptTradeRequest](#acceptTradeRequest(java.lang.String))​(java.lang.String trader)` | Accepts a trade request from the specified trader |
| `static boolean` | `[hide](#hide())()` | Hides the chatbox by clicking switch tab on the currently open tab |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the chatbox is open (not hidden) |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Chatbox

```
public Chatbox()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Checks if the chatbox is open (not hidden)

Returns:
true if the chatbox is open, false otherwise
- #### hide

```
public static boolean hide()
```

Hides the chatbox by clicking switch tab on the currently open tab

Returns:
true if the chatbox was hidden, false otherwise
- #### acceptTradeRequest

```
public static boolean acceptTradeRequest()
```

Accepts the most recent trade request

Returns:
true if the trade was accepted, false otherwise
- #### acceptTradeRequest

```
public static boolean acceptTradeRequest​(java.lang.String trader)
```

Accepts a trade request from the specified trader

Parameters:
`trader` - the player who traded us
Returns:
true if the trade was accepted, false otherwise