# ChatScreen.Config.ConfigBuilder (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/ChatScreen.Config.ConfigBuilder.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.ChatScreen.Config.ConfigBuilder

* Enclosing class:
[ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk")

---

```
public static class ChatScreen.Config.ConfigBuilder
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk")` | `[build](#build())()` | |
| `[ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | `[holdSpaceForContinue](#holdSpaceForContinue(boolean))​(boolean holdSpaceForContinue)` | If the space bar should be held consistently and not let go while click continue screens are open, until dialog is over or an option screen comes up |
| `[ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | `[pressSpaceForContinue](#pressSpaceForContinue(boolean))​(boolean pressSpaceForContinue)` | If the space bar should be pressed each time the click continue screen is open |
| `[ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | `[timeout](#timeout(java.util.function.IntSupplier))​(java.util.function.IntSupplier timeout)` | The timeout for a single call to [`ChatScreen.handle(String...)`](ChatScreen.html#handle(java.lang.String...)) (or any of the overloaded methods). |
| `java.lang.String` | `[toString](#toString())()` | |
| `[ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk")` | `[useKeysForOptions](#useKeysForOptions(boolean))​(boolean useKeysForOptions)` | If the number keys should be used to select an option rather than clicking |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### useKeysForOptions

```
public [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk") useKeysForOptions​(boolean useKeysForOptions)
```

If the number keys should be used to select an option rather than clicking

Returns:
`this`.
- #### pressSpaceForContinue

```
public [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk") pressSpaceForContinue​(boolean pressSpaceForContinue)
```

If the space bar should be pressed each time the click continue screen is open

Returns:
`this`.
- #### holdSpaceForContinue

```
public [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk") holdSpaceForContinue​(boolean holdSpaceForContinue)
```

If the space bar should be held consistently and not let go while click continue screens are open, until dialog is over or an option screen comes up

Returns:
`this`.
- #### timeout

```
public [ChatScreen.Config.ConfigBuilder](ChatScreen.Config.ConfigBuilder.html "class in org.tribot.script.sdk") timeout​(java.util.function.IntSupplier timeout)
```

The timeout for a single call to [`ChatScreen.handle(String...)`](ChatScreen.html#handle(java.lang.String...)) (or any of the overloaded methods).
This supplier should provide the number of milliseconds. Ex. `() -> 50000` for 50 seconds.

Returns:
`this`.
- #### build

```
public [ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk") build()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`