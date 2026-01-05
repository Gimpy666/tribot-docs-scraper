# Widget (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/Widget.html

**Package:** Packagenet.runelite.api.widgets

**Description:** It should be noted that most RuneLite-added elements are not Widgets, but are
 an Overlay. Notable exceptions include bank tag tabs and chatbox inputsExamples of Widgets include:The fairy ring configu...

---

* ---

```
public interface Widget
```

Represents an on-screen UI element that is drawn on the canvas.

It should be noted that most RuneLite-added elements are not Widgets, but are
an Overlay. Notable exceptions include bank tag tabs and chatbox inputs

Examples of Widgets include:

+ The fairy ring configuration selector
+ The mini-map
+ The bank inventory

For a more complete idea of what is classified as a widget, see [`WidgetID`](WidgetID.html "class in net.runelite.api.widgets").

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `void` | `[clearActions](#clearActions())()` | Clear the menu options on a widget. |
| `boolean` | `[contains](#contains(net.runelite.api.Point))​([Point](../Point.html "class in net.runelite.api") point)` | Checks if the passed canvas points is inside of this widget's
[`bounds`](#getBounds()) |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[createChild](#createChild(int))​(int type)` | Creates a dynamic widget child at the end of the children list |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[createChild](#createChild(int,int))​(int index,
int type)` | Creates a dynamic widget child |
| `void` | `[deleteAllChildren](#deleteAllChildren())()` | Removes all of this widget's dynamic children |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[]` | `[getActions](#getActions())()` | Gets the menu options available on the widget as a sparse array. |
| `int` | `[getAnimationId](#getAnimationId())()` | Gets the sequence ID used to animate the model in the widget |
| `int` | `[getBorderType](#getBorderType())()` | Returns the border type of item/sprite on the widget
0 - No border
1 - 1px black border
2 - 1px black under 1px white border (selected item) |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getBounds](#getBounds())()` | Gets the area where the widget is drawn on the canvas. |
| `[Point](../Point.html "class in net.runelite.api")` | `[getCanvasLocation](#getCanvasLocation())()` | Gets the location the widget is being drawn on the canvas. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[getChild](#getChild(int))​(int index)` | Gets a dynamic child by index |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")[]` | `[getChildren](#getChildren())()` | Gets the dynamic children of this widget in a sparse array |
| `int` | `[getClickMask](#getClickMask())()` | Gets the current click configuration of the widget. |
| `int` | `[getContentType](#getContentType())()` | Gets the type of content displayed by the widget. |
| `int` | `[getDragDeadTime](#getDragDeadTime())()` | Returns the widget drag dead time |
| `int` | `[getDragDeadZone](#getDragDeadZone())()` | Returns the widget drag dead zone |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[getDragParent](#getDragParent())()` | Container this can be dragged in |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")[]` | `[getDynamicChildren](#getDynamicChildren())()` | Gets all dynamic children. |
| `[FontTypeFace](../FontTypeFace.html "interface in net.runelite.api")` | `[getFont](#getFont())()` | Gets the font that this widget uses |
| `int` | `[getFontId](#getFontId())()` | Returns the archive id of the font used |
| `int` | `[getHeight](#getHeight())()` | Gets the height of the widget. |
| `int` | `[getHeightMode](#getHeightMode())()` | Gets the mode controlling widget width |
| `int` | `[getId](#getId())()` | Gets the widgets ID. |
| `int` | `[getIndex](#getIndex())()` | The index of this widget in it's parent's children array |
| `int` | `[getItemId](#getItemId())()` | Gets the item ID displayed by the widget. |
| `int` | `[getItemQuantity](#getItemQuantity())()` | Gets the quantity of the item displayed by the widget. |
| `int` | `[getItemQuantityMode](#getItemQuantityMode())()` | Returns widget [`ItemQuantityMode`](ItemQuantityMode.html "class in net.runelite.api.widgets"). |
| `int` | `[getLineHeight](#getLineHeight())()` | Get the line height for this widget. |
| `int` | `[getModelId](#getModelId())()` | Gets the Model/NPC/Item ID displayed in the widget. |
| `int` | `[getModelType](#getModelType())()` | Gets the model type of the widget. |
| `int` | `[getModelZoom](#getModelZoom())()` | Gets the amount zoomed in on the model displayed in the widget. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name "op base" of the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")[]` | `[getNestedChildren](#getNestedChildren())()` | Gets all nested children. |
| `boolean` | `[getNoClickThrough](#getNoClickThrough())()` | Can widgets under this widgets be clicked in this widgets bounding box |
| `boolean` | `[getNoScrollThrough](#getNoScrollThrough())()` | Can widgets under this widgets be scrolled in this widgets bounding box |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getOnInvTransmitListener](#getOnInvTransmitListener())()` | Gets the script and arguments to be ran when one of the listened for inventories changes. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getOnKeyListener](#getOnKeyListener())()` | Gets the script and arguments to be ran when a key is pressed. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getOnLoadListener](#getOnLoadListener())()` | Gets the script and arguments to be ran when a interface is loaded. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getOnOpListener](#getOnOpListener())()` | Gets the script and arguments to be ran when a menu action is clicked. |
| `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[]` | `[getOnVarTransmitListener](#getOnVarTransmitListener())()` | Gets the script and arguments to be ran when one of the listened for vars changes. |
| `int` | `[getOpacity](#getOpacity())()` | Gets the transparency of the rectangle |
| `int` | `[getOriginalHeight](#getOriginalHeight())()` | Gets the height coordinate of this widget before being adjusted by
[`getHeightMode()`](#getHeightMode()) |
| `int` | `[getOriginalWidth](#getOriginalWidth())()` | Gets the width coordinate of this widget before being adjusted by
[`getWidthMode()`](#getWidthMode()) |
| `int` | `[getOriginalX](#getOriginalX())()` | Gets the X coordinate of this widget before being adjusted by
[`getXPositionMode()`](#getXPositionMode())}. |
| `int` | `[getOriginalY](#getOriginalY())()` | Gets the Y coordinate of this widget before being adjusted by
[`getYPositionMode()`](#getYPositionMode())} |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[getParent](#getParent())()` | Gets the parent widget, if this widget is a child. |
| `int` | `[getParentId](#getParentId())()` | Gets the ID of the parent widget. |
| `int` | `[getRelativeX](#getRelativeX())()` | Gets the relative x-axis coordinate to the widgets parent. |
| `int` | `[getRelativeY](#getRelativeY())()` | Gets the relative y-axis coordinate to the widgets parent. |
| `@org.jetbrains.annotations.Range(from=0L, to=2047L) int` | `[getRotationX](#getRotationX())()` | Gets the x rotation of the model displayed in the widget. |
| `@org.jetbrains.annotations.Range(from=0L, to=2047L) int` | `[getRotationY](#getRotationY())()` | Gets the y rotation of the model displayed in the widget. |
| `@org.jetbrains.annotations.Range(from=0L, to=2047L) int` | `[getRotationZ](#getRotationZ())()` | Gets the z rotation of the model displayed in the widget. |
| `int` | `[getScrollHeight](#getScrollHeight())()` | Gets the size of the widget's viewport in the Y axis |
| `int` | `[getScrollWidth](#getScrollWidth())()` | Gets the size of the widget's viewport in the X axis |
| `int` | `[getScrollX](#getScrollX())()` | Gets the amount of pixels the widget is scrolled in the X axis |
| `int` | `[getScrollY](#getScrollY())()` | Gets the amount of pixels the widget is scrolled in the Y axis |
| `int` | `[getSpriteId](#getSpriteId())()` | Gets the sprite ID displayed in the widget. |
| `boolean` | `[getSpriteTiling](#getSpriteTiling())()` | Gets if sprites are repeated or stretched |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")[]` | `[getStaticChildren](#getStaticChildren())()` | Gets all static children. |
| `int` | `[getTargetPriority](#getTargetPriority())()` | Get the priority that the target verb op is at |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getTargetVerb](#getTargetVerb())()` | Verb for op targets |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getText](#getText())()` | Gets the text displayed on this widget. |
| `int` | `[getTextColor](#getTextColor())()` | Gets the color as an RGB value. |
| `boolean` | `[getTextShadowed](#getTextShadowed())()` | Returns if text is shadowed |
| `int` | `[getType](#getType())()` | Gets the type of the widget. |
| `int[]` | `[getVarTransmitTrigger](#getVarTransmitTrigger())()` | `VarPlayerID`s that triggers this widgets varTransmitListener |
| `int` | `[getWidth](#getWidth())()` | Gets the width of the widget. |
| `int` | `[getWidthMode](#getWidthMode())()` | Gets the mode controlling widget width |
| `int` | `[getXPositionMode](#getXPositionMode())()` | Gets the mode that the X position is calculated from the original X position |
| `int` | `[getXTextAlignment](#getXTextAlignment())()` | Gets the X axis text position mode |
| `int` | `[getYPositionMode](#getYPositionMode())()` | Gets the mode that the Y position is calculated from the original Y position |
| `int` | `[getYTextAlignment](#getYTextAlignment())()` | Gets the Y axis text position mode |
| `boolean` | `[hasListener](#hasListener())()` | If this widget has any listeners on it |
| `boolean` | `[isFilled](#isFilled())()` | Gets if the rectangle is filled or just stroked |
| `boolean` | `[isFlippedHorizontally](#isFlippedHorizontally())()` | Get if this graphic flipped horizontally |
| `boolean` | `[isFlippedVertically](#isFlippedVertically())()` | Get if this graphic flipped vertically |
| `boolean` | `[isHidden](#isHidden())()` | Checks whether this widget or any of its parents are hidden. |
| `boolean` | `[isIf3](#isIf3())()` | This is true if the widget is from an if3 interface, or is dynamically created |
| `boolean` | `[isSelfHidden](#isSelfHidden())()` | Checks whether this widget is hidden, not taking into account
any parent hidden states. |
| `void` | `[revalidate](#revalidate())()` | Recomputes this widget's x/y/w/h, excluding scroll |
| `void` | `[revalidateScroll](#revalidateScroll())()` | Recomputes this widget's group's x/y/w/h including scroll |
| `void` | `[setAction](#setAction(int,java.lang.String))​(int index,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") action)` | Creates a menu option on the widget |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setAnimationId](#setAnimationId(int))​(int animationId)` | Sets the sequence ID used to animate the model in the widget |
| `void` | `[setBorderType](#setBorderType(int))​(int thickness)` | |
| `void` | `[setChildren](#setChildren(net.runelite.api.widgets.Widget%5B%5D))​([Widget](Widget.html "interface in net.runelite.api.widgets")[] children)` | Sets the dynamic children sparse array |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setClickMask](#setClickMask(int))​(int mask)` | Sets the click configuration of the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setContentType](#setContentType(int))​(int contentType)` | Sets the type of content displayed by the widget. |
| `void` | `[setDragDeadTime](#setDragDeadTime(int))​(int deadTime)` | Sets the widget drag dead time |
| `void` | `[setDragDeadZone](#setDragDeadZone(int))​(int deadZone)` | Sets the widget drag dead zone |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setDragParent](#setDragParent(net.runelite.api.widgets.Widget))​([Widget](Widget.html "interface in net.runelite.api.widgets") dragParent)` | Container this can be dragged in |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setFilled](#setFilled(boolean))​(boolean filled)` | Sets if the rectangle is filled or just stroked |
| `void` | `[setFlippedHorizontally](#setFlippedHorizontally(boolean))​(boolean flip)` | Set if this graphic is flipped horizontally |
| `void` | `[setFlippedVertically](#setFlippedVertically(boolean))​(boolean flip)` | Set if this graphic is flipped vertically |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setFontId](#setFontId(int))​(int id)` | Sets the archive id of the font |
| `void` | `[setForcedPosition](#setForcedPosition(int,int))​(int x,
int y)` | Set a forced position for the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setHasListener](#setHasListener(boolean))​(boolean hasListener)` | Sets if the widget has any listeners. |
| `void` | `[setHeight](#setHeight(int))​(int height)` | Deprecated. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setHeightMode](#setHeightMode(int))​(int heightMode)` | Sets the mode controlling widget width. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setHidden](#setHidden(boolean))​(boolean hidden)` | Sets the self-hidden state of this widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setItemId](#setItemId(int))​(int itemId)` | Sets the item ID displayed by the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setItemQuantity](#setItemQuantity(int))​(int quantity)` | Sets the item quantity displayed by the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setItemQuantityMode](#setItemQuantityMode(int))​(int itemQuantityMode)` | Sets the widget [`ItemQuantityMode`](ItemQuantityMode.html "class in net.runelite.api.widgets") |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setLineHeight](#setLineHeight(int))​(int lineHeight)` | Set the line height for this widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setModelId](#setModelId(int))​(int id)` | Sets the Model/NPC/Item ID displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setModelType](#setModelType(int))​(int type)` | Sets the model type of the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setModelZoom](#setModelZoom(int))​(int modelZoom)` | Sets the amount zoomed in on the model displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setName](#setName(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Sets the name of the widget. |
| `void` | `[setNoClickThrough](#setNoClickThrough(boolean))​(boolean noClickThrough)` | Can widgets under this widgets be clicked in this widgets bounding box |
| `void` | `[setNoScrollThrough](#setNoScrollThrough(boolean))​(boolean noScrollThrough)` | Can widgets under this widgets be scrolled in this widgets bounding box |
| `void` | `[setOnClickListener](#setOnClickListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran the first client tick the mouse is held ontop of this widget |
| `void` | `[setOnDialogAbortListener](#setOnDialogAbortListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the dialog is canceled |
| `void` | `[setOnDragCompleteListener](#setOnDragCompleteListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when a drag operation is finished on this widget |
| `void` | `[setOnDragListener](#setOnDragListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when this widget moves due to a drag |
| `void` | `[setOnHoldListener](#setOnHoldListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran the every client tick the mouse is held ontop of this widget,
except the first client tick. |
| `void` | `[setOnKeyListener](#setOnKeyListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran on key input |
| `void` | `[setOnMouseLeaveListener](#setOnMouseLeaveListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the mouse leaves the widget bounds |
| `void` | `[setOnMouseOverListener](#setOnMouseOverListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the mouse enters the widget bounds |
| `void` | `[setOnMouseRepeatListener](#setOnMouseRepeatListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran every client tick when the mouse is in the widget bounds |
| `void` | `[setOnOpListener](#setOnOpListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the a menu action is clicked. |
| `void` | `[setOnReleaseListener](#setOnReleaseListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran the first client tick the mouse is not held ontop of this widget |
| `void` | `[setOnScrollWheelListener](#setOnScrollWheelListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the mouse is scrolled when on the widget |
| `void` | `[setOnTargetEnterListener](#setOnTargetEnterListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the target mode has been activated for this widget |
| `void` | `[setOnTargetLeaveListener](#setOnTargetLeaveListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when the target mode has been deactivated for this widget |
| `void` | `[setOnTimerListener](#setOnTimerListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran every client tick |
| `void` | `[setOnVarTransmitListener](#setOnVarTransmitListener(java.lang.Object...))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)` | Sets a script to be ran when a varplayer changes |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setOpacity](#setOpacity(int))​(int transparency)` | Sets the transparency of the rectangle |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setOriginalHeight](#setOriginalHeight(int))​(int originalHeight)` | Sets the height input to the [`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets"). |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setOriginalWidth](#setOriginalWidth(int))​(int originalWidth)` | Sets the width input to the [`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets"). |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setOriginalX](#setOriginalX(int))​(int originalX)` | Sets the X input to the [`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets"). |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setOriginalY](#setOriginalY(int))​(int originalY)` | Sets the Y input to the [`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets"). |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setPos](#setPos(int,int))​(int x,
int y)` | Sets the X/Y coordinates |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setPos](#setPos(int,int,int,int))​(int x,
int y,
int xMode,
int yMode)` | |
| `void` | `[setRelativeX](#setRelativeX(int))​(int x)` | Deprecated. |
| `void` | `[setRelativeY](#setRelativeY(int))​(int y)` | Deprecated. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setRotationX](#setRotationX(@org.jetbrains.annotations.Range(from=0L,to=2047L)int))​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelX)` | Sets the x rotation of the model displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setRotationY](#setRotationY(@org.jetbrains.annotations.Range(from=0L,to=2047L)int))​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelY)` | Sets the y rotation of the model displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setRotationZ](#setRotationZ(@org.jetbrains.annotations.Range(from=0L,to=2047L)int))​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelZ)` | Sets the z rotation of the model displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setScrollHeight](#setScrollHeight(int))​(int height)` | Sets the size of the widget's viewport in the Y axis |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setScrollWidth](#setScrollWidth(int))​(int width)` | Sets the size of the widget's viewport in the X axis |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setScrollX](#setScrollX(int))​(int scrollX)` | Sets the amount of pixels the widget is scrolled in the X axis |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setScrollY](#setScrollY(int))​(int scrollY)` | sets the amount of pixels the widget is scrolled in the Y axis |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setSize](#setSize(int,int))​(int width,
int height)` | |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setSize](#setSize(int,int,int,int))​(int width,
int height,
int widthMode,
int heightMode)` | |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setSpriteId](#setSpriteId(int))​(int spriteId)` | Sets the sprite ID displayed in the widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setSpriteTiling](#setSpriteTiling(boolean))​(boolean tiling)` | Sets if sprites are repeated or stretched |
| `void` | `[setTargetPriority](#setTargetPriority(int))​(int priority)` | Set the priority that the target verb op is at |
| `void` | `[setTargetVerb](#setTargetVerb(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") targetVerb)` | Verb for op targets |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setText](#setText(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)` | Sets the text displayed on this widget. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setTextColor](#setTextColor(int))​(int textColor)` | Sets the RGB color of the displayed text or rectangle. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setTextShadowed](#setTextShadowed(boolean))​(boolean shadowed)` | Sets if text should be shadowed |
| `void` | `[setType](#setType(int))​(int type)` | Sets the type of the widget. |
| `void` | `[setVarTransmitTrigger](#setVarTransmitTrigger(int...))​(int... trigger)` | `VarPlayerID`s that triggers this widgets varTransmitListener |
| `void` | `[setWidth](#setWidth(int))​(int width)` | Deprecated. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setWidthMode](#setWidthMode(int))​(int widthMode)` | Sets the mode controlling widget width. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setXPositionMode](#setXPositionMode(int))​(int xpm)` | Sets the mode that the X position is calculated from the original X position. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setXTextAlignment](#setXTextAlignment(int))​(int xta)` | Sets the X axis text position mode |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setYPositionMode](#setYPositionMode(int))​(int ypm)` | Sets the mode that the Y position is calculated from the original Y position. |
| `[Widget](Widget.html "interface in net.runelite.api.widgets")` | `[setYTextAlignment](#setYTextAlignment(int))​(int yta)` | Sets the Y axis text position mode |

* + ### Method Detail

- #### getId

```
[@Component](../annotations/Component.html "annotation in net.runelite.api.annotations")
int getId()
```

Gets the widgets ID.

See Also:
[`WidgetID`](WidgetID.html "class in net.runelite.api.widgets")
- #### getType

```
int getType()
```

Gets the type of the widget.

See Also:
[`WidgetType`](WidgetType.html "class in net.runelite.api.widgets")
- #### setType

```
void setType​(int type)
```

Sets the type of the widget.

See Also:
[`WidgetType`](WidgetType.html "class in net.runelite.api.widgets")
- #### getContentType

```
int getContentType()
```

Gets the type of content displayed by the widget.
- #### setContentType

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setContentType​(int contentType)
```

Sets the type of content displayed by the widget.
- #### getClickMask

```
int getClickMask()
```

Gets the current click configuration of the widget.

See Also:
[`WidgetConfig`](WidgetConfig.html "class in net.runelite.api.widgets")
- #### setClickMask

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setClickMask​(int mask)
```

Sets the click configuration of the widget.

See Also:
[`WidgetConfig`](WidgetConfig.html "class in net.runelite.api.widgets")
- #### getParent

```
[Widget](Widget.html "interface in net.runelite.api.widgets") getParent()
```

Gets the parent widget, if this widget is a child.

Returns:
the parent widget, or null
- #### getParentId

```
int getParentId()
```

Gets the ID of the parent widget.

Returns:
the parent ID, or -1 if this widget is not a child
- #### getChild

```
@Nullable
[Widget](Widget.html "interface in net.runelite.api.widgets") getChild​(int index)
```

Gets a dynamic child by index
- #### getChildren

```
@Nullable
[Widget](Widget.html "interface in net.runelite.api.widgets")[] getChildren()
```

Gets the dynamic children of this widget in a sparse array
- #### setChildren

```
void setChildren​([Widget](Widget.html "interface in net.runelite.api.widgets")[] children)
```

Sets the dynamic children sparse array
- #### getDynamicChildren

```
[Widget](Widget.html "interface in net.runelite.api.widgets")[] getDynamicChildren()
```

Gets all dynamic children.

Returns:
the dynamic children
- #### getStaticChildren

```
[Widget](Widget.html "interface in net.runelite.api.widgets")[] getStaticChildren()
```

Gets all static children.

Returns:
the static children
- #### getNestedChildren

```
[Widget](Widget.html "interface in net.runelite.api.widgets")[] getNestedChildren()
```

Gets all nested children.

Returns:
the nested children
- #### getRelativeX

```
int getRelativeX()
```

Gets the relative x-axis coordinate to the widgets parent.

Returns:
the relative x-axis coordinate
- #### setRelativeX

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setRelativeX​(int x)
```

Deprecated.
Sets the relative x-axis coordinate to the widgets parent.

You do not want to use this. Use [`setOriginalX(int)`](#setOriginalX(int)), [`setXPositionMode(int)`](#setXPositionMode(int))
and [`revalidate()`](#revalidate()). Almost any interaction with this widget from a clientscript will
recalculate this value.
- #### getRelativeY

```
int getRelativeY()
```

Gets the relative y-axis coordinate to the widgets parent.

Returns:
the relative coordinate
- #### setRelativeY

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setRelativeY​(int y)
```

Deprecated.
Sets the relative y-axis coordinate to the widgets parent.

You do not want to use this. Use [`setOriginalY(int)`](#setOriginalY(int)), [`setYPositionMode(int)`](#setYPositionMode(int))
and [`revalidate()`](#revalidate()). Almost any interaction with this widget from a clientscript will
recalculate this value.
- #### setForcedPosition

```
void setForcedPosition​(int x,
int y)
```

Set a forced position for the widget. This position overrides the relative x/y for the
widget, even if the widget is revalidated. To clear the forced position pass -1 for x/y.

Parameters:
`x` - x pos relative to the parent
`y` - y pos relative to the parent
- #### getText

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getText()
```

Gets the text displayed on this widget.

Returns:
the displayed text
- #### setText

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setText​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text)
```

Sets the text displayed on this widget.

Parameters:
`text` - the text to display
- #### getTextColor

```
int getTextColor()
```

Gets the color as an RGB value.

Returns:
RGB24 color
See Also:
[`Color.getRGB()`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Color.html?is-external=true#getRGB() "class or interface in java.awt")
- #### setTextColor

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setTextColor​(int textColor)
```

Sets the RGB color of the displayed text or rectangle.

Parameters:
`textColor` - RGB24 color
See Also:
[`Color.getRGB()`](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Color.html?is-external=true#getRGB() "class or interface in java.awt")
- #### getOpacity

```
int getOpacity()
```

Gets the transparency of the rectangle

Returns:
0 = fully opaque, 255 = fully transparent
- #### setOpacity

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setOpacity​(int transparency)
```

Sets the transparency of the rectangle

Parameters:
`transparency` - 0 = fully opaque, 255 = fully transparent
- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name "op base" of the widget.

The name of the widget is used in the tooltip when an action is
available. For example, the widget that activates quick prayers
has the name "Quick-prayers" so when hovering there is a tooltip
that says "Activate Quick-prayers".

Returns:
the name
- #### setName

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setName​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Sets the name of the widget.

Parameters:
`name` - the new name
- #### getModelId

```
int getModelId()
```

Gets the Model/NPC/Item ID displayed in the widget.

See Also:
[`getModelType()`](#getModelType())
- #### setModelId

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setModelId​(int id)
```

Sets the Model/NPC/Item ID displayed in the widget.

See Also:
[`WidgetModelType`](WidgetModelType.html "class in net.runelite.api.widgets")
- #### getModelType

```
int getModelType()
```

Gets the model type of the widget.

See Also:
[`WidgetModelType`](WidgetModelType.html "class in net.runelite.api.widgets")
- #### setModelType

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setModelType​(int type)
```

Sets the model type of the widget.

Parameters:
`type` - the new model type
See Also:
[`WidgetModelType`](WidgetModelType.html "class in net.runelite.api.widgets")
- #### getAnimationId

```
int getAnimationId()
```

Gets the sequence ID used to animate the model in the widget

See Also:
`AnimationID`
- #### setAnimationId

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setAnimationId​(int animationId)
```

Sets the sequence ID used to animate the model in the widget

See Also:
`AnimationID`
- #### getRotationX

```
@org.jetbrains.annotations.Range(from=0L, to=2047L) int getRotationX()
```

Gets the x rotation of the model displayed in the widget.
0 = no rotation, 2047 = full rotation
- #### setRotationX

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setRotationX​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelX)
```

Sets the x rotation of the model displayed in the widget.

Note: Setting this value outside of the input range defined by [`getRotationX()`](#getRotationX()) will cause a client
crash.

Parameters:
`modelX` - the new model x rotation value
- #### getRotationY

```
@org.jetbrains.annotations.Range(from=0L, to=2047L) int getRotationY()
```

Gets the y rotation of the model displayed in the widget.
0 = no rotation, 2047 = full rotation
- #### setRotationY

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setRotationY​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelY)
```

Sets the y rotation of the model displayed in the widget.

Note: Setting this value outside of the input range defined by [`getRotationY()`](#getRotationY()) will cause a client
crash.

Parameters:
`modelY` - the new model y rotation value
- #### getRotationZ

```
@org.jetbrains.annotations.Range(from=0L, to=2047L) int getRotationZ()
```

Gets the z rotation of the model displayed in the widget.
0 = no rotation, 2047 = full rotation
- #### setRotationZ

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setRotationZ​(@org.jetbrains.annotations.Range(from=0L, to=2047L) int modelZ)
```

Sets the z rotation of the model displayed in the widget.

Note: Setting this value outside of the input range defined by [`getRotationZ()`](#getRotationZ()) will cause a client
crash.

Parameters:
`modelZ` - the new model z rotation value
- #### getModelZoom

```
int getModelZoom()
```

Gets the amount zoomed in on the model displayed in the widget.
- #### setModelZoom

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setModelZoom​(int modelZoom)
```

Sets the amount zoomed in on the model displayed in the widget.

Parameters:
`modelZoom` - the new model zoom value
- #### getSpriteId

```
int getSpriteId()
```

Gets the sprite ID displayed in the widget.

Returns:
the sprite ID
See Also:
`SpriteID`
- #### getSpriteTiling

```
boolean getSpriteTiling()
```

Gets if sprites are repeated or stretched
- #### setSpriteTiling

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setSpriteTiling​(boolean tiling)
```

Sets if sprites are repeated or stretched
- #### setSpriteId

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setSpriteId​(int spriteId)
```

Sets the sprite ID displayed in the widget.

Parameters:
`spriteId` - the sprite ID
See Also:
`SpriteID`
- #### isHidden

```
boolean isHidden()
```

Checks whether this widget or any of its parents are hidden.

This must be ran on the client thread

Returns:
true if this widget or any parent is hidden, false otherwise
- #### isSelfHidden

```
boolean isSelfHidden()
```

Checks whether this widget is hidden, not taking into account
any parent hidden states.

Returns:
true if this widget is hidden, false otherwise
- #### setHidden

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setHidden​(boolean hidden)
```

Sets the self-hidden state of this widget.

Parameters:
`hidden` - new hidden state
- #### getIndex

```
int getIndex()
```

The index of this widget in it's parent's children array
- #### getCanvasLocation

```
[Point](../Point.html "class in net.runelite.api") getCanvasLocation()
```

Gets the location the widget is being drawn on the canvas.

This method accounts for the relative coordinates and bounds
of any parent widgets.

Returns:
the upper-left coordinate of where this widget is drawn
- #### getWidth

```
int getWidth()
```

Gets the width of the widget.

If this widget is storing any [`WidgetItem`](WidgetItem.html "class in net.runelite.api.widgets")s, this value is
used to store the number of item slot columns.

Returns:
the width
- #### setWidth

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setWidth​(int width)
```

Deprecated.
Sets the width of the widget.

You do not want to use this. Use [`setOriginalWidth(int)`](#setOriginalWidth(int)), [`setWidthMode(int)`](#setWidthMode(int))
and [`revalidate()`](#revalidate()). Almost any interaction with this widget from a clientscript will
recalculate this value.
- #### getHeight

```
int getHeight()
```

Gets the height of the widget.

Returns:
the height
- #### setHeight

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setHeight​(int height)
```

Deprecated.
Sets the height of the widget.

You do not want to use this. Use [`setOriginalHeight(int)`](#setOriginalHeight(int)), [`setHeightMode(int)`](#setHeightMode(int))
and [`revalidate()`](#revalidate()). Almost any interaction with this widget from a clientscript will
recalculate this value.
- #### getBounds

```
[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") getBounds()
```

Gets the area where the widget is drawn on the canvas.

Returns:
the occupied area of the widget
- #### getItemId

```
int getItemId()
```

Gets the item ID displayed by the widget.

Returns:
the item ID
- #### setItemId

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setItemId​(int itemId)
```

Sets the item ID displayed by the widget.

Parameters:
`itemId` - the item ID
- #### getItemQuantity

```
int getItemQuantity()
```

Gets the quantity of the item displayed by the widget.

Returns:
the item quantity
- #### setItemQuantity

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setItemQuantity​(int quantity)
```

Sets the item quantity displayed by the widget.

Parameters:
`quantity` - the quantity of the item
- #### contains

```
boolean contains​([Point](../Point.html "class in net.runelite.api") point)
```

Checks if the passed canvas points is inside of this widget's
[`bounds`](#getBounds())

Parameters:
`point` - the canvas point
Returns:
true if this widget contains the point, false otherwise
- #### getScrollX

```
int getScrollX()
```

Gets the amount of pixels the widget is scrolled in the X axis
- #### setScrollX

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setScrollX​(int scrollX)
```

Sets the amount of pixels the widget is scrolled in the X axis
- #### getScrollY

```
int getScrollY()
```

Gets the amount of pixels the widget is scrolled in the Y axis
- #### setScrollY

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setScrollY​(int scrollY)
```

sets the amount of pixels the widget is scrolled in the Y axis
- #### getScrollWidth

```
int getScrollWidth()
```

Gets the size of the widget's viewport in the X axis
- #### setScrollWidth

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setScrollWidth​(int width)
```

Sets the size of the widget's viewport in the X axis
- #### getScrollHeight

```
int getScrollHeight()
```

Gets the size of the widget's viewport in the Y axis
- #### setScrollHeight

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setScrollHeight​(int height)
```

Sets the size of the widget's viewport in the Y axis
- #### getOriginalX

```
int getOriginalX()
```

Gets the X coordinate of this widget before being adjusted by
[`getXPositionMode()`](#getXPositionMode())}.
- #### setOriginalX

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setOriginalX​(int originalX)
```

Sets the X input to the [`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets"). [`revalidate()`](#revalidate()) must be
called for the new values to take effect.

See Also:
[`setXPositionMode(int)`](#setXPositionMode(int))
- #### getOriginalY

```
int getOriginalY()
```

Gets the Y coordinate of this widget before being adjusted by
[`getYPositionMode()`](#getYPositionMode())}
- #### setOriginalY

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setOriginalY​(int originalY)
```

Sets the Y input to the [`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets"). [`revalidate()`](#revalidate()) must be
called for the new values to take effect.

See Also:
[`setYPositionMode(int)`](#setYPositionMode(int))
- #### setPos

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setPos​(int x,
int y)
```

Sets the X/Y coordinates
- #### setPos

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setPos​(int x,
int y,
int xMode,
int yMode)
```
- #### getOriginalHeight

```
int getOriginalHeight()
```

Gets the height coordinate of this widget before being adjusted by
[`getHeightMode()`](#getHeightMode())
- #### setOriginalHeight

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setOriginalHeight​(int originalHeight)
```

Sets the height input to the [`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets"). [`revalidate()`](#revalidate()) must be
called for the new values to take effect.

See Also:
[`setHeightMode(int)`](#setHeightMode(int))
- #### getOriginalWidth

```
int getOriginalWidth()
```

Gets the width coordinate of this widget before being adjusted by
[`getWidthMode()`](#getWidthMode())
- #### setOriginalWidth

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setOriginalWidth​(int originalWidth)
```

Sets the width input to the [`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets"). [`revalidate()`](#revalidate()) must be
called for the new values to take effect.

See Also:
[`setWidthMode(int)`](#setWidthMode(int))
- #### setSize

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setSize​(int width,
int height)
```
- #### setSize

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setSize​(int width,
int height,
int widthMode,
int heightMode)
```
- #### getActions

```
@Nullable
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[] getActions()
```

Gets the menu options available on the widget as a sparse array.
- #### createChild

```
[Widget](Widget.html "interface in net.runelite.api.widgets") createChild​(int index,
int type)
```

Creates a dynamic widget child

Parameters:
`index` - the index of the new widget in the children list or -1 to append to the back
`type` - the [`WidgetType`](WidgetType.html "class in net.runelite.api.widgets") of the widget
- #### createChild

```
[Widget](Widget.html "interface in net.runelite.api.widgets") createChild​(int type)
```

Creates a dynamic widget child at the end of the children list

Parameters:
`type` - the [`WidgetType`](WidgetType.html "class in net.runelite.api.widgets") of the widget
- #### deleteAllChildren

```
void deleteAllChildren()
```

Removes all of this widget's dynamic children
- #### setAction

```
void setAction​(int index,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") action)
```

Creates a menu option on the widget

Parameters:
`index` - The index of the menu
`action` - The verb to be displayed next to the widget's name in the context menu
- #### clearActions

```
void clearActions()
```

Clear the menu options on a widget.
- #### setOnOpListener

```
void setOnOpListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the a menu action is clicked.
hasListener must be true for this to take effect

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnDialogAbortListener

```
void setOnDialogAbortListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the dialog is canceled

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnKeyListener

```
void setOnKeyListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran on key input

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnMouseOverListener

```
void setOnMouseOverListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the mouse enters the widget bounds

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnMouseRepeatListener

```
void setOnMouseRepeatListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran every client tick when the mouse is in the widget bounds

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnMouseLeaveListener

```
void setOnMouseLeaveListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the mouse leaves the widget bounds

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnTimerListener

```
void setOnTimerListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran every client tick

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnTargetEnterListener

```
void setOnTargetEnterListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the target mode has been activated for this widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnTargetLeaveListener

```
void setOnTargetLeaveListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the target mode has been deactivated for this widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### hasListener

```
boolean hasListener()
```

If this widget has any listeners on it
- #### setHasListener

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setHasListener​(boolean hasListener)
```

Sets if the widget has any listeners. This should be called whenever a setXListener function is called
- #### isIf3

```
boolean isIf3()
```

This is true if the widget is from an if3 interface, or is dynamically created
- #### revalidate

```
void revalidate()
```

Recomputes this widget's x/y/w/h, excluding scroll
- #### revalidateScroll

```
void revalidateScroll()
```

Recomputes this widget's group's x/y/w/h including scroll
- #### getOnOpListener

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getOnOpListener()
```

Gets the script and arguments to be ran when a menu action is clicked.

Returns:
- #### getOnKeyListener

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getOnKeyListener()
```

Gets the script and arguments to be ran when a key is pressed.

Returns:
- #### getOnLoadListener

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getOnLoadListener()
```

Gets the script and arguments to be ran when a interface is loaded.

Returns:
- #### getOnInvTransmitListener

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getOnInvTransmitListener()
```

Gets the script and arguments to be ran when one of the listened for inventories changes.

Returns:
- #### getFontId

```
int getFontId()
```

Returns the archive id of the font used

See Also:
[`FontID`](../FontID.html "class in net.runelite.api")
- #### setFontId

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setFontId​(int id)
```

Sets the archive id of the font

See Also:
[`FontID`](../FontID.html "class in net.runelite.api")
- #### getBorderType

```
int getBorderType()
```

Returns the border type of item/sprite on the widget
0 - No border
1 - 1px black border
2 - 1px black under 1px white border (selected item)
- #### setBorderType

```
void setBorderType​(int thickness)
```

See Also:
[`getBorderType()`](#getBorderType())
- #### isFlippedVertically

```
boolean isFlippedVertically()
```

Get if this graphic flipped vertically

Returns:
- #### setFlippedVertically

```
void setFlippedVertically​(boolean flip)
```

Set if this graphic is flipped vertically

Parameters:
`flip` -
- #### isFlippedHorizontally

```
boolean isFlippedHorizontally()
```

Get if this graphic flipped horizontally

Returns:
- #### setFlippedHorizontally

```
void setFlippedHorizontally​(boolean flip)
```

Set if this graphic is flipped horizontally

Parameters:
`flip` -
- #### getTextShadowed

```
boolean getTextShadowed()
```

Returns if text is shadowed
- #### setTextShadowed

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setTextShadowed​(boolean shadowed)
```

Sets if text should be shadowed
- #### getDragDeadZone

```
int getDragDeadZone()
```

Returns the widget drag dead zone
- #### setDragDeadZone

```
void setDragDeadZone​(int deadZone)
```

Sets the widget drag dead zone
- #### getDragDeadTime

```
int getDragDeadTime()
```

Returns the widget drag dead time
- #### setDragDeadTime

```
void setDragDeadTime​(int deadTime)
```

Sets the widget drag dead time
- #### getItemQuantityMode

```
int getItemQuantityMode()
```

Returns widget [`ItemQuantityMode`](ItemQuantityMode.html "class in net.runelite.api.widgets").
- #### setItemQuantityMode

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setItemQuantityMode​(int itemQuantityMode)
```

Sets the widget [`ItemQuantityMode`](ItemQuantityMode.html "class in net.runelite.api.widgets")
- #### getXPositionMode

```
int getXPositionMode()
```

Gets the mode that the X position is calculated from the original X position

See Also:
[`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets")
- #### setXPositionMode

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setXPositionMode​(int xpm)
```

Sets the mode that the X position is calculated from the original X position.
[`revalidate()`](#revalidate()) must be called for new values to take effect.

See Also:
[`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets")
- #### getYPositionMode

```
int getYPositionMode()
```

Gets the mode that the Y position is calculated from the original Y position

See Also:
[`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets")
- #### setYPositionMode

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setYPositionMode​(int ypm)
```

Sets the mode that the Y position is calculated from the original Y position.
[`revalidate()`](#revalidate()) must be called for new values to take effect.

See Also:
[`WidgetPositionMode`](WidgetPositionMode.html "class in net.runelite.api.widgets")
- #### getLineHeight

```
int getLineHeight()
```

Get the line height for this widget.

Returns:
- #### setLineHeight

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setLineHeight​(int lineHeight)
```

Set the line height for this widget. If set to 0, the line height is taken from the font instead.

Parameters:
`lineHeight` -
- #### getXTextAlignment

```
int getXTextAlignment()
```

Gets the X axis text position mode

See Also:
[`WidgetTextAlignment`](WidgetTextAlignment.html "class in net.runelite.api.widgets")
- #### setXTextAlignment

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setXTextAlignment​(int xta)
```

Sets the X axis text position mode

See Also:
[`WidgetTextAlignment`](WidgetTextAlignment.html "class in net.runelite.api.widgets")
- #### getYTextAlignment

```
int getYTextAlignment()
```

Gets the Y axis text position mode

See Also:
[`WidgetTextAlignment`](WidgetTextAlignment.html "class in net.runelite.api.widgets")
- #### setYTextAlignment

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setYTextAlignment​(int yta)
```

Sets the Y axis text position mode

See Also:
[`WidgetTextAlignment`](WidgetTextAlignment.html "class in net.runelite.api.widgets")
- #### getWidthMode

```
int getWidthMode()
```

Gets the mode controlling widget width

See Also:
[`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets")
- #### setWidthMode

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setWidthMode​(int widthMode)
```

Sets the mode controlling widget width.
[`revalidate()`](#revalidate()) must be called for new values to take effect.

See Also:
[`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets")
- #### getHeightMode

```
int getHeightMode()
```

Gets the mode controlling widget width

See Also:
[`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets")
- #### setHeightMode

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setHeightMode​(int heightMode)
```

Sets the mode controlling widget width.
[`revalidate()`](#revalidate()) must be called for new values to take effect.

See Also:
[`WidgetSizeMode`](WidgetSizeMode.html "class in net.runelite.api.widgets")
- #### getFont

```
[FontTypeFace](../FontTypeFace.html "interface in net.runelite.api") getFont()
```

Gets the font that this widget uses
- #### isFilled

```
boolean isFilled()
```

Gets if the rectangle is filled or just stroked
- #### setFilled

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setFilled​(boolean filled)
```

Sets if the rectangle is filled or just stroked
- #### getTargetVerb

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getTargetVerb()
```

Verb for op targets
- #### setTargetVerb

```
void setTargetVerb​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") targetVerb)
```

Verb for op targets
- #### getTargetPriority

```
int getTargetPriority()
```

Get the priority that the target verb op is at
- #### setTargetPriority

```
void setTargetPriority​(int priority)
```

Set the priority that the target verb op is at

Parameters:
`priority` - priority, default 4
- #### getNoClickThrough

```
boolean getNoClickThrough()
```

Can widgets under this widgets be clicked in this widgets bounding box
- #### setNoClickThrough

```
void setNoClickThrough​(boolean noClickThrough)
```

Can widgets under this widgets be clicked in this widgets bounding box
- #### getNoScrollThrough

```
boolean getNoScrollThrough()
```

Can widgets under this widgets be scrolled in this widgets bounding box
- #### setNoScrollThrough

```
void setNoScrollThrough​(boolean noScrollThrough)
```

Can widgets under this widgets be scrolled in this widgets bounding box
- #### getVarTransmitTrigger

```
int[] getVarTransmitTrigger()
```

`VarPlayerID`s that triggers this widgets varTransmitListener
- #### setVarTransmitTrigger

```
void setVarTransmitTrigger​(int... trigger)
```

`VarPlayerID`s that triggers this widgets varTransmitListener
- #### setOnClickListener

```
void setOnClickListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran the first client tick the mouse is held ontop of this widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnHoldListener

```
void setOnHoldListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran the every client tick the mouse is held ontop of this widget,
except the first client tick.

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnReleaseListener

```
void setOnReleaseListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran the first client tick the mouse is not held ontop of this widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnDragCompleteListener

```
void setOnDragCompleteListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when a drag operation is finished on this widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnDragListener

```
void setOnDragListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when this widget moves due to a drag

Parameters:
`args` - A ScriptID, then the args for the script
- #### setOnScrollWheelListener

```
void setOnScrollWheelListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when the mouse is scrolled when on the widget

Parameters:
`args` - A ScriptID, then the args for the script
- #### getDragParent

```
[Widget](Widget.html "interface in net.runelite.api.widgets") getDragParent()
```

Container this can be dragged in
- #### setDragParent

```
[Widget](Widget.html "interface in net.runelite.api.widgets") setDragParent​([Widget](Widget.html "interface in net.runelite.api.widgets") dragParent)
```

Container this can be dragged in
- #### getOnVarTransmitListener

```
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")[] getOnVarTransmitListener()
```

Gets the script and arguments to be ran when one of the listened for vars changes.

Returns:
- #### setOnVarTransmitListener

```
void setOnVarTransmitListener​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")... args)
```

Sets a script to be ran when a varplayer changes

Parameters:
`args` - A ScriptID, then the args for the script