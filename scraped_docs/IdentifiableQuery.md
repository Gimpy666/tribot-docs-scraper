# IdentifiableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/IdentifiableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GraphicObjectQuery](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface IdentifiableQuery<EntityType extends [Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery")` | `[distinctById](#distinctById())()` | Removes duplicate entities from this query based on the id (keeps the first match, removes the rest) |
| `default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery")` | `[idEquals](#idEquals(int...))​(int... id)` | Only match entities with the specified id |
| `default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery")` | `[idNotEquals](#idNotEquals(int...))​(int... id)` | Only match entities who do not have the specified id |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### idEquals

```
default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery") idEquals​(int... id)
```

Only match entities with the specified id

Parameters:
`id` - the id to check
Returns:
this query
- #### idNotEquals

```
default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery") idNotEquals​(int... id)
```

Only match entities who do not have the specified id

Parameters:
`id` - the id to check
Returns:
this query
- #### distinctById

```
default [QueryType](IdentifiableQuery.html "type parameter in IdentifiableQuery") distinctById()
```

Removes duplicate entities from this query based on the id (keeps the first match, removes the rest)

Returns:
this query