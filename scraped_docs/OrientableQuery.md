# OrientableQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/OrientableQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* All Superinterfaces:
`[Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Subinterfaces:
`[CharacterQuery](CharacterQuery.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>`

All Known Implementing Classes:
`[GameObjectQuery](GameObjectQuery.html "class in org.tribot.script.sdk.query")`, `[NpcQuery](NpcQuery.html "class in org.tribot.script.sdk.query")`, `[PlayerQuery](PlayerQuery.html "class in org.tribot.script.sdk.query")`

---

```
public interface OrientableQuery<EntityType extends [Orientable](../interfaces/Orientable.html "interface in org.tribot.script.sdk.interfaces"),​QueryType extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>>
extends [Query](Query.html "interface in org.tribot.script.sdk.query")<EntityType,​QueryType>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default [QueryType](OrientableQuery.html "type parameter in OrientableQuery")` | `[orientationEquals](#orientationEquals(org.tribot.script.sdk.interfaces.Orientable.Orientation...))​([Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")... orientations)` | Only matches entities with the specified orientation |
| `default [QueryType](OrientableQuery.html "type parameter in OrientableQuery")` | `[orientationNotEquals](#orientationNotEquals(org.tribot.script.sdk.interfaces.Orientable.Orientation...))​([Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")... orientations)` | Only matches entities that don't have the specified orientation |

- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### orientationEquals

```
default [QueryType](OrientableQuery.html "type parameter in OrientableQuery") orientationEquals​([Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")... orientations)
```

Only matches entities with the specified orientation

Parameters:
`orientations` - the orientations to check if this entity has
Returns:
this query
- #### orientationNotEquals

```
default [QueryType](OrientableQuery.html "type parameter in OrientableQuery") orientationNotEquals​([Orientable.Orientation](../interfaces/Orientable.Orientation.html "class in org.tribot.script.sdk.interfaces")... orientations)
```

Only matches entities that don't have the specified orientation

Parameters:
`orientations` - the orientations to check if this entity has
Returns:
this query