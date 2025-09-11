# NpcQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/NpcQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.NpcQuery

* All Implemented Interfaces:
`[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class NpcQuery
extends java.lang.Object
implements [CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>, [IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>, [ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over entities of type [`Npc`](../types/Npc.html "class in org.tribot.script.sdk.types")

See Also:
[`Query.npcs()`](Query.html#npcs())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")` | `[indexEquals](#indexEquals(int...))​(int... index)` | Only match entities with the specified index |
| `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")` | `[isMyPlayerInteractingWith](#isMyPlayerInteractingWith())()` | Only match entities that my player is interacting with (this limits the query to 0 or 1 results) |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")

`[actionContains](ActionableQuery.html#actionContains(java.lang.String...)), [actionEquals](ActionableQuery.html#actionEquals(java.lang.String...)), [actionNotContains](ActionableQuery.html#actionNotContains(java.lang.String...)), [actionNotEquals](ActionableQuery.html#actionNotEquals(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")

`[hasHitsplat](CharacterQuery.html#hasHitsplat()), [hasHitsplat](CharacterQuery.html#hasHitsplat(java.util.function.Predicate)), [hasNoHitsplat](CharacterQuery.html#hasNoHitsplat()), [hasOverheadIcon](CharacterQuery.html#hasOverheadIcon()), [isAnimating](CharacterQuery.html#isAnimating()), [isAnimation](CharacterQuery.html#isAnimation(int...)), [isBeingInteractedWith](CharacterQuery.html#isBeingInteractedWith()), [isFacing](CharacterQuery.html#isFacing(org.tribot.script.sdk.interfaces.Positionable)), [isFacingMe](CharacterQuery.html#isFacingMe()), [isHealthBarEmpty](CharacterQuery.html#isHealthBarEmpty()), [isHealthBarFull](CharacterQuery.html#isHealthBarFull()), [isHealthBarNotEmpty](CharacterQuery.html#isHealthBarNotEmpty()), [isHealthBarNotFull](CharacterQuery.html#isHealthBarNotFull()), [isHealthBarNotVisible](CharacterQuery.html#isHealthBarNotVisible()), [isHealthBarVisible](CharacterQuery.html#isHealthBarVisible()), [isInteractingWith](CharacterQuery.html#isInteractingWith(org.tribot.script.sdk.interfaces.Character...)), [isInteractingWithCharacter](CharacterQuery.html#isInteractingWithCharacter()), [isInteractingWithMe](CharacterQuery.html#isInteractingWithMe()), [isMoving](CharacterQuery.html#isMoving()), [isMyPlayerNotInteractingWith](CharacterQuery.html#isMyPlayerNotInteractingWith()), [isNotAnimating](CharacterQuery.html#isNotAnimating()), [isNotAnimation](CharacterQuery.html#isNotAnimation(int...)), [isNotBeingInteractedWith](CharacterQuery.html#isNotBeingInteractedWith()), [isNotInteractingWith](CharacterQuery.html#isNotInteractingWith(org.tribot.script.sdk.interfaces.Character...)), [isNotInteractingWithCharacter](CharacterQuery.html#isNotInteractingWithCharacter()), [isNotMoving](CharacterQuery.html#isNotMoving()), [maxHealthBarPercent](CharacterQuery.html#maxHealthBarPercent(double)), [maxLevel](CharacterQuery.html#maxLevel(int)), [minHealthBarPercent](CharacterQuery.html#minHealthBarPercent(double)), [minLevel](CharacterQuery.html#minLevel(int)), [overheadIconEquals](CharacterQuery.html#overheadIconEquals(org.tribot.script.sdk.types.Player.OverheadIcon...)), [overheadMessageContains](CharacterQuery.html#overheadMessageContains(java.lang.String...)), [overheadMessageEquals](CharacterQuery.html#overheadMessageEquals(java.lang.String...)), [overheadMessageNotContains](CharacterQuery.html#overheadMessageNotContains(java.lang.String...)), [overheadMessageNotEquals](CharacterQuery.html#overheadMessageNotEquals(java.lang.String...)), [walkingDirectionEquals](CharacterQuery.html#walkingDirectionEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...)), [walkingDirectionNotEquals](CharacterQuery.html#walkingDirectionNotEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...)), [withinCombatLevels](CharacterQuery.html#withinCombatLevels(int)), [withinCombatLevelsAbove](CharacterQuery.html#withinCombatLevelsAbove(int)), [withinCombatLevelsBelow](CharacterQuery.html#withinCombatLevelsBelow(int))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")

`[distinctById](IdentifiableQuery.html#distinctById()), [idEquals](IdentifiableQuery.html#idEquals(int...)), [idNotEquals](IdentifiableQuery.html#idNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")

`[indexNotEquals](IndexableQuery.html#indexNotEquals(int...))`
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
protected java.util.stream.Stream<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### isMyPlayerInteractingWith

```
public [NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query") isMyPlayerInteractingWith()
```

Description copied from interface: `[CharacterQuery](CharacterQuery.html#isMyPlayerInteractingWith())`
Only match entities that my player is interacting with (this limits the query to 0 or 1 results)

Specified by:
`[isMyPlayerInteractingWith](CharacterQuery.html#isMyPlayerInteractingWith())` in interface `[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`
Returns:
this query
- #### indexEquals

```
public [NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query") indexEquals​(int... index)
```

Description copied from interface: `[IndexableQuery](IndexableQuery.html#indexEquals(int...))`
Only match entities with the specified index

Specified by:
`[indexEquals](IndexableQuery.html#indexEquals(int...))` in interface `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Npc](../types/Npc.html "class in org.tribot.script.sdk.types"),​[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`index` - the index to check
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