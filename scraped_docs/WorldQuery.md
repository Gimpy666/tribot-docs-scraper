# WorldQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/WorldQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.WorldQuery

* All Implemented Interfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<[World](../types/World.html "class in org.tribot.script.sdk.types"),​[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class WorldQuery
extends java.lang.Object
```

A query to search over all available game worlds

See Also:
[`Query.worlds()`](Query.html#worlds())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[activityContains](#activityContains(java.lang.String...))​(java.lang.String... activity)` | Only matches worlds whose activity contains one of the specified activities |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[activityEquals](#activityEquals(java.lang.String...))​(java.lang.String... activity)` | Only matches worlds whose activity equals one of the specified activities |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[activityNotContains](#activityNotContains(java.lang.String...))​(java.lang.String... activity)` | Only matches worlds whose activity does not contain one of the specified activities |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[activityNotEquals](#activityNotEquals(java.lang.String...))​(java.lang.String... activity)` | Only matches worlds whose activity does not equal one of the specified activities |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[World](../types/World.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[hostAddressContains](#hostAddressContains(java.lang.String...))​(java.lang.String... address)` | Only matches worlds whose host address contains one of the specified addresses |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[hostAddressEquals](#hostAddressEquals(java.lang.String...))​(java.lang.String... address)` | Only matches worlds whose host address equals one of the specified addresses |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[hostAddressNotContains](#hostAddressNotContains(java.lang.String...))​(java.lang.String... address)` | Only matches worlds whose host address does not contain one of the specified addresses |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[hostAddressNotEquals](#hostAddressNotEquals(java.lang.String...))​(java.lang.String... address)` | Only matches worlds whose host address does not equal one of the specified addresses |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isDangerous](#isDangerous())()` | Only match worlds that are dangerous |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isLowPing](#isLowPing())()` | Only accept worlds that have 'low' ping relative to other worlds |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isMainGame](#isMainGame())()` | Only match worlds that are the main game |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isMembers](#isMembers())()` | Only matches worlds that are members worlds |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNonMembers](#isNonMembers())()` | Only matches worlds that are non members worlds |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNotAllTypes](#isNotAllTypes(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only matches worlds that do not contain all of the specified types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNotAnyType](#isNotAnyType(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only matches worlds that do not contain any of the specified types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNotCurrentWorld](#isNotCurrentWorld())()` | Only match worlds that are not the current world |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNotDangerous](#isNotDangerous())()` | Only match worlds that are not dangerous |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isNotMainGame](#isNotMainGame())()` | Only match worlds that are not the main game |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isRequirementsMet](#isRequirementsMet())()` | Only match worlds where the requirements to enter are met |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isRequirementsNotMet](#isRequirementsNotMet())()` | Only match worlds where the requirements to enter are not met |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isType](#isType(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only match worlds that contain all of the specified types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isTypesAny](#isTypesAny(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only match worlds that contain any of the specified types

param types the world types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isTypesExactly](#isTypesExactly(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only match worlds that contain exactly the specified types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[isTypesNotExactly](#isTypesNotExactly(org.tribot.script.sdk.types.World.Type...))​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)` | Only match worlds that do not contain exactly the specified types |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[locationEquals](#locationEquals(org.tribot.script.sdk.types.World.Location...))​([World.Location](../types/World.Location.html "enum in org.tribot.script.sdk.types")... location)` | Only match worlds with one of the specified locations |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[locationNotEquals](#locationNotEquals(org.tribot.script.sdk.types.World.Location...))​([World.Location](../types/World.Location.html "enum in org.tribot.script.sdk.types")... location)` | Only match worlds that do not have one of the specified locations |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[maxPing](#maxPing(int))​(int max)` | Only match worlds whose ping is less than or equal to the max ping |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[maxPlayerCount](#maxPlayerCount(int))​(int max)` | Only matches worlds whose player count is less than or equal to the max player count |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[maxTotalLevelRequirement](#maxTotalLevelRequirement(int))​(int max)` | Only match worlds whose total level requirement is at most the specified max threshold |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[maxWorldNumber](#maxWorldNumber(int))​(int max)` | Only matches worlds whose world number is less than or equal to the max world number |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[minPing](#minPing(int))​(int min)` | Only match worlds whose ping is greater than or equal to the min ping |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[minPlayerCount](#minPlayerCount(int))​(int min)` | Only matches worlds whose player count is greater than or equal to the min player count |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[minTotalLevelRequirement](#minTotalLevelRequirement(int))​(int min)` | Only match worlds whose total level requirement is at least the specified min threshold |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[minWorldNumber](#minWorldNumber(int))​(int min)` | Only matches worlds whose world number is greater than or equal to the min world number |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[worldNumberEquals](#worldNumberEquals(int...))​(int... worldNumber)` | Only matches worlds with the specified world number |
| `[WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query")` | `[worldNumberNotEquals](#worldNumberNotEquals(int...))​(int... worldNumber)` | Only matches worlds that do not have the specified world number |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[World](../types/World.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### isMembers

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isMembers()
```

Only matches worlds that are members worlds

Returns:
this query
- #### isNonMembers

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNonMembers()
```

Only matches worlds that are non members worlds

Returns:
this query
- #### worldNumberEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") worldNumberEquals​(int... worldNumber)
```

Only matches worlds with the specified world number

Parameters:
`worldNumber` - the world number
Returns:
this query
- #### worldNumberNotEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") worldNumberNotEquals​(int... worldNumber)
```

Only matches worlds that do not have the specified world number

Parameters:
`worldNumber` - the world number
Returns:
this query
- #### minWorldNumber

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") minWorldNumber​(int min)
```

Only matches worlds whose world number is greater than or equal to the min world number

Parameters:
`min` - the min world number
Returns:
this query
- #### maxWorldNumber

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") maxWorldNumber​(int max)
```

Only matches worlds whose world number is less than or equal to the max world number

Parameters:
`max` - the max world number
Returns:
this query
- #### maxPlayerCount

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") maxPlayerCount​(int max)
```

Only matches worlds whose player count is less than or equal to the max player count

Parameters:
`max` - the max player count
Returns:
this query
- #### minPlayerCount

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") minPlayerCount​(int min)
```

Only matches worlds whose player count is greater than or equal to the min player count

Parameters:
`min` - the min player count
Returns:
this query
- #### activityEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") activityEquals​(java.lang.String... activity)
```

Only matches worlds whose activity equals one of the specified activities

Parameters:
`activity` - the activity name
Returns:
this query
- #### activityContains

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") activityContains​(java.lang.String... activity)
```

Only matches worlds whose activity contains one of the specified activities

Parameters:
`activity` - the activity name
Returns:
this query
- #### activityNotEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") activityNotEquals​(java.lang.String... activity)
```

Only matches worlds whose activity does not equal one of the specified activities

Parameters:
`activity` - the activity name
Returns:
this query
- #### activityNotContains

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") activityNotContains​(java.lang.String... activity)
```

Only matches worlds whose activity does not contain one of the specified activities

Parameters:
`activity` - the activity name
Returns:
this query
- #### hostAddressEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") hostAddressEquals​(java.lang.String... address)
```

Only matches worlds whose host address equals one of the specified addresses

Parameters:
`address` - the host address
Returns:
this query
- #### hostAddressContains

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") hostAddressContains​(java.lang.String... address)
```

Only matches worlds whose host address contains one of the specified addresses

Parameters:
`address` - the host address
Returns:
this query
- #### hostAddressNotEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") hostAddressNotEquals​(java.lang.String... address)
```

Only matches worlds whose host address does not equal one of the specified addresses

Parameters:
`address` - the host address
Returns:
this query
- #### hostAddressNotContains

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") hostAddressNotContains​(java.lang.String... address)
```

Only matches worlds whose host address does not contain one of the specified addresses

Parameters:
`address` - the host address
Returns:
this query
- #### locationEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") locationEquals​([World.Location](../types/World.Location.html "enum in org.tribot.script.sdk.types")... location)
```

Only match worlds with one of the specified locations

Parameters:
`location` - the world location
Returns:
this query
- #### locationNotEquals

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") locationNotEquals​([World.Location](../types/World.Location.html "enum in org.tribot.script.sdk.types")... location)
```

Only match worlds that do not have one of the specified locations

Parameters:
`location` - the world location
Returns:
this query
- #### isType

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isType​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only match worlds that contain all of the specified types

Parameters:
`types` - the world types
Returns:
this query
See Also:
[`World.isType(World.Type...)`](../types/World.html#isType(org.tribot.script.sdk.types.World.Type...))
- #### isTypesAny

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isTypesAny​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only match worlds that contain any of the specified types

param types the world types

Returns:
this query
See Also:
[`World.isTypesAny(World.Type...)`](../types/World.html#isTypesAny(org.tribot.script.sdk.types.World.Type...))
- #### isTypesExactly

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isTypesExactly​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only match worlds that contain exactly the specified types

Parameters:
`types` - the world types
Returns:
this query
See Also:
[`World.isTypesExactly(World.Type...)`](../types/World.html#isTypesExactly(org.tribot.script.sdk.types.World.Type...))
- #### isNotAllTypes

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNotAllTypes​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only matches worlds that do not contain all of the specified types

Returns:
this query
See Also:
[`World.isType(World.Type...)`](../types/World.html#isType(org.tribot.script.sdk.types.World.Type...))
- #### isNotAnyType

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNotAnyType​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only matches worlds that do not contain any of the specified types

Parameters:
`types` - the world types
Returns:
this query
See Also:
[`World.isTypesAny(World.Type...)`](../types/World.html#isTypesAny(org.tribot.script.sdk.types.World.Type...))
- #### isTypesNotExactly

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isTypesNotExactly​([World.Type](../types/World.Type.html "enum in org.tribot.script.sdk.types")... types)
```

Only match worlds that do not contain exactly the specified types

Parameters:
`types` - the world types
Returns:
this query
See Also:
[`World.isTypesExactly(World.Type...)`](../types/World.html#isTypesExactly(org.tribot.script.sdk.types.World.Type...))
- #### minPing

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") minPing​(int min)
```

Only match worlds whose ping is greater than or equal to the min ping

Parameters:
`min` - the min ping
Returns:
this query
See Also:
[`World.getPing()`](../types/World.html#getPing())
- #### maxPing

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") maxPing​(int max)
```

Only match worlds whose ping is less than or equal to the max ping

Parameters:
`max` - the max ping
Returns:
this query
See Also:
[`World.getPing()`](../types/World.html#getPing())
- #### isLowPing

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isLowPing()
```

Only accept worlds that have 'low' ping relative to other worlds

Returns:
this query
- #### isMainGame

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isMainGame()
```

Only match worlds that are the main game

Returns:
this query
- #### isNotMainGame

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNotMainGame()
```

Only match worlds that are not the main game

Returns:
this query
- #### isDangerous

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isDangerous()
```

Only match worlds that are dangerous

Returns:
this query
- #### isNotDangerous

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNotDangerous()
```

Only match worlds that are not dangerous

Returns:
this query
- #### isRequirementsMet

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isRequirementsMet()
```

Only match worlds where the requirements to enter are met

Returns:
this query
See Also:
[`World.isRequirementsMet()`](../types/World.html#isRequirementsMet())
- #### isRequirementsNotMet

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isRequirementsNotMet()
```

Only match worlds where the requirements to enter are not met

Returns:
this query
See Also:
[`World.isRequirementsMet()`](../types/World.html#isRequirementsMet())
- #### minTotalLevelRequirement

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") minTotalLevelRequirement​(int min)
```

Only match worlds whose total level requirement is at least the specified min threshold

Parameters:
`min` - the min total level requirement
Returns:
this query
- #### maxTotalLevelRequirement

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") maxTotalLevelRequirement​(int max)
```

Only match worlds whose total level requirement is at most the specified max threshold

Parameters:
`max` - the max total level requirement
Returns:
this query
- #### isNotCurrentWorld

```
public [WorldQuery](WorldQuery.html "class in org.tribot.script.sdk.query") isNotCurrentWorld()
```

Only match worlds that are not the current world

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