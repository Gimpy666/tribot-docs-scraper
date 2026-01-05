# Jarvis (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/model/Jarvis.html

**Package:** Packagenet.runelite.api.model

**Description:** The implementation uses the Jarvis march algorithm and runs in O(nh)
 time in the worst case, where n is the number of points and h the
 number of points on the convex hull....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.model.Jarvis

* ---

```
public class Jarvis
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Provides utility methods for computing the convex hull of a list of
*n* points.

The implementation uses the Jarvis march algorithm and runs in O(nh)
time in the worst case, where n is the number of points and h the
number of points on the convex hull.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Jarvis](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static [SimplePolygon](../geometry/SimplePolygon.html "class in net.runelite.api.geometry")` | `[convexHull](#convexHull(int%5B%5D,int%5B%5D))​(int[] xs,
int[] ys)` | Computes and returns the convex hull of the passed points. |
| `static [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")>` | `[convexHull](#convexHull(java.util.List))​([List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")> points)` | Deprecated. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### Jarvis

```
public Jarvis()
```

+ ### Method Detail

- #### convexHull

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")> convexHull​([List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")> points)
```

Deprecated.
Computes and returns the convex hull of the passed points.

The size of the list must be at least 3, otherwise this method will
return null.

Parameters:
`points` - list of points
Returns:
list containing the points part of the convex hull
- #### convexHull

```
public static [SimplePolygon](../geometry/SimplePolygon.html "class in net.runelite.api.geometry") convexHull​(int[] xs,
int[] ys)
```

Computes and returns the convex hull of the passed points.

The size of the list must be at least 3, otherwise this method will
return null.

Returns:
a shape the points part of the convex hull