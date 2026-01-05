# ItemContainer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ItemContainer.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface ItemContainer
extends [Node](Node.html "interface in net.runelite.api")
```

Represents an inventory that contains items.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `boolean` | `[contains](#contains(int))​(int itemId)` | Check if this item container contains the given item |
| `int` | `[count](#count())()` | Get the total number of filled slots in the item container. |
| `int` | `[count](#count(int))​(int itemId)` | Counts how many of an item this item container contains |
| `int` | `[find](#find(int))​(int itemId)` | Find the first index of an item in the container |
| `int` | `[getId](#getId())()` | Get the item container id |
| `[Item](Item.html "class in net.runelite.api")` | `[getItem](#getItem(int))​(int slot)` | Gets an item from the container at the given slot. |
| `[Item](Item.html "class in net.runelite.api")[]` | `[getItems](#getItems())()` | Gets an array of all items in the container. |
| `int` | `[size](#size())()` | Get the number of slots in this item container. |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getId

```
int getId()
```

Get the item container id

Returns:
See Also:
`InventoryID`
- #### getItems

```
@Nonnull
[Item](Item.html "class in net.runelite.api")[] getItems()
```

Gets an array of all items in the container.

Returns:
the items held
- #### getItem

```
@Nullable
[Item](Item.html "class in net.runelite.api") getItem​(int slot)
```

Gets an item from the container at the given slot.

Parameters:
`slot` -
Returns:
the item
See Also:
[`Item`](Item.html "class in net.runelite.api")
- #### contains

```
boolean contains​(int itemId)
```

Check if this item container contains the given item

Parameters:
`itemId` -
Returns:
See Also:
`ItemID`
- #### count

```
int count​(int itemId)
```

Counts how many of an item this item container contains

Parameters:
`itemId` -
Returns:
See Also:
`ItemID`
- #### size

```
int size()
```

Get the number of slots in this item container. This includes empty slots.
For example for the player inventory it can be 28 even with no items in the inventory.

Returns:
See Also:
[`to get the number of filled slots instead`](#count())
- #### count

```
int count()
```

Get the total number of filled slots in the item container.

Returns:
- #### find

```
int find​(int itemId)
```

Find the first index of an item in the container

Parameters:
`itemId` - the item
Returns:
the item index, or -1 if not found