# Tile (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Tile.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* All Superinterfaces:
`[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")`

All Known Implementing Classes:
`[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")`, `[WorldTile](../types/WorldTile.html "class in org.tribot.script.sdk.types")`

---

```
public interface Tile
extends [Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents a position in the game. Could be relative (LocalTile) or global (WorldTile).

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `boolean` | `[clickOnMinimap](#clickOnMinimap())()` | Clicks the tile on the minimap interface. |
| `java.util.Optional<java.awt.Polygon>` | `[getBounds](#getBounds())()` | Gets the bounds of this tile on the screen |
| `int` | `[getPlane](#getPlane())()` | Gets the plane of this tile |
| `int` | `[getX](#getX())()` | Gets the x coordinate of this tile |
| `int` | `[getY](#getY())()` | Gets the y coordinate of this tile |
| `default boolean` | `[hasLineOfSightTo](#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") other)` | Unmaintained. |
| `boolean` | `[hoverOnMinimap](#hoverOnMinimap())()` | Attempts to hover the tile on the minimap |
| `default boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `default boolean` | `[isInLineOfSight](#isInLineOfSight())()` | Unmaintained. |
| `boolean` | `[isOnMinimap](#isOnMinimap())()` | Determines if this tile is visible on the minimap interface. |
| `boolean` | `[isRendered](#isRendered())()` | Checks if this tile is currently being rendered (a tile is not rendered if it's covered by the 'black fog') |
| `boolean` | `[leftClickOnScreen](#leftClickOnScreen())()` | Attempts to left-click this tile on the screen. |
| `[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")` | `[translate](#translate(int,int))​(int x,
int y)` | Translates (shifts) this tile by the specified x and y |
| `[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces")` | `[translate](#translate(int,int,int))​(int x,
int y,
int z)` | Translates (shifts) this tile by the specified x, y, and z |

- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[click](Clickable.html#click()), [click](Clickable.html#click(java.lang.String)), [hover](Clickable.html#hover()), [hover](Clickable.html#hover(java.lang.String)), [hoverMenu](Clickable.html#hoverMenu(java.lang.String)), [isVisible](Clickable.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Interactable](Interactable.html "interface in org.tribot.script.sdk.interfaces")

`[interact](Interactable.html#interact(java.lang.String)), [interact](Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[adjustCameraTo](Positionable.html#adjustCameraTo()), [distance](Positionable.html#distance()), [distanceTo](Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable)), [getTile](Positionable.html#getTile())`

* + ### Method Detail

- #### getX

```
int getX()
```

Gets the x coordinate of this tile

Returns:
the x coordinate
- #### getY

```
int getY()
```

Gets the y coordinate of this tile

Returns:
the y coordinate
- #### getPlane

```
int getPlane()
```

Gets the plane of this tile

Returns:
the plane of this tile
- #### isOnMinimap

```
boolean isOnMinimap()
```

Determines if this tile is visible on the minimap interface.

Returns:
True if the tile is on the minimap. False otherwise.
- #### clickOnMinimap

```
boolean clickOnMinimap()
```

Clicks the tile on the minimap interface.

Returns:
True if the click happens. False otherwise.
- #### hoverOnMinimap

```
boolean hoverOnMinimap()
```

Attempts to hover the tile on the minimap

Returns:
true if the tile was hovered, false otherwise
- #### translate

```
[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces") translate​(int x,
int y)
```

Translates (shifts) this tile by the specified x and y

Parameters:
`x` - the x translation
`y` - the y translation
Returns:
a new tile with the specified translation
- #### translate

```
[Tile](Tile.html "interface in org.tribot.script.sdk.interfaces") translate​(int x,
int y,
int z)
```

Translates (shifts) this tile by the specified x, y, and z

Parameters:
`x` - the x translation
`y` - the y translation
`z` - the z translation (plane)
Returns:
a new tile with the specified translation
- #### isRendered

```
boolean isRendered()
```

Checks if this tile is currently being rendered (a tile is not rendered if it's covered by the 'black fog')

Returns:
true if this tile is being rendered, false otherwise
- #### leftClickOnScreen

```
boolean leftClickOnScreen()
```

Attempts to left-click this tile on the screen. This will only left click.
It can fail in some cases if it can't find a spot to left-click.

Returns:
true if the tile was clicked, false otherwise
- #### getBounds

```
java.util.Optional<java.awt.Polygon> getBounds()
```

Gets the bounds of this tile on the screen

Returns:
the bounds of this tile on the screen
- #### isInLineOfSight

```
default boolean isInLineOfSight()
```

Unmaintained. Checks if this tile is in the line of sight of the local player.
Line of sight means that you can attack a target on this tile without moving (dependent on weapon range) around some obstacle.

Returns:
true if this tile is in the line of sight of the local player, false otherwise
- #### hasLineOfSightTo

```
default boolean hasLineOfSightTo​([Positionable](Positionable.html "interface in org.tribot.script.sdk.interfaces") other)
```

Unmaintained. Checks if this tile has line of sight to the target

Parameters:
`other` - the target to check if this tile has line of sight to
Returns:
true if this tile has line of sight to the target, false otherwise
- #### isHovering

```
default boolean isHovering()
```

Description copied from interface: `[Clickable](Clickable.html#isHovering())`
Checks if the mouse is currently over this entity

Specified by:
`[isHovering](Clickable.html#isHovering())` in interface `[Clickable](Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the mouse if over this entity, false otherwise