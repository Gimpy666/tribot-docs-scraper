# Region (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Region.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Region

* ---

```
public class Region
extends java.lang.Object
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Region](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getCurrentRegionID](#getCurrentRegionID())()` | Gets the region id of the region the player is currently in |
| `static java.util.Optional<[WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")>` | `[getInstancedTile](#getInstancedTile(org.tribot.script.sdk.interfaces.Tile))​([Tile](interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") tile)` | Gets the accurate WorldTile of a tile in an instance |
| `static int[][][]` | `[getInstanceTemplateChunks](#getInstanceTemplateChunks())()` | Gets instance template chunks |
| `static int[]` | `[getLoadedRegions](#getLoadedRegions())()` | Gets the loaded regions |
| `static boolean` | `[isLoaded](#isLoaded(int))​(int regionID)` | Checks if the loaded regions contains the given region id |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Region

```
public Region()
```

+ ### Method Detail

- #### getLoadedRegions

```
public static int[] getLoadedRegions()
```

Gets the loaded regions

Returns:
the loaded regions
- #### getCurrentRegionID

```
public static int getCurrentRegionID()
```

Gets the region id of the region the player is currently in

Returns:
the region id of the region the player is currently in
- #### getInstancedTile

```
public static java.util.Optional<[WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")> getInstancedTile​([Tile](interfaces/Tile.html "interface in org.tribot.script.sdk.interfaces") tile)
```

Gets the accurate WorldTile of a tile in an instance

Parameters:
`tile` - the tile that is in an instance
Returns:
the accurate WorldTile of the tile in the instance, empty if not in an instance
- #### isLoaded

```
public static boolean isLoaded​(int regionID)
```

Checks if the loaded regions contains the given region id

Parameters:
`regionID` - the region id to check
Returns:
true if the loaded regions contains the given region id, false otherwise
- #### getInstanceTemplateChunks

```
public static int[][][] getInstanceTemplateChunks()
```

Gets instance template chunks

Returns:
instance template chunks