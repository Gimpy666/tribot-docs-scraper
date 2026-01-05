# WidgetConfig (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/WidgetConfig.html

**Package:** Packagenet.runelite.api.widgets

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.widgets.WidgetConfig

* ---

```
public final class WidgetConfig
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Utility class used for defining options to be used on the click mask
of a [`Widget`](Widget.html "interface in net.runelite.api.widgets").

See Also:
[`Widget.getClickMask()`](Widget.html#getClickMask())

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[DRAG](#DRAG)` | Controls whether this widget can be dragged around. |
| `static int` | `[DRAG\_ON](#DRAG_ON)` | Controls whether this widget can have other widgets dragged onto it. |
| `static int` | `[SHOW\_MENU\_OPTION\_NINE](#SHOW_MENU_OPTION_NINE)` | Enables displaying a ninth option on a menu. |
| `static int` | `[USE\_GROUND\_ITEM](#USE_GROUND_ITEM)` | Can this widget be used on a item on the floor |
| `static int` | `[USE\_ITEM](#USE_ITEM)` | Deprecated. |
| `static int` | `[USE\_NPC](#USE_NPC)` | Can this widget be used on a NPC |
| `static int` | `[USE\_OBJECT](#USE_OBJECT)` | Can this widget be used on a game object |
| `static int` | `[USE\_PLAYER](#USE_PLAYER)` | Can this widget be used on a player |
| `static int` | `[USE\_WIDGET](#USE_WIDGET)` | Can this widget be used on a widget with the WIDGET\_USE\_TARGET flag |
| `static int` | `[WIDGET\_USE\_TARGET](#WIDGET_USE_TARGET)` | Can widgets with USE\_WIDGET be used on this widget |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[WidgetConfig](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[transmitAction](#transmitAction(int))​(int action)` | Does the action (zero bosed) get transmitted to the server
when clicked |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### SHOW\_MENU\_OPTION\_NINE

```
public static final int SHOW_MENU_OPTION_NINE
```

Enables displaying a ninth option on a menu.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.SHOW_MENU_OPTION_NINE)
- #### USE\_GROUND\_ITEM

```
public static final int USE_GROUND_ITEM
```

Can this widget be used on a item on the floor

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_GROUND_ITEM)
- #### USE\_NPC

```
public static final int USE_NPC
```

Can this widget be used on a NPC

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_NPC)
- #### USE\_OBJECT

```
public static final int USE_OBJECT
```

Can this widget be used on a game object

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_OBJECT)
- #### USE\_PLAYER

```
public static final int USE_PLAYER
```

Can this widget be used on a player

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_PLAYER)
- #### USE\_ITEM

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final int USE_ITEM
```

Deprecated.
Can this widget be used on a item in your inventory

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_ITEM)
- #### USE\_WIDGET

```
public static final int USE_WIDGET
```

Can this widget be used on a widget with the WIDGET\_USE\_TARGET flag

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.USE_WIDGET)
- #### DRAG

```
public static final int DRAG
```

Controls whether this widget can be dragged around.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.DRAG)
- #### DRAG\_ON

```
public static final int DRAG_ON
```

Controls whether this widget can have other widgets dragged onto it.

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.DRAG_ON)
- #### WIDGET\_USE\_TARGET

```
public static final int WIDGET_USE_TARGET
```

Can widgets with USE\_WIDGET be used on this widget

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetConfig.WIDGET_USE_TARGET)

+ ### Constructor Detail

- #### WidgetConfig

```
public WidgetConfig()
```

+ ### Method Detail

- #### transmitAction

```
public static int transmitAction​(int action)
```

Does the action (zero bosed) get transmitted to the server
when clicked