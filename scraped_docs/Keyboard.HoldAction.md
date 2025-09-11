# Keyboard.HoldAction (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Keyboard.HoldAction.html

**Package:** Packageorg.tribot.script.sdk.input

---

* java.lang.Object
* + org.tribot.script.sdk.input.Keyboard.HoldAction

* Enclosing class:
[Keyboard](Keyboard.html "class in org.tribot.script.sdk.input")

---

```
public static class Keyboard.HoldAction
extends java.lang.Object
```

Represents a key hold configuration

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input")` | Represents a key that can be held. |
| `static class` | `[Keyboard.HoldAction.KeyHoldContext](Keyboard.HoldAction.KeyHoldContext.html "class in org.tribot.script.sdk.input")` | Represents the context of a current key hold action. |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[key](#key(char))​(char key)` | Specifies the key to use for this hold action |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[key](#key(char,int))​(char key,
int keyCode)` | Specifies the key and keyCode to use for this hold action |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[key](#key(org.tribot.script.sdk.input.Keyboard.HoldAction.Key))​([Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") key)` | Specifies the key to use for this hold action |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[presses](#presses(int))​(int presses)` | Specifies this hold action should press the key the specified amount of times. |
| `[Keyboard.HoldAction.KeyHoldContext](Keyboard.HoldAction.KeyHoldContext.html "class in org.tribot.script.sdk.input")` | `[start](#start())()` | Starts this hold action. |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[timeout](#timeout(long))​(long timeout)` | Specifies this hold action should execute for a maximum amount of time. |
| `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[until](#until(java.util.function.BooleanSupplier))​(java.util.function.BooleanSupplier stopCondition)` | Specifies a stop condition for this hold action. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### key

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") key​(char key)
```

Specifies the key to use for this hold action

Parameters:
`key` - the key to use for this hold action
Returns:
this hold action
- #### key

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") key​(char key,
int keyCode)
```

Specifies the key and keyCode to use for this hold action

Parameters:
`key` - the key to use for this hold action
`keyCode` - the keyCode to use for this hold action
Returns:
this hold action
- #### key

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") key​([Keyboard.HoldAction.Key](Keyboard.HoldAction.Key.html "enum in org.tribot.script.sdk.input") key)
```

Specifies the key to use for this hold action

Parameters:
`key` - the key to use for this hold action
Returns:
this hold action
- #### until

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") until​(java.util.function.BooleanSupplier stopCondition)
```

Specifies a stop condition for this hold action. It will terminate when this condition is true. Optional.

Parameters:
`stopCondition` - the stop condition for this hold action
Returns:
this hold action
- #### timeout

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") timeout​(long timeout)
```

Specifies this hold action should execute for a maximum amount of time. Optional.

Parameters:
`timeout` - the timeout of this hold action, if this is exceeded the hold action will end
Returns:
this hold action
- #### presses

```
public [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") presses​(int presses)
```

Specifies this hold action should press the key the specified amount of times. Optional.

Parameters:
`presses` - the amount of times to press the key
Returns:
this hold action
- #### start

```
public [Keyboard.HoldAction.KeyHoldContext](Keyboard.HoldAction.KeyHoldContext.html "class in org.tribot.script.sdk.input") start()
```

Starts this hold action.
Note that the hold action runs on a separate thread

Returns:
a [`Keyboard.HoldAction.KeyHoldContext`](Keyboard.HoldAction.KeyHoldContext.html "class in org.tribot.script.sdk.input") that can be used to interrupt the key hold action