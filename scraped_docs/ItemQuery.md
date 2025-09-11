# ItemQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ItemQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[ItemDefinableQuery](ItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[BankQuery](BankQuery.html "class in org.tribot.script.sdk.query")`, `[EquipmentQuery](EquipmentQuery.html "class in org.tribot.script.sdk.query")`, `[InventoryQuery](InventoryQuery.html "class in org.tribot.script.sdk.query")`, `[ShopItemQuery](ShopItemQuery.html "class in org.tribot.script.sdk.query")`, `[TradeQuery](TradeQuery.html "class in org.tribot.script.sdk.query")`, `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface ItemQuery<EntityType extends [Item](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default java.util.Optional<[EntityType](ItemQuery.html "type parameter in ItemQuery")>` | `[findClosestToMouse](#findClosestToMouse())()` | Executes this query and gets the closest item to the mouse |
| `default [QueryType](ItemQuery.html "type parameter in ItemQuery")` | `[sortedByDistanceToMouse](#sortedByDistanceToMouse())()` | Sorts this query by distance to the mouse, with closer entities first |

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
- ### Methods inherited from interface org.tribot.script.sdk.query.[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")

`[distinctByName](NamedQuery.html#distinctByName()), [nameContains](NamedQuery.html#nameContains(java.lang.String...)), [nameEquals](NamedQuery.html#nameEquals(java.lang.String...)), [nameNotContains](NamedQuery.html#nameNotContains(java.lang.String...)), [nameNotEquals](NamedQuery.html#nameNotEquals(java.lang.String...)), [nameNotStartsWith](NamedQuery.html#nameNotStartsWith(java.lang.String...)), [nameStartsWith](NamedQuery.html#nameStartsWith(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[StackableItemDefinableQuery](StackableItemDefinableQuery.html "interface in org.tribot.script.sdk.query")

`[maxPrice](StackableItemDefinableQuery.html#maxPrice(int)), [maxStackPrice](StackableItemDefinableQuery.html#maxStackPrice(int)), [minPrice](StackableItemDefinableQuery.html#minPrice(int)), [minStackPrice](StackableItemDefinableQuery.html#minStackPrice(int))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[StackableQuery](StackableQuery.html "interface in org.tribot.script.sdk.query")

`[maxStack](StackableQuery.html#maxStack(int)), [minStack](StackableQuery.html#minStack(int)), [stackEquals](StackableQuery.html#stackEquals(int...)), [stackNotEquals](StackableQuery.html#stackNotEquals(int...)), [stackWithin](StackableQuery.html#stackWithin(int,int)), [sumStacks](StackableQuery.html#sumStacks())`

* + ### Method Detail

- #### findClosestToMouse

```
default java.util.Optional<[EntityType](ItemQuery.html "type parameter in ItemQuery")> findClosestToMouse()
```

Executes this query and gets the closest item to the mouse

Returns:
the closest inventory item to the mouse
- #### sortedByDistanceToMouse

```
default [QueryType](ItemQuery.html "type parameter in ItemQuery") sortedByDistanceToMouse()
```

Sorts this query by distance to the mouse, with closer entities first

Returns:
this query