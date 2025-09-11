# TradeQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/TradeQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.TradeQuery

* All Implemented Interfaces:
`[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`, `[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class TradeQuery
extends java.lang.Object
implements [ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")>
```

A query for searching over items in the trade screen.

The items to search over can be controlled with [`includeMyItems()`](#includeMyItems()) and [`includeOtherPlayerItems()`](#includeOtherPlayerItems())

See Also:
[`Query.trade()`](Query.html#trade())

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[TradeQuery](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")` | `[includeMyItems](#includeMyItems())()` | Includes my player's items in the trade query. |
| `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")` | `[includeOtherPlayerItems](#includeOtherPlayerItems())()` | Includes the other player's items in the trade query. |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")

`[actionContains](ActionableQuery.html#actionContains(java.lang.String...)), [actionEquals](ActionableQuery.html#actionEquals(java.lang.String...)), [actionNotContains](ActionableQuery.html#actionNotContains(java.lang.String...)), [actionNotEquals](ActionableQuery.html#actionNotEquals(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")

`[distinctById](IdentifiableQuery.html#distinctById()), [idEquals](IdentifiableQuery.html#idEquals(int...)), [idNotEquals](IdentifiableQuery.html#idNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")

`[indexEquals](IndexableQuery.html#indexEquals(int...)), [indexNotEquals](IndexableQuery.html#indexNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")

`[isBankable](ItemDefinableQuery.html#isBankable()), [isGrandExchangeTradeable](ItemDefinableQuery.html#isGrandExchangeTradeable()), [isMembersOnly](ItemDefinableQuery.html#isMembersOnly()), [isNotBankable](ItemDefinableQuery.html#isNotBankable()), [isNoted](ItemDefinableQuery.html#isNoted()), [isNotGrandExchangeTradeable](ItemDefinableQuery.html#isNotGrandExchangeTradeable()), [isNotMembersOnly](ItemDefinableQuery.html#isNotMembersOnly()), [isNotNoted](ItemDefinableQuery.html#isNotNoted()), [isNotStackable](ItemDefinableQuery.html#isNotStackable()), [isStackable](ItemDefinableQuery.html#isStackable())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")

`[findClosestToMouse](ItemQuery.html#findClosestToMouse()), [sortedByDistanceToMouse](ItemQuery.html#sortedByDistanceToMouse())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")

`[distinctByName](NamedQuery.html#distinctByName()), [nameContains](NamedQuery.html#nameContains(java.lang.String...)), [nameEquals](NamedQuery.html#nameEquals(java.lang.String...)), [nameNotContains](NamedQuery.html#nameNotContains(java.lang.String...)), [nameNotEquals](NamedQuery.html#nameNotEquals(java.lang.String...)), [nameNotStartsWith](NamedQuery.html#nameNotStartsWith(java.lang.String...)), [nameStartsWith](NamedQuery.html#nameStartsWith(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")

`[maxPrice](StackableItemDefinableQuery.html#maxPrice(int)), [maxStackPrice](StackableItemDefinableQuery.html#maxStackPrice(int)), [minPrice](StackableItemDefinableQuery.html#minPrice(int)), [minStackPrice](StackableItemDefinableQuery.html#minStackPrice(int))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")

`[maxStack](StackableQuery.html#maxStack(int)), [minStack](StackableQuery.html#minStack(int)), [stackEquals](StackableQuery.html#stackEquals(int...)), [stackNotEquals](StackableQuery.html#stackNotEquals(int...)), [stackWithin](StackableQuery.html#stackWithin(int,int)), [sumStacks](StackableQuery.html#sumStacks())`

* + ### Constructor Detail

- #### TradeQuery

```
public TradeQuery()
```

+ ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces")> createSourceStream()
```
- #### includeMyItems

```
public [TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query") includeMyItems()
```

Includes my player's items in the trade query.

Note that if both [`includeMyItems()`](#includeMyItems()) and [`includeOtherPlayerItems()`](#includeOtherPlayerItems()) are not called on a [`TradeQuery`](TradeQuery.html "class in org.tribot.script.sdk.query"),
it will default to searching over my items only.

Returns:
this query
- #### includeOtherPlayerItems

```
public [TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query") includeOtherPlayerItems()
```

Includes the other player's items in the trade query.

Note that if both [`includeMyItems()`](#includeMyItems()) and [`includeOtherPlayerItems()`](#includeOtherPlayerItems()) are not called on a [`TradeQuery`](TradeQuery.html "class in org.tribot.script.sdk.query"),
it will default to searching over my items only.

Calling [`includeOtherPlayerItems()`](#includeOtherPlayerItems()) without calling [`includeMyItems()`](#includeMyItems()) will only search over the other player's items.

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