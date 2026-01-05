# ItemComposition (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ItemComposition.html

**Package:** Packagenet.runelite.api

**Description:** Calling this method on a noted item will result in the ID of itself
 in unnoted form, and on an unnoted item its noted variant....

---

* All Superinterfaces:
`[ParamHolder](ParamHolder.html "interface in net.runelite.api")`

---

```
public interface ItemComposition
extends [ParamHolder](ParamHolder.html "interface in net.runelite.api")
```

Represents the template of a specific item type.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getAmbient](#getAmbient())()` | Get the ambient light value |
| `short[]` | `[getColorToReplace](#getColorToReplace())()` | Get the colors to be replaced on this item's model for this item. |
| `short[]` | `[getColorToReplaceWith](#getColorToReplaceWith())()` | Get the colors applied to this item's model for this item. |
| `int` | `[getContrast](#getContrast())()` | Get the contrast light value |
| `int` | `[getHaPrice](#getHaPrice())()` | Get the high alchemy price for this item. |
| `int` | `[getId](#getId())()` | Gets the items ID. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[]` | `[getInventoryActions](#getInventoryActions())()` | Gets an array of possible right-click menu actions the item
has in a player inventory. |
| `int` | `[getInventoryModel](#getInventoryModel())()` | Gets the model ID of the inventory item. |
| `int` | `[getLinkedNoteId](#getLinkedNoteId())()` | Gets the item ID of the noted or unnoted variant of this item. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getMembersName](#getMembersName())()` | Gets the real item name, even if the player is on a F2P server. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the item's name as it appears in game. |
| `int` | `[getNote](#getNote())()` | Gets a value specifying whether the item is noted. |
| `int` | `[getPlaceholderId](#getPlaceholderId())()` | Gets the item ID of the normal or placeholder variant of this item. |
| `int` | `[getPlaceholderTemplateId](#getPlaceholderTemplateId())()` | Gets a value specifying whether the item is a placeholder. |
| `int` | `[getPrice](#getPrice())()` | Gets the store price of the item. |
| `int` | `[getShiftClickActionIndex](#getShiftClickActionIndex())()` | Gets the menu action index of the shift-click action. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[][]` | `[getSubops](#getSubops())()` | The subops for each op, indexed by op id. |
| `short[]` | `[getTextureToReplace](#getTextureToReplace())()` | Get the textures to be replaced on this item's model for this item. |
| `short[]` | `[getTextureToReplaceWith](#getTextureToReplaceWith())()` | Get the textures applied to this item's model for this item. |
| `int` | `[getXan2d](#getXan2d())()` | Get the x angle for 2d item sprites used in the inventory. |
| `int` | `[getYan2d](#getYan2d())()` | Get the y angle for 2d item sprites used in the inventory. |
| `int` | `[getZan2d](#getZan2d())()` | Get the z angle for 2d item sprites used in the inventory. |
| `boolean` | `[isMembers](#isMembers())()` | Checks whether the item is members only. |
| `boolean` | `[isStackable](#isStackable())()` | Checks whether the item is able to stack in a players inventory. |
| `boolean` | `[isTradeable](#isTradeable())()` | Returns whether or not the item can be sold on the grand exchange. |
| `void` | `[setColorToReplace](#setColorToReplace(short%5B%5D))​(short[] colorsToReplace)` | Set the colors to be replaced on this item's model for this item. |
| `void` | `[setColorToReplaceWith](#setColorToReplaceWith(short%5B%5D))​(short[] colorToReplaceWith)` | Set the colors applied to this item's model for this item. |
| `void` | `[setInventoryModel](#setInventoryModel(int))​(int model)` | Set the model ID of the inventory item. |
| `void` | `[setName](#setName(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Sets the item's name. |
| `void` | `[setShiftClickActionIndex](#setShiftClickActionIndex(int))​(int shiftClickActionIndex)` | Sets the menu action index of the shift-click action. |
| `void` | `[setTextureToReplace](#setTextureToReplace(short%5B%5D))​(short[] textureToFind)` | Set the textures to be replaced on this item's model for this item. |
| `void` | `[setTextureToReplaceWith](#setTextureToReplaceWith(short%5B%5D))​(short[] textureToReplaceWith)` | Set the textures applied to this item's model for this item. |
| `void` | `[setXan2d](#setXan2d(int))​(int angle)` | Set the x angle for 2d item sprites used in the inventory. |
| `void` | `[setYan2d](#setYan2d(int))​(int angle)` | Set the y angle for 2d item sprites used in the inventory. |
| `void` | `[setZan2d](#setZan2d(int))​(int angle)` | Set the z angle for 2d item sprites used in the inventory. |

- ### Methods inherited from interface net.runelite.api.[ParamHolder](ParamHolder.html "interface in net.runelite.api")

`[getIntValue](ParamHolder.html#getIntValue(int)), [getParams](ParamHolder.html#getParams()), [getStringValue](ParamHolder.html#getStringValue(int)), [setParams](ParamHolder.html#setParams(net.runelite.api.IterableHashTable)), [setValue](ParamHolder.html#setValue(int,int)), [setValue](ParamHolder.html#setValue(int,java.lang.String))`

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the item's name as it appears in game.
On a members server, this is always the item's actual name.
On a free server, this will be the actual name, with " (Members)" appended to it, e.g. Twisted bow (Members)

Returns:
the name of the item as it appears in game
- #### getMembersName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getMembersName()
```

Gets the real item name, even if the player is on a F2P server.
Unlike [`getName()`](#getName()), this will not have " (Members)" at the end on F2P servers.

Returns:
the real name of the item
- #### setName

```
void setName​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Sets the item's name.

Parameters:
`name` - the new name
- #### getId

```
int getId()
```

Gets the items ID.

Returns:
the items ID
See Also:
`ItemID`
- #### getNote

```
int getNote()
```

Gets a value specifying whether the item is noted.

Returns:
799 if noted, -1 otherwise
- #### getLinkedNoteId

```
int getLinkedNoteId()
```

Gets the item ID of the noted or unnoted variant of this item.

Calling this method on a noted item will result in the ID of itself
in unnoted form, and on an unnoted item its noted variant.

Returns:
the noted or unnoted variant of this item
- #### getPlaceholderId

```
int getPlaceholderId()
```

Gets the item ID of the normal or placeholder variant of this item.

Calling this method on a normal item will result in the ID of itself
in placeholder form, and on a placeholder item its normal variant.

Returns:
the normal or placeholder variant of this item
- #### getPlaceholderTemplateId

```
int getPlaceholderTemplateId()
```

Gets a value specifying whether the item is a placeholder.

Returns:
14401 if placeholder, -1 otherwise
- #### getPrice

```
int getPrice()
```

Gets the store price of the item.

Although not all items can be found in a store, they have a store price
which can be used to calculate high and low alchemy values. Multiplying
the price by `0.6` and `0.4` gives these high and low
alchemy values, respectively.

Returns:
the general store value of the item
See Also:
[`Constants.HIGH_ALCHEMY_MULTIPLIER`](Constants.html#HIGH_ALCHEMY_MULTIPLIER),
[`getHaPrice()`](#getHaPrice())
- #### getHaPrice

```
int getHaPrice()
```

Get the high alchemy price for this item. All items have a high alchemy price,
but not all items can be alched.

Returns:
the high alch price
- #### isMembers

```
boolean isMembers()
```

Checks whether the item is members only.

Returns:
true if members only, false otherwise.
- #### isStackable

```
boolean isStackable()
```

Checks whether the item is able to stack in a players inventory.

Returns:
true if stackable, false otherwise
- #### isTradeable

```
boolean isTradeable()
```

Returns whether or not the item can be sold on the grand exchange.
- #### getInventoryActions

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[] getInventoryActions()
```

Gets an array of possible right-click menu actions the item
has in a player inventory.

Returns:
the inventory menu actions
- #### getSubops

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[][] getSubops()
```

The subops for each op, indexed by op id.

Returns:
- #### getShiftClickActionIndex

```
int getShiftClickActionIndex()
```

Gets the menu action index of the shift-click action.

Returns:
the index of the shift-click action
- #### setShiftClickActionIndex

```
void setShiftClickActionIndex​(int shiftClickActionIndex)
```

Sets the menu action index of the shift-click action.

Parameters:
`shiftClickActionIndex` - the new index of the shift-click action
- #### getInventoryModel

```
int getInventoryModel()
```

Gets the model ID of the inventory item.

Returns:
the model ID
- #### setInventoryModel

```
void setInventoryModel​(int model)
```

Set the model ID of the inventory item. You will also need to flush the item model cache and the item
sprite cache to have the changes fully propagated after changing this value.

See Also:
[`Client.getItemModelCache()`](Client.html#getItemModelCache()),
[`Client.getItemSpriteCache()`](Client.html#getItemSpriteCache())
- #### getColorToReplace

```
@Nullable
short[] getColorToReplace()
```

Get the colors to be replaced on this item's model for this item.

Returns:
the colors to be replaced
See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api"),
[`getColorToReplaceWith()`](#getColorToReplaceWith())
- #### setColorToReplace

```
void setColorToReplace​(short[] colorsToReplace)
```

Set the colors to be replaced on this item's model for this item.

See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api"),
[`setColorToReplaceWith(short[])`](#setColorToReplaceWith(short%5B%5D))
- #### getColorToReplaceWith

```
@Nullable
short[] getColorToReplaceWith()
```

Get the colors applied to this item's model for this item.

Returns:
the colors to replace with
See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api"),
[`getColorToReplace()`](#getColorToReplace())
- #### setColorToReplaceWith

```
void setColorToReplaceWith​(short[] colorToReplaceWith)
```

Set the colors applied to this item's model for this item.

See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api"),
[`setColorToReplace(short[])`](#setColorToReplace(short%5B%5D))
- #### getTextureToReplace

```
@Nullable
short[] getTextureToReplace()
```

Get the textures to be replaced on this item's model for this item.

Returns:
the textures to be replaced
See Also:
[`getTextureToReplaceWith()`](#getTextureToReplaceWith())
- #### setTextureToReplace

```
void setTextureToReplace​(short[] textureToFind)
```

Set the textures to be replaced on this item's model for this item.

See Also:
[`setTextureToReplaceWith(short[])`](#setTextureToReplaceWith(short%5B%5D))
- #### getTextureToReplaceWith

```
@Nullable
short[] getTextureToReplaceWith()
```

Get the textures applied to this item's model for this item.

Returns:
the textures to replace with
See Also:
[`getTextureToReplace()`](#getTextureToReplace())
- #### setTextureToReplaceWith

```
void setTextureToReplaceWith​(short[] textureToReplaceWith)
```

Set the textures applied to this item's model for this item.

See Also:
[`setTextureToReplace(short[])`](#setTextureToReplace(short%5B%5D))
- #### getXan2d

```
int getXan2d()
```

Get the x angle for 2d item sprites used in the inventory.

Returns:
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getYan2d

```
int getYan2d()
```

Get the y angle for 2d item sprites used in the inventory.

Returns:
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getZan2d

```
int getZan2d()
```

Get the z angle for 2d item sprites used in the inventory.

Returns:
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### setXan2d

```
void setXan2d​(int angle)
```

Set the x angle for 2d item sprites used in the inventory.

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### setYan2d

```
void setYan2d​(int angle)
```

Set the y angle for 2d item sprites used in the inventory.

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### setZan2d

```
void setZan2d​(int angle)
```

Set the z angle for 2d item sprites used in the inventory.

See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getAmbient

```
int getAmbient()
```

Get the ambient light value

Returns:
- #### getContrast

```
int getContrast()
```

Get the contrast light value

Returns: