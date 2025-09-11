# Keyboard.HoldAction.KeyHoldContext (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Keyboard.HoldAction.KeyHoldContext.html

**Package:** Packageorg.tribot.script.sdk.input

---

* java.lang.Object
* + org.tribot.script.sdk.input.Keyboard.HoldAction.KeyHoldContext

* Enclosing class:
[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")

---

```
public static class Keyboard.HoldAction.KeyHoldContext
extends java.lang.Object
```

Represents the context of a current key hold action.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[isActive](#isActive())()` | Checks if the current key hold action is running |
| `boolean` | `[isStarted](#isStarted())()` | Checks if the key hold action thread has started holding the key |
| `boolean` | `[isStopped](#isStopped())()` | Checks if the current key hold action was stopped through [`stop()`](#stop()) |
| `void` | `[stop](#stop())()` | Stops the current key hold action |
| `void` | `[waitFor](#waitFor())()` | Waits for the key hold action to complete. |
| `boolean` | `[waitFor](#waitFor(long))​(long timeoutMs)` | Waits for the key hold action to complete up until the specified timeout. |
| `void` | `[waitForStart](#waitForStart())()` | Waits for the key hold action to start holding the key |
| `boolean` | `[waitForStart](#waitForStart(long))​(long timeoutMs)` | Waits for the key hold action to start holding the key, up to the specified timeout time |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### stop

```
public void stop()
```

Stops the current key hold action
- #### isStopped

```
public boolean isStopped()
```

Checks if the current key hold action was stopped through [`stop()`](#stop())

Returns:
true if the current key hold action was stopped via [`stop()`](#stop()), false otherwise
- #### isActive

```
public boolean isActive()
```

Checks if the current key hold action is running

Returns:
true if it is running, false otherwise
- #### isStarted

```
public boolean isStarted()
```

Checks if the key hold action thread has started holding the key

Returns:
true if the key hold action has started holding the key, false otherwise
- #### waitForStart

```
public void waitForStart()
```

Waits for the key hold action to start holding the key
- #### waitForStart

```
public boolean waitForStart​(long timeoutMs)
```

Waits for the key hold action to start holding the key, up to the specified timeout time

Parameters:
`timeoutMs` - the maximum amount of time in milliseconds to wait
Returns:
true if started, false otherwise
- #### waitFor

```
public void waitFor()
```

Waits for the key hold action to complete. Note this can wait indefinitely.
- #### waitFor

```
public boolean waitFor​(long timeoutMs)
```

Waits for the key hold action to complete up until the specified timeout.

Returns:
true if the key hold action ended, false if the timeout was reached