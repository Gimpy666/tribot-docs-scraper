# ActionableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ActionableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` - the entity type
`QueryType` - the query type

All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface ActionableQuery<EntityType extends [Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

A query to search over entities with actions

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](ActionableQuery.html "type parameter in ActionableQuery")` | `[actionContains](#actionContains(java.lang.String...))​(java.lang.String... actions)` | Checks if any of the actions of this entity contains any of the specified actions, case insensitive |
| `default [QueryType](ActionableQuery.html "type parameter in ActionableQuery")` | `[actionEquals](#actionEquals(java.lang.String...))​(java.lang.String... actions)` | Checks if any of the actions of this entity equal any of the specified actions, case sensitive |
| `default [QueryType](ActionableQuery.html "type parameter in ActionableQuery")` | `[actionNotContains](#actionNotContains(java.lang.String...))​(java.lang.String... actions)` | Checks if none of the actions of this entity contains any of the specified actions, case insensitive |
| `default [QueryType](ActionableQuery.html "type parameter in ActionableQuery")` | `[actionNotEquals](#actionNotEquals(java.lang.String...))​(java.lang.String... actions)` | Checks if none of the actions of this entity equal any of the specified actions, case sensitive |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### actionContains

```
default [QueryType](ActionableQuery.html "type parameter in ActionableQuery") actionContains​(java.lang.String... actions)
```

Checks if any of the actions of this entity contains any of the specified actions, case insensitive

Parameters:
`actions` - the actions to check if this entity contains
Returns:
this query
- #### actionEquals

```
default [QueryType](ActionableQuery.html "type parameter in ActionableQuery") actionEquals​(java.lang.String... actions)
```

Checks if any of the actions of this entity equal any of the specified actions, case sensitive

Parameters:
`actions` - the actions to check if this entity equals
Returns:
this query
- #### actionNotContains

```
default [QueryType](ActionableQuery.html "type parameter in ActionableQuery") actionNotContains​(java.lang.String... actions)
```

Checks if none of the actions of this entity contains any of the specified actions, case insensitive

Parameters:
`actions` - the actions to check if this entity does not contain
Returns:
this query
- #### actionNotEquals

```
default [QueryType](ActionableQuery.html "type parameter in ActionableQuery") actionNotEquals​(java.lang.String... actions)
```

Checks if none of the actions of this entity equal any of the specified actions, case sensitive

Parameters:
`actions` - the actions to check if this entity does not equal
Returns:
this query