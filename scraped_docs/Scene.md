# Scene (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Scene.html

**Package:** Packagenet.runelite.api

**Description:** This value is the x-axis world coordinate of tile (0, 0) in
 this scene (ie. the bottom-left most coordinates in the scene)....

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface Scene
extends [Renderable](Renderable.html "interface in net.runelite.api")
```

Represents a 3D scene

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[buildRoofs](#buildRoofs())()` | |
| `int` | `[getBaseX](#getBaseX())()` | Returns the x-axis base coordinate. |
| `int` | `[getBaseY](#getBaseY())()` | Returns the y-axis base coordinate. |
| `int` | `[getDrawDistance](#getDrawDistance())()` | |
| `[Tile](Tile.html "interface in net.runelite.api")[][][]` | `[getExtendedTiles](#getExtendedTiles())()` | Get the extended scene. |
| `byte[][][]` | `[getExtendedTileSettings](#getExtendedTileSettings())()` | Get the extended tile settings. |
| `int[][][]` | `[getInstanceTemplateChunks](#getInstanceTemplateChunks())()` | Contains a 3D array of template chunks for instanced areas. |
| `int[]` | `[getMapRegions](#getMapRegions())()` | Gets an array of map region IDs that are currently loaded. |
| `int` | `[getMinLevel](#getMinLevel())()` | Get the minimum scene level which will be rendered |
| `short[][][]` | `[getOverlayIds](#getOverlayIds())()` | Get the overlay ids for the scene. |
| `byte` | `[getOverrideAmount](#getOverrideAmount())()` | |
| `byte` | `[getOverrideHue](#getOverrideHue())()` | |
| `byte` | `[getOverrideLuminance](#getOverrideLuminance())()` | |
| `byte` | `[getOverrideSaturation](#getOverrideSaturation())()` | |
| `int` | `[getRoofRemovalMode](#getRoofRemovalMode())()` | |
| `int[][][]` | `[getRoofs](#getRoofs())()` | |
| `int[][][]` | `[getTileHeights](#getTileHeights())()` | Get the heights of the tiles on the scene. |
| `[Tile](Tile.html "interface in net.runelite.api")[][][]` | `[getTiles](#getTiles())()` | Gets the tiles in the scene |
| `byte[][][]` | `[getTileShapes](#getTileShapes())()` | Get the shapes of the tiles for the scene. |
| `short[][][]` | `[getUnderlayIds](#getUnderlayIds())()` | Get the underlay ids for the scene. |
| `int` | `[getWorldViewId](#getWorldViewId())()` | Get the world view id of this scene |
| `boolean` | `[isInstance](#isInstance())()` | Check if this scene is an instance |
| `void` | `[removeGameObject](#removeGameObject(net.runelite.api.GameObject))​([GameObject](GameObject.html "interface in net.runelite.api") gameObject)` | Remove a game object from the scene |
| `void` | `[removeTile](#removeTile(net.runelite.api.Tile))​([Tile](Tile.html "interface in net.runelite.api") tile)` | Remove a tile from the scene |
| `void` | `[setDrawDistance](#setDrawDistance(int))​(int drawDistance)` | |
| `void` | `[setMinLevel](#setMinLevel(int))​(int minLevel)` | Set the minimum scene level which will be rendered |
| `void` | `[setRoofRemovalMode](#setRoofRemovalMode(int))​(int flags)` | |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getTiles

```
[Tile](Tile.html "interface in net.runelite.api")[][][] getTiles()
```

Gets the tiles in the scene

Returns:
a 4x104x104 array of tiles in [plane][x][y]
- #### getExtendedTiles

```
[Tile](Tile.html "interface in net.runelite.api")[][][] getExtendedTiles()
```

Get the extended scene. This is larger than 104x104, and its size is [`Constants.EXTENDED_SCENE_SIZE`](Constants.html#EXTENDED_SCENE_SIZE).
- #### getExtendedTileSettings

```
byte[][][] getExtendedTileSettings()
```

Get the extended tile settings. This is larger than 104x104, and its size is [`Constants.EXTENDED_SCENE_SIZE`](Constants.html#EXTENDED_SCENE_SIZE).
- #### getDrawDistance

```
int getDrawDistance()
```
- #### setDrawDistance

```
void setDrawDistance​(int drawDistance)
```
- #### getWorldViewId

```
int getWorldViewId()
```

Get the world view id of this scene

Returns:
the world view id, or -1 if this is the top level scene
- #### getMinLevel

```
int getMinLevel()
```

Get the minimum scene level which will be rendered

Returns:
the plane of the minimum level
- #### setMinLevel

```
void setMinLevel​(int minLevel)
```

Set the minimum scene level which will be rendered

Parameters:
`minLevel` - the plane of the minimum level
- #### removeTile

```
void removeTile​([Tile](Tile.html "interface in net.runelite.api") tile)
```

Remove a tile from the scene

Parameters:
`tile` -
- #### removeGameObject

```
void removeGameObject​([GameObject](GameObject.html "interface in net.runelite.api") gameObject)
```

Remove a game object from the scene

Parameters:
`gameObject` -
- #### buildRoofs

```
void buildRoofs()
```
- #### getRoofs

```
int[][][] getRoofs()
```
- #### setRoofRemovalMode

```
void setRoofRemovalMode​(int flags)
```
- #### getRoofRemovalMode

```
int getRoofRemovalMode()
```
- #### getUnderlayIds

```
short[][][] getUnderlayIds()
```

Get the underlay ids for the scene. The value stored is id + 1, with 0 for no underlay.

Returns:
- #### getOverlayIds

```
short[][][] getOverlayIds()
```

Get the overlay ids for the scene. The value stored is id + 1, with 0 for no overlay.

Returns:
- #### getTileShapes

```
byte[][][] getTileShapes()
```

Get the shapes of the tiles for the scene.

Returns:
- #### getTileHeights

```
int[][][] getTileHeights()
```

Get the heights of the tiles on the scene.

Returns:
- #### getBaseX

```
int getBaseX()
```

Returns the x-axis base coordinate.

This value is the x-axis world coordinate of tile (0, 0) in
this scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base x-axis coordinate
- #### getBaseY

```
int getBaseY()
```

Returns the y-axis base coordinate.

This value is the y-axis world coordinate of tile (0, 0) in
this scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base y-axis coordinate
- #### isInstance

```
boolean isInstance()
```

Check if this scene is an instance

Returns:
See Also:
[`getInstanceTemplateChunks()`](#getInstanceTemplateChunks())
- #### getInstanceTemplateChunks

```
int[][][] getInstanceTemplateChunks()
```

Contains a 3D array of template chunks for instanced areas.

The array returned is of format [z][x][y], where z is the
plane, x and y the x-axis and y-axis coordinates of a tile
divided by the size of a chunk.

The bits of the int value held by the coordinates are -1 if there is no data,
structured in the following format:

```

0 1 2 3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| |rot| y chunk coord | x chunk coord |pln| |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

```

Returns:
the array of instance template chunks
See Also:
[`Constants.CHUNK_SIZE`](Constants.html#CHUNK_SIZE),
[`InstanceTemplates`](InstanceTemplates.html "enum in net.runelite.api")
- #### getMapRegions

```
int[] getMapRegions()
```

Gets an array of map region IDs that are currently loaded.

Returns:
the map regions
- #### getOverrideAmount

```
byte getOverrideAmount()
```
- #### getOverrideHue

```
byte getOverrideHue()
```
- #### getOverrideSaturation

```
byte getOverrideSaturation()
```
- #### getOverrideLuminance

```
byte getOverrideLuminance()
```