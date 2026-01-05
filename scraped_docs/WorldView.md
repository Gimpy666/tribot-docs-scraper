# WorldView (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/WorldView.html

**Package:** Packagenet.runelite.api

**Description:** The index into the array is the plane/z-axis coordinate....

---

* ---

```
public interface WorldView
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[TOPLEVEL](#TOPLEVEL)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `boolean` | `[contains](#contains(net.runelite.api.coords.LocalPoint))​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)` | Test if this worldview contains the given point |
| `boolean` | `[contains](#contains(net.runelite.api.coords.WorldPoint))​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)` | Test if this worldview contains the given point |
| `[Projectile](Projectile.html "interface in net.runelite.api")` | `[createProjectile](#createProjectile(int,int,int,int,int,int,int,int,int,int,net.runelite.api.Actor,int,int))​(int id,
int plane,
int startX,
int startY,
int startZ,
int startCycle,
int endCycle,
int slope,
int startHeight,
int endHeight,
[Actor](Actor.html "interface in net.runelite.api") target,
int targetX,
int targetY)` | Deprecated. |
| `int` | `[getBaseX](#getBaseX())()` | Returns the x-axis base coordinate. |
| `int` | `[getBaseY](#getBaseY())()` | Returns the y-axis base coordinate. |
| `[Projection](Projection.html "interface in net.runelite.api")` | `[getCanvasProjection](#getCanvasProjection())()` | Returns a [`Projection`](Projection.html "interface in net.runelite.api") to translate from this world view to the canvas |
| `[CollisionData](CollisionData.html "interface in net.runelite.api")[]` | `[getCollisionMaps](#getCollisionMaps())()` | Gets an array of tile collision data. |
| `[Deque](Deque.html "interface in net.runelite.api")<[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")>` | `[getGraphicsObjects](#getGraphicsObjects())()` | Gets a list of all graphics objects currently drawn. |
| `int` | `[getId](#getId())()` | Get the world view id |
| `int[][][]` | `[getInstanceTemplateChunks](#getInstanceTemplateChunks())()` | Contains a 3D array of template chunks for instanced areas. |
| `[Projection](Projection.html "interface in net.runelite.api")` | `[getMainWorldProjection](#getMainWorldProjection())()` | Returns a [`Projection`](Projection.html "interface in net.runelite.api") to translate from this world view to the main world |
| `int[]` | `[getMapRegions](#getMapRegions())()` | Gets an array of map region IDs that are currently loaded. |
| `int` | `[getPlane](#getPlane())()` | Gets the current plane the player is on. |
| `[Scene](Scene.html "interface in net.runelite.api")` | `[getScene](#getScene())()` | Gets the worldview's scene |
| `[Tile](Tile.html "interface in net.runelite.api")` | `[getSelectedSceneTile](#getSelectedSceneTile())()` | Gets the currently selected tile. |
| `int` | `[getSizeX](#getSizeX())()` | Get the size of the world view, x-axis |
| `int` | `[getSizeY](#getSizeY())()` | Get the size of the world view, y-axis |
| `int[][][]` | `[getTileHeights](#getTileHeights())()` | Gets a 3D array containing the heights of tiles in the
current scene. |
| `byte[][][]` | `[getTileSettings](#getTileSettings())()` | Gets a 3D array containing the settings of tiles in the
current scene. |
| `int[][]` | `[getXteaKeys](#getXteaKeys())()` | Returns a 2D array containing XTEA encryption keys used to decrypt
map region files. |
| `int` | `[getYellowClickAction](#getYellowClickAction())()` | Returns how clicking on tiles should behave for this WorldView. |
| `boolean` | `[isInstance](#isInstance())()` | Check if this scene is an instance |
| `boolean` | `[isTopLevel](#isTopLevel())()` | Test if this worldview is the top level world view. |
| `[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [NPC](NPC.html "interface in net.runelite.api")>` | `[npcs](#npcs())()` | Gets all the Non Player Characters in this view |
| `[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [Player](Player.html "interface in net.runelite.api")>` | `[players](#players())()` | Gets all of the Players in this view |
| `[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [WorldEntity](WorldEntity.html "interface in net.runelite.api")>` | `[worldEntities](#worldEntities())()` | Gets all the WorldEntities in this view |
| `[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [WorldView](WorldView.html "interface in net.runelite.api")>` | `[worldViews](#worldViews())()` | Get the worldviews of each worldentity in this worldview. |

* + ### Field Detail

- #### TOPLEVEL

```
static final int TOPLEVEL
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.WorldView.TOPLEVEL)

+ ### Method Detail

- #### getId

```
int getId()
```

Get the world view id

Returns:
the id, or -1 if this is the top level worldview
- #### isTopLevel

```
boolean isTopLevel()
```

Test if this worldview is the top level world view.

Returns:
- #### getScene

```
[Scene](Scene.html "interface in net.runelite.api") getScene()
```

Gets the worldview's scene
- #### players

```
[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [Player](Player.html "interface in net.runelite.api")> players()
```

Gets all of the Players in this view
- #### npcs

```
[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [NPC](NPC.html "interface in net.runelite.api")> npcs()
```

Gets all the Non Player Characters in this view
- #### worldEntities

```
[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [WorldEntity](WorldEntity.html "interface in net.runelite.api")> worldEntities()
```

Gets all the WorldEntities in this view
- #### worldViews

```
[IndexedObjectSet](IndexedObjectSet.html "interface in net.runelite.api")<? extends [WorldView](WorldView.html "interface in net.runelite.api")> worldViews()
```

Get the worldviews of each worldentity in this worldview.

Returns:
- #### getCollisionMaps

```
@Nullable
[CollisionData](CollisionData.html "interface in net.runelite.api")[] getCollisionMaps()
```

Gets an array of tile collision data.

The index into the array is the plane/z-axis coordinate.

Returns:
the collision data
- #### getPlane

```
int getPlane()
```

Gets the current plane the player is on.

This value indicates the current map level above ground level, where
ground level is 0. For example, going up a ladder in Lumbridge castle
will put the player on plane 1.

Note: This value will never be below 0. Basements and caves below ground
level use a tile offset and are still considered plane 0 by the game.

Returns:
the plane
- #### getTileHeights

```
int[][][] getTileHeights()
```

Gets a 3D array containing the heights of tiles in the
current scene.

Returns:
the tile heights
- #### getTileSettings

```
byte[][][] getTileSettings()
```

Gets a 3D array containing the settings of tiles in the
current scene.

Returns:
the tile settings
- #### getSizeX

```
int getSizeX()
```

Get the size of the world view, x-axis

Returns:
- #### getSizeY

```
int getSizeY()
```

Get the size of the world view, y-axis

Returns:
- #### getBaseX

```
int getBaseX()
```

Returns the x-axis base coordinate.

This value is the x-axis world coordinate of tile (0, 0) in
the current scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base x-axis coordinate
- #### getBaseY

```
int getBaseY()
```

Returns the y-axis base coordinate.

This value is the y-axis world coordinate of tile (0, 0) in
the current scene (ie. the bottom-left most coordinates in the scene).

Returns:
the base y-axis coordinate
- #### createProjectile

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
[Projectile](Projectile.html "interface in net.runelite.api") createProjectile​(int id,
int plane,
int startX,
int startY,
int startZ,
int startCycle,
int endCycle,
int slope,
int startHeight,
int endHeight,
@Nullable
[Actor](Actor.html "interface in net.runelite.api") target,
int targetX,
int targetY)
```

Deprecated.
Create a projectile.

Parameters:
`id` - projectile/spotanim id
`plane` - plane the projectile is on
`startX` - local x coordinate the projectile starts at
`startY` - local y coordinate the projectile starts at
`startZ` - local z coordinate the projectile starts at - includes tile height
`startCycle` - cycle the project starts
`endCycle` - cycle the projectile ends
`slope` -
`startHeight` - start height of projectile - excludes tile height
`endHeight` - end height of projectile - excludes tile height
`target` - optional actor target
`targetX` - target x - if an actor target is supplied should be the target x
`targetY` - target y - if an actor target is supplied should be the target y
Returns:
the new projectile
- #### getGraphicsObjects

```
[Deque](Deque.html "interface in net.runelite.api")<[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")> getGraphicsObjects()
```

Gets a list of all graphics objects currently drawn.

Returns:
all graphics objects
- #### getSelectedSceneTile

```
@Nullable
[Tile](Tile.html "interface in net.runelite.api") getSelectedSceneTile()
```

Gets the currently selected tile. (ie. last right clicked tile)

Returns:
the selected tile
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
- #### getXteaKeys

```
int[][] getXteaKeys()
```

Returns a 2D array containing XTEA encryption keys used to decrypt
map region files.

The array maps the region keys at index `n` to the region
ID held in [`getMapRegions()`](#getMapRegions()) at `n`.

The array of keys for the region make up a 128-bit encryption key
spread across 4 integers.

Returns:
the XTEA encryption keys
- #### contains

```
boolean contains​([WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") point)
```

Test if this worldview contains the given point

Parameters:
`point` -
Returns:
- #### contains

```
boolean contains​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point)
```

Test if this worldview contains the given point

Parameters:
`point` -
Returns:
- #### getMainWorldProjection

```
@Nullable
[Projection](Projection.html "interface in net.runelite.api") getMainWorldProjection()
```

Returns a [`Projection`](Projection.html "interface in net.runelite.api") to translate from this world view to the main world

Returns:
- #### getCanvasProjection

```
@Nullable
[Projection](Projection.html "interface in net.runelite.api") getCanvasProjection()
```

Returns a [`Projection`](Projection.html "interface in net.runelite.api") to translate from this world view to the canvas

Returns:
- #### getYellowClickAction

```
int getYellowClickAction()
```

Returns how clicking on tiles should behave for this WorldView.

Returns:
one of [`Constants.CLICK_ACTION_NONE`](Constants.html#CLICK_ACTION_NONE), [`Constants.CLICK_ACTION_WALK`](Constants.html#CLICK_ACTION_WALK), [`Constants.CLICK_ACTION_SET_HEADING`](Constants.html#CLICK_ACTION_SET_HEADING)