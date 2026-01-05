# WidgetItem (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/WidgetItem.html

**Package:** Packagenet.runelite.api.widgets

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.widgets.WidgetItem

* ---

```
public class WidgetItem
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An item that is being represented in a [`Widget`](Widget.html "interface in net.runelite.api.widgets").

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[WidgetItem](#%3Cinit%3E(int,int,java.awt.Rectangle,net.runelite.api.widgets.Widget,java.awt.Rectangle))​(int id,
int quantity,
[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") canvasBounds,
[Widget](Widget.html "interface in net.runelite.api.widgets") widget,
[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") draggingCanvasBounds)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getCanvasBounds](#getCanvasBounds())()` | Get the area where the widget item is drawn on the canvas, accounting for drag |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getCanvasBounds](#getCanvasBounds(boolean))​(boolean dragging)` | Get the area where the widget item is drawn on the canvas |
| `[Point](../Point.html "class in net.runelite.api")` | `[getCanvasLocation](#getCanvasLocation())()` | Gets the upper-left coordinate of where the widget is being drawn
on the canvas, accounting for drag. |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getDraggingCanvasBounds](#getDraggingCanvasBounds())()` | The canvas bounds for the widget, if it is being dragged. |
| `int` | `[getId](#getId())()` | The ID of the item represented. |
| `int` | `[getQuantity](#getQuantity())()` | The quantity of the represented item. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget())()` | The widget which contains this item. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### WidgetItem

```
public WidgetItem​(int id,
int quantity,
[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") canvasBounds,
[Widget](Widget.html "interface in net.runelite.api.widgets") widget,
@Nullable
[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") draggingCanvasBounds)
```

+ ### Method Detail

- #### getCanvasBounds

```
public [Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") getCanvasBounds()
```

Get the area where the widget item is drawn on the canvas, accounting for drag

Returns:
- #### getCanvasBounds

```
public [Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") getCanvasBounds​(boolean dragging)
```

Get the area where the widget item is drawn on the canvas

Parameters:
`dragging` - whether the returned area should account for widget drag
Returns:
- #### getCanvasLocation

```
public [Point](../Point.html "class in net.runelite.api") getCanvasLocation()
```

Gets the upper-left coordinate of where the widget is being drawn
on the canvas, accounting for drag.

Returns:
the upper-left coordinate of where this widget is drawn
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### getId

```
public int getId()
```

The ID of the item represented.

See Also:
`ItemID`
- #### getQuantity

```
public int getQuantity()
```

The quantity of the represented item.
- #### getWidget

```
public [Widget](Widget.html "interface in net.runelite.api.widgets") getWidget()
```

The widget which contains this item.
- #### getDraggingCanvasBounds

```
@Nullable
public [Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") getDraggingCanvasBounds()
```

The canvas bounds for the widget, if it is being dragged.