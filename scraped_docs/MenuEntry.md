# MenuEntry (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/MenuEntry.html

**Package:** Packagenet.runelite.api

**Description:** If the option does not apply to any target, this field
 will be set to empty string....

---

* ---

```
public interface MenuEntry
```

A menu entry in a right-click menu.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Menu](Menu.html "interface in net.runelite.api")` | `[createSubMenu](#createSubMenu())()` | Create a new submenu for this menu entry. |
| `void` | `[deleteSubMenu](#deleteSubMenu())()` | Remove the submenu from this menu entry. |
| `[Actor](Actor.html "interface in net.runelite.api")` | `[getActor](#getActor())()` | Get the [`Actor`](Actor.html "interface in net.runelite.api") this menu entry is targeting, if any. |
| `int` | `[getIdentifier](#getIdentifier())()` | An identifier value for the target of the action. |
| `int` | `[getItemId](#getItemId())()` | Get the item id |
| `int` | `[getItemOp](#getItemOp())()` | If this menu entry is an item op, get the item op id |
| `[NPC](NPC.html "interface in net.runelite.api")` | `[getNpc](#getNpc())()` | Get the [`NPC`](NPC.html "interface in net.runelite.api") this menu entry is targeting, if any. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getOption](#getOption())()` | The option text added to the menu. |
| `int` | `[getParam0](#getParam0())()` | An additional parameter for the action. |
| `int` | `[getParam1](#getParam1())()` | A second additional parameter for the action. |
| `[Player](Player.html "interface in net.runelite.api")` | `[getPlayer](#getPlayer())()` | Get the [`Player`](Player.html "interface in net.runelite.api") this menu entry is targeting, if any. |
| `[Menu](Menu.html "interface in net.runelite.api")` | `[getSubMenu](#getSubMenu())()` | Get the submenu for this menu entry. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getTarget](#getTarget())()` | The target of the action. |
| `[MenuAction](MenuAction.html "enum in net.runelite.api")` | `[getType](#getType())()` | The action the entry will trigger. |
| `[Widget](widgets/Widget.html "interface in net.runelite.api.widgets")` | `[getWidget](#getWidget())()` | Get the widget this menu entry is on, if this is a menu entry
with an associated widget. |
| `int` | `[getWorldViewId](#getWorldViewId())()` | |
| `boolean` | `[isDeprioritized](#isDeprioritized())()` | Deprioritized menus are sorted in the menu to be below the other menu entries. |
| `boolean` | `[isForceLeftClick](#isForceLeftClick())()` | If this is true and you have single mouse button on and this entry is
the top entry the right click menu will not be opened when you left click

This is used for shift click |
| `boolean` | `[isItemOp](#isItemOp())()` | Test if this menu entry is an item op. |
| `[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[MenuEntry](MenuEntry.html "interface in net.runelite.api")>` | `[onClick](#onClick())()` | Get the callback called when the menu option is clicked |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[onClick](#onClick(java.util.function.Consumer))​([Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[MenuEntry](MenuEntry.html "interface in net.runelite.api")> callback)` | Set a callback to be called when this menu option is clicked |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setDeprioritized](#setDeprioritized(boolean))​(boolean deprioritized)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setForceLeftClick](#setForceLeftClick(boolean))​(boolean forceLeftClick)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setIdentifier](#setIdentifier(int))​(int identifier)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setItemId](#setItemId(int))​(int itemId)` | Set the item id |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setOption](#setOption(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") option)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setParam0](#setParam0(int))​(int param0)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setParam1](#setParam1(int))​(int param1)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setTarget](#setTarget(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") target)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setType](#setType(net.runelite.api.MenuAction))​([MenuAction](MenuAction.html "enum in net.runelite.api") type)` | |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[setWorldViewId](#setWorldViewId(int))​(int worldViewId)` | |

* + ### Method Detail

- #### getOption

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getOption()
```

The option text added to the menu. (ie. "Walk here", "Use")
- #### setOption

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setOption​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") option)
```
- #### getTarget

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getTarget()
```

The target of the action. (ie. Item or Actor name)

If the option does not apply to any target, this field
will be set to empty string.
- #### setTarget

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setTarget​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") target)
```
- #### getIdentifier

```
int getIdentifier()
```

An identifier value for the target of the action.
- #### setIdentifier

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setIdentifier​(int identifier)
```
- #### getType

```
[MenuAction](MenuAction.html "enum in net.runelite.api") getType()
```

The action the entry will trigger.
- #### setType

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setType​([MenuAction](MenuAction.html "enum in net.runelite.api") type)
```
- #### getParam0

```
int getParam0()
```

An additional parameter for the action.
- #### setParam0

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setParam0​(int param0)
```
- #### getParam1

```
int getParam1()
```

A second additional parameter for the action.
- #### setParam1

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setParam1​(int param1)
```
- #### isForceLeftClick

```
boolean isForceLeftClick()
```

If this is true and you have single mouse button on and this entry is
the top entry the right click menu will not be opened when you left click

This is used for shift click
- #### setForceLeftClick

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setForceLeftClick​(boolean forceLeftClick)
```
- #### getWorldViewId

```
int getWorldViewId()
```
- #### setWorldViewId

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setWorldViewId​(int worldViewId)
```
- #### isDeprioritized

```
boolean isDeprioritized()
```

Deprioritized menus are sorted in the menu to be below the other menu entries.

Returns:
- #### setDeprioritized

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setDeprioritized​(boolean deprioritized)
```
- #### onClick

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") onClick​([Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[MenuEntry](MenuEntry.html "interface in net.runelite.api")> callback)
```

Set a callback to be called when this menu option is clicked

Parameters:
`callback` -
Returns:
- #### onClick

```
[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[MenuEntry](MenuEntry.html "interface in net.runelite.api")> onClick()
```

Get the callback called when the menu option is clicked

Returns:
- #### isItemOp

```
boolean isItemOp()
```

Test if this menu entry is an item op. "Use" and "Examine" are not considered item ops.

Returns:
- #### getItemOp

```
int getItemOp()
```

If this menu entry is an item op, get the item op id

Returns:
1-5
- #### getItemId

```
int getItemId()
```

Get the item id

Returns:
See Also:
`ItemID`
- #### setItemId

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") setItemId​(int itemId)
```

Set the item id

Parameters:
`itemId` -
Returns:
- #### getWidget

```
@Nullable
[Widget](widgets/Widget.html "interface in net.runelite.api.widgets") getWidget()
```

Get the widget this menu entry is on, if this is a menu entry
with an associated widget. Such as eg, CC\_OP.

Returns:
- #### getNpc

```
@Nullable
[NPC](NPC.html "interface in net.runelite.api") getNpc()
```

Get the [`NPC`](NPC.html "interface in net.runelite.api") this menu entry is targeting, if any.

Returns:
- #### getPlayer

```
@Nullable
[Player](Player.html "interface in net.runelite.api") getPlayer()
```

Get the [`Player`](Player.html "interface in net.runelite.api") this menu entry is targeting, if any.

Returns:
- #### getActor

```
@Nullable
[Actor](Actor.html "interface in net.runelite.api") getActor()
```

Get the [`Actor`](Actor.html "interface in net.runelite.api") this menu entry is targeting, if any.

Returns:
- #### getSubMenu

```
@Nullable
[Menu](Menu.html "interface in net.runelite.api") getSubMenu()
```

Get the submenu for this menu entry.

Returns:
the submenu, or null if one doesn't exist
See Also:
[`createSubMenu()`](#createSubMenu())
- #### createSubMenu

```
@Nonnull
[Menu](Menu.html "interface in net.runelite.api") createSubMenu()
```

Create a new submenu for this menu entry.
This will erase any previous submenu.

Returns:
the new submenu
- #### deleteSubMenu

```
void deleteSubMenu()
```

Remove the submenu from this menu entry.