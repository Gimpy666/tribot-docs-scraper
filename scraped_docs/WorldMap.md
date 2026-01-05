# WorldMap (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/worldmap/WorldMap.html

**Package:** Packagenet.runelite.api.worldmap

---

* All Known Subinterfaces:
`[RenderOverview](../RenderOverview.html "interface in net.runelite.api")`

---

```
public interface WorldMap
```

Represents the World Map

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[WorldMapData](WorldMapData.html "interface in net.runelite.api.worldmap")` | `[getWorldMapData](#getWorldMapData())()` | The data represented by the render. |
| `[Point](../Point.html "class in net.runelite.api")` | `[getWorldMapPosition](#getWorldMapPosition())()` | Gets the current position of the local player on the world map. |
| `[WorldMapRenderer](WorldMapRenderer.html "interface in net.runelite.api.worldmap")` | `[getWorldMapRenderer](#getWorldMapRenderer())()` | Gets the world map renderer. |
| `float` | `[getWorldMapZoom](#getWorldMapZoom())()` | Gets the current zoom level of the world map. |
| `void` | `[initializeWorldMap](#initializeWorldMap(net.runelite.api.worldmap.WorldMapData))​([WorldMapData](WorldMapData.html "interface in net.runelite.api.worldmap") worldMapData)` | Initializes the world map with the provided data. |
| `void` | `[setWorldMapPositionTarget](#setWorldMapPositionTarget(net.runelite.api.coords.WorldPoint))​([WorldPoint](../coords/WorldPoint.html "class in net.runelite.api.coords") worldPoint)` | Sets the target position of the world map. |

* + ### Method Detail

- #### getWorldMapPosition

```
[Point](../Point.html "class in net.runelite.api") getWorldMapPosition()
```

Gets the current position of the local player on the world map.

Returns:
the world map position
- #### getWorldMapZoom

```
float getWorldMapZoom()
```

Gets the current zoom level of the world map.

Returns:
the world map zoon
- #### setWorldMapPositionTarget

```
void setWorldMapPositionTarget​([WorldPoint](../coords/WorldPoint.html "class in net.runelite.api.coords") worldPoint)
```

Sets the target position of the world map.

Parameters:
`worldPoint` - the new target position
- #### getWorldMapRenderer

```
[WorldMapRenderer](WorldMapRenderer.html "interface in net.runelite.api.worldmap") getWorldMapRenderer()
```

Gets the world map renderer.

Returns:
the world map renderer
- #### initializeWorldMap

```
void initializeWorldMap​([WorldMapData](WorldMapData.html "interface in net.runelite.api.worldmap") worldMapData)
```

Initializes the world map with the provided data.

Parameters:
`worldMapData` - the new map data
- #### getWorldMapData

```
[WorldMapData](WorldMapData.html "interface in net.runelite.api.worldmap") getWorldMapData()
```

The data represented by the render.

Returns:
the map data