# MakeScreen (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MakeScreen.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.MakeScreen

* ---

```
public class MakeScreen
extends java.lang.Object
```

Contains methods regarding the commonly used 'make' interface. For example, it appears when cooking or combining items

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[MakeScreen.SelectPreference](MakeScreen.SelectPreference.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[MakeScreen](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[contains](#contains(int...))​(int... id)` | Checks if the make screen contains an item with the specified id |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if the make screen contains an item with the specified name |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Checks if the make screen contains an item that matches the filter |
| `static java.util.Optional<java.lang.Integer>` | `[getCustomQuantity](#getCustomQuantity())()` | Gets the currently selected custom quantity, if a custom quantity is selected |
| `static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk")` | `[getQuantity](#getQuantity())()` | Gets the currently selected quantity in the make screen. |
| `static [MakeScreen.SelectPreference](MakeScreen.SelectPreference.html "enum in org.tribot.script.sdk")` | `[getSelectPreference](#getSelectPreference())()` | Gets the make all item select preference. |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the make screen is open |
| `static boolean` | `[make](#make(int...))​(int... id)` | Attempts to make an item with the specified id |
| `static boolean` | `[make](#make(java.lang.String...))​(java.lang.String... name)` | Attempts to make an item with the specified name |
| `static boolean` | `[make](#make(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Attempts to make an item matching the filter |
| `static boolean` | `[makeAll](#makeAll(int...))​(int... id)` | Utility method to set the quantity to all if not already set, then makes an item with the specified id |
| `static boolean` | `[makeAll](#makeAll(java.lang.String...))​(java.lang.String... name)` | Utility method to set the quantity to all if not already set, then makes an item with the specified name |
| `static boolean` | `[makeAll](#makeAll(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Utility method to set the quantity to all if not already set, then makes an item matching the filter |
| `static boolean` | `[setCustomQuantity](#setCustomQuantity(int))​(int quantity)` | Sets the custom quantity |
| `static boolean` | `[setQuantity](#setQuantity(org.tribot.script.sdk.MakeScreen.Quantity))​([MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") quantity)` | Sets the specified quantity. |
| `static void` | `[setSelectPreference](#setSelectPreference(org.tribot.script.sdk.MakeScreen.SelectPreference))​([MakeScreen.SelectPreference](MakeScreen.SelectPreference.html "enum in org.tribot.script.sdk") pref)` | Sets the make all item select preference. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### MakeScreen

```
public MakeScreen()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Checks if the make screen is open

Returns:
true if the make screen is open, false otherwise
- #### getQuantity

```
public static [MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") getQuantity()
```

Gets the currently selected quantity in the make screen. If the result is [`MakeScreen.Quantity.X`](MakeScreen.Quantity.html#X), use [`getCustomQuantity()`](#getCustomQuantity()) to check the quantity

Returns:
the currently selected quantity in the make screen
- #### getCustomQuantity

```
public static java.util.Optional<java.lang.Integer> getCustomQuantity()
```

Gets the currently selected custom quantity, if a custom quantity is selected

Returns:
the currently selected custom quantity
- #### setQuantity

```
public static boolean setQuantity​([MakeScreen.Quantity](MakeScreen.Quantity.html "enum in org.tribot.script.sdk") quantity)
```

Sets the specified quantity. This does not accept [`MakeScreen.Quantity.X`](MakeScreen.Quantity.html#X), use [`setCustomQuantity(int)`](#setCustomQuantity(int)) instead

Parameters:
`quantity` - the quantity to set, not X
Returns:
true if set successfully, false otherwise
- #### setCustomQuantity

```
public static boolean setCustomQuantity​(int quantity)
```

Sets the custom quantity

Parameters:
`quantity` - the custom quantity to set, at least 1
Returns:
true if set successfully, false otherwise
- #### contains

```
public static boolean contains​(int... id)
```

Checks if the make screen contains an item with the specified id

Parameters:
`id` - the item id
Returns:
true if the make screen contains an item with the specified id, false otherwise
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if the make screen contains an item with the specified name

Parameters:
`name` - the item name
Returns:
true if the make screen contains an item with the specified name, false otherwise
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Checks if the make screen contains an item that matches the filter

Parameters:
`filter` - the filter to check the items with
Returns:
true if the make screen contains an item that matches the filter, false otherwise
- #### make

```
public static boolean make​(int... id)
```

Attempts to make an item with the specified id

Parameters:
`id` - the item id
Returns:
true if the item was selected successfully, false otherwise
- #### make

```
public static boolean make​(java.lang.String... name)
```

Attempts to make an item with the specified name

Parameters:
`name` - the item name
Returns:
true if the item was selected successfully, false otherwise
- #### make

```
public static boolean make​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Attempts to make an item matching the filter

Parameters:
`filter` - the item filter
Returns:
true if the item was selected successfully, false otherwise
- #### makeAll

```
public static boolean makeAll​(int... id)
```

Utility method to set the quantity to all if not already set, then makes an item with the specified id

Parameters:
`id` - the item id
Returns:
true if quantity was set to all successfully, and selected the item successfully, false otherwise
- #### makeAll

```
public static boolean makeAll​(java.lang.String... name)
```

Utility method to set the quantity to all if not already set, then makes an item with the specified name

Parameters:
`name` - the item name
Returns:
true if quantity was set to all successfully, and selected the item successfully, false otherwise
- #### makeAll

```
public static boolean makeAll​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Utility method to set the quantity to all if not already set, then makes an item matching the filter

Parameters:
`filter` - the item filter
Returns:
true if quantity was set to all successfully, and selected the item successfully, false otherwise
- #### getSelectPreference

```
public static [MakeScreen.SelectPreference](MakeScreen.SelectPreference.html "enum in org.tribot.script.sdk") getSelectPreference()
```

Gets the make all item select preference. By default, [`MakeScreen.SelectPreference.KEYS`](MakeScreen.SelectPreference.html#KEYS) is used

Returns:
the make all item select preference
- #### setSelectPreference

```
public static void setSelectPreference​([MakeScreen.SelectPreference](MakeScreen.SelectPreference.html "enum in org.tribot.script.sdk") pref)
```

Sets the make all item select preference. By default, [`MakeScreen.SelectPreference.KEYS`](MakeScreen.SelectPreference.html#KEYS) is used

Parameters:
`pref` - the select preference