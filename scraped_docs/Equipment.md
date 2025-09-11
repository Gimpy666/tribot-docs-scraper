# Equipment (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Equipment.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Equipment

* ---

```
public class Equipment
extends java.lang.Object
```

Utilities for interacting with the equipment tab

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk")` | Represents an equipment slot in the equipment tab |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Equipment](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[contains](#contains(int...))​(int... itemId)` | Determines if an item with the given itemId is equipped |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... itemName)` | Determines if an item with the given itemName is equipped |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> filter)` | Checks if any equipped item exists matching the specified filter |
| `static boolean` | `[equip](#equip(int))​(int itemId)` | Equips an item from the inventory with the given itemId. |
| `static boolean` | `[equip](#equip(java.lang.String))​(java.lang.String itemName)` | Equips an item from the inventory with the given itemName. |
| `static boolean` | `[equip](#equip(org.tribot.script.sdk.types.InventoryItem))​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item)` | Equips the given InventoryItem. |
| `static java.util.List<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")>` | `[getAll](#getAll())()` | Gets all the items that the player character has equipped. |
| `static int` | `[getCount](#getCount(int...))​(int... id)` | Counts the stacks of all items with the specified ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Counts the stacks of all items with the specified names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> filter)` | Counts the stacks of all items matching the specified filter |
| `static int` | `[remove](#remove(int))​(int itemId)` | Unequips an item from equipment with the given itemId |
| `static int` | `[remove](#remove(java.lang.String))​(java.lang.String itemName)` | Unequips an item from equipment with the given itemName |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Equipment

```
public Equipment()
```

+ ### Method Detail

- #### getAll

```
public static java.util.List<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> getAll()
```

Gets all the items that the player character has equipped.

Returns:
The equipped items.
- #### contains

```
public static boolean contains​(int... itemId)
```

Determines if an item with the given itemId is equipped
- #### contains

```
public static boolean contains​(java.lang.String... itemName)
```

Determines if an item with the given itemName is equipped
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> filter)
```

Checks if any equipped item exists matching the specified filter

Parameters:
`filter` - the filter
Returns:
true if any equipped item matches the filter, false otherwise
- #### getCount

```
public static int getCount​(int... id)
```

Counts the stacks of all items with the specified ids

Parameters:
`id` - the item ids
Returns:
the sum of all item stacks with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Counts the stacks of all items with the specified names

Parameters:
`name` - the item ids
Returns:
the sum of all item stacks with the specified names
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[EquipmentItem](types/EquipmentItem.html "class in org.tribot.script.sdk.types")> filter)
```

Counts the stacks of all items matching the specified filter

Parameters:
`filter` - the item filter
Returns:
the sum of all item stacks matching the specified filter
- #### remove

```
public static int remove​(int itemId)
```

Unequips an item from equipment with the given itemId

Returns:
The stack amount of the item that was removed. 0 if no item was removed.
- #### remove

```
public static int remove​(java.lang.String itemName)
```

Unequips an item from equipment with the given itemName

Returns:
The stack amount of the item that was removed. 0 if no item was removed.
- #### equip

```
public static boolean equip​(int itemId)
```

Equips an item from the inventory with the given itemId.

Returns:
True if the item click was successful. False otherwise.
- #### equip

```
public static boolean equip​(java.lang.String itemName)
```

Equips an item from the inventory with the given itemName.

Returns:
True if the item click was successful. False otherwise.
- #### equip

```
public static boolean equip​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item)
```

Equips the given InventoryItem.

Returns:
True if the item click was successful. False otherwise.