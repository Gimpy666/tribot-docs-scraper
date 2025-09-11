# CharacterQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/CharacterQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* Type Parameters:
`EntityType` - the entity type
`QueryType` - the query type

All Superinterfaces:
`[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[PositionableQuery](PositionableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface CharacterQuery<EntityType extends [Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [InteractableQuery](InteractableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>, [OrientableQuery](OrientableQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

A query to search over character entities

See Also:
[`Character`](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces"),
[`NpcQuery`](NpcQuery.html "class in org.tribot.script.sdk.query"),
[`PlayerQuery`](PlayerQuery.html "class in org.tribot.script.sdk.query")

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[hasHitsplat](#hasHitsplat())()` | Checks if any hitsplat is present |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[hasHitsplat](#hasHitsplat(java.util.function.Predicate))​(java.util.function.Predicate<[Hitsplat](../types/Hitsplat.html "class in org.tribot.script.sdk.types")> filter)` | Checks if any hitsplat is present that matches the filter |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[hasNoHitsplat](#hasNoHitsplat())()` | Checks if no hitsplat is present |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[hasOverheadIcon](#hasOverheadIcon())()` | Only match players who have an overhead icon |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isAnimating](#isAnimating())()` | Only match characters who are animating |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isAnimation](#isAnimation(int...))​(int... animation)` | Only match characters with any of the specified animations |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isBeingInteractedWith](#isBeingInteractedWith())()` | Only match entities that at least one character is interacting with |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isFacing](#isFacing(org.tribot.script.sdk.interfaces.Positionable))​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)` | Only matches characters that are facing the specified position |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isFacingMe](#isFacingMe())()` | Only matches characters that are facing our player |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarEmpty](#isHealthBarEmpty())()` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarFull](#isHealthBarFull())()` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarNotEmpty](#isHealthBarNotEmpty())()` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarNotFull](#isHealthBarNotFull())()` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarNotVisible](#isHealthBarNotVisible())()` | Only matches characters who's health bar is not visible |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isHealthBarVisible](#isHealthBarVisible())()` | Only matches characters who's health bar is currently visible |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isInteractingWith](#isInteractingWith(org.tribot.script.sdk.interfaces.Character...))​([Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")... interacting)` | Only match entities that are interacting with any of the specified entities |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isInteractingWithCharacter](#isInteractingWithCharacter())()` | Only match entities that are interacting with another character |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isInteractingWithMe](#isInteractingWithMe())()` | Only matches characters that are interacting with our player |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isMoving](#isMoving())()` | Only matches characters that are moving |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isMyPlayerInteractingWith](#isMyPlayerInteractingWith())()` | Only match entities that my player is interacting with (this limits the query to 0 or 1 results) |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isMyPlayerNotInteractingWith](#isMyPlayerNotInteractingWith())()` | Only match entities that my player is interacting with |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotAnimating](#isNotAnimating())()` | Only match characters who are not animating |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotAnimation](#isNotAnimation(int...))​(int... animation)` | Only match characters who do not have any of the specified animations |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotBeingInteractedWith](#isNotBeingInteractedWith())()` | Only match entities that no character is interacting with |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotInteractingWith](#isNotInteractingWith(org.tribot.script.sdk.interfaces.Character...))​([Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")... interacting)` | Only match entities that are not interacting with any of the specified entities |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotInteractingWithCharacter](#isNotInteractingWithCharacter())()` | Only match entities that are not interacting with another character |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[isNotMoving](#isNotMoving())()` | Only matches characters that are not moving |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[maxHealthBarPercent](#maxHealthBarPercent(double))​(double max)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[maxLevel](#maxLevel(int))​(int maxLevel)` | Only matches characters who are at most the specific level |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[minHealthBarPercent](#minHealthBarPercent(double))​(double min)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[minLevel](#minLevel(int))​(int minLevel)` | Only matches characters who are at least the specified level |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[overheadIconEquals](#overheadIconEquals(org.tribot.script.sdk.types.Player.OverheadIcon...))​([Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")... overhead)` | Only match players with the specified overhead icon |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[overheadMessageContains](#overheadMessageContains(java.lang.String...))​(java.lang.String... msg)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[overheadMessageEquals](#overheadMessageEquals(java.lang.String...))​(java.lang.String... msg)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[overheadMessageNotContains](#overheadMessageNotContains(java.lang.String...))​(java.lang.String... msg)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[overheadMessageNotEquals](#overheadMessageNotEquals(java.lang.String...))​(java.lang.String... msg)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[walkingDirectionEquals](#walkingDirectionEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...))​([Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")... walkingDirection)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[walkingDirectionNotEquals](#walkingDirectionNotEquals(org.tribot.script.sdk.interfaces.Character.WalkingDirection...))​([Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")... walkingDirection)` | |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[withinCombatLevels](#withinCombatLevels(int))​(int within)` | Only matches characters who are within the specified range from our player's level. |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[withinCombatLevelsAbove](#withinCombatLevelsAbove(int))​(int within)` | Only matches characters who are within the specified range above our player's level. |
| `default [QueryType](CharacterQuery.html "type parameter in CharacterQuery")` | `[withinCombatLevelsBelow](#withinCombatLevelsBelow(int))​(int within)` | Only matches characters who are within the specified range below our player's level. |

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

- #### isMoving

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isMoving()
```

Only matches characters that are moving

Returns:
this query
- #### isNotMoving

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotMoving()
```

Only matches characters that are not moving

Returns:
this query
- #### isInteractingWithMe

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isInteractingWithMe()
```

Only matches characters that are interacting with our player

Returns:
this query
- #### isHealthBarVisible

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarVisible()
```

Only matches characters who's health bar is currently visible

Returns:
this query
- #### isHealthBarNotVisible

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarNotVisible()
```

Only matches characters who's health bar is not visible

Returns:
this query
- #### isFacing

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isFacing​([Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces") position)
```

Only matches characters that are facing the specified position

Parameters:
`position` - the position to check if a character is facing
Returns:
this query
- #### isFacingMe

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isFacingMe()
```

Only matches characters that are facing our player

Returns:
this query
- #### minLevel

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") minLevel​(int minLevel)
```

Only matches characters who are at least the specified level

Parameters:
`minLevel` - the minimum character level to accept
Returns:
this query
- #### maxLevel

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") maxLevel​(int maxLevel)
```

Only matches characters who are at most the specific level

Parameters:
`maxLevel` - the maximum character level to accept
Returns:
this query
- #### withinCombatLevels

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") withinCombatLevels​(int within)
```

Only matches characters who are within the specified range from our player's level.

For example, within 10 levels would be accept players within the range of our player level - 10 to our player level + 10.

Parameters:
`within` - the range to accept other character combat levels from our player's combat level
Returns:
this query
- #### withinCombatLevelsBelow

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") withinCombatLevelsBelow​(int within)
```

Only matches characters who are within the specified range below our player's level.

For example within 10 levels below would be require that any player be at least our combat level - 10 or greater

Parameters:
`within` - the range to accept combat levels below our player's combat level
Returns:
this query
- #### withinCombatLevelsAbove

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") withinCombatLevelsAbove​(int within)
```

Only matches characters who are within the specified range above our player's level.

For example within 10 levels above would be require that any player be at most our combat level + 10 or less

Parameters:
`within` - the range to accept combat levels below our player's combat level
Returns:
this query
- #### isAnimating

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isAnimating()
```

Only match characters who are animating

Returns:
this query
- #### isNotAnimating

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotAnimating()
```

Only match characters who are not animating

Returns:
this query
- #### isAnimation

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isAnimation​(int... animation)
```

Only match characters with any of the specified animations

Parameters:
`animation` - the animations to check
Returns:
this query
- #### isNotAnimation

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotAnimation​(int... animation)
```

Only match characters who do not have any of the specified animations

Parameters:
`animation` - the animations to check
Returns:
this query
- #### walkingDirectionEquals

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") walkingDirectionEquals​([Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")... walkingDirection)
```
- #### walkingDirectionNotEquals

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") walkingDirectionNotEquals​([Character.WalkingDirection](../interfaces/Character.WalkingDirection.html "enum in org.tribot.script.sdk.interfaces")... walkingDirection)
```
- #### overheadMessageEquals

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") overheadMessageEquals​(java.lang.String... msg)
```
- #### overheadMessageNotEquals

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") overheadMessageNotEquals​(java.lang.String... msg)
```
- #### overheadMessageContains

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") overheadMessageContains​(java.lang.String... msg)
```
- #### overheadMessageNotContains

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") overheadMessageNotContains​(java.lang.String... msg)
```
- #### minHealthBarPercent

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") minHealthBarPercent​(double min)
```
- #### maxHealthBarPercent

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") maxHealthBarPercent​(double max)
```
- #### isHealthBarEmpty

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarEmpty()
```
- #### isHealthBarNotEmpty

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarNotEmpty()
```
- #### isHealthBarFull

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarFull()
```
- #### isHealthBarNotFull

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isHealthBarNotFull()
```
- #### isBeingInteractedWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isBeingInteractedWith()
```

Only match entities that at least one character is interacting with

Returns:
this query
- #### isNotBeingInteractedWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotBeingInteractedWith()
```

