# Constants (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Constants.html

**Package:** Packagenet.runelite.api

**Description:** This value is exclusive. The plane is set by 2 bits which restricts
 the plane value to 0-3....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.Constants

* ---

```
public class Constants
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A utility class containing constant values.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[CHUNK\_SIZE](#CHUNK_SIZE)` | The width and length of a chunk (8x8 tiles). |
| `static int` | `[CLICK\_ACTION\_NONE](#CLICK_ACTION_NONE)` | |
| `static int` | `[CLICK\_ACTION\_SET\_HEADING](#CLICK_ACTION_SET_HEADING)` | |
| `static int` | `[CLICK\_ACTION\_WALK](#CLICK_ACTION_WALK)` | |
| `static int` | `[CLIENT\_DEFAULT\_ZOOM](#CLIENT_DEFAULT_ZOOM)` | The default camera zoom value. |
| `static int` | `[CLIENT\_TICK\_LENGTH](#CLIENT_TICK_LENGTH)` | The number of milliseconds in a client tick. |
| `static int` | `[EXTENDED\_SCENE\_SIZE](#EXTENDED_SCENE_SIZE)` | Size of the extended scene. |
| `static double` | `[GAME\_FIXED\_ASPECT\_RATIO](#GAME_FIXED_ASPECT_RATIO)` | The aspect ratio of the game when running in fixed mode. |
| `static int` | `[GAME\_FIXED\_HEIGHT](#GAME_FIXED_HEIGHT)` | The original height of the game when running in fixed mode. |
| `static [Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt")` | `[GAME\_FIXED\_SIZE](#GAME_FIXED_SIZE)` | Dimension representation of the width and height of the game in fixed mode. |
| `static int` | `[GAME\_FIXED\_WIDTH](#GAME_FIXED_WIDTH)` | The original width of the game when running in fixed mode. |
| `static int` | `[GAME\_TICK\_LENGTH](#GAME_TICK_LENGTH)` | The number of milliseconds in a server game tick. |
| `static float` | `[HIGH\_ALCHEMY\_MULTIPLIER](#HIGH_ALCHEMY_MULTIPLIER)` | High alchemy = shop price \* HIGH\_ALCHEMY\_MULTIPLIER |
| `static int` | `[ITEM\_SPRITE\_HEIGHT](#ITEM_SPRITE_HEIGHT)` | Height of a standard item sprite |
| `static int` | `[ITEM\_SPRITE\_WIDTH](#ITEM_SPRITE_WIDTH)` | Width of a standard item sprite |
| `static int` | `[MAX\_Z](#MAX_Z)` | The max allowed plane by the game. |
| `static int` | `[OVERWORLD\_MAX\_Y](#OVERWORLD_MAX_Y)` | The height of the overworld, in tiles. |
| `static int` | `[REGION\_SIZE](#REGION_SIZE)` | The width and length of a map region (64x64 tiles). |
| `static int` | `[ROOF\_FLAG\_BETWEEN](#ROOF_FLAG_BETWEEN)` | Flag for roof removal to remove the roofs that are above any tile between the camera and the player. |
| `static int` | `[ROOF\_FLAG\_DESTINATION](#ROOF_FLAG_DESTINATION)` | Flag for roof removal to remove the roofs above the player's destination tile. |
| `static int` | `[ROOF\_FLAG\_HOVERED](#ROOF_FLAG_HOVERED)` | Flag for roof removal to remove the roofs above the currently hovered tile. |
| `static int` | `[ROOF\_FLAG\_POSITION](#ROOF_FLAG_POSITION)` | Flag for roof removal to remove the roofs above the player's current position. |
| `static int` | `[SCENE\_SIZE](#SCENE_SIZE)` | The width and length of the scene (13 chunks x 8 tiles). |
| `static int` | `[TILE\_FLAG\_BRIDGE](#TILE_FLAG_BRIDGE)` | |
| `static int` | `[TILE\_FLAG\_UNDER\_ROOF](#TILE_FLAG_UNDER_ROOF)` | |
| `static int` | `[TILE\_FLAG\_VIS\_BELOW](#TILE_FLAG_VIS_BELOW)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Constants](#%3Cinit%3E())()` | |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### GAME\_FIXED\_WIDTH

```
public static final int GAME_FIXED_WIDTH
```

The original width of the game when running in fixed mode.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.GAME_FIXED_WIDTH)
- #### GAME\_FIXED\_HEIGHT

```
public static final int GAME_FIXED_HEIGHT
```

The original height of the game when running in fixed mode.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.GAME_FIXED_HEIGHT)
- #### GAME\_FIXED\_SIZE

```
public static final [Dimension](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Dimension.html?is-external=true "class or interface in java.awt") GAME_FIXED_SIZE
```

Dimension representation of the width and height of the game in fixed mode.
- #### GAME\_FIXED\_ASPECT\_RATIO

