# PlayerComposition (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/PlayerComposition.html

**Package:** Packagenet.runelite.api

**Description:** IDs betweenKIT_OFFSETandITEM_OFFSETare kits, offset byKIT_OFFSET.
 IDs greater than or equal toITEM_OFFSETare items, offset byITEM_OFFSET....

---

* ---

```
public interface PlayerComposition
```

Represents the template of a player.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[ITEM\_OFFSET](#ITEM_OFFSET)` | |
| `static int` | `[KIT\_OFFSET](#KIT_OFFSET)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `int[]` | `[getColors](#getColors())()` | Get the body part colors for this player composition. |
| `[ColorTextureOverride](ColorTextureOverride.html "interface in net.runelite.api")[]` | `[getColorTextureOverrides](#getColorTextureOverrides())()` | Get the overrides for this player composition, indexed by kit id. |
| `int` | `[getEquipmentId](#getEquipmentId(net.runelite.api.kit.KitType))​([KitType](kit/KitType.html "enum in net.runelite.api.kit") type)` | Gets the equipment ID of a particular slot. |
| `int[]` | `[getEquipmentIds](#getEquipmentIds())()` | Gets an array of IDs related to equipment slots. |
| `int` | `[getGender](#getGender())()` | Get the player gender |
| `int` | `[getKitId](#getKitId(net.runelite.api.kit.KitType))​([KitType](kit/KitType.html "enum in net.runelite.api.kit") type)` | Gets the kit ID of a particular slot. |
| `int` | `[getTransformedNpcId](#getTransformedNpcId())()` | Get the ID of the NPC that the player is currently transformed into. |
| `boolean` | `[isFemale](#isFemale())()` | Deprecated.
use getGender
|
| `void` | `[setHash](#setHash())()` | Update the cached hash value for player equipment
Used to cache the player models based on equipment. |
| `void` | `[setTransformedNpcId](#setTransformedNpcId(int))​(int id)` | Set the ID of the NPC that the player should transform into. |

* + ### Field Detail

- #### KIT\_OFFSET

```
static final int KIT_OFFSET
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.PlayerComposition.KIT_OFFSET)
- #### ITEM\_OFFSET

```
static final int ITEM_OFFSET
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.PlayerComposition.ITEM_OFFSET)

+ ### Method Detail

- #### isFemale

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
boolean isFemale()
```

Deprecated.
use getGender

Checks if the player is female.

Returns:
true if the player is female
- #### getGender

```
int getGender()
```

Get the player gender

Returns:
0 for male, 1 for female
- #### getColors

```
int[] getColors()
```

Get the body part colors for this player composition.

Returns:
an array of the colors, always size 5
- #### getEquipmentIds

```
int[] getEquipmentIds()
```

Gets an array of IDs related to equipment slots.

IDs between [`KIT_OFFSET`](#KIT_OFFSET) and [`ITEM_OFFSET`](#ITEM_OFFSET) are kits, offset by [`KIT_OFFSET`](#KIT_OFFSET).
IDs greater than or equal to [`ITEM_OFFSET`](#ITEM_OFFSET) are items, offset by [`ITEM_OFFSET`](#ITEM_OFFSET).

Returns:
the equipment IDs
- #### getEquipmentId

```
int getEquipmentId​([KitType](kit/KitType.html "enum in net.runelite.api.kit") type)
```

Gets the equipment ID of a particular slot.

Parameters:
`type` - equipment slot
Returns:
the equipment ID
- #### getKitId

```
int getKitId​([KitType](kit/KitType.html "enum in net.runelite.api.kit") type)
```

Gets the kit ID of a particular slot.

Parameters:
`type` - equipment slot
Returns:
the kit ID
- #### setHash

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
void setHash()
```

Update the cached hash value for player equipment
Used to cache the player models based on equipment.
- #### getTransformedNpcId

```
int getTransformedNpcId()
```

Get the ID of the NPC that the player is currently transformed into.
Used natively for cutscenes.

Returns:
the id of the npc that the player is rendering as
See Also:
[`setTransformedNpcId(int)`](#setTransformedNpcId(int))
- #### setTransformedNpcId

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
void setTransformedNpcId​(int id)
```

Set the ID of the NPC that the player should transform into.
Used natively for cutscenes.

Parameters:
`id` - the id of the npc that the player should render as
See Also:
[`getTransformedNpcId()`](#getTransformedNpcId())
- #### getColorTextureOverrides

```
@Nullable
[ColorTextureOverride](ColorTextureOverride.html "interface in net.runelite.api")[] getColorTextureOverrides()
```

Get the overrides for this player composition, indexed by kit id. The overrides
replace the target color/textures for the item instead of using the target colors/textures
from the item composition. Only works if the kittype is an item.

Returns: