# WidgetAddress (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/WidgetAddress.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.WidgetAddress

* ---

```
public class WidgetAddress
extends java.lang.Object
```

Contains an "address" (the index path) for a widget to avoid avoid hardcoding the indexes.
This will dynamically resolve the widget and cache the index path. The cached index path will be used for subsequent lookups.

* + ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk")` | `[create](#create(int,java.util.function.Predicate))​(int rootIndex,
java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> componentFilter)` | Creates a widget address by searching all widgets in the specified root index with the specified predicate. |
| `static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk")` | `[create](#create(java.util.function.Predicate))​(java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> masterInterfaceFilter)` | Creates a widget address by searching all widgets with the specified predicate. |
| `static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk")` | `[create](#create(java.util.function.Supplier))​(java.util.function.Supplier<java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>> getInterfaceFunc)` | Creates a widget address using the specified supplier |
| `int[]` | `[getIndexPath](#getIndexPath())()` | Gets the index path of this address |
| `java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>` | `[lookup](#lookup())()` | Attempts to look up the widget, using the cached indexes if it exists, otherwise performs a dynamic lookup and attempts to check the widget. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### create

```
public static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk") create​(java.util.function.Supplier<java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>> getInterfaceFunc)
```

Creates a widget address using the specified supplier

Parameters:
`getInterfaceFunc` - the interface supplier
Returns:
a new widget address
See Also:
[`Query.widgets()`](query/Query.html#widgets()),
[`Query.findFirst()`](query/Query.html#findFirst())
- #### create

```
public static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk") create​(java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> masterInterfaceFilter)
```

Creates a widget address by searching all widgets with the specified predicate.
This is not recommended. You should provide a root widget to search for performance reasons (such as [`create(int, Predicate)`](#create(int,java.util.function.Predicate)).

Parameters:
`masterInterfaceFilter` - the widget predicate
Returns:
a new widget address
- #### create

```
public static [WidgetAddress](WidgetAddress.html "class in org.tribot.script.sdk") create​(int rootIndex,
java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> componentFilter)
```

Creates a widget address by searching all widgets in the specified root index with the specified predicate.

Parameters:
`rootIndex` - the widget root index to search under
`componentFilter` - the widget predicate
Returns:
a new widget address
- #### getIndexPath

```
public int[] getIndexPath()
```

Gets the index path of this address

Returns:
the widget path, or an empty array if this hasn't been cached yet
- #### lookup

```
public java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> lookup()
```

Attempts to look up the widget, using the cached indexes if it exists, otherwise performs a dynamic lookup and attempts to check the widget.

Returns:
the widget