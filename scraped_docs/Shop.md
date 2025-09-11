# Shop (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Shop.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Shop

* ---

```
public class Shop
extends java.lang.Object
```

Contains methods for interacting with and inspecting the common shop interface. An example is a general store.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk")` | Represents a quantity that can be bought/sold at a shop |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Shop](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[buy](#buy(org.tribot.script.sdk.Shop.Quantity,int...))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
int... id)` | Attempts to buy the specified quantity of the first item whose id matches the specified id |
| `static boolean` | `[buy](#buy(org.tribot.script.sdk.Shop.Quantity,java.lang.String...))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.lang.String... name)` | Attempts to buy the specified quantity of the first item whose name equals one of the specified names |
| `static boolean` | `[buy](#buy(org.tribot.script.sdk.Shop.Quantity,java.util.function.Predicate))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Attempts to buy the specified quantity of the first item which matches the specified predicate |
| `static boolean` | `[close](#close())()` | Closes the shop screen by clicking the Close button |
| `static boolean` | `[contains](#contains(int...))​(int... id)` | Checks if the shop has any item with any of the specified ids |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if the shop has any item whose name contains any of the specified names |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Checks if the shop has any item that matches the specified filter |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getAll](#getAll())()` | Gets all the items listed in the shop |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getAll](#getAll(int...))​(int... id)` | Gets all the items listed in the shop with the specified ids |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getAll](#getAll(java.lang.String...))​(java.lang.String... name)` | Gets all the items listed in the shop that have exactly the specified names |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getAll](#getAll(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Gets all the items listed in the shop that match the specified predicate |
| `static int` | `[getCount](#getCount(int...))​(int... id)` | Gets the total stack sum of all items with the specified ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Gets the total stack sum of all items whose name contains any of the specified names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Gets the total stack sum of all items matching the specified filter |
| `static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getFirst](#getFirst(int...))​(int... id)` | Gets the first item listed in the shop that has any of the specified ids |
| `static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getFirst](#getFirst(java.lang.String...))​(java.lang.String... name)` | Gets the first item listed in the shop that has exactly any of the specified names |
| `static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getFirst](#getFirst(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Gets the first item listed in the shop that matches the specified predicate |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the shop screen is open |
| `static boolean` | `[sell](#sell(org.tribot.script.sdk.Shop.Quantity,int...))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
int... id)` | Attempts to sell the specified quantity of the first item whose id matches the specified id |
| `static boolean` | `[sell](#sell(org.tribot.script.sdk.Shop.Quantity,java.lang.String...))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.lang.String... name)` | Attempts to sell the specified quantity of the first item whose name equals one of the specified names |
| `static boolean` | `[sell](#sell(org.tribot.script.sdk.Shop.Quantity,java.util.function.Predicate))​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Attempts to sell the specified quantity of the first item which matches the specified predicate |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Shop

```
public Shop()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Checks if the shop screen is open

Returns:
true if the shop screen is open, false otherwise
- #### close

```
public static boolean close()
```

Closes the shop screen by clicking the Close button

Returns:
true if the click to close the shop screen was successful, false otherwise
- #### getAll

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getAll()
```

Gets all the items listed in the shop

Returns:
all the items listed in the shop
- #### getAll

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getAll​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Gets all the items listed in the shop that match the specified predicate

Parameters:
`filter` - the filter to use to get all items
Returns:
all the items listed in the shop that match the specified predicate
- #### getAll

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getAll​(java.lang.String... name)
```

Gets all the items listed in the shop that have exactly the specified names

Parameters:
`name` - the item names
Returns:
all the items listed in the shop with the specified item names
- #### getAll

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getAll​(int... id)
```

Gets all the items listed in the shop with the specified ids

Parameters:
`id` - the item ids
Returns:
all the items listed in the shop with the specified item ids
- #### getFirst

```
public static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getFirst​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Gets the first item listed in the shop that matches the specified predicate

Parameters:
`filter` - the filter to find an item in the shop
Returns:
the first item in the shop that matches the specified predicate, or an empty optional if no item was found
- #### getFirst

```
public static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getFirst​(java.lang.String... name)
```

Gets the first item listed in the shop that has exactly any of the specified names

Parameters:
`name` - the item names to find an item in the shop
Returns:
the first item in the shop that has exactly any of the specified names, or an empty optional if no item was found
- #### getFirst

```
public static java.util.Optional<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getFirst​(int... id)
```

Gets the first item listed in the shop that has any of the specified ids

Parameters:
`id` - the item ids to find an item in the shop
Returns:
the first item in the shop that has any of the specified ids, or an empty optional if no item was found
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Checks if the shop has any item that matches the specified filter

Parameters:
`filter` - the filter to check if any item exists
Returns:
true if any item in the shop matches the specified filter, false otherwise
- #### contains

```
public static boolean contains​(int... id)
```

Checks if the shop has any item with any of the specified ids

Parameters:
`id` - the item ids
Returns:
true if any item in the shop has any of the specified ids, false otherwise
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if the shop has any item whose name contains any of the specified names

Parameters:
`name` - the item name
Returns:
true if any item in the shop contains any of the specified names, false otherwise
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Gets the total stack sum of all items matching the specified filter

Parameters:
`filter` - the item filter to use
Returns:
the total stack sum of all items matching the specified filter
- #### getCount

```
public static int getCount​(int... id)
```

Gets the total stack sum of all items with the specified ids

Parameters:
`id` - the item ids
Returns:
the total stack sum of all items with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Gets the total stack sum of all items whose name contains any of the specified names

Parameters:
`name` - the item names
Returns:
the total stack sum of all items whose name contains any of the specified names
- #### buy

```
public static boolean buy​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
int... id)
```

Attempts to buy the specified quantity of the first item whose id matches the specified id

Parameters:
`quantity` - the quantity to buy
`id` - the item id to buy
Returns:
true if the click to buy the item was successful, false otherwise
- #### buy

```
public static boolean buy​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.lang.String... name)
```

Attempts to buy the specified quantity of the first item whose name equals one of the specified names

Parameters:
`quantity` - the quantity to buy
`name` - the item name to buy
Returns:
true if the click to buy the item was successful, false otherwise
- #### buy

```
public static boolean buy​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Attempts to buy the specified quantity of the first item which matches the specified predicate

Parameters:
`quantity` - the quantity to buy
`filter` - the item filter
Returns:
true if the click to buy the item was successful, false otherwise
- #### sell

```
public static boolean sell​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
int... id)
```

Attempts to sell the specified quantity of the first item whose id matches the specified id

Parameters:
`quantity` - the quantity to sell
`id` - the item id
Returns:
true if the click to sell the item was successful, false otherwise
- #### sell

```
public static boolean sell​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.lang.String... name)
```

Attempts to sell the specified quantity of the first item whose name equals one of the specified names

Parameters:
`quantity` - the quantity to sell
`name` - the item name
Returns:
true if the click to sell the item was successful, false otherwise
- #### sell

```
public static boolean sell​([Shop.Quantity](Shop.Quantity.html "enum in org.tribot.script.sdk") quantity,
java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Attempts to sell the specified quantity of the first item which matches the specified predicate

Parameters:
`quantity` - the quantity to sell
`filter` - the item filter
Returns:
true if the click to sell the item was successful, false otherwise