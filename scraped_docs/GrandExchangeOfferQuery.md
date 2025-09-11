# GrandExchangeOfferQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/GrandExchangeOfferQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.GrandExchangeOfferQuery

* All Implemented Interfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<[GrandExchangeOffer](../types/GrandExchangeOffer.html "class in org.tribot.script.sdk.types"),​[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class GrandExchangeOfferQuery
extends java.lang.Object
```

A query to search over entities of type [`GrandExchangeOffer`](../types/GrandExchangeOffer.html "class in org.tribot.script.sdk.types")

See Also:
[`Query.grandExchangeOffers()`](Query.html#grandExchangeOffers())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[GrandExchangeOffer](../types/GrandExchangeOffer.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[isEnabled](#isEnabled())()` | Only match offer slots that are enabled |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemIdEquals](#itemIdEquals(int...))​(int... id)` | Only match offers with the specified item id |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemIdNotEquals](#itemIdNotEquals(int...))​(int... id)` | Only match offers who do not have the specified item id |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemNameContains](#itemNameContains(java.lang.String...))​(java.lang.String... itemName)` | Only matches offers whose item name contains any of the specified names |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemNameEquals](#itemNameEquals(java.lang.String...))​(java.lang.String... itemName)` | Only matches offers whose item name equals any of the specified names |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemNameNotContains](#itemNameNotContains(java.lang.String...))​(java.lang.String... itemName)` | Only matches offers whose item name does not contain any of the specified names |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[itemNameNotEquals](#itemNameNotEquals(java.lang.String...))​(java.lang.String... itemName)` | Only matches offers whose item name does not equal any of the specified names |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxCollectableGoldQuantity](#maxCollectableGoldQuantity(int))​(int max)` | Only match offers whose collectable gold quantity is at most the specified max value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxCollectableItemQuantity](#maxCollectableItemQuantity(int))​(int max)` | Only match offers whose collectable item quantity is at most the specified max value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxPercentComplete](#maxPercentComplete(double))​(double completionPercent)` | Only match offers that have at most the specified completion percent |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxPrice](#maxPrice(int))​(int maxPrice)` | Only match offers whose price is at most the specified max price |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxTotalQuantity](#maxTotalQuantity(int))​(int max)` | Only match offers whose total quantity is at most the specified max total quantity |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxTransferredGoldQuantity](#maxTransferredGoldQuantity(int))​(int max)` | Only match offers whose transferred gold quantity is at most the specified max value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[maxTransferredItemQuantity](#maxTransferredItemQuantity(int))​(int max)` | Only match offers whose transferred item quantity is at most the specified max value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minCollectableGoldQuantity](#minCollectableGoldQuantity(int))​(int min)` | Only match offers whose collectable gold quantity is at least the specified min value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minCollectableItemQuantity](#minCollectableItemQuantity(int))​(int min)` | Only match offers whose collectable item quantity is at least the specified min value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minPercentComplete](#minPercentComplete(double))​(double completionPercent)` | Only match offers that have at least the specified completion percent |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minPrice](#minPrice(int))​(int minPrice)` | Only match offers whose price is at least the specified min price |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minTotalQuantity](#minTotalQuantity(int))​(int min)` | Only match offers whose total quantity is at least the specified min total quantity |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minTransferredGoldQuantity](#minTransferredGoldQuantity(int))​(int min)` | Only match offers whose transferred gold quantity is at least the specified min value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[minTransferredItemQuantity](#minTransferredItemQuantity(int))​(int min)` | Only match offers whose transferred item quantity is at least the specified min value |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[priceEquals](#priceEquals(int...))​(int... price)` | Only match offers whose price equals the specified price |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[priceNotEquals](#priceNotEquals(int...))​(int... price)` | Only match offers whose price does not equal the specified price |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[slotEquals](#slotEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Slot...))​([GrandExchangeOffer.Slot](../types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")... slot)` | Only match offers that are in the specified slots |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[slotNotEquals](#slotNotEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Slot...))​([GrandExchangeOffer.Slot](../types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")... slot)` | Only match offers that are not in the specified slots |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[statusEquals](#statusEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Status...))​([GrandExchangeOffer.Status](../types/GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")... status)` | Only match offers with the specified grand exchange offer status |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[statusNotEquals](#statusNotEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Status...))​([GrandExchangeOffer.Status](../types/GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")... status)` | Only match offers that do not have the specified grand exchange offer status |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[totalQuantityEquals](#totalQuantityEquals(int...))​(int... totalQuantity)` | Only match offers whose total quantity equals the specified max total quantity |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[totalQuantityNotEquals](#totalQuantityNotEquals(int...))​(int... totalQuantity)` | Only match offers whose total quantity does not equal the specified max total quantity |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[typeEquals](#typeEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Type...))​([GrandExchangeOffer.Type](../types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")... type)` | Only match offers with the specified grand exchange offer type |
| `[GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query")` | `[typeNotEquals](#typeNotEquals(org.tribot.script.sdk.types.GrandExchangeOffer.Type...))​([GrandExchangeOffer.Type](../types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")... type)` | Only match offers that do not haev the specified grand exchange offer type |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[GrandExchangeOffer](../types/GrandExchangeOffer.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### itemIdEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemIdEquals​(int... id)
```

Only match offers with the specified item id

Parameters:
`id` - the id to check
Returns:
this query
- #### itemIdNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemIdNotEquals​(int... id)
```

Only match offers who do not have the specified item id

Parameters:
`id` - the id to check
Returns:
this query
- #### itemNameEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemNameEquals​(java.lang.String... itemName)
```

Only matches offers whose item name equals any of the specified names

Parameters:
`itemName` - the itemName to check
Returns:
this query
- #### itemNameContains

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemNameContains​(java.lang.String... itemName)
```

Only matches offers whose item name contains any of the specified names

Parameters:
`itemName` - the itemName to check
Returns:
this query
- #### itemNameNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemNameNotEquals​(java.lang.String... itemName)
```

Only matches offers whose item name does not equal any of the specified names

Parameters:
`itemName` - the itemName to check
Returns:
this query
- #### itemNameNotContains

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") itemNameNotContains​(java.lang.String... itemName)
```

Only matches offers whose item name does not contain any of the specified names

Parameters:
`itemName` - the itemName to check
Returns:
this query
- #### minPrice

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minPrice​(int minPrice)
```

Only match offers whose price is at least the specified min price

Parameters:
`minPrice` - the min price
Returns:
this query
- #### maxPrice

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxPrice​(int maxPrice)
```

Only match offers whose price is at most the specified max price

Parameters:
`maxPrice` - the max price
Returns:
this query
- #### priceEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") priceEquals​(int... price)
```

Only match offers whose price equals the specified price

Parameters:
`price` - the price
Returns:
this query
- #### priceNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") priceNotEquals​(int... price)
```

Only match offers whose price does not equal the specified price

Parameters:
`price` - the price
Returns:
this query
- #### minTotalQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minTotalQuantity​(int min)
```

Only match offers whose total quantity is at least the specified min total quantity

Parameters:
`min` - the min total quantity
Returns:
this query
- #### maxTotalQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxTotalQuantity​(int max)
```

Only match offers whose total quantity is at most the specified max total quantity

Parameters:
`max` - the max total quantity
Returns:
this query
- #### totalQuantityEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") totalQuantityEquals​(int... totalQuantity)
```

Only match offers whose total quantity equals the specified max total quantity

Parameters:
`totalQuantity` - the total quantity
Returns:
this query
- #### totalQuantityNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") totalQuantityNotEquals​(int... totalQuantity)
```

Only match offers whose total quantity does not equal the specified max total quantity

Parameters:
`totalQuantity` - the total quantity
Returns:
this query
- #### minTransferredItemQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minTransferredItemQuantity​(int min)
```

Only match offers whose transferred item quantity is at least the specified min value

Parameters:
`min` - the min transferred item quantity
Returns:
this query
- #### maxTransferredItemQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxTransferredItemQuantity​(int max)
```

Only match offers whose transferred item quantity is at most the specified max value

Parameters:
`max` - the max transferred item quantity
Returns:
this query
- #### minTransferredGoldQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minTransferredGoldQuantity​(int min)
```

Only match offers whose transferred gold quantity is at least the specified min value

Parameters:
`min` - the min transferred gold quantity
Returns:
this query
- #### maxTransferredGoldQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxTransferredGoldQuantity​(int max)
```

Only match offers whose transferred gold quantity is at most the specified max value

Parameters:
`max` - the max transferred gold quantity
Returns:
this query
- #### minCollectableItemQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minCollectableItemQuantity​(int min)
```

Only match offers whose collectable item quantity is at least the specified min value

Parameters:
`min` - the min collectable item quantity
Returns:
this query
- #### maxCollectableItemQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxCollectableItemQuantity​(int max)
```

Only match offers whose collectable item quantity is at most the specified max value

Parameters:
`max` - the max collectable item quantity
Returns:
this query
- #### minCollectableGoldQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minCollectableGoldQuantity​(int min)
```

Only match offers whose collectable gold quantity is at least the specified min value

Parameters:
`min` - the min collectable gold quantity
Returns:
this query
- #### maxCollectableGoldQuantity

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxCollectableGoldQuantity​(int max)
```

Only match offers whose collectable gold quantity is at most the specified max value

Parameters:
`max` - the max collectable gold quantity
Returns:
this query
- #### typeEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") typeEquals​([GrandExchangeOffer.Type](../types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")... type)
```

Only match offers with the specified grand exchange offer type

Parameters:
`type` - the type
Returns:
this query
- #### typeNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") typeNotEquals​([GrandExchangeOffer.Type](../types/GrandExchangeOffer.Type.html "enum in org.tribot.script.sdk.types")... type)
```

Only match offers that do not haev the specified grand exchange offer type

Parameters:
`type` - the type
Returns:
this query
- #### statusEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") statusEquals​([GrandExchangeOffer.Status](../types/GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")... status)
```

Only match offers with the specified grand exchange offer status

Parameters:
`status` - the status
Returns:
this query
- #### statusNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") statusNotEquals​([GrandExchangeOffer.Status](../types/GrandExchangeOffer.Status.html "enum in org.tribot.script.sdk.types")... status)
```

Only match offers that do not have the specified grand exchange offer status

Parameters:
`status` - the status
Returns:
this query
- #### slotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") slotEquals​([GrandExchangeOffer.Slot](../types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")... slot)
```

Only match offers that are in the specified slots

Parameters:
`slot` - the slots
Returns:
this query
- #### slotNotEquals

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") slotNotEquals​([GrandExchangeOffer.Slot](../types/GrandExchangeOffer.Slot.html "enum in org.tribot.script.sdk.types")... slot)
```

Only match offers that are not in the specified slots

Parameters:
`slot` - the slots
Returns:
this query
- #### maxPercentComplete

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") maxPercentComplete​(double completionPercent)
```

Only match offers that have at most the specified completion percent

Parameters:
`completionPercent` - the max completion percent
Returns:
this query
- #### minPercentComplete

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") minPercentComplete​(double completionPercent)
```

Only match offers that have at least the specified completion percent

Parameters:
`completionPercent` - the min completion percent
Returns:
this query
- #### isEnabled

```
public [GrandExchangeOfferQuery](GrandExchangeOfferQuery.html "class in org.tribot.script.sdk.query") isEnabled()
```

Only match offer slots that are enabled

Returns:
this query
- #### filter

```
public QueryType filter​(java.util.function.Predicate<EntityType> filter)
```

Description copied from interface: `[Query](Query.html#filter(java.util.function.Predicate))`
Applies the specified filter to this query.
This query is **not** executed at this point.

Specified by:
`[filter](Query.html#filter(java.util.function.Predicate))` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Parameters:
`filter` - the filter to apply to this query
Returns:
this query
- #### sorted

```
public QueryType sorted​(java.util.Comparator<EntityType> comparator)
```

Description copied from interface: `[Query](Query.html#sorted(java.util.Comparator))`
Orders the query by the specified comparator.
This query is **not** executed at this point.

Specified by:
`[sorted](Query.html#sorted(java.util.Comparator))` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Parameters:
`comparator` - the comparator to order the query by
Returns:
this query
- #### stream

```
public java.util.stream.Stream<EntityType> stream()
```

Description copied from interface: `[Query](Query.html#stream())`
Returns this query as a stream.
This query is **not** executed at this point **but** it will be executed whenever the stream executes a terminal operation.

Specified by:
`[stream](Query.html#stream())` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Returns:
this query as a stream
- #### asQueryType

```
protected final QueryType asQueryType()
```