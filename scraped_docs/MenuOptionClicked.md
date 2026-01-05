# MenuOptionClicked (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/MenuOptionClicked.html

**Package:** Packagenet.runelite.api.events

**Description:** This event does not only trigger when clicking an option in a
 right-clicked menu. The event will trigger for any left click
 action performed (ie. clicking an item, walking to a tile, etc) as
 well a...

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.MenuOptionClicked

* ---

```
public class MenuOptionClicked
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event where a menu option has been clicked.

This event does not only trigger when clicking an option in a
right-clicked menu. The event will trigger for any left click
action performed (ie. clicking an item, walking to a tile, etc) as
well as any right-click menu option.

By default, when there is no action performed when left-clicking,
it seems that this event still triggers with the "Cancel" action.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[MenuOptionClicked](#%3Cinit%3E(net.runelite.api.MenuEntry))​([MenuEntry](../MenuEntry.html "interface in net.runelite.api") menuEntry)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `void` | `[consume](#consume())()` | Marks the event as having been consumed. |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `int` | `[getActionParam](#getActionParam())()` | Deprecated. |
| `int` | `[getId](#getId())()` | The ID of the object, actor, or item that the interaction targets. |
| `int` | `[getItemId](#getItemId())()` | If this menu entry is an item op, get the item id |
| `int` | `[getItemOp](#getItemOp())()` | If this menu entry is an item op, get the item op id |
| `[MenuAction](../MenuAction.html "enum in net.runelite.api")` | `[getMenuAction](#getMenuAction())()` | The action performed. |
| `[MenuEntry](../MenuEntry.html "interface in net.runelite.api")` | `[getMenuEntry](#getMenuEntry())()` | The clicked menu entry |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getMenuOption](#getMenuOption())()` | The option text added to the menu. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getMenuTarget](#getMenuTarget())()` | The target of the action. |
| `int` | `[getParam0](#getParam0())()` | Action parameter 0. |
| `int` | `[getParam1](#getParam1())()` | Action parameter 1. |
| `[Widget](../widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget())()` | Get the widget this menu entry is on, if this is a menu entry
with an associated widget. |
| `int` | `[getWidgetId](#getWidgetId())()` | Deprecated. |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[isConsumed](#isConsumed())()` | Whether or not the event has been consumed by a subscriber. |
| `boolean` | `[isItemOp](#isItemOp())()` | Test if this menu entry is an item op. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### MenuOptionClicked

```
public MenuOptionClicked​([MenuEntry](../MenuEntry.html "interface in net.runelite.api") menuEntry)
```

+ ### Method Detail

- #### getParam0

```
public int getParam0()
```

Action parameter 0. Its value depends on the menuAction.
- #### getParam1

```
public int getParam1()
```

Action parameter 1. Its value depends on the menuAction.
- #### getMenuOption

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getMenuOption()
```

The option text added to the menu.
- #### getMenuTarget

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getMenuTarget()
```

The target of the action.
- #### getMenuAction

```
public [MenuAction](../MenuAction.html "enum in net.runelite.api") getMenuAction()
```

The action performed.
- #### getId

```
public int getId()
```

The ID of the object, actor, or item that the interaction targets.
- #### isItemOp

```
public boolean isItemOp()
```

Test if this menu entry is an item op. "Use" and "Examine" are not considered item ops.

Returns:
- #### getItemOp

```
public int getItemOp()
```

If this menu entry is an item op, get the item op id

Returns:
1-5
- #### getItemId

```
public int getItemId()
```

If this menu entry is an item op, get the item id

Returns:
See Also:
`ItemID`
- #### getWidget

```
@Nullable
public [Widget](../widgets/Widget.html "interface in net.runelite.api.widgets") getWidget()
```

Get the widget this menu entry is on, if this is a menu entry
with an associated widget. Such as eg, CC\_OP.

Returns:
- #### consume

```
public void consume()
```

Marks the event as having been consumed.

Setting this state indicates that a plugin has processed the menu
option being clicked and that the event will not be passed on
for handling by vanilla client code.
- #### getActionParam

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public int getActionParam()
```

Deprecated.
- #### getWidgetId

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public int getWidgetId()
```

Deprecated.
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### canEqual

```
protected boolean canEqual​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)
```
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### getMenuEntry

```
public [MenuEntry](../MenuEntry.html "interface in net.runelite.api") getMenuEntry()
```

The clicked menu entry
- #### isConsumed

```
public boolean isConsumed()
```

Whether or not the event has been consumed by a subscriber.