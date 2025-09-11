# StackableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/StackableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` - the entity type
`QueryType` - the query type

All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface StackableQuery<EntityType extends [Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

A query to search over [`Stackable`](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces") entities

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](StackableQuery.html "type parameter in StackableQuery")` | `[maxStack](#maxStack(int))​(int maxStack)` | Only match entities with at most the specified stack size |
| `default [QueryType](StackableQuery.html "type parameter in StackableQuery")` | `[minStack](#minStack(int))​(int minStack)` | Only match entities with at least the specified stack size |
| `default [QueryType](StackableQuery.html "type parameter in StackableQuery")` | `[stackEquals](#stackEquals(int...))​(int... stack)` | Only match entities who have the specified stack |
| `default [QueryType](StackableQuery.html "type parameter in StackableQuery")` | `[stackNotEquals](#stackNotEquals(int...))​(int... stack)` | Only match entities who do not have the specified stack |
| `default [QueryType](StackableQuery.html "type parameter in StackableQuery")` | `[stackWithin](#stackWithin(int,int))​(int minStack,
int maxStack)` | Only match entities whose stack size is within the specified min/max range |
| `default int` | `[sumStacks](#sumStacks())()` | Executes this query and sums the stack of all matching items |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### sumStacks

```
default int sumStacks()
```

Executes this query and sums the stack of all matching items

Returns:
the sum of the stacks found by this query
- #### stackEquals

```
default [QueryType](StackableQuery.html "type parameter in StackableQuery") stackEquals​(int... stack)
```

Only match entities who have the specified stack

Parameters:
`stack` - the stack
Returns:
this query
- #### stackNotEquals

```
default [QueryType](StackableQuery.html "type parameter in StackableQuery") stackNotEquals​(int... stack)
```

Only match entities who do not have the specified stack

Parameters:
`stack` - the stack
Returns:
this query
- #### minStack

```
default [QueryType](StackableQuery.html "type parameter in StackableQuery") minStack​(int minStack)
```

Only match entities with at least the specified stack size

Parameters:
`minStack` - the minimum stack size to accept
Returns:
this query
- #### maxStack

```
default [QueryType](StackableQuery.html "type parameter in StackableQuery") maxStack​(int maxStack)
```

Only match entities with at most the specified stack size

Parameters:
`maxStack` - the maximum stack size to accept
Returns:
this query
- #### stackWithin

```
default [QueryType](StackableQuery.html "type parameter in StackableQuery") stackWithin​(int minStack,
int maxStack)
```

Only match entities whose stack size is within the specified min/max range

Parameters:
`minStack` - the minimum stack size to accept
`maxStack` - the maximum stack size to accept
Returns:
this query