Only match entities that no character is interacting with

Returns:
this query
- #### isMyPlayerInteractingWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isMyPlayerInteractingWith()
```

Only match entities that my player is interacting with (this limits the query to 0 or 1 results)

Returns:
this query
- #### isMyPlayerNotInteractingWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isMyPlayerNotInteractingWith()
```

Only match entities that my player is interacting with

Returns:
this query
- #### isInteractingWithCharacter

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isInteractingWithCharacter()
```

Only match entities that are interacting with another character

Returns:
this query
- #### isNotInteractingWithCharacter

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotInteractingWithCharacter()
```

Only match entities that are not interacting with another character

Returns:
this query
- #### isInteractingWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isInteractingWith​([Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")... interacting)
```

Only match entities that are interacting with any of the specified entities

Parameters:
`interacting` - the characters to check against
Returns:
this query
- #### isNotInteractingWith

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") isNotInteractingWith​([Character](../interfaces/Character.html "interface in org.tribot.script.sdk.interfaces")... interacting)
```

Only match entities that are not interacting with any of the specified entities

Parameters:
`interacting` - the characters to check against
Returns:
this query
- #### hasHitsplat

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") hasHitsplat()
```

Checks if any hitsplat is present

Returns:
true if any hitsplat is present, false otherwise
- #### hasNoHitsplat

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") hasNoHitsplat()
```

Checks if no hitsplat is present

Returns:
true if no hitsplat is present
- #### hasHitsplat

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") hasHitsplat​(java.util.function.Predicate<[Hitsplat](../types/Hitsplat.html "class in org.tribot.script.sdk.types")> filter)
```

Checks if any hitsplat is present that matches the filter

Parameters:
`filter` - the hitsplat filter
Returns:
true if any hitsplat is present that matches the filter, false otherwise
- #### hasOverheadIcon

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") hasOverheadIcon()
```

Only match players who have an overhead icon

Returns:
this query
- #### overheadIconEquals

```
default [QueryType](CharacterQuery.html "type parameter in CharacterQuery") overheadIconEquals​([Player.OverheadIcon](../types/Player.OverheadIcon.html "enum in org.tribot.script.sdk.types")... overhead)
```

Only match players with the specified overhead icon

Parameters:
`overhead` - the overhead icon
Returns:
this query