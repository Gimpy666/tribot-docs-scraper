# StackableItemDefinableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/StackableItemDefinableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` -
`QueryType` -

All Superinterfaces:
`[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface StackableItemDefinableQuery<EntityType extends [ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces") & [Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

A query to search over [`Stackable`](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces") entities that are [`ItemDefinable`](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")

This type serves as a bridge between ground items/interface items

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery")` | `[maxPrice](#maxPrice(int))​(int max)` | Only match items that have at most the specified price. |
| `default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery")` | `[maxStackPrice](#maxStackPrice(int))​(int max)` | Only match items that have at most the specified stack price (stack price = price \* item stack). |
| `default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery")` | `[minPrice](#minPrice(int))​(int min)` | Only match items that have at least the specified price. |
| `default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery")` | `[minStackPrice](#minStackPrice(int))​(int min)` | Only match items that have at least the stack price (stack price = price \* item stack). |

- ### Methods inherited from interface org.tribot.script.sdk.query.[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")

`[isBankable](ItemDefinableQuery.html#isBankable()), [isGrandExchangeTradeable](ItemDefinableQuery.html#isGrandExchangeTradeable()), [isMembersOnly](ItemDefinableQuery.html#isMembersOnly()), [isNotBankable](ItemDefinableQuery.html#isNotBankable()), [isNoted](ItemDefinableQuery.html#isNoted()), [isNotGrandExchangeTradeable](ItemDefinableQuery.html#isNotGrandExchangeTradeable()), [isNotMembersOnly](ItemDefinableQuery.html#isNotMembersOnly()), [isNotNoted](ItemDefinableQuery.html#isNotNoted()), [isNotStackable](ItemDefinableQuery.html#isNotStackable()), [isStackable](ItemDefinableQuery.html#isStackable())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")

`[maxStack](StackableQuery.html#maxStack(int)), [minStack](StackableQuery.html#minStack(int)), [stackEquals](StackableQuery.html#stackEquals(int...)), [stackNotEquals](StackableQuery.html#stackNotEquals(int...)), [stackWithin](StackableQuery.html#stackWithin(int,int)), [sumStacks](StackableQuery.html#sumStacks())`

* + ### Method Detail

- #### minPrice

```
default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery") minPrice​(int min)
```

Only match items that have at least the specified price.

Parameters:
`min` - the min price
Returns:
this query
- #### maxPrice

```
default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery") maxPrice​(int max)
```

Only match items that have at most the specified price.

Parameters:
`max` - the max price
Returns:
this query
- #### minStackPrice

```
default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery") minStackPrice​(int min)
```

Only match items that have at least the stack price (stack price = price \* item stack).

Parameters:
`min` - the min price
Returns:
this query
- #### maxStackPrice

```
default [QueryType](StackableItemDefinableQuery.html "type parameter in StackableItemDefinableQuery") maxStackPrice​(int max)
```

Only match items that have at most the specified stack price (stack price = price \* item stack).

Parameters:
`max` - the max price
Returns:
this query