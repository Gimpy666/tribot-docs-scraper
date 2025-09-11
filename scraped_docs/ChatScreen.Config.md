# ChatScreen.Config (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/ChatScreen.Config.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.ChatScreen.Config

* Enclosing class:
[ChatScreen](ChatScreen.html "class in org.tribot.script.sdk")

---

```
public static final class ChatScreen.Config
extends java.lang.Object
```

The config for the chat handler. This provides default values so you don't have to configure everything, or even anything at all unless you want to change something.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | `[builder](#builder())()` | |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.function.IntSupplier` | `[getTimeout](#getTimeout())()` | The timeout for a single call to [`ChatScreen.handle(String...)`](ChatScreen.html#handle(java.lang.String...)) (or any of the overloaded methods). |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isHoldSpaceForContinue](#isHoldSpaceForContinue())()` | If the space bar should be held consistently and not let go while click continue screens are open, until dialog is over or an option screen comes up |
| `boolean` | `[isPressSpaceForContinue](#isPressSpaceForContinue())()` | If the space bar should be pressed each time the click continue screen is open |
| `boolean` | `[isUseKeysForOptions](#isUseKeysForOptions())()` | If the number keys should be used to select an option rather than clicking |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### builder

```
public static [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk") builder()
```
- #### isUseKeysForOptions

```
public boolean isUseKeysForOptions()
```

If the number keys should be used to select an option rather than clicking
- #### isPressSpaceForContinue

```
public boolean isPressSpaceForContinue()
```

If the space bar should be pressed each time the click continue screen is open
- #### isHoldSpaceForContinue

```
public boolean isHoldSpaceForContinue()
```

If the space bar should be held consistently and not let go while click continue screens are open, until dialog is over or an option screen comes up
- #### getTimeout

```
public java.util.function.IntSupplier getTimeout()
```

The timeout for a single call to [`ChatScreen.handle(String...)`](ChatScreen.html#handle(java.lang.String...)) (or any of the overloaded methods).
This supplier should provide the number of milliseconds. Ex. `() -> 50000` for 50 seconds.
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`