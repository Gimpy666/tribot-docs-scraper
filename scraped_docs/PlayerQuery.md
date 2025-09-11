# PlayerQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/PlayerQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.PlayerQuery

* All Implemented Interfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class PlayerQuery
extends java.lang.Object
implements [CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over entities of type [`Player`](../types/Player.html "class in org.tribot.script.sdk.types")

See Also:
[`Query.players()`](Query.html#players())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[Player](../types/Player.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[hasOverheadIcon](#hasOverheadIcon())()` | Only match players who have an overhead icon |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[hasSkullIcon](#hasSkullIcon())()` | Only match players who have a skull icon |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[includeLocalPlayer](#includeLocalPlayer())()` | Deprecated.
see [`includeMyPlayer()`](#includeMyPlayer())
|
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[includeMyPlayer](#includeMyPlayer())()` | By default, this stream ignores the currently logged-in player. |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[isEquipped](#isEquipped(int...))​(int... ids)` | Only match players who have any of the specified item ids equipped |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[isEquipped](#isEquipped(java.lang.String...))​(java.lang.String... names)` | Only match players who have any of the specified item names equipped |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[isMyPlayerInteractingWith](#isMyPlayerInteractingWith())()` | Only match entities that my player is interacting with (this limits the query to 0 or 1 results) |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[isNotEquipped](#isNotEquipped(int...))​(int... ids)` | Only match players who do not have any of the specified item ids equipped |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[isNotEquipped](#isNotEquipped(java.lang.String...))​(java.lang.String... names)` | Only match players who do not have any of the specified item names equipped |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[overheadIconEquals](#overheadIconEquals(org.tribot.script.sdk.types.Player.OverheadIcon...))​([Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")... overhead)` | Only match players with the specified overhead icon |
| `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")` | `[skullIconEquals](#skullIconEquals(org.tribot.script.sdk.types.Player.SkullIcon...))​([Player.SkullIcon](../types/Player.SkullIcon.html "enum in org.tribot.script.sdk.types")... skull)` | Only match players with the specified skull icon |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")

`[hasHitsplat](CharacterQuery.html#hasHitsplat()), [hasHitsplat](CharacterQuery.html#hasHitsplat(java.util.function.Predicate)), [hasNoHitsplat](CharacterQuery.html#hasNoHitsplat()), [isAnimating](CharacterQuery.html#isAnimating()), [isAnimation](CharacterQuery.html#isAnimation(int...)), [isBeingInteractedWith](CharacterQuery.html#isBeingInteractedWith()), [isFacing](CharacterQuery.html#isFacing(org.tribot.script.sdk.interfaces.Positionable)), [isFacingMe](CharacterQuery.html#isFacingMe()), [isHealthBarEmpty](CharacterQuery.html#isHealthBarEmpty()), [isHealthBarFull](CharacterQuery.html#isHealthBarFull()), [isHealthBarNotEmpty](CharacterQuery.html#isHealthBarNotEmpty()), [isHealthBarNotFull](CharacterQuery.html#isHealthBarNotFull()), [isHealthBarNotVisible](CharacterQuery.html#isHealthBarNotVisible()), [isHealthBarVisible](CharacterQuery.html#isHealthBarVisible()), [isInteractingWith](CharacterQuery.html#isInteractingWith(org.tribot.script.sdk.interfaces.Character...)), [isInteractingWithCharacter](CharacterQuery.html#isInteractingWithCharacter()), [isInteractingWithMe](CharacterQuery.html#isInteractingWithMe()), [isMoving](CharacterQuery.html#isMoving()), [isMyPlayerNotInteractingWith](CharacterQuery.html#isMyPlayerNotInteractingWith()), [isNotAnimating](CharacterQuery.html#isNotAnimating()), [isNotAnimation](CharacterQuery.html#isNotAnimation(int...)), [isNotBeingInteractedWith](CharacterQuery.html#isNotBeingInteractedWith()), [isNotInteractingWith](CharacterQuery.html#isNotInteractingWith(org.tribot.script.sdk.interfaces.Character...)), [isNotInteractingWithCharacter](CharacterQuery.html#isNotInteractingWithCharacter()), [isNotMoving](CharacterQuery.html#isNotMoving()), [maxHealthBarPercent](CharacterQuery.html#maxHealthBarPercent(double)), [maxLevel](CharacterQuery.html#maxLevel(int)), [minHealthBarPercent](CharacterQuery.html#minHealthBarPercent(double)), [minLevel](CharacterQuery.html#minLevel(int)), [overheadMessageContains](CharacterQuery.html#overheadMessageContains(java.lang.String...)), [overheadMessageEquals](CharacterQuery.html#overheadMessageEquals(java.lang.String...)), [overheadMessageNotContains](CharacterQuery.html#overheadMessageNotContains(java.lang.String...)), [overheadMessageNotEquals](CharacterQuery.html#overheadMessageNotEquals(java.lang.String...)), [walkingDirectionEquals](CharacterQuery.html#walkingDirectionEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...)), [walkingDirectionNotEquals](CharacterQuery.html#walkingDirectionNotEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...)), [withinCombatLevels](CharacterQuery.html#withinCombatLevels(int)), [withinCombatLevelsAbove](CharacterQuery.html#withinCombatLevelsAbove(int)), [withinCombatLevelsBelow](CharacterQuery.html#withinCombatLevelsBelow(int))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")

`[indexEquals](IndexableQuery.html#indexEquals(int...)), [indexNotEquals](IndexableQuery.html#indexNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")

`[findBestInteractable](InteractableQuery.html#findBestInteractable()), [sortedByInteractionCost](InteractableQuery.html#sortedByInteractionCost())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")

`[distinctByName](NamedQuery.html#distinctByName()), [nameContains](NamedQuery.html#nameContains(java.lang.String...)), [nameEquals](NamedQuery.html#nameEquals(java.lang.String...)), [nameNotContains](NamedQuery.html#nameNotContains(java.lang.String...)), [nameNotEquals](NamedQuery.html#nameNotEquals(java.lang.String...)), [nameNotStartsWith](NamedQuery.html#nameNotStartsWith(java.lang.String...)), [nameStartsWith](NamedQuery.html#nameStartsWith(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")

`[orientationEquals](OrientableQuery.html#orientationEquals(org.tribot.script.sdk.interfaces.Orientable.Orientation...)), [orientationNotEquals](OrientableQuery.html#orientationNotEquals(org.tribot.script.sdk.interfaces.Orientable.Orientation...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")

`[findClosest](PositionableQuery.html#findClosest()), [findClosestByPathDistance](PositionableQuery.html#findClosestByPathDistance()), [hasLineOfSightTo](PositionableQuery.html#hasLineOfSightTo(org.tribot.script.sdk.interfaces.Positionable)), [inArea](PositionableQuery.html#inArea(org.tribot.script.sdk.types.Area...)), [isInLineOfSight](PositionableQuery.html#isInLineOfSight()), [isInLineOfSight](PositionableQuery.html#isInLineOfSight(org.tribot.script.sdk.interfaces.Positionable)), [isOnMinimap](PositionableQuery.html#isOnMinimap()), [isReachable](PositionableQuery.html#isReachable()), [maxDistance](PositionableQuery.html#maxDistance(double)), [maxDistance](PositionableQuery.html#maxDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [maxPathDistance](PositionableQuery.html#maxPathDistance(double)), [minDistance](PositionableQuery.html#minDistance(double)), [minDistance](PositionableQuery.html#minDistance(org.tribot.script.sdk.interfaces.Positionable,double)), [minPathDistance](PositionableQuery.html#minPathDistance(double)), [notInArea](PositionableQuery.html#notInArea(org.tribot.script.sdk.types.Area...)), [sortedByDistance](PositionableQuery.html#sortedByDistance()), [sortedByDistance](PositionableQuery.html#sortedByDistance(org.tribot.script.sdk.interfaces.Positionable)), [sortedByPathDistance](PositionableQuery.html#sortedByPathDistance()), [tileEquals](PositionableQuery.html#tileEquals(org.tribot.script.sdk.interfaces.Positionable...)), [tileNotEquals](PositionableQuery.html#tileNotEquals(org.tribot.script.sdk.interfaces.Positionable...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[Player](../types/Player.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### isMyPlayerInteractingWith

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") isMyPlayerInteractingWith()
```

Description copied from interface: `[CharacterQuery](CharacterQuery.html#isMyPlayerInteractingWith())`
Only match entities that my player is interacting with (this limits the query to 0 or 1 results)

Specified by:
`[isMyPlayerInteractingWith](CharacterQuery.html#isMyPlayerInteractingWith())` in interface `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`
Returns:
this query
- #### includeLocalPlayer

```
@Deprecated
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") includeLocalPlayer()
```

Deprecated.
see [`includeMyPlayer()`](#includeMyPlayer())

By default, this stream ignores the local player.
Calling this method will cause the query to include the local player in the search as well.

Returns:
this query
- #### includeMyPlayer

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") includeMyPlayer()
```

By default, this stream ignores the currently logged-in player.
Calling this method will cause the query to include this player in the search as well.

Returns:
this query
- #### hasSkullIcon

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") hasSkullIcon()
```

Only match players who have a skull icon

Returns:
this query
- #### skullIconEquals

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") skullIconEquals​([Player.SkullIcon](../types/Player.SkullIcon.html "enum in org.tribot.script.sdk.types")... skull)
```

Only match players with the specified skull icon

Parameters:
`skull` - the skull icon
Returns:
this query
- #### hasOverheadIcon

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") hasOverheadIcon()
```

Only match players who have an overhead icon

Specified by:
`[hasOverheadIcon](CharacterQuery.html#hasOverheadIcon())` in interface `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`
Returns:
this query
- #### overheadIconEquals

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") overheadIconEquals​([Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")... overhead)
```

Only match players with the specified overhead icon

Specified by:
`[overheadIconEquals](CharacterQuery.html#overheadIconEquals(org.tribot.script.sdk.types.Player.OverheadIcon...))` in interface `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Player](../types/Player.html "class in org.tribot.script.sdk.types"),​[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`overhead` - the overhead icon
Returns:
this query
- #### isEquipped

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") isEquipped​(int... ids)
```

Only match players who have any of the specified item ids equipped

Parameters:
`ids` - the item ids to check
Returns:
this query
- #### isNotEquipped

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") isNotEquipped​(int... ids)
```

Only match players who do not have any of the specified item ids equipped

Parameters:
`ids` - the item ids to check
Returns:
this query
- #### isEquipped

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") isEquipped​(java.lang.String... names)
```

Only match players who have any of the specified item names equipped

Parameters:
`names` - the item names to check
Returns:
this query
- #### isNotEquipped

```
public [PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query") isNotEquipped​(java.lang.String... names)
```

Only match players who do not have any of the specified item names equipped

Parameters:
`names` - the item names to check
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