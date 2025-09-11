# WorldTile (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/WorldTile.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.WorldTile

* All Implemented Interfaces:
`[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class WorldTile
extends java.lang.Object
```

Represents a unique tile position in Runescape.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `protected org.tribot.api2007.types.RSTile` | `[rsTile](#rsTile)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[WorldTile](#%3Cinit%3E(int,int))​(int x,
int y)` | |
| `[WorldTile](#%3Cinit%3E(int,int,int))​(int x,
int y,
int plane)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[clickOnMinimap](#clickOnMinimap())()` | Clicks the tile on the minimap interface. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.Optional<java.awt.Polygon>` | `[getBounds](#getBounds())()` | Gets the bounds of this tile on the screen |
| `org.tribot.api2007.types.RSTile` | `[getLegacyTile](#getLegacyTile())()` | |
| `int` | `[getPlane](#getPlane())()` | Gets the plane of this tile |
| `int` | `[getRegionId](#getRegionId())()` | Gets this tile's region id. |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Returns "this". |
| `int` | `[getX](#getX())()` | Gets the x coordinate of this tile |
| `int` | `[getY](#getY())()` | Gets the y coordinate of this tile |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[hoverOnMinimap](#hoverOnMinimap())()` | Attempts to hover the tile on the minimap |
| `boolean` | `[isOnMinimap](#isOnMinimap())()` | Determines if this tile is visible on the minimap interface. |
| `boolean` | `[isRendered](#isRendered())()` | Checks if this tile is currently being rendered (a tile is not rendered if it's covered by the 'black fog') |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `boolean` | `[leftClickOnScreen](#leftClickOnScreen())()` | Attempts to left-click this tile on the screen. |
| `[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")` | `[toLocalTile](#toLocalTile())()` | |
| `java.lang.String` | `[toString](#toString())()` | |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int))​(int x,
int y)` | Translates (shifts) this tile by the specified x and y |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int,int))​(int x,
int y,
int z)` | Translates (shifts) this tile by the specified x, y, and z |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")

`[interact](../interfaces/Interactable.html#interact(java.lang.String)), [interact](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[distance](../interfaces/Positionable.html#distance()), [distanceTo](../interfaces/Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")

`[hasLineOfSightTo](../interfaces/Tile.html#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable)), [isHovering](../interfaces/Tile.html#isHovering()), [isInLineOfSight](../interfaces/Tile.html#isInLineOfSight())`

* + ### Field Detail

- #### rsTile

```
protected final org.tribot.api2007.types.RSTile rsTile
```

+ ### Constructor Detail

- #### WorldTile

```
public WorldTile​(int x,
int y)
```
- #### WorldTile

```
public WorldTile​(int x,
int y,
int plane)
```

+ ### Method Detail

- #### translate

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") translate​(int x,
int y)
```

Description copied from interface: `[Tile](../interfaces/Tile.html#translate(int,int))`
Translates (shifts) this tile by the specified x and y

Parameters:
`x` - the x translation
`y` - the y translation
Returns:
a new tile with the specified translation
- #### translate

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") translate​(int x,
int y,
int z)
```

Description copied from interface: `[Tile](../interfaces/Tile.html#translate(int,int,int))`
Translates (shifts) this tile by the specified x, y, and z

Parameters:
`x` - the x translation
`y` - the y translation
`z` - the z translation (plane)
Returns:
a new tile with the specified translation
- #### getTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Returns "this". Not meant to be used.
- #### toLocalTile

```
public [LocalTile](LocalTile.html "class in org.tribot.script.sdk.types") toLocalTile()
```
- #### equals

```
public boolean equals​(@Nullable
java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### getRegionId

```
public int getRegionId()
```

Gets this tile's region id. Each [`WorldTile`](WorldTile.html "class in org.tribot.script.sdk.types") could be described as a [`LocalTile`](LocalTile.html "class in org.tribot.script.sdk.types") along with a region id.

Returns:
this tile's region id
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
- #### getX

```
public int getX()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#getX())`
Gets the x coordinate of this tile

Specified by:
`[getX](../interfaces/Tile.html#getX())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the x coordinate
- #### getY

```
public int getY()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#getY())`
Gets the y coordinate of this tile

Specified by:
`[getY](../interfaces/Tile.html#getY())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the y coordinate
- #### getPlane

```
public int getPlane()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#getPlane())`
Gets the plane of this tile

Specified by:
`[getPlane](../interfaces/Tile.html#getPlane())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the plane of this tile
- #### isOnMinimap

```
public boolean isOnMinimap()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#isOnMinimap())`
Determines if this tile is visible on the minimap interface.

Specified by:
`[isOnMinimap](../interfaces/Tile.html#isOnMinimap())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the tile is on the minimap. False otherwise.
- #### clickOnMinimap

```
public boolean clickOnMinimap()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#clickOnMinimap())`
Clicks the tile on the minimap interface.

Specified by:
`[clickOnMinimap](../interfaces/Tile.html#clickOnMinimap())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the click happens. False otherwise.
- #### hoverOnMinimap

```
public boolean hoverOnMinimap()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#hoverOnMinimap())`
Attempts to hover the tile on the minimap

Specified by:
`[hoverOnMinimap](../interfaces/Tile.html#hoverOnMinimap())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the tile was hovered, false otherwise
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
- #### adjustCameraTo

```
public boolean adjustCameraTo()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#adjustCameraTo())`
Moves the camera to a position where the given entity or position is in view. Takes into account distance.
Uses an algorithm to move both the angle and rotation of the camera simultaneously at pseudo-random intervals
to simulate human camera movement.

Specified by:
`[adjustCameraTo](../interfaces/Positionable.html#adjustCameraTo())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the camera moved. False otherwise.
- #### isRendered

```
public boolean isRendered()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#isRendered())`
Checks if this tile is currently being rendered (a tile is not rendered if it's covered by the 'black fog')

Specified by:
`[isRendered](../interfaces/Tile.html#isRendered())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if this tile is being rendered, false otherwise
- #### leftClickOnScreen

```
public boolean leftClickOnScreen()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#leftClickOnScreen())`
Attempts to left-click this tile on the screen. This will only left click.
It can fail in some cases if it can't find a spot to left-click.

Specified by:
`[leftClickOnScreen](../interfaces/Tile.html#leftClickOnScreen())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the tile was clicked, false otherwise
- #### getLegacyTile

```
public org.tribot.api2007.types.RSTile getLegacyTile()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`
- #### getBounds

```
public java.util.Optional<java.awt.Polygon> getBounds()
```

Description copied from interface: `[Tile](../interfaces/Tile.html#getBounds())`
Gets the bounds of this tile on the screen

Specified by:
`[getBounds](../interfaces/Tile.html#getBounds())` in interface `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the bounds of this tile on the screen