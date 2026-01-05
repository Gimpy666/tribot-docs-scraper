# WidgetSizeMode (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/WidgetSizeMode.html

**Package:** Packagenet.runelite.api.widgets

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.widgets.WidgetSizeMode

* ---

```
public final class WidgetSizeMode
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[ABSOLUTE](#ABSOLUTE)` | dim = originalDim |
| `static int` | `[ABSOLUTE\_16384THS](#ABSOLUTE_16384THS)` | dim = parentDim \* (originalDim / 16384) |
| `static int` | `[MINUS](#MINUS)` | dim = parentDim - originalDim |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[WidgetSizeMode](#%3Cinit%3E())()` | |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### ABSOLUTE

```
public static final int ABSOLUTE
```

dim = originalDim

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetSizeMode.ABSOLUTE)
- #### MINUS

```
public static final int MINUS
```

dim = parentDim - originalDim

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetSizeMode.MINUS)
- #### ABSOLUTE\_16384THS

```
public static final int ABSOLUTE_16384THS
```

dim = parentDim \* (originalDim / 16384)

See Also:
[Constant Field Values](../../../../constant-values.html#net.runelite.api.widgets.WidgetSizeMode.ABSOLUTE_16384THS)

+ ### Constructor Detail

- #### WidgetSizeMode

```
public WidgetSizeMode()
```