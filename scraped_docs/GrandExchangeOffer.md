# GrandExchangeOffer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GrandExchangeOffer.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface GrandExchangeOffer
```

Represents an offer in a grand exchange slot.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getItemId](#getItemId())()` | Gets the ID of the item being bought or sold. |
| `int` | `[getPrice](#getPrice())()` | Gets the offer or sell price per item. |
| `int` | `[getQuantitySold](#getQuantitySold())()` | Gets the quantity of bought or sold items. |
| `int` | `[getSpent](#getSpent())()` | Gets the total amount of money spent so far. |
| `[GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api")` | `[getState](#getState())()` | Gets the current state of the offer. |
| `int` | `[getTotalQuantity](#getTotalQuantity())()` | Gets the total quantity being bought or sold. |

* + ### Method Detail

- #### getQuantitySold

```
int getQuantitySold()
```

Gets the quantity of bought or sold items.

Returns:
the quantity bought or sold
- #### getItemId

```
int getItemId()
```

Gets the ID of the item being bought or sold.

Returns:
item ID
See Also:
`ItemID`
- #### getTotalQuantity

```
int getTotalQuantity()
```

Gets the total quantity being bought or sold.

Returns:
the total quantity
- #### getPrice

```
int getPrice()
```

Gets the offer or sell price per item.

Returns:
the offer price
- #### getSpent

```
int getSpent()
```

Gets the total amount of money spent so far.

Returns:
the amount spent
- #### getState

```
[GrandExchangeOfferState](GrandExchangeOfferState.html "enum in net.runelite.api") getState()
```

Gets the current state of the offer.

Returns:
the offers state