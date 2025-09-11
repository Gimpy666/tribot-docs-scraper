# ItemDefinitionQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/ItemDefinitionQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.ItemDefinitionQuery

* All Implemented Interfaces:
`[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>`, `[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class ItemDefinitionQuery
extends java.lang.Object
implements [Query](Query.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>, [IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>, [NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over item definitions

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[idEquals](#idEquals(int...))​(int... id)` | Only match entities with the specified id |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isBankable](#isBankable())()` | Deprecated. |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isGrandExchangeTradeable](#isGrandExchangeTradeable())()` | Only match items that can be traded on the grand exchange |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isMembersOnly](#isMembersOnly())()` | Only match items that are members only |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotBankable](#isNotBankable())()` | Deprecated. |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNoted](#isNoted())()` | Only match items that are noted |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotGrandExchangeTradeable](#isNotGrandExchangeTradeable())()` | Only match items that cannot be traded on the grand exchange |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotMembersOnly](#isNotMembersOnly())()` | Only match items that are not members only |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotNoted](#isNotNoted())()` | Only match items that are not noted |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotPlaceholder](#isNotPlaceholder())()` | Only match items that are not placeholder |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isNotStackable](#isNotStackable())()` | Only match items that are not stackable |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isPlaceholder](#isPlaceholder())()` | Only match items that are placeholder |
| `[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")` | `[isStackable](#isStackable())()` | Only match items that are stackable |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")

`[distinctById](IdentifiableQuery.html#distinctById()), [idNotEquals](IdentifiableQuery.html#idNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[NamedQuery](NamedQuery.html "interface in org.tribot.script.sdk.query")

`[distinctByName](NamedQuery.html#distinctByName()), [nameContains](NamedQuery.html#nameContains(java.lang.String...)), [nameEquals](NamedQuery.html#nameEquals(java.lang.String...)), [nameNotContains](NamedQuery.html#nameNotContains(java.lang.String...)), [nameNotEquals](NamedQuery.html#nameNotEquals(java.lang.String...)), [nameNotStartsWith](NamedQuery.html#nameNotStartsWith(java.lang.String...)), [nameStartsWith](NamedQuery.html#nameStartsWith(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")> createSourceStream()
```
- #### idEquals

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") idEquals​(int... id)
```

Description copied from interface: `[IdentifiableQuery](IdentifiableQuery.html#idEquals(int...))`
Only match entities with the specified id

Specified by:
`[idEquals](IdentifiableQuery.html#idEquals(int...))` in interface `[IdentifiableQuery](IdentifiableQuery.html "interface in org.tribot.script.sdk.query")<[ItemDefinition](../types/definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions"),​[ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query")>`
Parameters:
`id` - the id to check
Returns:
this query
- #### isMembersOnly

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isMembersOnly()
```

Only match items that are members only

Returns:
this query
- #### isNotMembersOnly

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotMembersOnly()
```

Only match items that are not members only

Returns:
this query
- #### isStackable

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isStackable()
```

Only match items that are stackable

Returns:
this query
- #### isNotStackable

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotStackable()
```

Only match items that are not stackable

Returns:
this query
- #### isNoted

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNoted()
```

Only match items that are noted

Returns:
this query
- #### isNotNoted

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotNoted()
```

Only match items that are not noted

Returns:
this query
- #### isBankable

```
@Deprecated
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isBankable()
```

Deprecated.
Only match items that are bankable

Returns:
this query
- #### isNotBankable

```
@Deprecated
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotBankable()
```

Deprecated.
Only match items that are not bankable

Returns:
this query
- #### isGrandExchangeTradeable

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isGrandExchangeTradeable()
```

Only match items that can be traded on the grand exchange

Returns:
this query
- #### isNotGrandExchangeTradeable

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotGrandExchangeTradeable()
```

Only match items that cannot be traded on the grand exchange

Returns:
this query
- #### isPlaceholder

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isPlaceholder()
```

Only match items that are placeholder

Returns:
this query
- #### isNotPlaceholder

```
public [ItemDefinitionQuery](ItemDefinitionQuery.html "class in org.tribot.script.sdk.query") isNotPlaceholder()
```

Only match items that are not placeholder

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