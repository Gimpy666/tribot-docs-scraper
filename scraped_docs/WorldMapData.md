# WorldMapData (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/worldmap/WorldMapData.html

**Package:** Packagenet.runelite.api.worldmap

---

* All Known Subinterfaces:
`[WorldMapData](../WorldMapData.html "interface in net.runelite.api")`

---

```
public interface WorldMapData
```

Represents data for a worldmap surface

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `boolean` | `[surfaceContainsPosition](#surfaceContainsPosition(int,int))​(int x,
int y)` | Checks whether the passed coordinates are on the surface of the
world map. |

* + ### Method Detail

- #### surfaceContainsPosition

```
boolean surfaceContainsPosition​(int x,
int y)
```

Checks whether the passed coordinates are on the surface of the
world map.

Parameters:
`x` - x-axis coordinate
`y` - y-axis coordinate
Returns:
true if the coordinate is on the surface, false otherwise