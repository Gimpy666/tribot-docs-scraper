# LocalTile (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/LocalTile.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.LocalTile

* All Implemented Interfaces:
`[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class LocalTile
extends java.lang.Object
```

Represents a tile in the current scene

See Also:
[`Query.tiles()`](../query/Query.html#tiles())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[LocalTile.Collision](LocalTile.Collision.html "enum in org.tribot.script.sdk.types")` | |
| `static class` | `[LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types")` | |
| `static class` | `[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")` | |

+ ### Field Summary

Fields | Modifier and Type | Field | Description |
| `protected org.tribot.api2007.types.RSTile` | `[rsTile](#rsTile)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[LocalTile](#%3Cinit%3E(int,int))​(int x,
int y)` | |
| `[LocalTile](#%3Cinit%3E(int,int,int))​(int x,
int y,
int plane)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[clickOnMinimap](#clickOnMinimap())()` | Clicks the tile on the minimap interface. |
| `boolean` | `[containsWall](#containsWall(org.tribot.script.sdk.types.LocalTile.Direction))​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.Optional<java.awt.Polygon>` | `[getBounds](#getBounds())()` | Gets the bounds of this tile on the screen |
| `java.util.List<[LocalTile.Collision](LocalTile.Collision.html "enum in org.tribot.script.sdk.types")>` | `[getCollision](#getCollision())()` | |
| `int` | `[getHeight](#getHeight())()` | |
| `org.tribot.api2007.types.RSTile` | `[getLegacyTile](#getLegacyTile())()` | |
| `[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")` | `[getNeighbor](#getNeighbor(org.tribot.script.sdk.types.LocalTile.Direction))​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)` | Gets the neighboring tile in the specified direction |
| `int` | `[getPlane](#getPlane())()` | Gets the plane of this tile |
| `java.util.List<[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")>` | `[getSceneSettings](#getSceneSettings())()` | |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |
| `int` | `[getX](#getX())()` | Gets the x coordinate of this tile |
| `int` | `[getY](#getY())()` | Gets the y coordinate of this tile |
| `boolean` | `[hasCollision](#hasCollision(org.tribot.script.sdk.types.LocalTile.Collision))​([LocalTile.Collision](LocalTile.Collision.html "enum in org.tribot.script.sdk.types") flag)` | |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hasSceneSetting](#hasSceneSetting(org.tribot.script.sdk.types.LocalTile.SceneSetting))​([LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types") flag)` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[hoverOnMinimap](#hoverOnMinimap())()` | Attempts to hover the tile on the minimap |
| `boolean` | `[isDirectionWalkable](#isDirectionWalkable(org.tribot.script.sdk.types.LocalTile.Direction))​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)` | |
| `boolean` | `[isLoaded](#isLoaded())()` | Checks if this local tile is valid and in the loaded region. |
| `boolean` | `[isOnMinimap](#isOnMinimap())()` | Determines if this tile is visible on the minimap interface. |
| `boolean` | `[isRendered](#isRendered())()` | Checks if this tile is currently being rendered (a tile is not rendered if it's covered by the 'black fog') |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `boolean` | `[isWalkable](#isWalkable())()` | |
| `boolean` | `[leftClickOnScreen](#leftClickOnScreen())()` | Attempts to left-click this tile on the screen. |
| `java.lang.String` | `[toString](#toString())()` | |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[toWorldTile](#toWorldTile())()` | |
| `[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int))​(int x,
int y)` | Translates (shifts) this tile by the specified x and y |
| `[LocalTile](LocalTile.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int,int))​(int x,
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

- #### LocalTile

```
public LocalTile​(int x,
int y)
```
- #### LocalTile

```
public LocalTile​(int x,
int y,
int plane)
```

+ ### Method Detail

- #### translate

```
public [LocalTile](LocalTile.html "class in org.tribot.script.sdk.types") translate​(int x,
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
public [LocalTile](LocalTile.html "class in org.tribot.script.sdk.types") translate​(int x,
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

Description copied from interface: `[Positionable](../interfaces/Positionable.html#getTile())`
Gets the WorldTile of this entity/position
- #### toWorldTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") toWorldTile()
```
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### getSceneSettings

```
public java.util.List<[LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types")> getSceneSettings()
```
- #### hasSceneSetting

```
public boolean hasSceneSetting​([LocalTile.SceneSetting](LocalTile.SceneSetting.html "enum in org.tribot.script.sdk.types") flag)
```
- #### getCollision

```
public java.util.List<[LocalTile.Collision](LocalTile.Collision.html "enum in org.tribot.script.sdk.types")> getCollision()
```
- #### hasCollision

```
public boolean hasCollision​([LocalTile.Collision](LocalTile.Collision.html "enum in org.tribot.script.sdk.types") flag)
```
- #### isWalkable

```
public boolean isWalkable()
```
- #### isDirectionWalkable

```
public boolean isDirectionWalkable​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)
```
- #### getNeighbor

```
public [LocalTile](LocalTile.html "class in org.tribot.script.sdk.types") getNeighbor​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)
```

Gets the neighboring tile in the specified direction

Parameters:
`direction` - the direction
Returns:
the neighbor in the specified direction
- #### isLoaded

```
public boolean isLoaded()
```

Checks if this local tile is valid and in the loaded region.

A local tile is loaded if it's x and y coordinates are within [0, 103]

Returns:
true if this local tile is a valid, loaded local tile, false otherwise
- #### containsWall

```
public boolean containsWall​([LocalTile.Direction](LocalTile.Direction.html "enum in org.tribot.script.sdk.types") direction)
```
- #### getHeight

```
public int getHeight()
```
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