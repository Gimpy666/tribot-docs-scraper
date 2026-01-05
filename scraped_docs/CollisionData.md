# CollisionData (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/CollisionData.html

**Package:** Packagenet.runelite.api

**Description:** The array covers all tiles in the scene (104x104), and the index into
 the array is of format [x][y] where x and y are the tiles scene
 coordinates, respectively.Collision flags are checked using the ...

---

* ---

```
public interface CollisionData
```

Represents tile collision data for the scene

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int[][]` | `[getFlags](#getFlags())()` | Gets a 2D array of tile collision flags. |

* + ### Method Detail

- #### getFlags

```
int[][] getFlags()
```

Gets a 2D array of tile collision flags.

The array covers all tiles in the scene (104x104), and the index into
the array is of format [x][y] where x and y are the tiles scene
coordinates, respectively.

Collision flags are checked using the bitwise and (&) operator. Flag
values can be obtained and used with the [`CollisionDataFlag`](CollisionDataFlag.html "class in net.runelite.api") class.

Returns:
all collision flags for the tiles in the scene
See Also:
[`Constants.SCENE_SIZE`](Constants.html#SCENE_SIZE)