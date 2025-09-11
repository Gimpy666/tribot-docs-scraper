# PositionableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/PositionableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GraphicObjectQuery](GraphicObjectQuery.html "class in org.tribot.script.sdk.query")`, `[GroundItemQuery](GroundItemQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`, `[ProjectileQuery](ProjectileQuery.html "class in org.tribot.script.sdk.query")`, `[TileQuery](TileQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface PositionableQuery<EntityType extends [Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default java.util.Optional<[EntityType](PositionableQuery.html "type parameter in PositionableQuery")>` | `[findClosest](#findClosest())()` | Executes this query and gets the closest matching entity to our player |
| `default java.util.Optional<[EntityType](PositionableQuery.html "type parameter in PositionableQuery")>` | `[findClosestByPathDistance](#findClosestByPathDistance())()` | Executes this query and gets the closest matching entity to our player, based on path distance (the distance it would take to actually walk there based on the surrounding obstacles/collision) |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[hasLineOfSightTo](#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") other)` | Unmaintained. |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[inArea](#inArea(org.tribot.script.sdk.types.Area...))​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)` | Only match entities in the specified areas |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[isInLineOfSight](#isInLineOfSight())()` | Unmaintained. |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[isInLineOfSight](#isInLineOfSight(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)` | Unmaintained. |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[isOnMinimap](#isOnMinimap())()` | Only match entities that are on the minimap |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[isReachable](#isReachable())()` | Only match entities that are reachable via [`LocalWalking.Map.canReach(Positionable)`](../walking/LocalWalking.Map.html#canReach(org.tribot.script.sdk.interfaces.Positionable)) obtained from [`LocalWalking.createMap()`](../walking/LocalWalking.html#createMap()) |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[maxDistance](#maxDistance(double))​(double maxDistance)` | Only match entities who are at most the specified distance away from our player |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[maxDistance](#maxDistance(org.tribot.script.sdk.interfaces.Positionable,double))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source,
double maxDistance)` | Only match entities who are at most the specified distance away from the specified location |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[maxPathDistance](#maxPathDistance(double))​(double maxDistance)` | Only match entities who are at most the specified path distance away from our player (the distance it would take to actually walk there based on the surrounding obstacles/collision) |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[minDistance](#minDistance(double))​(double min)` | Only match entities who are at least the specified distance away from our player |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[minDistance](#minDistance(org.tribot.script.sdk.interfaces.Positionable,double))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source,
double min)` | Only match entities who are at least the specified distance away from the specified location |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[minPathDistance](#minPathDistance(double))​(double min)` | Only match entities who are at least the specified path distance away from our player (the distance it would take to actually walk there based on the surrounding obstacles/collision) |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[notInArea](#notInArea(org.tribot.script.sdk.types.Area...))​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)` | Only match entities who are not in any of the specified areas |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[sortedByDistance](#sortedByDistance())()` | Sorts the entities by their distance to our player, with the closest appearing first |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[sortedByDistance](#sortedByDistance(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)` | Sorts the entities by their distance to the specified location, with the closest appearing first |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[sortedByPathDistance](#sortedByPathDistance())()` | Sorts the entities by their path distance (the distance it would take to actually walk there based on the surrounding obstacles/collision) |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[tileEquals](#tileEquals(org.tribot.script.sdk.interfaces.Positionable...))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)` | Only matches entities at the specified positions |
| `default [QueryType](PositionableQuery.html "type parameter in PositionableQuery")` | `[tileNotEquals](#tileNotEquals(org.tribot.script.sdk.interfaces.Positionable...))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)` | Only match entities who are not at any of the specified positions |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### isReachable

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") isReachable()
```

Only match entities that are reachable via [`LocalWalking.Map.canReach(Positionable)`](../walking/LocalWalking.Map.html#canReach(org.tribot.script.sdk.interfaces.Positionable)) obtained from [`LocalWalking.createMap()`](../walking/LocalWalking.html#createMap())

Returns:
this query
- #### isOnMinimap

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") isOnMinimap()
```

Only match entities that are on the minimap

Returns:
this query
- #### findClosest

```
default java.util.Optional<[EntityType](PositionableQuery.html "type parameter in PositionableQuery")> findClosest()
```

Executes this query and gets the closest matching entity to our player

Returns:
the closest matching entity, or an empty optional if none matched
- #### findClosestByPathDistance

```
default java.util.Optional<[EntityType](PositionableQuery.html "type parameter in PositionableQuery")> findClosestByPathDistance()
```

Executes this query and gets the closest matching entity to our player, based on path distance (the distance it would take to actually walk there based on the surrounding obstacles/collision)

Returns:
the closest matching entity, or an empty optional if none matched
- #### tileEquals

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") tileEquals​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)
```

Only matches entities at the specified positions

Parameters:
`positions` - the positions to check
Returns:
this query
- #### inArea

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") inArea​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)
```

Only match entities in the specified areas

Parameters:
`area` - the areas to check
Returns:
this query
- #### tileNotEquals

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") tileNotEquals​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")... positions)
```

Only match entities who are not at any of the specified positions

Parameters:
`positions` - the positions to check
Returns:
this query
- #### notInArea

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") notInArea​([Area](../types/Area.html "class in org.tribot.script.sdk.types")... area)
```

