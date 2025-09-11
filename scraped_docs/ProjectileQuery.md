# ProjectileQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ProjectileQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.ProjectileQuery

* All Implemented Interfaces:
`[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types"),​[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types"),​[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class ProjectileQuery
extends java.lang.Object
implements [PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types"),​[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over entities of type [`Projectile`](../types/Projectile.html "class in org.tribot.script.sdk.types")

See Also:
[`Query.projectiles()`](Query.html#projectiles())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[graphicIdEquals](#graphicIdEquals(int...))​(int... graphicId)` | Only match projectiles with the specified graphic ids |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[graphicIdNotEquals](#graphicIdNotEquals(int...))​(int... graphicId)` | Only match projectiles which do not have the specified graphic ids |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[isMoving](#isMoving())()` | Only match projectiles that are moving |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[isNotMoving](#isNotMoving())()` | Only match projectiles that are not moving |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[isNotTargetingMe](#isNotTargetingMe())()` | Only match projectiles that are not targeting our player |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[isTargetingMe](#isTargetingMe())()` | Only match projectiles that are targeting our player |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[orientationEquals](#orientationEquals(int...))​(int... orientation)` | Only match projectiles with the specified orientations |
| `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")` | `[orientationNotEquals](#orientationNotEquals(int...))​(int... orientation)` | Only match projectiles which do not have the specified orientations |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")

`[findClosest](PositionableQuery.html#findClosest()), [findClosestByPathDistance](PositionableQuery.html#findClosestByPathDistance()), [hasLineOfSightTo](PositionableQuery.html#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable)), [inArea](PositionableQuery.html#inArea(org.tribot.script.sdk.types.Area...)), [isInLineOfSight](PositionableQuery.html#isInLineOfSight()), [isInLineOfSight](PositionableQuery.html#isInLineOfSight(org.tribot.script.sdk.interfaces.Positionable)), [isOnMinimap](PositionableQuery.html#isOnMinimap()), [isReachable](PositionableQuery.html#isReachable()), [maxDistance](PositionableQuery.html#maxDistance(double)), [maxDistance](PositionableQuery.html#maxDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [maxPathDistance](PositionableQuery.html#maxPathDistance(double)), [minDistance](PositionableQuery.html#minDistance(double)), [minDistance](PositionableQuery.html#minDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [minPathDistance](PositionableQuery.html#minPathDistance(double)), [notInArea](PositionableQuery.html#notInArea(org.tribot.script.sdk.types.Area...)), [sortedByDistance](PositionableQuery.html#sortedByDistance()), [sortedByDistance](PositionableQuery.html#sortedByDistance(org.tribot.script.sdk.interfaces.Positionable)), [sortedByPathDistance](PositionableQuery.html#sortedByPathDistance()), [tileEquals](PositionableQuery.html#tileEquals(org.tribot.script.sdk.interfaces.Positionable...)), [tileNotEquals](PositionableQuery.html#tileNotEquals(org.tribot.script.sdk.interfaces.Positionable...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[Projectile](../types/Projectile.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### isTargetingMe

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") isTargetingMe()
```

Only match projectiles that are targeting our player

Returns:
this query
- #### isMoving

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") isMoving()
```

Only match projectiles that are moving

Returns:
this query
- #### isNotTargetingMe

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") isNotTargetingMe()
```

Only match projectiles that are not targeting our player

Returns:
this query
- #### isNotMoving

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") isNotMoving()
```

Only match projectiles that are not moving

Returns:
this query
- #### graphicIdEquals

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") graphicIdEquals​(int... graphicId)
```

Only match projectiles with the specified graphic ids

Parameters:
`graphicId` - the graphic ids to check
Returns:
this query
- #### orientationEquals

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") orientationEquals​(int... orientation)
```

Only match projectiles with the specified orientations

Parameters:
`orientation` - the orientations to check
Returns:
this query
- #### graphicIdNotEquals

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") graphicIdNotEquals​(int... graphicId)
```

Only match projectiles which do not have the specified graphic ids

Parameters:
`graphicId` - the graphic ids to check
Returns:
this query
- #### orientationNotEquals

```
public [ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query") orientationNotEquals​(int... orientation)
```

Only match projectiles which do not have the specified orientations

Parameters:
`orientation` - the orientations to check
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