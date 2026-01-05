# WorldMapRenderer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/worldmap/WorldMapRenderer.html

**Package:** Packagenet.runelite.api.worldmap

---

* ---

```
public interface WorldMapRenderer
```

Renderer for the current worldmap map. Whenever the map is changed (eg between overworld and ancient cavern)
the renderer is recreated and reloaded with data from the new map.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[WorldMapRegion](WorldMapRegion.html "interface in net.runelite.api.worldmap")[][]` | `[getMapRegions](#getMapRegions())()` | Get the map regions in this map. |
| `boolean` | `[isLoaded](#isLoaded())()` | Checks whether the world map is currently loaded. |

* + ### Method Detail

- #### isLoaded

```
boolean isLoaded()
```

Checks whether the world map is currently loaded.

Returns:
true if the map is loaded, false otherwise
- #### getMapRegions

```
[WorldMapRegion](WorldMapRegion.html "interface in net.runelite.api.worldmap")[][] getMapRegions()
```

Get the map regions in this map. Each map region is 64x64 tiles.

Returns: