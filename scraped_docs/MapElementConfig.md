# MapElementConfig (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/worldmap/MapElementConfig.html

**Package:** Packagenet.runelite.api.worldmap

---

* ---

```
public interface MapElementConfig
```

Represents configuration for a map element

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getCategory](#getCategory())()` | Get the category of this icon type. |
| `[SpritePixels](../SpritePixels.html "interface in net.runelite.api")` | `[getMapIcon](#getMapIcon(boolean))​(boolean unused)` | Gets the sprite icon to display on the world map. |

* + ### Method Detail

- #### getMapIcon

```
[SpritePixels](../SpritePixels.html "interface in net.runelite.api") getMapIcon​(boolean unused)
```

Gets the sprite icon to display on the world map.

Parameters:
`unused` - unused value
Returns:
the sprite icon to display on the world map
- #### getCategory

```
int getCategory()
```

Get the category of this icon type.

Returns: