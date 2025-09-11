# Inventory (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Inventory.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Inventory

* ---

```
public class Inventory
extends java.lang.Object
```

Utilities for interacting with and inspecting the inventory

See Also:
[`Query.inventory()`](query/Query.html#inventory())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Inventory.DropPattern](Inventory.DropPattern.html "enum in org.tribot.script.sdk")` | A pattern, or order, to drop items in |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Inventory](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[contains](#contains(int...))​(int... id)` | Checks if any inventory item exists with any of the specified ids

param id the item ids |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if any inventory item exists with any of the specified names

param name the item names |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> filter)` | Checks if any inventory item exists matching the specified filter

param filter the item filter |
| `static int` | `[drop](#drop(int...))​(int... ids)` | Drops all items with the specified ids |
| `static int` | `[drop](#drop(java.lang.String...))​(java.lang.String... names)` | Drops all items with the specified names |
| `static int` | `[drop](#drop(java.util.List))​(java.util.List<? extends [Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> items)` | Drops all items in the specified list |
| `static java.util.List<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")>` | `[getAll](#getAll())()` | Gets all inventory items |
| `static int` | `[getCount](#getCount(int...))​(int... id)` | Sums the item stacks of all inventory items with the specified item ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Sums the item stacks of all inventory items with the specified item names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> filter)` | Sums the item stacks of all inventory items matching the specified filter |
| `static int` | `[getEmptySlots](#getEmptySlots())()` | Gets the number of open inventory slots |
| `static int` | `[getFilledSlots](#getFilledSlots())()` | Gets the amount of filled inventory slots |
| `static java.util.Optional<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")>` | `[getSelected](#getSelected())()` | Gets the selected inventory item, if an item is selected |
| `static boolean` | `[isEmpty](#isEmpty())()` | Checks if the inventory is completely empty |
| `static boolean` | `[isFull](#isFull())()` | Checks if the inventory is full |
| `static boolean` | `[sort](#sort(int...))​(int... ids)` | Sorts the inventory by ids in the order they are specified |
| `static boolean` | `[sort](#sort(java.lang.String...))​(java.lang.String... names)` | Sorts the inventory by names in the order they are specified |
| `static boolean` | `[sort](#sort(java.util.Comparator))​(java.util.Comparator<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> comparator)` | Sorts the inventory by the specified comparator |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Inventory

```
public Inventory()
```

+ ### Method Detail

- #### getAll

```
public static java.util.List<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> getAll()
```

Gets all inventory items

Returns:
all inventory items
- #### getSelected

```
public static java.util.Optional<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> getSelected()
```

Gets the selected inventory item, if an item is selected

Returns:
the selected inventory item, or an empty optional if none selected
- #### isFull

```
public static boolean isFull()
```

Checks if the inventory is full

Returns:
true if the inventory is full, false otherwise
- #### isEmpty

```
public static boolean isEmpty()
```

Checks if the inventory is completely empty

Returns:
true if the inventory is empty (contains no items), false otherwise
- #### getEmptySlots

```
public static int getEmptySlots()
```

Gets the number of open inventory slots

Returns:
the number of open inventory slots
- #### getFilledSlots

```
public static int getFilledSlots()
```

Gets the amount of filled inventory slots

Returns:
the number of filled inventory slots
- #### sort

```
public static boolean sort​(java.lang.String... names)
```

Sorts the inventory by names in the order they are specified

Parameters:
`names` - the item names to sort
Returns:
true if sorted, false otherwise
- #### sort

```
public static boolean sort​(int... ids)
```

Sorts the inventory by ids in the order they are specified

Parameters:
`ids` - the item ids to sort
Returns:
true if sorted, false otherwise
- #### sort

```
public static boolean sort​(java.util.Comparator<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> comparator)
```

Sorts the inventory by the specified comparator

Parameters:
`comparator` - the comparator to sort the inventory
Returns:
true if sorted successfully, false otherwise (timed out or too many attempts)
- #### getCount

```
public static int getCount​(int... id)
```

Sums the item stacks of all inventory items with the specified item ids

Parameters:
`id` - the item ids
Returns:
the sum of item stacks of inventory items with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Sums the item stacks of all inventory items with the specified item names

Parameters:
`name` - the item names
Returns:
the sum of item stacks of inventory items with the specified names
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> filter)
```

Sums the item stacks of all inventory items matching the specified filter

Parameters:
`filter` - the item filter
Returns:
the sum of item stacks of inventory items matching the specified filter
- #### contains

```
public static boolean contains​(int... id)
```

Checks if any inventory item exists with any of the specified ids

param id the item ids

Returns:
true if any inventory item exists with any of the specified ids, false otherwise
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if any inventory item exists with any of the specified names

param name the item names

Returns:
true if any inventory item exists with any of the specified names, false otherwise
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types")> filter)
```

Checks if any inventory item exists matching the specified filter

param filter the item filter

Returns:
true if any inventory item exists matching the specified filter, false otherwise
- #### drop

```
public static int drop​(int... ids)
```

Drops all items with the specified ids

Parameters:
`ids` - the ids to drop
Returns:
the dropped item's summed item stacks
- #### drop

```
public static int drop​(java.lang.String... names)
```

Drops all items with the specified names

Parameters:
`names` - the names to drop
Returns:
the dropped item's summed item stacks
- #### drop

```
public static int drop​(java.util.List<? extends [Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> items)
```

Drops all items in the specified list

Parameters:
`items` - the items to drop
Returns:
the dropped item's summed item stacks