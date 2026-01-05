# Tile (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Tile.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface Tile
```

Represents a tile in the game.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Tile](Tile.html "interface in net.runelite.api")` | `[getBridge](#getBridge())()` | Return the tile under this one, if this tile is a bridge |
| `[DecorativeObject](DecorativeObject.html "interface in net.runelite.api")` | `[getDecorativeObject](#getDecorativeObject())()` | Gets the decoration on the tile. |
| `[GameObject](GameObject.html "interface in net.runelite.api")[]` | `[getGameObjects](#getGameObjects())()` | Gets all game objects on the tile. |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[TileItem](TileItem.html "interface in net.runelite.api")>` | `[getGroundItems](#getGroundItems())()` | Get all the ground items for this tile |
| `[GroundObject](GroundObject.html "interface in net.runelite.api")` | `[getGroundObject](#getGroundObject())()` | Gets the object on the ground layer of the tile. |
| `[ItemLayer](ItemLayer.html "interface in net.runelite.api")` | `[getItemLayer](#getItemLayer())()` | Gets the items held on this tile. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocalLocation](#getLocalLocation())()` | Gets the local coordinate of the tile. |
| `int` | `[getPlane](#getPlane())()` | Gets the plane that this tile is on. |
| `int` | `[getRenderLevel](#getRenderLevel())()` | Get the plane this tile is rendered on, which is where the tile heights are from. |
| `[Point](Point.html "class in net.runelite.api")` | `[getSceneLocation](#getSceneLocation())()` | Gets the location coordinate of the tile in scene coords |
| `[SceneTileModel](SceneTileModel.html "interface in net.runelite.api")` | `[getSceneTileModel](#getSceneTileModel())()` | Gets the model of the tile in the scene. |
| `[SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api")` | `[getSceneTilePaint](#getSceneTilePaint())()` | Gets the scene paint of the tile. |
| `[WallObject](WallObject.html "interface in net.runelite.api")` | `[getWallObject](#getWallObject())()` | Gets the wall of the tile. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getWorldLocation](#getWorldLocation())()` | Gets the location coordinate of the tile in the world. |
| `void` | `[setGroundObject](#setGroundObject(net.runelite.api.GroundObject))​([GroundObject](GroundObject.html "interface in net.runelite.api") groundObject)` | Sets the object on the ground layer of the tile. |
| `void` | `[setSceneTileModel](#setSceneTileModel(net.runelite.api.SceneTileModel))​([SceneTileModel](SceneTileModel.html "interface in net.runelite.api") model)` | Sets the model of the tile in the scene. |
| `void` | `[setSceneTilePaint](#setSceneTilePaint(net.runelite.api.SceneTilePaint))​([SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api") paint)` | Sets the scene paint of the tile. |

* + ### Method Detail

- #### getDecorativeObject

```
[DecorativeObject](DecorativeObject.html "interface in net.runelite.api") getDecorativeObject()
```

Gets the decoration on the tile.

Returns:
the tile decoration
- #### getGameObjects

```
[GameObject](GameObject.html "interface in net.runelite.api")[] getGameObjects()
```

Gets all game objects on the tile.

Returns:
the game objects
- #### getItemLayer

```
[ItemLayer](ItemLayer.html "interface in net.runelite.api") getItemLayer()
```

Gets the items held on this tile.

Returns:
the item
- #### getGroundObject

```
[GroundObject](GroundObject.html "interface in net.runelite.api") getGroundObject()
```

Gets the object on the ground layer of the tile.

Returns:
the ground object
- #### setGroundObject

```
void setGroundObject​([GroundObject](GroundObject.html "interface in net.runelite.api") groundObject)
```

Sets the object on the ground layer of the tile.

Parameters:
`groundObject` - the ground object
- #### getWallObject

```
[WallObject](WallObject.html "interface in net.runelite.api") getWallObject()
```

Gets the wall of the tile.

Returns:
the wall object
- #### getSceneTilePaint

```
[SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api") getSceneTilePaint()
```

Gets the scene paint of the tile.

Returns:
the paint
- #### setSceneTilePaint

```
void setSceneTilePaint​([SceneTilePaint](SceneTilePaint.html "interface in net.runelite.api") paint)
```

Sets the scene paint of the tile.
Must only be mutated during map load.

Parameters:
`paint` - the paint
- #### getSceneTileModel

```
[SceneTileModel](SceneTileModel.html "interface in net.runelite.api") getSceneTileModel()
```

Gets the model of the tile in the scene.

Returns:
the tile model
- #### setSceneTileModel

```
void setSceneTileModel​([SceneTileModel](SceneTileModel.html "interface in net.runelite.api") model)
```

Sets the model of the tile in the scene.
Must only be mutated during map load.

Parameters:
`model` - the tile model
- #### getWorldLocation

```
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getWorldLocation()
```

Gets the location coordinate of the tile in the world.

Returns:
the world location
- #### getSceneLocation

```
[Point](Point.html "class in net.runelite.api") getSceneLocation()
```

Gets the location coordinate of the tile in scene coords

Returns:
the scene location
- #### getLocalLocation

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocalLocation()
```

Gets the local coordinate of the tile.

Returns:
the local location
- #### getPlane

```
int getPlane()
```

Gets the plane that this tile is on.

Returns:
the plane
- #### getRenderLevel

```
int getRenderLevel()
```

Get the plane this tile is rendered on, which is where the tile heights are from.

Returns:
- #### getGroundItems

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[TileItem](TileItem.html "interface in net.runelite.api")> getGroundItems()
```

Get all the ground items for this tile

Returns:
the ground items
- #### getBridge

```
[Tile](Tile.html "interface in net.runelite.api") getBridge()
```

Return the tile under this one, if this tile is a bridge

Returns: