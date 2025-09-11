# Widget (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Widget.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Widget

* All Implemented Interfaces:
`[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class Widget
extends java.lang.Object
implements [Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces"), [Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces"), [Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents an on-screen UI element that is drawn on the game canvas

See Also:
[`Query.widgets()`](../query/Query.html#widgets())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[dragTo](#dragTo(org.tribot.script.sdk.types.Widget))​([Widget](Widget.html "class in org.tribot.script.sdk.types") destination)` | Drags this widget to the destination widget |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |
| `int` | `[getAnimationId](#getAnimationId())()` | Gets the widget animation ID |
| `java.awt.Rectangle` | `[getBounds](#getBounds())()` | |
| `java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")>` | `[getChild](#getChild(int))​(int index)` | Gets the child of this widget at the specified index |
| `java.util.List<[Widget](Widget.html "class in org.tribot.script.sdk.types")>` | `[getChildren](#getChildren())()` | |
| `int` | `[getIndex](#getIndex())()` | Gets the index of the entity. |
| `int[]` | `[getIndexPath](#getIndexPath())()` | |
| `int` | `[getItemStack](#getItemStack())()` | |
| `org.tribot.api2007.types.RSInterface` | `[getLegacyInterface](#getLegacyInterface())()` | Not exposed |
| `int` | `[getModelId](#getModelId())()` | Gets this widget's model id. |
| `java.util.Optional<java.lang.String>` | `[getName](#getName())()` | Returns the name of this widget, if one exists. |
| `java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")>` | `[getParent](#getParent())()` | Gets the parent of this widget in the widget tree |
| `java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")>` | `[getSibling](#getSibling(int))​(int siblingOffset)` | Gets a sibling of this widget from the specified offset |
| `java.util.Optional<java.lang.String>` | `[getText](#getText())()` | |
| `int` | `[getTextColor](#getTextColor())()` | Gets the text color of this widget as an rgb color |
| `int` | `[getTextureId](#getTextureId())()` | Gets the widget texture ID |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `boolean` | `[scrollTo](#scrollTo())()` | Scroll to the desired widget |
| `java.util.Optional<[ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")>` | `[toItemDefinition](#toItemDefinition())()` | |
| `java.lang.String` | `[toString](#toString())()` | |
| `java.util.Optional<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[toWidgetItem](#toWidgetItem())()` | |
| `java.util.List<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[toWidgetItemTable](#toWidgetItemTable())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`

* + ### Method Detail

- #### getChildren

```
public java.util.List<[Widget](Widget.html "class in org.tribot.script.sdk.types")> getChildren()
```
- #### getText

```
public java.util.Optional<java.lang.String> getText()
```
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```

Description copied from interface: `[Actionable](../interfaces/Actionable.html#getActions())`
Gets the available actions for the entity, usually dependent on their definition.

Specified by:
`[getActions](../interfaces/Actionable.html#getActions())` in interface `[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getIndexPath

```
public int[] getIndexPath()
```
- #### toItemDefinition

```
public java.util.Optional<[ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")> toItemDefinition()
```
- #### toWidgetItem

```
public java.util.Optional<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> toWidgetItem()
```
- #### toWidgetItemTable

```
public java.util.List<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> toWidgetItemTable()
```
- #### getItemStack

```
public int getItemStack()
```
- #### getBounds

```
public java.awt.Rectangle getBounds()
```
- #### getLegacyInterface

```
public org.tribot.api2007.types.RSInterface getLegacyInterface()
```

Not exposed
- #### click

```
public boolean click()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click())`
Interacts with the entity, with the first action available. This will generally perform a left-click, unless there is an action blocking in which case it will right click.

Specified by:
`[click](../interfaces/Clickable.html#click())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the entity was clicked, false otherwise
- #### click

```
public boolean click​(java.lang.String action)
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click(java.lang.String))`
Interacts with the entity, given a specific action. The "action" string is the part of the option that comes first.
For example, to attack an NPC, the action is "Attack". Case insensitive.

Specified by:
`[click](../interfaces/Clickable.html#click(java.lang.String))` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the entity was successfully clicked
- #### hover

```
public boolean hover()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#hover())`
Moves the mouse to a human-randomized point on the entity.

Specified by:
`[hover](../interfaces/Clickable.html#hover())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the mouse successfully moved over the entity
- #### isVisible

```
public boolean isVisible()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#isVisible())`
Determines if the entity is on the screen and able to be clicked.

Specified by:
`[isVisible](../interfaces/Clickable.html#isVisible())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
- #### isHovering

```
public boolean isHovering()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#isHovering())`
Checks if the mouse is currently over this entity

Specified by:
`[isHovering](../interfaces/Clickable.html#isHovering())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the mouse if over this entity, false otherwise
- #### getIndex

```
public int getIndex()
```

Description copied from interface: `[Indexable](../interfaces/Indexable.html#getIndex())`
Gets the index of the entity.

Specified by:
`[getIndex](../interfaces/Indexable.html#getIndex())` in interface `[Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getName

```
public java.util.Optional<java.lang.String> getName()
```

Returns the name of this widget, if one exists.
For example, the quick-prayer orb is named Quick-prayers which is seen in the tooltip when hovering the widget

Returns:
the name of the widget, or an empty optional
- #### getTextColor

```
public int getTextColor()
```

Gets the text color of this widget as an rgb color

Returns:
the text color of this widget
- #### getSibling

```
public java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")> getSibling​(int siblingOffset)
```

Gets a sibling of this widget from the specified offset

Parameters:
`siblingOffset` - the offset (for example, an offset of 1 would find a child from the parent of this widget that has this index + 1)
Returns:
a sibling of this widget from the specified offset
- #### getParent

```
public java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")> getParent()
```

Gets the parent of this widget in the widget tree

Returns:
the parent of this widget
- #### getChild

```
public java.util.Optional<[Widget](Widget.html "class in org.tribot.script.sdk.types")> getChild​(int index)
```

Gets the child of this widget at the specified index

Parameters:
`index` - the child index
Returns:
the child widget at the specified index
- #### getTextureId

```
public int getTextureId()
```

Gets the widget texture ID

Returns:
widget texture ID
- #### getAnimationId

```
public int getAnimationId()
```

Gets the widget animation ID

Returns:
widget animation ID
- #### getModelId

```
public int getModelId()
```

Gets this widget's model id.
This id corresponds to widgets that have a 3d model display, such as a widget in the barrows puzzle screen.

Returns:
this widget's model id
- #### scrollTo

```
public boolean scrollTo()
```

Scroll to the desired widget

Returns:
true if the widget is on screen false otherwise;
- #### dragTo

```
public boolean dragTo​([Widget](Widget.html "class in org.tribot.script.sdk.types") destination)
```

Drags this widget to the destination widget

Parameters:
`destination` - the destination widget
Returns:
true if dragged successfully, false otherwise
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`