# Callbacks (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/hooks/Callbacks.html

**Package:** Packagenet.runelite.api.hooks

---

* ---

```
public interface Callbacks
```

Interface of callbacks the injected client uses to send events

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[draw](#draw(net.runelite.api.MainBufferProvider,java.awt.Graphics,int,int))​([MainBufferProvider](../MainBufferProvider.html "interface in net.runelite.api") mainBufferProvider,
[Graphics](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics.html?is-external=true "class or interface in java.awt") graphics,
int x,
int y)` | Client top-most draw method, rendering over top of most of game interfaces. |
| `boolean` | `[draw](#draw(net.runelite.api.Renderable,boolean))​([Renderable](../Renderable.html "interface in net.runelite.api") renderable,
boolean drawingUi)` | Called to test if a renderable should be drawn this frame |
| `void` | `[drawAboveOverheads](#drawAboveOverheads())()` | Called after logic that is drawing 2D objects is processed. |
| `void` | `[drawInterface](#drawInterface(int,java.util.List))​(int interfaceId,
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WidgetItem](../widgets/WidgetItem.html "class in net.runelite.api.widgets")> widgetItems)` | Called after an interface has been drawn |
| `void` | `[drawLayer](#drawLayer(net.runelite.api.widgets.Widget,java.util.List))​([Widget](../widgets/Widget.html "interface in net.runelite.api.widgets") layer,
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WidgetItem](../widgets/WidgetItem.html "class in net.runelite.api.widgets")> widgetItems)` | Called after a widget layer has been drawn |
| `void` | `[drawScene](#drawScene())()` | Called after the scene is drawn. |
| `void` | `[error](#error(java.lang.String,java.lang.Throwable))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html?is-external=true "class or interface in java.lang") reason)` | Called when a client error occurs |
| `void` | `[frame](#frame())()` | Called each frame |
| `boolean` | `[isRuneLiteClientOutdated](#isRuneLiteClientOutdated())()` | Returns if the current runelite client is outdated or not |
| `void` | `[keyPressed](#keyPressed(java.awt.event.KeyEvent))​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)` | Key pressed event. |
| `void` | `[keyReleased](#keyReleased(java.awt.event.KeyEvent))​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)` | Key released event. |
| `void` | `[keyTyped](#keyTyped(java.awt.event.KeyEvent))​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)` | Key typed event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseClicked](#mouseClicked(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse clicked event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseDragged](#mouseDragged(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse dragged event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseEntered](#mouseEntered(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse entered event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseExited](#mouseExited(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse exited event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseMoved](#mouseMoved(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse moved event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mousePressed](#mousePressed(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse pressed event. |
| `[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseReleased](#mouseReleased(java.awt.event.MouseEvent))​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)` | Mouse released event. |
| `[MouseWheelEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseWheelEvent.html?is-external=true "class or interface in java.awt.event")` | `[mouseWheelMoved](#mouseWheelMoved(java.awt.event.MouseWheelEvent))​([MouseWheelEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseWheelEvent.html?is-external=true "class or interface in java.awt.event") event)` | Mouse wheel moved event. |
| `void` | `[openUrl](#openUrl(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") url)` | Called when the client wants to open a URL |
| `void` | `[post](#post(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") event)` | Post an event. |
| `void` | `[postDeferred](#postDeferred(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") event)` | Post a deferred event, which gets delayed until the next cycle. |
| `void` | `[serverTick](#serverTick())()` | Called each server tick |
| `void` | `[tick](#tick())()` | Called at the beginning of each tick |
| `void` | `[tickEnd](#tickEnd())()` | Called at the end of each tick |

* + ### Method Detail

- #### post

```
void post​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") event)
```

Post an event. See the events in net.runelite.api.events.

Parameters:
`event` - the event
- #### postDeferred

```
void postDeferred​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") event)
```

Post a deferred event, which gets delayed until the next cycle.

Parameters:
`event` - the event
- #### tick

```
void tick()
```

Called at the beginning of each tick
- #### tickEnd

```
void tickEnd()
```

Called at the end of each tick
- #### frame

```
void frame()
```

Called each frame
- #### serverTick

```
void serverTick()
```

Called each server tick
- #### drawScene

```
void drawScene()
```

Called after the scene is drawn.
- #### drawAboveOverheads

```
void drawAboveOverheads()
```

Called after logic that is drawing 2D objects is processed.
- #### draw

```
void draw​([MainBufferProvider](../MainBufferProvider.html "interface in net.runelite.api") mainBufferProvider,
[Graphics](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics.html?is-external=true "class or interface in java.awt") graphics,
int x,
int y)
```

Client top-most draw method, rendering over top of most of game interfaces.

Parameters:
`mainBufferProvider` - the main buffer provider
`graphics` - the graphics
`x` - the x
`y` - the y
- #### drawInterface

```
void drawInterface​(int interfaceId,
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WidgetItem](../widgets/WidgetItem.html "class in net.runelite.api.widgets")> widgetItems)
```

Called after an interface has been drawn

Parameters:
`interfaceId` - the interface id
`widgetItems` - Widget items within the interface
- #### drawLayer

```
void drawLayer​([Widget](../widgets/Widget.html "interface in net.runelite.api.widgets") layer,
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[WidgetItem](../widgets/WidgetItem.html "class in net.runelite.api.widgets")> widgetItems)
```

Called after a widget layer has been drawn

Parameters:
`layer` - The layer
`widgetItems` - Widget items within the layer
- #### mousePressed

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mousePressed​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse pressed event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseReleased

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseReleased​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse released event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseClicked

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseClicked​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse clicked event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseEntered

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEntered​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse entered event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseExited

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseExited​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse exited event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseDragged

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseDragged​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse dragged event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseMoved

```
[MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseMoved​([MouseEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseEvent.html?is-external=true "class or interface in java.awt.event") mouseEvent)
```

Mouse moved event. If this event will be consumed it will not be propagated further to client.

Parameters:
`mouseEvent` - the mouse event
Returns:
the mouse event
- #### mouseWheelMoved

```
[MouseWheelEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseWheelEvent.html?is-external=true "class or interface in java.awt.event") mouseWheelMoved​([MouseWheelEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/MouseWheelEvent.html?is-external=true "class or interface in java.awt.event") event)
```

Mouse wheel moved event. If this event will be consumed it will not be propagated further to client.

Parameters:
`event` - the event
Returns:
the mouse wheel event
- #### keyPressed

```
void keyPressed​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)
```

Key pressed event.

Parameters:
`keyEvent` - the key event
- #### keyReleased

```
void keyReleased​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)
```

Key released event.

Parameters:
`keyEvent` - the key event
- #### keyTyped

```
void keyTyped​([KeyEvent](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/event/KeyEvent.html?is-external=true "class or interface in java.awt.event") keyEvent)
```

Key typed event.

Parameters:
`keyEvent` - the key event
- #### draw

```
boolean draw​([Renderable](../Renderable.html "interface in net.runelite.api") renderable,
boolean drawingUi)
```

Called to test if a renderable should be drawn this frame

Parameters:
`renderable` - the renderable
`drawingUi` - if this is the 2d ui, such as hp bars or hitsplats
Returns:
false to prevent drawing
- #### error

```
void error​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html?is-external=true "class or interface in java.lang") reason)
```

Called when a client error occurs

Parameters:
`message` -
`reason` -
- #### openUrl

```
void openUrl​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") url)
```

Called when the client wants to open a URL

Parameters:
`url` -
- #### isRuneLiteClientOutdated

```
boolean isRuneLiteClientOutdated()
```

Returns if the current runelite client is outdated or not

Returns: