# Menu (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Menu.html

**Package:** Packagenet.runelite.api

**Description:** This method should typically be used in the context of theMenuOpenedevent, since setting the menu entries will be overwritten the next frame...

---

* ---

```
public interface Menu
```

The client minimenu.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")` | `[createMenuEntry](#createMenuEntry(int))​(int idx)` | Create a new menu entry |
| `[MenuEntry](MenuEntry.html "interface in net.runelite.api")[]` | `[getMenuEntries](#getMenuEntries())()` | Gets the current mini menu entries. |
| `int` | `[getMenuHeight](#getMenuHeight())()` | Get the menu height. |
| `int` | `[getMenuWidth](#getMenuWidth())()` | Get the menu width. |
| `int` | `[getMenuX](#getMenuX())()` | Get the menu x location. |
| `int` | `[getMenuY](#getMenuY())()` | Get the menu y location. |
| `void` | `[removeMenuEntry](#removeMenuEntry(net.runelite.api.MenuEntry))​([MenuEntry](MenuEntry.html "interface in net.runelite.api") entry)` | Remove a menu entry |
| `void` | `[setMenuEntries](#setMenuEntries(net.runelite.api.MenuEntry%5B%5D))​([MenuEntry](MenuEntry.html "interface in net.runelite.api")[] entries)` | Sets the array of menu entries. |

* + ### Method Detail

- #### createMenuEntry

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api") createMenuEntry​(int idx)
```

Create a new menu entry

Parameters:
`idx` - the index to create the menu entry at. Accepts negative indexes eg. -1 inserts at the end.
Returns:
the newly created menu entry
- #### getMenuEntries

```
[MenuEntry](MenuEntry.html "interface in net.runelite.api")[] getMenuEntries()
```

Gets the current mini menu entries.

Returns:
array of menu entries
- #### setMenuEntries

```
void setMenuEntries​([MenuEntry](MenuEntry.html "interface in net.runelite.api")[] entries)
```

Sets the array of menu entries.

This method should typically be used in the context of the [`MenuOpened`](events/MenuOpened.html "class in net.runelite.api.events")
event, since setting the menu entries will be overwritten the next frame

Parameters:
`entries` - new array of open menu entries
- #### removeMenuEntry

```
void removeMenuEntry​([MenuEntry](MenuEntry.html "interface in net.runelite.api") entry)
```

Remove a menu entry

Parameters:
`entry` - the menu entry
- #### getMenuX

```
int getMenuX()
```

Get the menu x location. Only valid if the menu is open.

Returns:
the menu x location
- #### getMenuY

```
int getMenuY()
```

Get the menu y location. Only valid if the menu is open.

Returns:
the menu y location
- #### getMenuWidth

```
int getMenuWidth()
```

Get the menu width. Only valid if the menu is open.

Returns:
the menu width
- #### getMenuHeight

```
int getMenuHeight()
```

Get the menu height. Only valid if the menu is open.

Returns:
the menu height