# TradeScreen.OtherPlayer (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/TradeScreen.OtherPlayer.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.TradeScreen.OtherPlayer

* Enclosing class:
[TradeScreen](TradeScreen.html "class in org.tribot.script.sdk")

---

```
public static class TradeScreen.OtherPlayer
extends java.lang.Object
```

The other player's trade screen information

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[OtherPlayer](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[contains](#contains(int...))​(int... id)` | Checks if any of the other player's offered items exists with any of the specified ids

param id the item ids |
| `static boolean` | `[contains](#contains(java.lang.String...))​(java.lang.String... name)` | Checks if any of the other player's offered items exists with any of the specified names

param name the item names |
| `static boolean` | `[contains](#contains(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Checks if any of the other player's offered items exists matching the specified filter

param filter the item filter |
| `static int` | `[getCount](#getCount(int...))​(int... id)` | Sums the item stacks of the other player's offered items with the specified item ids |
| `static int` | `[getCount](#getCount(java.lang.String...))​(java.lang.String... name)` | Sums the item stacks of the other player's offered items with the specified item names |
| `static int` | `[getCount](#getCount(java.util.function.Predicate))​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)` | Sums the item stacks of the other player's offered items matching the specified filter |
| `static java.util.Optional<java.lang.String>` | `[getName](#getName())()` | Gets the name of the other player. |
| `static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[getOffers](#getOffers())()` | Gets the offered items by the other player. |
| `static boolean` | `[hasAccepted](#hasAccepted())()` | Determines if the other player has accepted the offer. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### OtherPlayer

```
public OtherPlayer()
```

+ ### Method Detail

- #### getName

```
public static java.util.Optional<java.lang.String> getName()
```

Gets the name of the other player.

Returns:
Name of the other player. Empty if not trading.
- #### hasAccepted

```
public static boolean hasAccepted()
```

Determines if the other player has accepted the offer. Works on both screens.

Returns:
True if the other player has accepted. False otherwise.
- #### getOffers

```
public static java.util.List<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> getOffers()
```

Gets the offered items by the other player.

Returns:
A list of items the other player is offering.
- #### getCount

```
public static int getCount​(int... id)
```

Sums the item stacks of the other player's offered items with the specified item ids

Parameters:
`id` - the item ids
Returns:
the sum of item stacks of the other player's offered items with the specified ids
- #### getCount

```
public static int getCount​(java.lang.String... name)
```

Sums the item stacks of the other player's offered items with the specified item names

Parameters:
`name` - the item names
Returns:
the sum of item stacks of the other player's offered items with the specified names
- #### getCount

```
public static int getCount​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Sums the item stacks of the other player's offered items matching the specified filter

Parameters:
`filter` - the item filter
Returns:
the sum of item stacks of the other player's offered items matching the specified filter
- #### contains

```
public static boolean contains​(int... id)
```

Checks if any of the other player's offered items exists with any of the specified ids

param id the item ids

Returns:
true if any of the other player's offered items exists with any of the specified ids, false otherwise
- #### contains

```
public static boolean contains​(java.lang.String... name)
```

Checks if any of the other player's offered items exists with any of the specified names

param name the item names

Returns:
true if any of the other player's offered items exists with any of the specified names, false otherwise
- #### contains

```
public static boolean contains​(java.util.function.Predicate<[Item](interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> filter)
```

Checks if any of the other player's offered items exists matching the specified filter

param filter the item filter

Returns:
true if any of the other player's offered items exists matching the specified filter, false otherwise