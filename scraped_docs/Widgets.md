# Widgets (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Widgets.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Widgets

* ---

```
public class Widgets
extends java.lang.Object
```

Utilities for inspecting Widgets. These make up the user interface of the game, such as the inventory tab or chatbox.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Widgets](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[closeAll](#closeAll())()` | Attempts to close all "closable" widgets. |
| `static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>` | `[find](#find(java.util.function.Predicate,int...))​(java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> filter,
int... startInterfacePath)` | Walks the tree of widget, starting with the widget provided by the given path. |
| `static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>` | `[findWhereAction](#findWhereAction(java.lang.String,int...))​(java.lang.String action,
int... startInterfacePath)` | Walks the tree of widget, starting with the interface provided by the given path. |
| `static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")>` | `[get](#get(int...))​(int... path)` | Finds the widget with the given indexes. |
| `static boolean` | `[isVisible](#isVisible(int...))​(int... indexPath)` | Checks if a widget with the specified index path is visible |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Widgets

```
public Widgets()
```

+ ### Method Detail

- #### get

```
public static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> get​(int... path)
```

Finds the widget with the given indexes.
- #### find

```
public static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> find​(java.util.function.Predicate<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> filter,
int... startInterfacePath)
```

Walks the tree of widget, starting with the widget provided by the given path.
If no path is given, it walks through all widget. The walking is done depth-first.
The first interface to match the filter is returned.
- #### findWhereAction

```
public static java.util.Optional<[Widget](types/Widget.html "class in org.tribot.script.sdk.types")> findWhereAction​(java.lang.String action,
int... startInterfacePath)
```

Walks the tree of widget, starting with the interface provided by the given path.
If no path is given, it walks through all widget. The walking is done depth-first.
The first widget who has an action equal to the given action is returned.
- #### closeAll

```
public static void closeAll()
```

Attempts to close all "closable" widgets.
- #### isVisible

```
public static boolean isVisible​(int... indexPath)
```

Checks if a widget with the specified index path is visible

Parameters:
`indexPath` - the widget index path
Returns:
true if the widget is visible, false otherwise