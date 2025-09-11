# WidgetQuery (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/query/WidgetQuery.html

**Package:** Packageorg.tribot.script.sdk.query

---

* java.lang.Object
* + org.tribot.script.sdk.query.WidgetQuery

* All Implemented Interfaces:
`[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>`, `[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>`, `[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>`, `[Query](Query.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>`

---

```
public class WidgetQuery
extends java.lang.Object
implements [ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>, [ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>, [IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types"),​[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")>
```

A query to search over entities of type [`Widget`](../types/Widget.html "class in org.tribot.script.sdk.types")

See Also:
[`Query.widgets()`](Query.html#widgets())

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[animationEquals](#animationEquals(int...))​(int... animationId)` | Only match widgets whose animation id does not exactly equal any of the specified animation ids |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[animationNotEquals](#animationNotEquals(int...))​(int... animationId)` | Only match widgets whose animation id does not exactly equal any of the specified animation ids |
| `protected QueryType` | `[asQueryType](#asQueryType())()` | |
| `protected java.util.stream.Stream<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types")>` | `[createSourceStream](#createSourceStream())()` | |
| `QueryType` | `[filter](#filter(java.util.function.Predicate))​(java.util.function.Predicate<EntityType> filter)` | Applies the specified filter to this query. |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[hasChildren](#hasChildren())()` | Only match widgets who have children |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[heightEquals](#heightEquals(int...))​(int... height)` | Only match widgets whose height exactly equals one of the specified heights |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[heightNotEquals](#heightNotEquals(int...))​(int... height)` | Only match widgets whose height does not exactly equal any of the specified heights |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[inIndexPath](#inIndexPath(int...))​(int... indexPath)` | Adds the specified index path as one of the roots that will be searched. |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[inRoots](#inRoots(int...))​(int... roots)` | See how [`inIndexPath(int...)`](#inIndexPath(int...)) works - this is equivalent to: |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isAnimating](#isAnimating())()` | Only match widgets that are animating |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isDepth](#isDepth(int...))​(int... depth)` | Requires that any matching widget be of the specified depth (depth is `widget.getIndexPath().length)` |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isItem](#isItem())()` | Only matches widgets that represent an item |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isItemTable](#isItemTable())()` | Only matches widgets that represent an item table |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isNotAnimating](#isNotAnimating())()` | Only match widgets that are not animating |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[isNotDepth](#isNotDepth(int...))​(int... depth)` | Requires that any matching widget not be of the specified depth (depth is `widget.getIndexPath().length)` |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[maxHeight](#maxHeight(int))​(int height)` | Only match widgets whose height is at most the specified max height |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[maxWidth](#maxWidth(int))​(int width)` | Only match widgets whose width is at most the specified max width |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[minHeight](#minHeight(int))​(int height)` | Only match widgets whose height is at least the specified min height |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[minWidth](#minWidth(int))​(int width)` | Only match widgets whose width is at least the specified min width |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[modelIdEquals](#modelIdEquals(int...))​(int... modelId)` | Only match widgets with the specified model id |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[modelIdNotEquals](#modelIdNotEquals(int...))​(int... modelId)` | Only match widgets without the specified model id |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[nameContains](#nameContains(java.lang.String...))​(java.lang.String... name)` | Only matches widgets whose name contains any of the specified names |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[nameEquals](#nameEquals(java.lang.String...))​(java.lang.String... name)` | Only matches widgets whose name equals any of the specified names |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[nameNotContains](#nameNotContains(java.lang.String...))​(java.lang.String... name)` | Only matches widgets whose name does not contain any of the specified names |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[nameNotEquals](#nameNotEquals(java.lang.String...))​(java.lang.String... name)` | Only matches widgets whose name does not equal any of the specified names |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[positionEquals](#positionEquals(java.awt.Point...))​(java.awt.Point... p)` | Only match widgets whose position equals one of the specified points |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[positionNotEquals](#positionNotEquals(java.awt.Point...))​(java.awt.Point... p)` | Only match widgets whose position does not equal one of the specified points |
| `QueryType` | `[sorted](#sorted(java.util.Comparator))​(java.util.Comparator<EntityType> comparator)` | Orders the query by the specified comparator. |
| `java.util.stream.Stream<EntityType>` | `[stream](#stream())()` | Returns this query as a stream. |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textColorEquals](#textColorEquals(int...))​(int... color)` | Only match widgets with the specified text color |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textColorNotEquals](#textColorNotEquals(int...))​(int... color)` | Only match widgets without the specified text color |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textContains](#textContains(java.lang.String...))​(java.lang.String... text)` | Only matches widgets whose text contains any of the specified texts |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textEquals](#textEquals(java.lang.String...))​(java.lang.String... text)` | Only matches widgets whose text equals any of the specified texts |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textNotContains](#textNotContains(java.lang.String...))​(java.lang.String... text)` | Only matches widgets whose text does not contain any of the specified texts |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textNotEquals](#textNotEquals(java.lang.String...))​(java.lang.String... text)` | Only matches widgets whose text does not equal any of the specified texts |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textureIdEquals](#textureIdEquals(int...))​(int... textureId)` | Only match widgets with the specified texture id |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[textureIdNotEquals](#textureIdNotEquals(int...))​(int... textureId)` | Only match widgets without the specified texture id |
| `[WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query")` | `[toItemQuery](#toItemQuery())()` | Converts this widget query to an widget item query that will match any of the widgets
of this query, but the entity to search over is in the form of an [`Item`](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces"). |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[widthEquals](#widthEquals(int...))​(int... width)` | Only match widgets whose width exactly equals one of the specified widths |
| `[WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query")` | `[widthNotEquals](#widthNotEquals(int...))​(int... width)` | Only match widgets whose width does not exactly equal any of the specified widths |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ActionableQuery](ActionableQuery.html "interface in org.tribot.script.sdk.query")

`[actionContains](ActionableQuery.html#actionContains(java.lang.String...)), [actionEquals](ActionableQuery.html#actionEquals(java.lang.String...)), [actionNotContains](ActionableQuery.html#actionNotContains(java.lang.String...)), [actionNotEquals](ActionableQuery.html#actionNotEquals(java.lang.String...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[ClickableQuery](ClickableQuery.html "interface in org.tribot.script.sdk.query")

`[isHovering](ClickableQuery.html#isHovering()), [isNotHovering](ClickableQuery.html#isNotHovering()), [isNotVisible](ClickableQuery.html#isNotVisible()), [isVisible](ClickableQuery.html#isVisible())`
- ### Methods inherited from interface org.tribot.script.sdk.query.[IndexableQuery](IndexableQuery.html "interface in org.tribot.script.sdk.query")

`[indexEquals](IndexableQuery.html#indexEquals(int...)), [indexNotEquals](IndexableQuery.html#indexNotEquals(int...))`
- ### Methods inherited from interface org.tribot.script.sdk.query.[Query](Query.html "interface in org.tribot.script.sdk.query")

`[count](Query.html#count()), [filter](Query.html#filter(java.util.function.Predicate)), [findFirst](Query.html#findFirst()), [findRandom](Query.html#findRandom()), [forEach](Query.html#forEach(java.util.function.Consumer)), [isAny](Query.html#isAny()), [sorted](Query.html#sorted(java.util.Comparator)), [stream](Query.html#stream()), [toList](Query.html#toList())`

* + ### Method Detail

- #### createSourceStream

```
protected java.util.stream.Stream<[Widget](../types/Widget.html "class in org.tribot.script.sdk.types")> createSourceStream()
```
- #### inIndexPath

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") inIndexPath​(int... indexPath)
```

Adds the specified index path as one of the roots that will be searched.
If any index path is added, this query won't do an exhaustive search over all roots, but rather
consider the index paths given by this method (inIndexPath can be called more then once) as the roots of the search.

This can help performance because an exhaustive search can be slow due to the amount of widgets to search.
If there's a specific root index or some index path the widget is known to be under, it's recommended to supply at least the root index.

Parameters:
`indexPath` - the index path of an widget to search as a root
Returns:
this query
- #### inRoots

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") inRoots​(int... roots)
```

See how [`inIndexPath(int...)`](#inIndexPath(int...)) works - this is equivalent to:

```

for (int i : roots) {
inIndexPath(i);
}

```

Parameters:
`roots` - the widget search root indexes
Returns:
this query
See Also:
[`inIndexPath(int...)`](#inIndexPath(int...))
- #### isDepth

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isDepth​(int... depth)
```

Requires that any matching widget be of the specified depth (depth is `widget.getIndexPath().length)`

Parameters:
`depth` - the depth of the widget
Returns:
this query
- #### isNotDepth

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isNotDepth​(int... depth)
```

Requires that any matching widget not be of the specified depth (depth is `widget.getIndexPath().length)`

Parameters:
`depth` - the depth of the widget
Returns:
this query
- #### isItem

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isItem()
```

Only matches widgets that represent an item

Returns:
this query
- #### isItemTable

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isItemTable()
```

Only matches widgets that represent an item table

Returns:
this query
- #### textEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textEquals​(java.lang.String... text)
```

Only matches widgets whose text equals any of the specified texts

Parameters:
`text` - the text to check
Returns:
this query
- #### textContains

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textContains​(java.lang.String... text)
```

Only matches widgets whose text contains any of the specified texts

Parameters:
`text` - the text to check
Returns:
this query
- #### textNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textNotEquals​(java.lang.String... text)
```

Only matches widgets whose text does not equal any of the specified texts

Parameters:
`text` - the text to check
Returns:
this query
- #### textNotContains

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textNotContains​(java.lang.String... text)
```

Only matches widgets whose text does not contain any of the specified texts

Parameters:
`text` - the text to check
Returns:
this query
- #### nameEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") nameEquals​(java.lang.String... name)
```

Only matches widgets whose name equals any of the specified names

Parameters:
`name` - the name to check
Returns:
this query
- #### nameContains

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") nameContains​(java.lang.String... name)
```

Only matches widgets whose name contains any of the specified names

Parameters:
`name` - the name to check
Returns:
this query
- #### nameNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") nameNotEquals​(java.lang.String... name)
```

Only matches widgets whose name does not equal any of the specified names

Parameters:
`name` - the name to check
Returns:
this query
- #### nameNotContains

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") nameNotContains​(java.lang.String... name)
```

Only matches widgets whose name does not contain any of the specified names

Parameters:
`name` - the name to check
Returns:
this query
- #### toItemQuery

```
public [WidgetItemQuery](WidgetItemQuery.html "class in org.tribot.script.sdk.query") toItemQuery()
```

Converts this widget query to an widget item query that will match any of the widgets
of this query, but the entity to search over is in the form of an [`Item`](../interfaces/Item.html "interface in org.tribot.script.sdk.interfaces").
This will filter the widgets to make sure they are items first.

Note that when the query returned by this method is executed, this query is executed as well.

Returns:
this query as an widget item query
- #### textColorEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textColorEquals​(int... color)
```

Only match widgets with the specified text color

Parameters:
`color` - the text color
Returns:
this query
- #### textColorNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textColorNotEquals​(int... color)
```

Only match widgets without the specified text color

Parameters:
`color` - the text color
Returns:
this query
- #### textureIdEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textureIdEquals​(int... textureId)
```

Only match widgets with the specified texture id

Parameters:
`textureId` - the texture id
Returns:
this query
- #### textureIdNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") textureIdNotEquals​(int... textureId)
```

Only match widgets without the specified texture id

Parameters:
`textureId` - the texture id
Returns:
this query
- #### modelIdEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") modelIdEquals​(int... modelId)
```

Only match widgets with the specified model id

Parameters:
`modelId` - the model id
Returns:
this query
- #### modelIdNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") modelIdNotEquals​(int... modelId)
```

Only match widgets without the specified model id

Parameters:
`modelId` - the model id
Returns:
this query
- #### positionEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") positionEquals​(java.awt.Point... p)
```

Only match widgets whose position equals one of the specified points

Parameters:
`p` - the points to check
Returns:
this query
- #### positionNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") positionNotEquals​(java.awt.Point... p)
```

Only match widgets whose position does not equal one of the specified points

Parameters:
`p` - the points to check
Returns:
this query
- #### minWidth

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") minWidth​(int width)
```

Only match widgets whose width is at least the specified min width

Parameters:
`width` - the min width
Returns:
this query
- #### maxWidth

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") maxWidth​(int width)
```

Only match widgets whose width is at most the specified max width

Parameters:
`width` - the max width
Returns:
this query
- #### widthEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") widthEquals​(int... width)
```

Only match widgets whose width exactly equals one of the specified widths

Parameters:
`width` - the width to check
Returns:
this query
- #### widthNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") widthNotEquals​(int... width)
```

Only match widgets whose width does not exactly equal any of the specified widths

Parameters:
`width` - the width to check
Returns:
this query
- #### minHeight

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") minHeight​(int height)
```

Only match widgets whose height is at least the specified min height

Parameters:
`height` - the min height
Returns:
this query
- #### maxHeight

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") maxHeight​(int height)
```

Only match widgets whose height is at most the specified max height

Parameters:
`height` - the max height
Returns:
this query
- #### heightEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") heightEquals​(int... height)
```

Only match widgets whose height exactly equals one of the specified heights

Parameters:
`height` - the height to check
Returns:
this query
- #### heightNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") heightNotEquals​(int... height)
```

Only match widgets whose height does not exactly equal any of the specified heights

Parameters:
`height` - the height to check
Returns:
this query
- #### hasChildren

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") hasChildren()
```

Only match widgets who have children

Returns:
this query
- #### isAnimating

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isAnimating()
```

Only match widgets that are animating

Returns:
this query
- #### isNotAnimating

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") isNotAnimating()
```

Only match widgets that are not animating

Returns:
this query
- #### animationEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") animationEquals​(int... animationId)
```

Only match widgets whose animation id does not exactly equal any of the specified animation ids

Parameters:
`animationId` - the animation ids to check
Returns:
this query
- #### animationNotEquals

```
public [WidgetQuery](WidgetQuery.html "class in org.tribot.script.sdk.query") animationNotEquals​(int... animationId)
```

Only match widgets whose animation id does not exactly equal any of the specified animation ids

Parameters:
`animationId` - the animation ids to check
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