# IndexableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/IndexableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface IndexableQuery<EntityType extends [Indexable](../interfaces/Indexable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](IndexableQuery.html "type parameter in IndexableQuery")` | `[indexEquals](#indexEquals(int...))​(int... index)` | Only match entities with the specified index |
| `default [QueryType](IndexableQuery.html "type parameter in IndexableQuery")` | `[indexNotEquals](#indexNotEquals(int...))​(int... index)` | Only match entities who do not have the specified index |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### indexEquals

```
default [QueryType](IndexableQuery.html "type parameter in IndexableQuery") indexEquals​(int... index)
```

Only match entities with the specified index

Parameters:
`index` - the index to check
Returns:
this query
- #### indexNotEquals

```
default [QueryType](IndexableQuery.html "type parameter in IndexableQuery") indexNotEquals​(int... index)
```

Only match entities who do not have the specified index

Parameters:
`index` - the index to check
Returns:
this query