Only match entities who are not in any of the specified areas

Parameters:
`area` - the areas to check
Returns:
this query
- #### maxDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") maxDistance​(double maxDistance)
```

Only match entities who are at most the specified distance away from our player

Parameters:
`maxDistance` - the max distance of entities to find
Returns:
this query
- #### maxDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") maxDistance​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source,
double maxDistance)
```

Only match entities who are at most the specified distance away from the specified location

Parameters:
`source` - the position to use as the base for calculating the entities distance from
`maxDistance` - the max distance of entities to find
Returns:
this query
- #### maxPathDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") maxPathDistance​(double maxDistance)
```

Only match entities who are at most the specified path distance away from our player (the distance it would take to actually walk there based on the surrounding obstacles/collision)

Parameters:
`maxDistance` - the max distance of entities to find
Returns:
this query
- #### minDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") minDistance​(double min)
```

Only match entities who are at least the specified distance away from our player

Parameters:
`min` - the min distance of entities to find
Returns:
this query
- #### minPathDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") minPathDistance​(double min)
```

Only match entities who are at least the specified path distance away from our player (the distance it would take to actually walk there based on the surrounding obstacles/collision)

Parameters:
`min` - the min distance of entities to find
Returns:
this query
- #### minDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") minDistance​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source,
double min)
```

Only match entities who are at least the specified distance away from the specified location

Parameters:
`source` - the position to use as the base for calculating the entities distance from
`min` - the min distance of entities to find
Returns:
this query
- #### sortedByDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") sortedByDistance()
```

Sorts the entities by their distance to our player, with the closest appearing first

Returns:
this query
- #### sortedByDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") sortedByDistance​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)
```

Sorts the entities by their distance to the specified location, with the closest appearing first

Parameters:
`source` - the position to use as the base for calculating the entities distance from
Returns:
this query
- #### sortedByPathDistance

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") sortedByPathDistance()
```

Sorts the entities by their path distance (the distance it would take to actually walk there based on the surrounding obstacles/collision)

Returns:
this query
- #### isInLineOfSight

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") isInLineOfSight()
```

Unmaintained. Only match entities that are in the line of sight

Returns:
this query
- #### hasLineOfSightTo

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") hasLineOfSightTo​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") other)
```

Unmaintained. Only match entities that have line of sight to the target

Parameters:
`other` - the target entity
Returns:
this query
- #### isInLineOfSight

```
default [QueryType](PositionableQuery.html "type parameter in PositionableQuery") isInLineOfSight​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") source)
```

Unmaintained. Only match entities that are in the line of sight of the source

Parameters:
`source` - the source position
Returns:
this query