# GrandExchange (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GrandExchange.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.GrandExchange

* ---

```
public class GrandExchange
extends java.lang.Object
```

Contains utility methods for inspecting and interacting with the grand exchange

See Also:
[`GrandExchangeOffer`](types/GrandExchangeOffer.html "class in org.tribot.script.sdk.types"),
[`Query.grandExchangeOffers()`](query/Query.html#grandExchangeOffers())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GrandExchange.CollectMethod](GrandExchange.CollectMethod.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk")` | Describes a configuration for a new grand exchange offer.
Each of the following config requirements must be met:
A type must be specified.
A price adjustment or a price must be specified.
A quantity must be specified.
An item name or an item id must be specified.

Custom search text (only used for buying) is completely optional. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[GrandExchange](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[abort](#abort(org.tribot.script.sdk.types.GrandExchangeOffer.Slot))​([GrandExchangeOffer.Slot](types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") slot)` | Attempts to abort an offer in the specified slot |
| `static boolean` | `[close](#close())()` | Closes the grand exchange widget by clicking the close button |
| `static boolean` | `[collectAll](#collectAll())()` | Collects all items using the default collect option (the left click option) |
| `static boolean` | `[collectAll](#collectAll(org.tribot.script.sdk.GrandExchange.CollectMethod))​([GrandExchange.CollectMethod](GrandExchange.CollectMethod.html "enum in org.tribot.script.sdk") method)` | Collects all items using the specified collect method |
| `static boolean` | `[isNearby](#isNearby())()` | Checks if we are near the grand exchange by searching for a nearby exchange booth. |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the grand exchange is open |
| `static boolean` | `[open](#open())()` | Attempts to open the grand exchange |
| `static boolean` | `[placeOffer](#placeOffer(org.tribot.script.sdk.GrandExchange.CreateOfferConfig))​([GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk") config)` | Attempts to place a new grand exchange with the specified config. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### GrandExchange

```
public GrandExchange()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Checks if the grand exchange is open

Returns:
true if the grand exchange is open, false otherwise
- #### close

```
public static boolean close()
```

Closes the grand exchange widget by clicking the close button

Returns:
true if the click to close was successful, false otherwise
- #### isNearby

```
public static boolean isNearby()
```

Checks if we are near the grand exchange by searching for a nearby exchange booth.
If this is true, a subsequent call to [`open()`](#open()) will probably be successful.

Returns:
true if we are near the grand exchange, false otherwise
- #### open

```
public static boolean open()
```

Attempts to open the grand exchange

Returns:
true if the grand exchange was opened, false otherwise
- #### abort

```
public static boolean abort​([GrandExchangeOffer.Slot](types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") slot)
```

Attempts to abort an offer in the specified slot

Parameters:
`slot` - the grand exchange offer slot
Returns:
true if the offer was aborted, false otherwise
- #### collectAll

```
public static boolean collectAll()
```

Collects all items using the default collect option (the left click option)

Returns:
true if all items were collected, false otherwise
- #### collectAll

```
public static boolean collectAll​([GrandExchange.CollectMethod](GrandExchange.CollectMethod.html "enum in org.tribot.script.sdk") method)
```

Collects all items using the specified collect method

Parameters:
`method` - the collect method to use
Returns:
true if all items were collected, false otherwise
- #### placeOffer

```
public static boolean placeOffer​([GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk") config)
```

Attempts to place a new grand exchange with the specified config.
If the script is paused or stopped during this, it will return false shortly after.

Parameters:
`config` - the config for the grand exchange offer
Returns:
true if the offer was placed successfully, false otherwise