# TileQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/TileQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.TileQuery

* All Implemented Interfaces:
`[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class TileQuery
extends java.lang.Object
implements [InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over tiles in the local region

See Also:
[`Query.tiles()`](Query.html#tiles())

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[TileQuery](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")` | `[inArea](#inArea(org.tribot.script.sdk.types.Area...))​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)` | Only match entities in the specified areas |
| `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")` | `[maxDistance](#maxDistance(double))​(double max)` | Only match entities who are at most the specified distance away from our player |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |
| `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")` | `[tileEquals](#tileEquals(org.tribot.script.sdk.interfaces.Positionable...))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)` | Only matches entities at the specified positions |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")

`[findBestInteractable](InteractableQuery.html#findBestInteractable()), [sortedByInteractionCost](InteractableQuery.html#sortedByInteractionCost())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")

`[findClosest](PositionableQuery.html#findClosest()), [findClosestByPathDistance](PositionableQuery.html#findClosestByPathDistance()), [hasLineOfSightTo](PositionableQuery.html#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable)), [isInLineOfSight](PositionableQuery.html#isInLineOfSight()), [isInLineOfSight](PositionableQuery.html#isInLineOfSight(org.tribot.script.sdk.interfaces.Positionable)), [isOnMinimap](PositionableQuery.html#isOnMinimap()), [isReachable](PositionableQuery.html#isReachable()), [maxDistance](PositionableQuery.html#maxDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [maxPathDistance](PositionableQuery.html#maxPathDistance(double)), [minDistance](PositionableQuery.html#minDistance(double)), [minDistance](PositionableQuery.html#minDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [minPathDistance](PositionableQuery.html#minPathDistance(double)), [notInArea](PositionableQuery.html#notInArea(org.tribot.script.sdk.types.Area...)), [sortedByDistance](PositionableQuery.html#sortedByDistance()), [sortedByDistance](PositionableQuery.html#sortedByDistance(org.tribot.script.sdk.interfaces.Positionable)), [sortedByPathDistance](PositionableQuery.html#sortedByPathDistance()), [tileNotEquals](PositionableQuery.html#tileNotEquals(org.tribot.script.sdk.interfaces.Positionable...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Constructor Detail

- #### TileQuery

```
public TileQuery()
```

+ ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### tileEquals

```
public [TileQuery](TileQuery.html "class in org.tribot.script.sdk.query") tileEquals​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)
```

Description copied from interface: `[PositionableQuery](PositionableQuery.html#tileEquals(org.tribot.script.sdk.interfaces.Positionable...))`
Only matches entities at the specified positions

Specified by:
`[tileEquals](PositionableQuery.html#tileEquals(org.tribot.script.sdk.interfaces.Positionable...))` in interface `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`positions` - the positions to check
Returns:
this query
- #### inArea

```
public [TileQuery](TileQuery.html "class in org.tribot.script.sdk.query") inArea​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)
```

Description copied from interface: `[PositionableQuery](PositionableQuery.html#inArea(org.tribot.script.sdk.types.Area...))`
Only match entities in the specified areas

Specified by:
`[inArea](PositionableQuery.html#inArea(org.tribot.script.sdk.types.Area...))` in interface `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`area` - the areas to check
Returns:
this query
- #### maxDistance

```
public [TileQuery](TileQuery.html "class in org.tribot.script.sdk.query") maxDistance​(double max)
```

Description copied from interface: `[PositionableQuery](PositionableQuery.html#maxDistance(double))`
Only match entities who are at most the specified distance away from our player

Specified by:
`[maxDistance](PositionableQuery.html#maxDistance(double))` in interface `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[LocalTile](../types/LocalTile.html "class in org.tribot.script.sdk.types"),​[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`max` - the max distance of entities to find
Returns:
this query
- #### filter

```
public QueryType filter​(java.util.function.Predicate<EntityType> filter)
```

Description copied from interface: `[Query](Query.html#filter(java.util.function.Predicate))`
Applies the specified filter to this query.
This query is **not** executed at this point.

Specified by:
`[filter](Query.html#filter(java.util.function.Predicate))` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Parameters:
`filter` - the filter to apply to this query
Returns:
this query
- #### sorted

```
public QueryType sorted​(java.util.Comparator<EntityType> comparator)
```

Description copied from interface: `[Query](Query.html#sorted(java.util.Comparator))`
Orders the query by the specified comparator.
This query is **not** executed at this point.

Specified by:
`[sorted](Query.html#sorted(java.util.Comparator))` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Parameters:
`comparator` - the comparator to order the query by
Returns:
this query
- #### stream

```
public java.util.stream.Stream<EntityType> stream()
```

Description copied from interface: `[Query](Query.html#stream())`
Returns this query as a stream.
This query is **not** executed at this point **but** it will be executed whenever the stream executes a terminal operation.

Specified by:
`[stream](Query.html#stream())` in interface `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>`
Returns:
this query as a stream
- #### asQueryType

```
protected final QueryType asQueryType()
```