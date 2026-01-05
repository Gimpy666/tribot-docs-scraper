# WorldMapRegion (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/worldmap/WorldMapRegion.html

**Package:** Packagenet.runelite.api.worldmap

---

* ---

```
public interface WorldMapRegion
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldMapIcon](WorldMapIcon.html "interface in net.runelite.api.worldmap")>` | `[getMapIcons](#getMapIcons())()` | Gets visible map icons. |

* + ### Method Detail

- #### getMapIcons

```
[Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldMapIcon](WorldMapIcon.html "interface in net.runelite.api.worldmap")> getMapIcons()
```

Gets visible map icons. The underlying list is modified as the map is panned around.

Returns: