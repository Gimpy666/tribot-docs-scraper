# ScriptListening (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/ScriptListening.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.ScriptListening

* ---

```
public class ScriptListening
extends java.lang.Object
```

Contains listeners for script events. These are scoped to the script and are removed when it ends.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ScriptListening](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[addBreakEndListener](#addBreakEndListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run when a break ends |
| `static void` | `[addBreakStartListener](#addBreakStartListener(org.tribot.script.sdk.interfaces.BreakStartListener))​([BreakStartListener](interfaces/BreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a listener that will run when a break starts |
| `static void` | `[addEndingListener](#addEndingListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run when the script ends. |
| `static void` | `[addKeyEventOverrideListener](#addKeyEventOverrideListener(org.tribot.script.sdk.interfaces.KeyEventOverrideListener))​([KeyEventOverrideListener](interfaces/KeyEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a key event override listener |
| `static void` | `[addMouseClickListener](#addMouseClickListener(org.tribot.script.sdk.interfaces.MouseClickListener))​([MouseClickListener](interfaces/MouseClickListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a mouse click listener |
| `static void` | `[addMouseDragListener](#addMouseDragListener(org.tribot.script.sdk.interfaces.MouseDragListener))​([MouseDragListener](interfaces/MouseDragListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a mouse drag listener |
| `static void` | `[addMouseEventOverrideListener](#addMouseEventOverrideListener(org.tribot.script.sdk.interfaces.MouseEventOverrideListener))​([MouseEventOverrideListener](interfaces/MouseEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a mouse event override listener |
| `static void` | `[addMouseMoveListener](#addMouseMoveListener(org.tribot.script.sdk.interfaces.MouseMoveListener))​([MouseMoveListener](interfaces/MouseMoveListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a mouse move listener |
| `static void` | `[addMouseReleaseListener](#addMouseReleaseListener(org.tribot.script.sdk.interfaces.MouseReleaseListener))​([MouseReleaseListener](interfaces/MouseReleaseListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a mouse release listener |
| `static void` | `[addPauseListener](#addPauseListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run when the script is paused by the pause button |
| `static void` | `[addPreBreakStartListener](#addPreBreakStartListener(org.tribot.script.sdk.interfaces.PreBreakStartListener))​([PreBreakStartListener](interfaces/PreBreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Adds a listener that will run before a break starts, before the break handler actually triggers. |
| `static void` | `[addPreEndingListener](#addPreEndingListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run right before the script ends. |
| `static void` | `[addResumeListener](#addResumeListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Adds a listener that will run when the script is resumed by the resume button |
| `static void` | `[removeBreakEndListener](#removeBreakEndListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes a break end listener |
| `static void` | `[removeBreakStartListener](#removeBreakStartListener(org.tribot.script.sdk.interfaces.BreakStartListener))​([BreakStartListener](interfaces/BreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a break start listener |
| `static void` | `[removeEndingListener](#removeEndingListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes an ending listener |
| `static void` | `[removeKeyEventOverrideListener](#removeKeyEventOverrideListener(org.tribot.script.sdk.interfaces.KeyEventOverrideListener))​([KeyEventOverrideListener](interfaces/KeyEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a key event override listener |
| `static void` | `[removeMouseClickListener](#removeMouseClickListener(org.tribot.script.sdk.interfaces.MouseClickListener))​([MouseClickListener](interfaces/MouseClickListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a mouse click listener |
| `static void` | `[removeMouseDragListener](#removeMouseDragListener(org.tribot.script.sdk.interfaces.MouseDragListener))​([MouseDragListener](interfaces/MouseDragListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a mouse drag listener |
| `static void` | `[removeMouseEventOverrideListener](#removeMouseEventOverrideListener(org.tribot.script.sdk.interfaces.MouseEventOverrideListener))​([MouseEventOverrideListener](interfaces/MouseEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a mouse event override listener |
| `static void` | `[removeMouseMoveListener](#removeMouseMoveListener(org.tribot.script.sdk.interfaces.MouseMoveListener))​([MouseMoveListener](interfaces/MouseMoveListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a mouse move listener |
| `static void` | `[removeMouseReleaseListener](#removeMouseReleaseListener(org.tribot.script.sdk.interfaces.MouseReleaseListener))​([MouseReleaseListener](interfaces/MouseReleaseListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a mouse release listener |
| `static void` | `[removePauseListener](#removePauseListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes a pause listener |
| `static void` | `[removePreBreakStartListener](#removePreBreakStartListener(org.tribot.script.sdk.interfaces.PreBreakStartListener))​([PreBreakStartListener](interfaces/PreBreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a pre break start listener |
| `static void` | `[removePreEndingListener](#removePreEndingListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes a pre ending listener |
| `static void` | `[removeResumeListener](#removeResumeListener(java.lang.Runnable))​(java.lang.Runnable listener)` | Removes a resume listener |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ScriptListening

```
public ScriptListening()
```

+ ### Method Detail

- #### addBreakEndListener

```
public static void addBreakEndListener​(java.lang.Runnable listener)
```

Adds a listener that will run when a break ends

Parameters:
`listener` - the break end listener
- #### removeBreakEndListener

```
public static void removeBreakEndListener​(java.lang.Runnable listener)
```

Removes a break end listener

Parameters:
`listener` - the listener to remove
- #### addBreakStartListener

```
public static void addBreakStartListener​([BreakStartListener](interfaces/BreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a listener that will run when a break starts

Parameters:
`listener` - the break start listener
- #### removeBreakStartListener

```
public static void removeBreakStartListener​([BreakStartListener](interfaces/BreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a break start listener

Parameters:
`listener` - the listener to remove
- #### addPreBreakStartListener

```
public static void addPreBreakStartListener​([PreBreakStartListener](interfaces/PreBreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a listener that will run before a break starts, before the break handler actually triggers. This can be used to prevent breaking while not in combat, for example.

Parameters:
`listener` - the pre break start listener
- #### removePreBreakStartListener

```
public static void removePreBreakStartListener​([PreBreakStartListener](interfaces/PreBreakStartListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a pre break start listener

Parameters:
`listener` - the listener to remove
- #### addEndingListener

```
public static void addEndingListener​(java.lang.Runnable listener)
```

Adds a listener that will run when the script ends. This is useful for cleanup tasks.

Parameters:
`listener` - the script end listener
- #### removeEndingListener

```
public static void removeEndingListener​(java.lang.Runnable listener)
```

Removes an ending listener

Parameters:
`listener` - the listener to remove
- #### addPreEndingListener

```
public static void addPreEndingListener​(java.lang.Runnable listener)
```

Adds a listener that will run right before the script ends. This is useful for cleanup tasks.

Parameters:
`listener` - the script pre end listener
- #### removePreEndingListener

```
public static void removePreEndingListener​(java.lang.Runnable listener)
```

Removes a pre ending listener

Parameters:
`listener` - the listener to remove
- #### addPauseListener

```
public static void addPauseListener​(java.lang.Runnable listener)
```

Adds a listener that will run when the script is paused by the pause button

Parameters:
`listener` - the script pause listener
- #### removePauseListener

```
public static void removePauseListener​(java.lang.Runnable listener)
```

Removes a pause listener

Parameters:
`listener` - the listener to remove
- #### addResumeListener

```
public static void addResumeListener​(java.lang.Runnable listener)
```

Adds a listener that will run when the script is resumed by the resume button

Parameters:
`listener` - the script resume listener
- #### removeResumeListener

```
public static void removeResumeListener​(java.lang.Runnable listener)
```

Removes a resume listener

Parameters:
`listener` - the listener to remove
- #### addMouseClickListener

```
public static void addMouseClickListener​([MouseClickListener](interfaces/MouseClickListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a mouse click listener

Parameters:
`listener` - the mouse click listener
- #### removeMouseClickListener

```
public static void removeMouseClickListener​([MouseClickListener](interfaces/MouseClickListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a mouse click listener

Parameters:
`listener` - the listener to remove
- #### addMouseDragListener

```
public static void addMouseDragListener​([MouseDragListener](interfaces/MouseDragListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a mouse drag listener

Parameters:
`listener` - the mouse drag listener
- #### removeMouseDragListener

```
public static void removeMouseDragListener​([MouseDragListener](interfaces/MouseDragListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a mouse drag listener

Parameters:
`listener` - the listener to remove
- #### addMouseMoveListener

```
public static void addMouseMoveListener​([MouseMoveListener](interfaces/MouseMoveListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a mouse move listener

Parameters:
`listener` - the mouse move listener
- #### removeMouseMoveListener

```
public static void removeMouseMoveListener​([MouseMoveListener](interfaces/MouseMoveListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a mouse move listener

Parameters:
`listener` - the listener to remove
- #### addMouseReleaseListener

```
public static void addMouseReleaseListener​([MouseReleaseListener](interfaces/MouseReleaseListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a mouse release listener

Parameters:
`listener` - the mouse release listener
- #### removeMouseReleaseListener

```
public static void removeMouseReleaseListener​([MouseReleaseListener](interfaces/MouseReleaseListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a mouse release listener

Parameters:
`listener` - the listener to remove
- #### addMouseEventOverrideListener

```
public static void addMouseEventOverrideListener​([MouseEventOverrideListener](interfaces/MouseEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a mouse event override listener

Parameters:
`listener` - the mouse event override listener
- #### removeMouseEventOverrideListener

```
public static void removeMouseEventOverrideListener​([MouseEventOverrideListener](interfaces/MouseEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a mouse event override listener

Parameters:
`listener` - the mouse event override to remove
- #### addKeyEventOverrideListener

```
public static void addKeyEventOverrideListener​([KeyEventOverrideListener](interfaces/KeyEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Adds a key event override listener

Parameters:
`listener` - the key event override listener
- #### removeKeyEventOverrideListener

```
public static void removeKeyEventOverrideListener​([KeyEventOverrideListener](interfaces/KeyEventOverrideListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a key event override listener

Parameters:
`listener` - the key event override to remove