```
public static final double GAME_FIXED_ASPECT_RATIO
```

The aspect ratio of the game when running in fixed mode.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.GAME_FIXED_ASPECT_RATIO)
- #### CLIENT\_DEFAULT\_ZOOM

```
public static final int CLIENT_DEFAULT_ZOOM
```

The default camera zoom value.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CLIENT_DEFAULT_ZOOM)
- #### CHUNK\_SIZE

```
public static final int CHUNK_SIZE
```

The width and length of a chunk (8x8 tiles).

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CHUNK_SIZE)
- #### REGION\_SIZE

```
public static final int REGION_SIZE
```

The width and length of a map region (64x64 tiles).

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.REGION_SIZE)
- #### SCENE\_SIZE

```
public static final int SCENE_SIZE
```

The width and length of the scene (13 chunks x 8 tiles).

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.SCENE_SIZE)
- #### EXTENDED\_SCENE\_SIZE

```
public static final int EXTENDED_SCENE_SIZE
```

Size of the extended scene. To compute the offset to convert from scene coordinate to
extended scene coordinate, use (EXTENDED\_SCENE\_SIZE-SCENE\_SIZE)/2.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.EXTENDED_SCENE_SIZE)
- #### MAX\_Z

```
public static final int MAX_Z
```

The max allowed plane by the game.

This value is exclusive. The plane is set by 2 bits which restricts
the plane value to 0-3.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.MAX_Z)
- #### TILE\_FLAG\_BRIDGE

```
public static final int TILE_FLAG_BRIDGE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.TILE_FLAG_BRIDGE)
- #### TILE\_FLAG\_UNDER\_ROOF

```
public static final int TILE_FLAG_UNDER_ROOF
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.TILE_FLAG_UNDER_ROOF)
- #### TILE\_FLAG\_VIS\_BELOW

```
public static final int TILE_FLAG_VIS_BELOW
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.TILE_FLAG_VIS_BELOW)
- #### ROOF\_FLAG\_POSITION

```
public static final int ROOF_FLAG_POSITION
```

Flag for roof removal to remove the roofs above the player's current position.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ROOF_FLAG_POSITION)
- #### ROOF\_FLAG\_HOVERED

```
public static final int ROOF_FLAG_HOVERED
```

Flag for roof removal to remove the roofs above the currently hovered tile.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ROOF_FLAG_HOVERED)
- #### ROOF\_FLAG\_DESTINATION

```
public static final int ROOF_FLAG_DESTINATION
```

Flag for roof removal to remove the roofs above the player's destination tile.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ROOF_FLAG_DESTINATION)
- #### ROOF\_FLAG\_BETWEEN

```
public static final int ROOF_FLAG_BETWEEN
```

Flag for roof removal to remove the roofs that are above any tile between the camera and the player.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ROOF_FLAG_BETWEEN)
- #### OVERWORLD\_MAX\_Y

```
public static final int OVERWORLD_MAX_Y
```

The height of the overworld, in tiles. Coordinates above this are in caves and other such zones.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.OVERWORLD_MAX_Y)
- #### CLIENT\_TICK\_LENGTH

```
public static final int CLIENT_TICK_LENGTH
```

The number of milliseconds in a client tick.

This is the length of a single frame when the client is running at
the maximum framerate of 50 fps.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CLIENT_TICK_LENGTH)
- #### GAME\_TICK\_LENGTH

```
public static final int GAME_TICK_LENGTH
```

The number of milliseconds in a server game tick.

This is the length of a single game cycle under ideal conditions.
All game-play actions operate within multiples of this duration.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.GAME_TICK_LENGTH)
- #### ITEM\_SPRITE\_WIDTH

```
public static final int ITEM_SPRITE_WIDTH
```

Width of a standard item sprite

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ITEM_SPRITE_WIDTH)
- #### ITEM\_SPRITE\_HEIGHT

```
public static final int ITEM_SPRITE_HEIGHT
```

Height of a standard item sprite

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.ITEM_SPRITE_HEIGHT)
- #### HIGH\_ALCHEMY\_MULTIPLIER

```
public static final float HIGH_ALCHEMY_MULTIPLIER
```

High alchemy = shop price \* HIGH\_ALCHEMY\_MULTIPLIER

See Also:
[`ItemComposition.getPrice()`](ItemComposition.html#getPrice()),
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.HIGH_ALCHEMY_MULTIPLIER)
- #### CLICK\_ACTION\_NONE

```
public static final int CLICK_ACTION_NONE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CLICK_ACTION_NONE)
- #### CLICK\_ACTION\_WALK

```
public static final int CLICK_ACTION_WALK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CLICK_ACTION_WALK)
- #### CLICK\_ACTION\_SET\_HEADING

```
public static final int CLICK_ACTION_SET_HEADING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Constants.CLICK_ACTION_SET_HEADING)

+ ### Constructor Detail

- #### Constants

```
public Constants()
```