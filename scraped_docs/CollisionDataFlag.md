# CollisionDataFlag (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/CollisionDataFlag.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.CollisionDataFlag

* ---

```
public final class CollisionDataFlag
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A utility class containing collision data flags for tiles.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[BLOCK\_LINE\_OF\_SIGHT\_EAST](#BLOCK_LINE_OF_SIGHT_EAST)` | |
| `static int` | `[BLOCK\_LINE\_OF\_SIGHT\_FULL](#BLOCK_LINE_OF_SIGHT_FULL)` | |
| `static int` | `[BLOCK\_LINE\_OF\_SIGHT\_NORTH](#BLOCK_LINE_OF_SIGHT_NORTH)` | Directional line of sight blocking flags. |
| `static int` | `[BLOCK\_LINE\_OF\_SIGHT\_SOUTH](#BLOCK_LINE_OF_SIGHT_SOUTH)` | |
| `static int` | `[BLOCK\_LINE\_OF\_SIGHT\_WEST](#BLOCK_LINE_OF_SIGHT_WEST)` | |
| `static int` | `[BLOCK\_MOVEMENT\_EAST](#BLOCK_MOVEMENT_EAST)` | |
| `static int` | `[BLOCK\_MOVEMENT\_FLOOR](#BLOCK_MOVEMENT_FLOOR)` | |
| `static int` | `[BLOCK\_MOVEMENT\_FLOOR\_DECORATION](#BLOCK_MOVEMENT_FLOOR_DECORATION)` | |
| `static int` | `[BLOCK\_MOVEMENT\_FULL](#BLOCK_MOVEMENT_FULL)` | |
| `static int` | `[BLOCK\_MOVEMENT\_NORTH](#BLOCK_MOVEMENT_NORTH)` | |
| `static int` | `[BLOCK\_MOVEMENT\_NORTH\_EAST](#BLOCK_MOVEMENT_NORTH_EAST)` | |
| `static int` | `[BLOCK\_MOVEMENT\_NORTH\_WEST](#BLOCK_MOVEMENT_NORTH_WEST)` | Directional movement blocking flags. |
| `static int` | `[BLOCK\_MOVEMENT\_OBJECT](#BLOCK_MOVEMENT_OBJECT)` | Movement blocking type flags. |
| `static int` | `[BLOCK\_MOVEMENT\_SOUTH](#BLOCK_MOVEMENT_SOUTH)` | |
| `static int` | `[BLOCK\_MOVEMENT\_SOUTH\_EAST](#BLOCK_MOVEMENT_SOUTH_EAST)` | |
| `static int` | `[BLOCK\_MOVEMENT\_SOUTH\_WEST](#BLOCK_MOVEMENT_SOUTH_WEST)` | |
| `static int` | `[BLOCK\_MOVEMENT\_WEST](#BLOCK_MOVEMENT_WEST)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[CollisionDataFlag](#%3Cinit%3E())()` | |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### BLOCK\_MOVEMENT\_NORTH\_WEST

```
public static final int BLOCK_MOVEMENT_NORTH_WEST
```

Directional movement blocking flags.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_NORTH_WEST)
- #### BLOCK\_MOVEMENT\_NORTH

```
public static final int BLOCK_MOVEMENT_NORTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_NORTH)
- #### BLOCK\_MOVEMENT\_NORTH\_EAST

```
public static final int BLOCK_MOVEMENT_NORTH_EAST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_NORTH_EAST)
- #### BLOCK\_MOVEMENT\_EAST

```
public static final int BLOCK_MOVEMENT_EAST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_EAST)
- #### BLOCK\_MOVEMENT\_SOUTH\_EAST

```
public static final int BLOCK_MOVEMENT_SOUTH_EAST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_SOUTH_EAST)
- #### BLOCK\_MOVEMENT\_SOUTH

```
public static final int BLOCK_MOVEMENT_SOUTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_SOUTH)
- #### BLOCK\_MOVEMENT\_SOUTH\_WEST

```
public static final int BLOCK_MOVEMENT_SOUTH_WEST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_SOUTH_WEST)
- #### BLOCK\_MOVEMENT\_WEST

```
public static final int BLOCK_MOVEMENT_WEST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_WEST)
- #### BLOCK\_MOVEMENT\_OBJECT

```
public static final int BLOCK_MOVEMENT_OBJECT
```

Movement blocking type flags.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_OBJECT)
- #### BLOCK\_MOVEMENT\_FLOOR\_DECORATION

```
public static final int BLOCK_MOVEMENT_FLOOR_DECORATION
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_FLOOR_DECORATION)
- #### BLOCK\_MOVEMENT\_FLOOR

```
public static final int BLOCK_MOVEMENT_FLOOR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_FLOOR)
- #### BLOCK\_MOVEMENT\_FULL

```
public static final int BLOCK_MOVEMENT_FULL
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_MOVEMENT_FULL)
- #### BLOCK\_LINE\_OF\_SIGHT\_NORTH

```
public static final int BLOCK_LINE_OF_SIGHT_NORTH
```

Directional line of sight blocking flags.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_LINE_OF_SIGHT_NORTH)
- #### BLOCK\_LINE\_OF\_SIGHT\_EAST

```
public static final int BLOCK_LINE_OF_SIGHT_EAST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_LINE_OF_SIGHT_EAST)
- #### BLOCK\_LINE\_OF\_SIGHT\_SOUTH

```
public static final int BLOCK_LINE_OF_SIGHT_SOUTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_LINE_OF_SIGHT_SOUTH)
- #### BLOCK\_LINE\_OF\_SIGHT\_WEST

```
public static final int BLOCK_LINE_OF_SIGHT_WEST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_LINE_OF_SIGHT_WEST)
- #### BLOCK\_LINE\_OF\_SIGHT\_FULL

```
public static final int BLOCK_LINE_OF_SIGHT_FULL
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.CollisionDataFlag.BLOCK_LINE_OF_SIGHT_FULL)

+ ### Constructor Detail

- #### CollisionDataFlag

```
public CollisionDataFlag()
```