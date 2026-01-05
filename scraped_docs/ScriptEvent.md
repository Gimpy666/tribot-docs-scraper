# ScriptEvent (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ScriptEvent.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface ScriptEvent
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[KEY\_CHAR](#KEY_CHAR)` | |
| `static int` | `[KEY\_CODE](#KEY_CODE)` | |
| `static int` | `[MENU\_OP](#MENU_OP)` | |
| `static int` | `[MOUSE\_X](#MOUSE_X)` | |
| `static int` | `[MOUSE\_Y](#MOUSE_Y)` | |
| `static [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[NAME](#NAME)` | |
| `static int` | `[WIDGET\_ID](#WIDGET_ID)` | |
| `static int` | `[WIDGET\_INDEX](#WIDGET_INDEX)` | |
| `static int` | `[WIDGET\_TARGET\_ID](#WIDGET_TARGET_ID)` | |
| `static int` | `[WIDGET\_TARGET\_INDEX](#WIDGET_TARGET_INDEX)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getArguments](#getArguments())()` | Arguments passed to the script. |
| `int` | `[getMouseX](#getMouseX())()` | Parent relative x coordinate for mouse related events |
| `int` | `[getMouseY](#getMouseY())()` | Parent relative y coordinate for mouse related events |
| `int` | `[getOp](#getOp())()` | Gets the menu op of the event |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getOpbase](#getOpbase())()` | Gets the target of the menu option |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getSource](#getSource())()` | Gets the widget the [`WIDGET_ID`](#WIDGET_ID) and [`WIDGET_INDEX`](#WIDGET_INDEX) args
are substituted with |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getTarget](#getTarget())()` | Gets the [`Widget`](widgets/Widget.html "interface in net.runelite.api.widgets") target. |
| `int` | `[getTypedKeyChar](#getTypedKeyChar())()` | Get the typed character, ascii. |
| `int` | `[getTypedKeyCode](#getTypedKeyCode())()` | Jagex typed keycode |
| `void` | `[run](#run())()` | Executes a cs2 script specified by this event

This method must be ran on the client thread and is not reentrant |
| `[ScriptEvent](ScriptEvent.html "interface in net.runelite.api")` | `[setOp](#setOp(int))​(int op)` | Set the menu op of the event |
| `[ScriptEvent](ScriptEvent.html "interface in net.runelite.api")` | `[setSource](#setSource(net.runelite.api.widgets.Widget))​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") widget)` | Sets the widget the [`WIDGET_ID`](#WIDGET_ID) and [`WIDGET_INDEX`](#WIDGET_INDEX) args
are substituted with. |
| `[ScriptEvent](ScriptEvent.html "interface in net.runelite.api")` | `[setTarget](#setTarget(net.runelite.api.widgets.Widget))​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") target)` | Sets the [`Widget`](widgets/Widget.html "interface in net.runelite.api.widgets") target. |

* + ### Field Detail

- #### MOUSE\_X

```
static final int MOUSE_X
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.MOUSE_X)
- #### MOUSE\_Y

```
static final int MOUSE_Y
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.MOUSE_Y)
- #### MENU\_OP

```
static final int MENU_OP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.MENU_OP)
- #### WIDGET\_ID

```
static final int WIDGET_ID
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.WIDGET_ID)
- #### WIDGET\_INDEX

```
static final int WIDGET_INDEX
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.WIDGET_INDEX)
- #### WIDGET\_TARGET\_ID

```
static final int WIDGET_TARGET_ID
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.WIDGET_TARGET_ID)
- #### WIDGET\_TARGET\_INDEX

```
static final int WIDGET_TARGET_INDEX
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.WIDGET_TARGET_INDEX)
- #### KEY\_CODE

```
static final int KEY_CODE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.KEY_CODE)
- #### KEY\_CHAR

```
static final int KEY_CHAR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.KEY_CHAR)
- #### NAME

```
static final [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") NAME
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptEvent.NAME)

+ ### Method Detail

- #### getSource

```
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getSource()
```

Gets the widget the [`WIDGET_ID`](#WIDGET_ID) and [`WIDGET_INDEX`](#WIDGET_INDEX) args
are substituted with
- #### setSource

```
[ScriptEvent](ScriptEvent.html "interface in net.runelite.api") setSource​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") widget)
```

Sets the widget the [`WIDGET_ID`](#WIDGET_ID) and [`WIDGET_INDEX`](#WIDGET_INDEX) args
are substituted with. This is useful for running widget listeners

See Also:
[`Widget.getOnLoadListener()`](widgets/Widget.html#getOnLoadListener())
- #### getTarget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getTarget()
```

Gets the [`Widget`](widgets/Widget.html "interface in net.runelite.api.widgets") target. This is only used for the drag complete listener

Returns:
See Also:
[`Widget.setOnDragCompleteListener(Object...)`](widgets/Widget.html#setOnDragCompleteListener(java.lang.Object...))
- #### setTarget

```
[ScriptEvent](ScriptEvent.html "interface in net.runelite.api") setTarget​([Widget](widgets/Widget.html "interface in net.runelite.api.widgets") target)
```

Sets the [`Widget`](widgets/Widget.html "interface in net.runelite.api.widgets") target. This is only used for the drag complete listener.

Parameters:
`target` -
Returns:
See Also:
[`Widget.setOnDragCompleteListener(Object...)`](widgets/Widget.html#setOnDragCompleteListener(java.lang.Object...))
- #### getArguments

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getArguments()
```

Arguments passed to the script. Index 0 is the script being run and is not an argument.

Returns:
- #### getOp

```
int getOp()
```

Gets the menu op of the event

Returns:
the menu op
- #### setOp

```
[ScriptEvent](ScriptEvent.html "interface in net.runelite.api") setOp​(int op)
```

Set the menu op of the event

Parameters:
`op` -
- #### getOpbase

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getOpbase()
```

Gets the target of the menu option

Returns:
the target
See Also:
[`MenuOptionClicked`](events/MenuOptionClicked.html "class in net.runelite.api.events")
- #### getMouseX

```
int getMouseX()
```

Parent relative x coordinate for mouse related events
- #### getMouseY

```
int getMouseY()
```

Parent relative y coordinate for mouse related events
- #### getTypedKeyCode

```
int getTypedKeyCode()
```

Jagex typed keycode

Returns:
- #### getTypedKeyChar

```
int getTypedKeyChar()
```

Get the typed character, ascii.

Returns:
- #### run

```
void run()
```

Executes a cs2 script specified by this event

This method must be ran on the client thread and is not reentrant