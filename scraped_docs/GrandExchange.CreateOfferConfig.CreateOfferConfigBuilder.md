# GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder

* Enclosing class:
[GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk")

---

```
public static class GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk")` | `[build](#build())()` | |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[interruptCondition](#interruptCondition(java.util.function.BooleanSupplier))​(java.util.function.BooleanSupplier interruptCondition)` | Function to break out of placing an offer. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[itemId](#itemId(int))​(int itemId)` | Either this or itemName is required. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[itemName](#itemName(java.lang.String))​(java.lang.String itemName)` | Either this or itemId is required. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[price](#price(int))​(int price)` | Either this or priceAdjustment is required

The price to place the offer at |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[priceAdjustment](#priceAdjustment(int))​(int priceAdjustment)` | Either this or price is required. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[quantity](#quantity(int))​(int quantity)` | The quantity to place the offer for. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[searchText](#searchText(java.lang.String))​(java.lang.String searchText)` | The search text to use when selecting the item to buy. |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[slot](#slot(org.tribot.script.sdk.types.GrandExchangeOffer.Slot))​([GrandExchangeOffer.Slot](types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") slot)` | The slot to place the offer in. |
| `java.lang.String` | `[toString](#toString())()` | |
| `[GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk")` | `[type](#type(org.tribot.script.sdk.types.GrandExchangeOffer.Type))​([GrandExchangeOffer.Type](types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types") type)` | The type of the grand exchange offer to place. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### type

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") type​([GrandExchangeOffer.Type](types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types") type)
```

The type of the grand exchange offer to place. Defaults to a buy offer.

Returns:
`this`.
- #### slot

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") slot​([GrandExchangeOffer.Slot](types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types") slot)
```

The slot to place the offer in. Optional.

Returns:
`this`.
- #### priceAdjustment

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") priceAdjustment​(int priceAdjustment)
```

Either this or price is required. However, this defaults to guide price.

A price adjustment is adding/subtracting 5%.
Specify a positive number for adding, and a negative number for subtractive.
The magnitude of the number is the amount of times to add/subtract 5%.
For example, a price adjustment of 10% would be 2. A price adjustment of -15% would be -3.

Returns:
`this`.
- #### price

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") price​(int price)
```

Either this or priceAdjustment is required

The price to place the offer at

Returns:
`this`.
- #### quantity

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") quantity​(int quantity)
```

The quantity to place the offer for. Defaults to 1.

Returns:
`this`.
- #### itemName

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") itemName​(java.lang.String itemName)
```

Either this or itemId is required.

The item name of the item to place the offer for.

Returns:
`this`.
- #### itemId

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") itemId​(int itemId)
```

Either this or itemName is required.

The item id to place the offer for.

Returns:
`this`.
- #### searchText

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") searchText​(java.lang.String searchText)
```

The search text to use when selecting the item to buy. Optional.

Returns:
`this`.
- #### interruptCondition

```
public [GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder](GrandExchange.CreateOfferConfig.CreateOfferConfigBuilder.html "class in org.tribot.script.sdk") interruptCondition​(java.util.function.BooleanSupplier interruptCondition)
```

Function to break out of placing an offer. If this is true when checked, placing an offer will return false asap.

Returns:
`this`.
- #### build

```
public [GrandExchange.CreateOfferConfig](GrandExchange.CreateOfferConfig.html "class in org.tribot.script.sdk") build()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`