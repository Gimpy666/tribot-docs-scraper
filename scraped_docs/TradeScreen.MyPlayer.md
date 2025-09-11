# TradeScreen.MyPlayer (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/TradeScreen.MyPlayer.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.TradeScreen.MyPlayer

* Enclosing class:
[TradeScreen](TradeScreen.html "class in org.tribot.script.sdk")

---

```
public static class TradeScreen.MyPlayer
extends java.lang.Object
```

My player's trade screen information

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[MyPlayer](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[contains](#contains(int...))​(int... id)` | Checks if any of my offered trade items exists with any of the specified ids

param id the item ids |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if any of my offered trade items exists with any of the specified names

param name the item names |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Checks if any of my offered trade items exists matching the specified filter

param filter the item filter |
| `static int` | `[getCount](#getCount(int...))​(int... id)` | Sums the item stacks of all my offered trade items with the specified item ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Sums the item stacks of my offered trade items with the specified item names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Sums the item stacks of my offered trade items matching the specified filter |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getOffers](#getOffers())()` | Gets the offered items by the player character. |
| `static boolean` | `[hasAccepted](#hasAccepted())()` | Determines if the player character has accepted the offer. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### MyPlayer

```
public MyPlayer()
```

+ ### Method Detail

- #### hasAccepted

```
public static boolean hasAccepted()
```

Determines if the player character has accepted the offer. Works on both screens.

Returns:
True if the player character has accepted. False otherwise.
- #### getOffers

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getOffers()
```

Gets the offered items by the player character.

Returns:
A list of items the player character is offering.
- #### getCount

```
public static int getCount​(int... id)
```

Sums the item stacks of all my offered trade items with the specified item ids

Parameters:
`id` - the item ids
Returns:
the sum of item stacks of my offered trade items with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Sums the item stacks of my offered trade items with the specified item names

Parameters:
`name` - the item names
Returns:
the sum of item stacks of my offered trade items with the specified names
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Sums the item stacks of my offered trade items matching the specified filter

Parameters:
`filter` - the item filter
Returns:
the sum of item stacks of my offered trade items matching the specified filter
- #### contains

```
public static boolean contains​(int... id)
```

Checks if any of my offered trade items exists with any of the specified ids

param id the item ids

Returns:
true if any of my offered trade items exists with any of the specified ids, false otherwise
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if any of my offered trade items exists with any of the specified names

param name the item names

Returns:
true if any of my offered trade items exists with any of the specified names, false otherwise
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Checks if any of my offered trade items exists matching the specified filter

param filter the item filter

Returns:
true if any of my offered trade items exists matching the specified filter, false otherwise