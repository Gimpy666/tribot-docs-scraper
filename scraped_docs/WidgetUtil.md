# WidgetUtil (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/WidgetUtil.html

**Package:** Packagenet.runelite.api.widgets

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.widgets.WidgetUtil

* ---

```
public class WidgetUtil
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[WidgetUtil](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[componentToId](#componentToId(int))​(int c)` | Utility method that converts a component id to the id it is within
its interface. |
| `static int` | `[componentToInterface](#componentToInterface(int))​(int c)` | Utility method that converts a component id to the interface it
belongs to. |
| `static int` | `[packComponentId](#packComponentId(int,int))​(int interfaceId,
int childId)` | Utility method that packs a component id from an interface id and child id. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### WidgetUtil

```
public WidgetUtil()
```

+ ### Method Detail

- #### componentToInterface

```
[@Interface](../annotations/Interface.html "annotation in net.runelite.api.annotations")
public static int componentToInterface​([@Component](../annotations/Component.html "annotation in net.runelite.api.annotations")
int c)
```

Utility method that converts a component id to the interface it
belongs to.

Parameters:
`c` - component id
Returns:
the interface id
- #### componentToId

```
public static int componentToId​([@Component](../annotations/Component.html "annotation in net.runelite.api.annotations")
int c)
```

Utility method that converts a component id to the id it is within
its interface.

Parameters:
`c` - component id
- #### packComponentId

```
[@Component](../annotations/Component.html "annotation in net.runelite.api.annotations")
public static int packComponentId​([@Interface](../annotations/Interface.html "annotation in net.runelite.api.annotations")
int interfaceId,
int childId)
```

Utility method that packs a component id from an interface id and child id.

Parameters:
`interfaceId` - interface id
`childId` - id within the interface
Returns:
the component id