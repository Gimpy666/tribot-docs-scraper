# ItemDefinableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ItemDefinableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface ItemDefinableQuery<EntityType extends [ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isBankable](#isBankable())()` | Deprecated. |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isGrandExchangeTradeable](#isGrandExchangeTradeable())()` | Only match items that can be traded on the grand exchange |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isMembersOnly](#isMembersOnly())()` | Only match items that are members only |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNotBankable](#isNotBankable())()` | Deprecated. |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNoted](#isNoted())()` | Only match items that are noted |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNotGrandExchangeTradeable](#isNotGrandExchangeTradeable())()` | Only match items that cannot be traded on the grand exchange |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNotMembersOnly](#isNotMembersOnly())()` | Only match items that are not members only |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNotNoted](#isNotNoted())()` | Only match items that are not noted |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isNotStackable](#isNotStackable())()` | Only match items that are not stackable |
| `default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery")` | `[isStackable](#isStackable())()` | Only match items that are stackable |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### isMembersOnly

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isMembersOnly()
```

Only match items that are members only

Returns:
this query
- #### isNotMembersOnly

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNotMembersOnly()
```

Only match items that are not members only

Returns:
this query
- #### isStackable

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isStackable()
```

Only match items that are stackable

Returns:
this query
- #### isNotStackable

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNotStackable()
```

Only match items that are not stackable

Returns:
this query
- #### isNoted

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNoted()
```

Only match items that are noted

Returns:
this query
- #### isNotNoted

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNotNoted()
```

Only match items that are not noted

Returns:
this query
- #### isBankable

```
@Deprecated
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isBankable()
```

Deprecated.
Only match items that are bankable

Returns:
this query
- #### isNotBankable

```
@Deprecated
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNotBankable()
```

Deprecated.
Only match items that are not bankable

Returns:
this query
- #### isGrandExchangeTradeable

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isGrandExchangeTradeable()
```

Only match items that can be traded on the grand exchange

Returns:
this query
- #### isNotGrandExchangeTradeable

```
default [QueryType](ItemDefinableQuery.html "type parameter in ItemDefinableQuery") isNotGrandExchangeTradeable()
```

Only match items that cannot be traded on the grand exchange

Returns:
this query