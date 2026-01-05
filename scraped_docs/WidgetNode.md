# WidgetNode (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/WidgetNode.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface WidgetNode
extends [Node](Node.html "interface in net.runelite.api")
```

Represents a widget as an iterable node.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | The ID of the widget. |
| `int` | `[getModalMode](#getModalMode())()` | |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getId

```
int getId()
```

The ID of the widget.

Returns:
the ID of the widget
See Also:
[`Widget`](widgets/Widget.html "interface in net.runelite.api.widgets")
- #### getModalMode

```
int getModalMode()
```

See Also:
[`WidgetModalMode`](widgets/WidgetModalMode.html "class in net.runelite.api.widgets")