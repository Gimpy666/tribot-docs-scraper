# ClickableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ClickableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` - the entity type
`QueryType` - the query type

All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemQuery](ItemQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface ClickableQuery<EntityType extends [Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

A query to search over clickable entities

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](ClickableQuery.html "type parameter in ClickableQuery")` | `[isHovering](#isHovering())()` | Only match entities that are being hovered |
| `default [QueryType](ClickableQuery.html "type parameter in ClickableQuery")` | `[isNotHovering](#isNotHovering())()` | Only match entities that are not being hovered |
| `default [QueryType](ClickableQuery.html "type parameter in ClickableQuery")` | `[isNotVisible](#isNotVisible())()` | Only match clickable entities that are not visible |
| `default [QueryType](ClickableQuery.html "type parameter in ClickableQuery")` | `[isVisible](#isVisible())()` | Only match clickable entities that are visible |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### isVisible

```
default [QueryType](ClickableQuery.html "type parameter in ClickableQuery") isVisible()
```

Only match clickable entities that are visible

Returns:
this query
- #### isNotVisible

```
default [QueryType](ClickableQuery.html "type parameter in ClickableQuery") isNotVisible()
```

Only match clickable entities that are not visible

Returns:
this query
- #### isHovering

```
default [QueryType](ClickableQuery.html "type parameter in ClickableQuery") isHovering()
```

Only match entities that are being hovered

Returns:
this query
- #### isNotHovering

```
default [QueryType](ClickableQuery.html "type parameter in ClickableQuery") isNotHovering()
```

Only match entities that are not being hovered

Returns:
this query