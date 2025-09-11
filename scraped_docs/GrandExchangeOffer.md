# GrandExchangeOffer (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/GrandExchangeOffer.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.GrandExchangeOffer

* ---

```
public class GrandExchangeOffer
extends java.lang.Object
```

A grand exchange offer active in the grand exchange

See Also:
[`Query.grandExchangeOffers()`](../query/Query.html#grandExchangeOffers())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")` | The grand exchange offer slots, starting from the top left to the top right, then the bottom left to the bottom right |
| `static class` | `[GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")` | |
| `static class` | `[GrandExchangeOffer.Type](GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `int` | `[getCollectableGoldQuantity](#getCollectableGoldQuantity())()` | Gets the quantity of gold that is currently collectable in this offer. |
| `int` | `[getCollectableItemQuantity](#getCollectableItemQuantity())()` | Gets the quantity of items that are currently collectable in this offer. |
| `int` | `[getItemId](#getItemId())()` | Gets the item id of this offer |
| `java.lang.String` | `[getItemName](#getItemName())()` | Gets the name of the item in this offer |
| `double` | `[getPercentComplete](#getPercentComplete())()` | Gets the current completion percent on this offer. |
| `int` | `[getPrice](#getPrice())()` | Gets the price of this offer |
| `[GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")` | `[getSlot](#getSlot())()` | Gets the [`GrandExchangeOffer.Slot`](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") of this offer |
| `[GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")` | `[getStatus](#getStatus())()` | Gets the [`GrandExchangeOffer.Status`](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") of this offer |
| `int` | `[getTotalQuantity](#getTotalQuantity())()` | Gets the total quantity of this offer (the quantity that was set when the offer was placed) |
| `int` | `[getTransferredGoldQuantity](#getTransferredGoldQuantity())()` | Gets the amount of gold that has already been transferred (or completed) in this offer so far |
| `int` | `[getTransferredItemQuantity](#getTransferredItemQuantity())()` | Gets the amount of items that have already been transferred (or completed) in this offer so far |
| `[GrandExchangeOffer.Type](GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")` | `[getType](#getType())()` | Gets the [`GrandExchangeOffer.Type`](GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types") of this offer |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### getItemName

```
public java.lang.String getItemName()
```

Gets the name of the item in this offer

Returns:
the name of the item
- #### getItemId

```
public int getItemId()
```

Gets the item id of this offer

Returns:
the id of the item
- #### getPrice

```
public int getPrice()
```

Gets the price of this offer

Returns:
the price of this offer
- #### getTotalQuantity

```
public int getTotalQuantity()
```

Gets the total quantity of this offer (the quantity that was set when the offer was placed)

Returns:
the total quantity of this offer
- #### getTransferredItemQuantity

```
public int getTransferredItemQuantity()
```

Gets the amount of items that have already been transferred (or completed) in this offer so far

Returns:
the transferred item quantity
- #### getTransferredGoldQuantity

```
public int getTransferredGoldQuantity()
```

Gets the amount of gold that has already been transferred (or completed) in this offer so far

Returns:
the transferred gold quantity
- #### getCollectableItemQuantity

```
public int getCollectableItemQuantity()
```

Gets the quantity of items that are currently collectable in this offer.

Due to how the game client functions, this information is only available when the grand exchange is open (and a few other situations such as the bank being open)

Returns:
the collectable item quantity
- #### getCollectableGoldQuantity

```
public int getCollectableGoldQuantity()
```

Gets the quantity of gold that is currently collectable in this offer.

Due to how the game client functions, this information is only available when the grand exchange is open (and a few other situations such as the bank being open)

Returns:
the collectable gold quantity
- #### getType

```
public [GrandExchangeOffer.Type](GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types") getType()
```

Gets the [`GrandExchangeOffer.Type`](GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types") of this offer

Returns:
the type of this offer
- #### getStatus

```
public [GrandExchangeOffer.Status](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") getStatus()
```

Gets the [`GrandExchangeOffer.Status`](GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types") of this offer

Returns:
the status of this offer
- #### getSlot

```
public [GrandExchangeOffer.Slot](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") getSlot()
```

Gets the [`GrandExchangeOffer.Slot`](GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") of this offer

Returns:
the slot of this offer
- #### getPercentComplete

```
public double getPercentComplete()
```

Gets the current completion percent on this offer. 0 is nothing transferred, 100 is complete

Returns:
the completion percent on this offer (0-100)
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`