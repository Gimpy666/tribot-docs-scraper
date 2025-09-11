# NamedQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/NamedQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface NamedQuery<EntityType extends [Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[distinctByName](#distinctByName())()` | Removes duplicate entities from this query based on the name (keeps the first match, removes the rest) |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameContains](#nameContains(java.lang.String...))​(java.lang.String... names)` | Only match entities whose name contains any of the specified names, case insensitive |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameEquals](#nameEquals(java.lang.String...))​(java.lang.String... names)` | Only match entities with the specified names, case sensitive |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameNotContains](#nameNotContains(java.lang.String...))​(java.lang.String... names)` | Only match entities whose name does not contains any of the specified names, case insensitive |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameNotEquals](#nameNotEquals(java.lang.String...))​(java.lang.String... names)` | Only match entities whose name does not equal any of the specified names, case sensitive |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameNotStartsWith](#nameNotStartsWith(java.lang.String...))​(java.lang.String... names)` | Only match entities whose name does not start with any of the specified names, case insensitive |
| `default [QueryType](NamedQuery.html "type parameter in NamedQuery")` | `[nameStartsWith](#nameStartsWith(java.lang.String...))​(java.lang.String... names)` | Only match entities whose name starts with any of the specified names, case insensitive |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### nameEquals

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameEquals​(java.lang.String... names)
```

Only match entities with the specified names, case sensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### nameContains

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameContains​(java.lang.String... names)
```

Only match entities whose name contains any of the specified names, case insensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### nameStartsWith

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameStartsWith​(java.lang.String... names)
```

Only match entities whose name starts with any of the specified names, case insensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### nameNotEquals

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameNotEquals​(java.lang.String... names)
```

Only match entities whose name does not equal any of the specified names, case sensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### nameNotContains

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameNotContains​(java.lang.String... names)
```

Only match entities whose name does not contains any of the specified names, case insensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### nameNotStartsWith

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") nameNotStartsWith​(java.lang.String... names)
```

Only match entities whose name does not start with any of the specified names, case insensitive

Parameters:
`names` - the names to check
Returns:
this query
- #### distinctByName

```
default [QueryType](NamedQuery.html "type parameter in NamedQuery") distinctByName()
```

Removes duplicate entities from this query based on the name (keeps the first match, removes the rest)

Returns:
this query