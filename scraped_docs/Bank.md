# Bank (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Bank.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Bank

* ---

```
public class Bank
extends java.lang.Object
```

Utilities for interacting with the Runescape bank.

See Also:
[`Query.bank()`](query/Query.html#bank())

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Bank](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static boolean` | `[close](#close())()` | Closes the banking interface. |
| `static boolean` | `[contains](#contains(int...))​(int... itemId)` | Determines if the bank contains the given itemId by looking through the banking interface. |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if any bank item exists with the specified name |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Checks if any bank item exists matching the specified filter |
| `static boolean` | `[deposit](#deposit(int,int))​(int itemId,
int amount)` | Deposits the specified amount of an item with the specified id |
| `static boolean` | `[deposit](#deposit(java.lang.String,int))​(java.lang.String itemName,
int amount)` | Deposits the specified amount of an item with the specified name |
| `static boolean` | `[deposit](#deposit(org.tribot.script.sdk.types.InventoryItem,int))​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item,
int amount)` | Deposits the specified quantity of the specified item |
| `static boolean` | `[depositAll](#depositAll(int))​(int itemId)` | Deposits all of an item with the specified id |
| `static boolean` | `[depositAll](#depositAll(java.lang.String))​(java.lang.String itemName)` | Deposits all of an item with the specified name |
| `static boolean` | `[depositAll](#depositAll(org.tribot.script.sdk.types.InventoryItem))​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item)` | Deposits all of the specified item |
| `static boolean` | `[depositEquipment](#depositEquipment())()` | Deposits all equipment |
| `static boolean` | `[depositInventory](#depositInventory())()` | Deposits the entire inventory |
| `static boolean` | `[ensureOpen](#ensureOpen())()` | Ensures the bank is open. |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getAll](#getAll())()` | Gets all the items from the banking interface. |
| `static int` | `[getCount](#getCount(int...))​(int... itemId)` | Sums the item stacks of the bank items with the specified item ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Sums the item stacks of the bank items with the specified item names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Sums the item stacks of the bank items matching the specified filter |
| `static boolean` | `[isDepositBoxOpen](#isDepositBoxOpen())()` | Determines if the deposit box interface is open. |
| `static boolean` | `[isNearby](#isNearby())()` | Determines if the player character is in a bank by looking for Bank objects/npcs within 15 tiles. |
| `static boolean` | `[isOpen](#isOpen())()` | Determines if the banking interface is open. |
| `static boolean` | `[open](#open())()` | Deprecated, for removal: This API element is subject to removal in a future version. |
| `static boolean` | `[withdraw](#withdraw(int,int))​(int itemId,
int amount)` | Withdraws the specified amount of an item with the specified id |
| `static boolean` | `[withdraw](#withdraw(java.lang.String,int))​(java.lang.String itemName,
int amount)` | Withdraws the specified amount of an item with the specified name |
| `static boolean` | `[withdraw](#withdraw(org.tribot.script.sdk.interfaces.Item,int))​([Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces") item,
int amount)` | Withdraws the specified amount of the specified item |
| `static boolean` | `[withdrawAll](#withdrawAll(int))​(int itemId)` | Withdraws all of an item with the specified id |
| `static boolean` | `[withdrawAll](#withdrawAll(java.lang.String))​(java.lang.String itemName)` | Withdraws all of an item with the specified name |
| `static boolean` | `[withdrawAll](#withdrawAll(org.tribot.script.sdk.interfaces.Item))​([Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces") item)` | Withdraws all of the specified item |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Bank

```
public Bank()
```

+ ### Method Detail

- #### getAll

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getAll()
```

Gets all the items from the banking interface.

Returns:
The bank items. Empty if the bank isn't open.
- #### contains

```
public static boolean contains​(int... itemId)
```

Determines if the bank contains the given itemId by looking through the banking interface.

Parameters:
`itemId` - The id of the item that is checked.
Returns:
True if the banking interface contains the itemId. False if the bank isn't open or doesn't contain the item.
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if any bank item exists with the specified name

Parameters:
`name` - the item name
Returns:
true if any bank item exists with the specified name, false otherwise
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Checks if any bank item exists matching the specified filter

Parameters:
`filter` - the item filter
Returns:
true if any bank item exists with the specified name, false otherwise
- #### getCount

```
public static int getCount​(int... itemId)
```

Sums the item stacks of the bank items with the specified item ids

Parameters:
`itemId` - the item ids
Returns:
the sum of the item stacks of items with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Sums the item stacks of the bank items with the specified item names

Parameters:
`name` - the item names
Returns:
the sum of the item stacks of items with the specified names
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Sums the item stacks of the bank items matching the specified filter

Parameters:
`filter` - the item filter
Returns:
the sum of the item stacks of items matching the specified filter
- #### isOpen

```
public static boolean isOpen()
```

Determines if the banking interface is open.

Returns:
True if the banking interface is visible. False otherwise.
- #### isDepositBoxOpen

```
public static boolean isDepositBoxOpen()
```

Determines if the deposit box interface is open.

Returns:
True if the deposit box interface is visible. False otherwise.
- #### isNearby

```
public static boolean isNearby()
```

Determines if the player character is in a bank by looking for Bank objects/npcs within 15 tiles.
If this is true, then calling [`open()`](#open()) will generally be successful

Returns:
True if there is a bank object/npc near. False otherwise.
- #### open

```
@Deprecated(forRemoval=true)
public static boolean open()
```

Deprecated, for removal: This API element is subject to removal in a future version.
Finds the best banking object/npc in the 15 tile area and interacts with it to open the banking interface. This will
walk to the bank if it is too far away to click, but will not walk to a bank outside the loaded region. Use
[`isNearby()`](#isNearby()) to determine if this method is appropriate to use.

Returns:
True if the bank interface opens. False otherwise.
- #### ensureOpen

```
public static boolean ensureOpen()
```

Ensures the bank is open. If it is already open, the cache will update and the method will return true.
If not, it'll open the bank as normal.

Returns:
true is the bank is already open, or the bank is opened successfully.
- #### close

```
public static boolean close()
```

Closes the banking interface.

Returns:
True if the bank closes. False otherwise.
- #### withdraw

```
public static boolean withdraw​(int itemId,
int amount)
```

Withdraws the specified amount of an item with the specified id

Parameters:
`itemId` - the item id
`amount` - the amount to withdraw
Returns:
true if withdrawn successfully, false otherwise
- #### withdraw

```
public static boolean withdraw​(java.lang.String itemName,
int amount)
```

Withdraws the specified amount of an item with the specified name

Parameters:
`itemName` - the item name
`amount` - the amount to withdraw
Returns:
true if withdrawn successfully, false otherwise
- #### withdrawAll

```
public static boolean withdrawAll​(int itemId)
```

Withdraws all of an item with the specified id

Parameters:
`itemId` - the item id
Returns:
true if withdrawn successfully, false otherwise
- #### withdrawAll

```
public static boolean withdrawAll​(java.lang.String itemName)
```

Withdraws all of an item with the specified name

Parameters:
`itemName` - the item name
Returns:
true if withdrawn successfully, false otherwise
- #### deposit

```
public static boolean deposit​(int itemId,
int amount)
```

Deposits the specified amount of an item with the specified id

Parameters:
`itemId` - the item id
`amount` - the amount to deposit
Returns:
true if deposited successfully, false otherwise
- #### deposit

```
public static boolean deposit​(java.lang.String itemName,
int amount)
```

Deposits the specified amount of an item with the specified name

Parameters:
`itemName` - the item name
`amount` - the amount to deposit
Returns:
true if deposited successfully, false otherwise
- #### depositAll

```
public static boolean depositAll​(int itemId)
```

Deposits all of an item with the specified id

Parameters:
`itemId` - the item id
Returns:
true if deposited successfully, false otherwise
- #### depositAll

```
public static boolean depositAll​(java.lang.String itemName)
```

Deposits all of an item with the specified name

Parameters:
`itemName` - the item name
Returns:
true if deposited successfully, false otherwise
- #### deposit

```
public static boolean deposit​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item,
int amount)
```

Deposits the specified quantity of the specified item

Parameters:
`item` - the item to deposit
`amount` - the amount to deposit
Returns:
true if deposited successfully, false otherwise
- #### depositAll

```
public static boolean depositAll​([InventoryItem](types/InventoryItem.html "class in org.tribot.script.sdk.types") item)
```

Deposits all of the specified item

Parameters:
`item` - the item to deposit
Returns:
true if deposited successfully, false otherwise
- #### withdraw

```
public static boolean withdraw​([Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces") item,
int amount)
```

Withdraws the specified amount of the specified item

Parameters:
`item` - the item to withdraw
`amount` - the amount to withdraw
Returns:
true if withdrawn successfully, false otherwise
- #### withdrawAll

```
public static boolean withdrawAll​([Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces") item)
```

Withdraws all of the specified item

Parameters:
`item` - the item to withdraw
Returns:
true if withdrawn successfully, false otherwise
- #### depositInventory

```
public static boolean depositInventory()
```

Deposits the entire inventory

Returns:
true if deposited successfully, false otherwise
- #### depositEquipment

```
public static boolean depositEquipment()
```

Deposits all equipment

Returns:
true if deposited successfully, false otherwise