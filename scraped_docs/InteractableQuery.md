# InteractableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/InteractableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface InteractableQuery<EntityType extends [Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default java.util.Optional<[EntityType](InteractableQuery.html "type parameter in InteractableQuery")>` | `[findBestInteractable](#findBestInteractable())()` | Orders the best entity according to [`PreferredTargetSelector`](../antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") (the element with the minimum cost) |
| `default [QueryType](InteractableQuery.html "type parameter in InteractableQuery")` | `[sortedByInteractionCost](#sortedByInteractionCost())()` | Orders the entities by [`PreferredTargetSelector`](../antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |

- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")

`[findClosest](PositionableQuery.html#findClosest()), [findClosestByPathDistance](PositionableQuery.html#findClosestByPathDistance()), [hasLineOfSightTo](PositionableQuery.html#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable)), [inArea](PositionableQuery.html#inArea(org.tribot.script.sdk.types.Area...)), [isInLineOfSight](PositionableQuery.html#isInLineOfSight()), [isInLineOfSight](PositionableQuery.html#isInLineOfSight(org.tribot.script.sdk.interfaces.Positionable)), [isOnMinimap](PositionableQuery.html#isOnMinimap()), [isReachable](PositionableQuery.html#isReachable()), [maxDistance](PositionableQuery.html#maxDistance(double)), [maxDistance](PositionableQuery.html#maxDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [maxPathDistance](PositionableQuery.html#maxPathDistance(double)), [minDistance](PositionableQuery.html#minDistance(double)), [minDistance](PositionableQuery.html#minDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [minPathDistance](PositionableQuery.html#minPathDistance(double)), [notInArea](PositionableQuery.html#notInArea(org.tribot.script.sdk.types.Area...)), [sortedByDistance](PositionableQuery.html#sortedByDistance()), [sortedByDistance](PositionableQuery.html#sortedByDistance(org.tribot.script.sdk.interfaces.Positionable)), [sortedByPathDistance](PositionableQuery.html#sortedByPathDistance()), [tileEquals](PositionableQuery.html#tileEquals(org.tribot.script.sdk.interfaces.Positionable...)), [tileNotEquals](PositionableQuery.html#tileNotEquals(org.tribot.script.sdk.interfaces.Positionable...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### sortedByInteractionCost

```
default [QueryType](InteractableQuery.html "type parameter in InteractableQuery") sortedByInteractionCost()
```

Orders the entities by [`PreferredTargetSelector`](../antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Returns:
this query
- #### findBestInteractable

```
default java.util.Optional<[EntityType](InteractableQuery.html "type parameter in InteractableQuery")> findBestInteractable()
```

Orders the best entity according to [`PreferredTargetSelector`](../antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") (the element with the minimum cost)

Returns:
this query