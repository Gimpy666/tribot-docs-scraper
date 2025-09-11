# Area (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Area.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Area

* ---

```
public class Area
extends java.lang.Object
```

Represents a contiguous set of tiles in the game

* + ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[contains](#contains(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Checks if this area contains the specified position |
| `boolean` | `[containsMyPlayer](#containsMyPlayer())()` | Checks if this area contains the local player |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `static [Area](Area.html "class in org.tribot.script.sdk.types")` | `[fromPolygon](#fromPolygon(java.util.List))​(java.util.List<[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")> tiles)` | Creates an Area from a polygon |
| `static [Area](Area.html "class in org.tribot.script.sdk.types")` | `[fromPolygon](#fromPolygon(org.tribot.script.sdk.interfaces.Tile...))​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")... tiles)` | Creates an Area from a polygon |
| `static [Area](Area.html "class in org.tribot.script.sdk.types")` | `[fromRadius](#fromRadius(org.tribot.script.sdk.interfaces.Tile,int))​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") centerTile,
int radius)` | Creates an area around the center tile with the specified radius |
| `static [Area](Area.html "class in org.tribot.script.sdk.types")` | `[fromRectangle](#fromRectangle(org.tribot.script.sdk.interfaces.Tile,org.tribot.script.sdk.interfaces.Tile))​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") base1,
[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") base2)` | Creates a rectangular area with the two specified tiles as the bounds |
| `java.util.List<[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")>` | `[getAllTiles](#getAllTiles())()` | Gets a list of all the tiles in the area. |
| `java.awt.Polygon` | `[getBounds](#getBounds())()` | Gets the bounds of this area on the screen |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getCenter](#getCenter())()` | Gets the center tile of this area |
| `org.tribot.api2007.types.RSArea` | `[getLegacyArea](#getLegacyArea())()` | |
| `java.awt.Polygon` | `[getMinimapBounds](#getMinimapBounds())()` | Gets the bounds of this area on the minimap |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getRandomTile](#getRandomTile())()` | Gets a random tile in this area |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |
| `[Area](Area.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int))​(int x,
int y)` | Translates (shifts) this area by the specified x and y |
| `[Area](Area.html "class in org.tribot.script.sdk.types")` | `[translate](#translate(int,int,int))​(int x,
int y,
int z)` | Translates (shifts) this area by the specified x, y, and z |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### fromPolygon

```
public static [Area](Area.html "class in org.tribot.script.sdk.types") fromPolygon​(java.util.List<[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")> tiles)
```

Creates an Area from a polygon

Parameters:
`tiles` - The points that make up the corners of the polygon
- #### fromRadius

```
public static [Area](Area.html "class in org.tribot.script.sdk.types") fromRadius​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") centerTile,
int radius)
```

Creates an area around the center tile with the specified radius

Parameters:
`centerTile` - the center tile
`radius` - the tile radius
Returns:
an area around the center tile with the specified radius
- #### fromPolygon

```
public static [Area](Area.html "class in org.tribot.script.sdk.types") fromPolygon​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces")... tiles)
```

Creates an Area from a polygon

Parameters:
`tiles` - The points that make up the corners of the polygon
- #### fromRectangle

```
public static [Area](Area.html "class in org.tribot.script.sdk.types") fromRectangle​([Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") base1,
[Tile](../interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") base2)
```

Creates a rectangular area with the two specified tiles as the bounds

Parameters:
`base1` - the first bound
`base2` - the second bound
Returns:
a rectangle area inbetween the two tiles
- #### getCenter

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getCenter()
```

Gets the center tile of this area

Returns:
the center tile of this area
- #### getBounds

```
public java.awt.Polygon getBounds()
```

Gets the bounds of this area on the screen

Returns:
this area's polygon bounds on the screen
- #### getMinimapBounds

```
public java.awt.Polygon getMinimapBounds()
```

Gets the bounds of this area on the minimap

Returns:
the bounds of this area on the minimap
- #### contains

```
public boolean contains​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Checks if this area contains the specified position

Parameters:
`position` - the position to check
Returns:
true if this area contains the specified position, false otherwise
- #### containsMyPlayer

```
public boolean containsMyPlayer()
```

Checks if this area contains the local player

Returns:
true if this area contains the local player, false otherwise
- #### translate

```
public [Area](Area.html "class in org.tribot.script.sdk.types") translate​(int x,
int y)
```

Translates (shifts) this area by the specified x and y

Parameters:
`x` - the x translation
`y` - the y translation
Returns:
a new area with the specified translation
- #### translate

```
public [Area](Area.html "class in org.tribot.script.sdk.types") translate​(int x,
int y,
int z)
```

Translates (shifts) this area by the specified x, y, and z

Parameters:
`x` - the x translation
`y` - the y translation
`z` - the z translation (plane)
Returns:
a new area with the specified translation
- #### getRandomTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getRandomTile()
```

Gets a random tile in this area

Returns:
a random tile in this area
- #### getAllTiles

```
public java.util.List<[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")> getAllTiles()
```

Gets a list of all the tiles in the area.
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
- #### getLegacyArea

```
public org.tribot.api2007.types.RSArea getLegacyArea()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`