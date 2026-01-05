# Geometry (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/geometry/Geometry.html

**Package:** Packagenet.runelite.api.geometry

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.geometry.Geometry

* ---

```
public class Geometry
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Geometry](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[clipPath](#clipPath(java.awt.geom.GeneralPath,java.awt.Shape))​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape)` | Removes lines from a path that lie outside the clipping area and cuts
lines intersecting with the clipping area so the resulting lines
lie within the clipping area. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[clipPath](#clipPath(java.awt.geom.PathIterator,java.awt.Shape))​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape)` | Removes lines from a path that lie outside the clipping area and cuts
lines intersecting with the clipping area so the resulting lines
lie within the clipping area. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[filterPath](#filterPath(java.awt.geom.GeneralPath,java.util.function.BiPredicate))​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[BiPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/BiPredicate.html?is-external=true "class or interface in java.util.function")<float[],​float[]> method)` | Removes lines from a path according to a method. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[filterPath](#filterPath(java.awt.geom.PathIterator,java.util.function.BiPredicate))​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[BiPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/BiPredicate.html?is-external=true "class or interface in java.util.function")<float[],​float[]> method)` | Removes lines from a path according to a method. |
| `static [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point2D.Float](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.Float.html?is-external=true "class or interface in java.awt.geom")>` | `[intersectionPoints](#intersectionPoints(java.awt.Shape,float,float,float,float))​([Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape,
float x1,
float y1,
float x2,
float y2)` | Find the intersection points between a Shape and a line. |
| `static [Point2D.Float](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.Float.html?is-external=true "class or interface in java.awt.geom")` | `[lineIntersectionPoint](#lineIntersectionPoint(float,float,float,float,float,float,float,float))​(float x1,
float y1,
float x2,
float y2,
float x3,
float y3,
float x4,
float y4)` | Find the point where two lines intersect. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[splitIntoSegments](#splitIntoSegments(java.awt.geom.GeneralPath,float))​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
float segmentLength)` | Splits a path into smaller segments. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[splitIntoSegments](#splitIntoSegments(java.awt.geom.PathIterator,float))​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
float segmentLength)` | Splits a path into smaller segments. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[transformPath](#transformPath(java.awt.geom.GeneralPath,java.util.function.Consumer))​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<float[]> method)` | Transforms the points in a path according to a method. |
| `static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom")` | `[transformPath](#transformPath(java.awt.geom.PathIterator,java.util.function.Consumer))​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<float[]> method)` | Transforms the points in a path according to a method. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### Geometry

```
public Geometry()
```

+ ### Method Detail

- #### lineIntersectionPoint

```
public static [Point2D.Float](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.Float.html?is-external=true "class or interface in java.awt.geom") lineIntersectionPoint​(float x1,
float y1,
float x2,
float y2,
float x3,
float y3,
float x4,
float y4)
```

Find the point where two lines intersect.

Parameters:
`x1` - X coordinate of the first endpoint of the first line.
`y1` - Y coordinate of the first endpoint of the first line.
`x2` - X coordinate of the second endpoint of the first line.
`y2` - Y coordinate of the second endpoint of the first line.
`x3` - X coordinate of the first endpoint of the second line.
`y3` - Y coordinate of the first endpoint of the second line.
`x4` - X coordinate of the second endpoint of the second line.
`y4` - Y coordinate of the second endpoint of the second line.
Returns:
The intersection point of the lines, or null if the lines don't intersect.
- #### intersectionPoints

```
public static [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point2D.Float](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.Float.html?is-external=true "class or interface in java.awt.geom")> intersectionPoints​([Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape,
float x1,
float y1,
float x2,
float y2)
```

Find the intersection points between a Shape and a line.

Parameters:
`shape` - The shape.
`x1` - X coordinate of the first endpoint of the line.
`y1` - Y coordinate of the first endpoint of the line.
`x2` - X coordinate of the second endpoint of the line.
`y2` - Y coordinate of the second endpoint of the line.
Returns:
A list with the intersection points.
- #### transformPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") transformPath​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<float[]> method)
```

Transforms the points in a path according to a method.

Parameters:
`it` - The iterator of the path to change the points on.
`method` - The method to use to transform the points. Takes a float[2] array with x and y coordinates as parameter.
Returns:
The transformed path.
- #### transformPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") transformPath​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<float[]> method)
```

Transforms the points in a path according to a method.

Parameters:
`path` - The path to change the points on.
`method` - The method to use to transform the points. Takes a float[2] array with x and y coordinates as parameter.
Returns:
The transformed path.
- #### splitIntoSegments

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") splitIntoSegments​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
float segmentLength)
```

Splits a path into smaller segments.
For example, calling this on a path with a line of length 6, with desired
segment length of 2, would split the path into 3 consecutive lines of length 2.

Parameters:
`it` - The iterator of the path to modify.
`segmentLength` - The desired length to use for the segments.
Returns:
The modified path.
- #### splitIntoSegments

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") splitIntoSegments​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
float segmentLength)
```

Splits a path into smaller segments.
For example, calling this on a path with a line of length 6, with desired
segment length of 2, would split the path into 3 consecutive lines of length 2.

Parameters:
`path` - The path to modify.
`segmentLength` - The desired length to use for the segments.
Returns:
The modified path.
- #### filterPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") filterPath​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[BiPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/BiPredicate.html?is-external=true "class or interface in java.util.function")<float[],​float[]> method)
```

Removes lines from a path according to a method.

Parameters:
`it` - The iterator of the path to filter.
`method` - The method to use to decide which lines to remove. Takes two float[2] arrays with x and y coordinates of the endpoints of the line. Lines for which the predicate returns false are removed.
Returns:
The filtered path.
- #### filterPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") filterPath​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[BiPredicate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/BiPredicate.html?is-external=true "class or interface in java.util.function")<float[],​float[]> method)
```

Removes lines from a path according to a method.

Parameters:
`path` - The path to filter.
`method` - The method to use to decide which lines to remove. Takes two float[2] arrays with x and y coordinates of the endpoints of the line. Lines for which the predicate returns false are removed.
Returns:
The filtered path.
- #### clipPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") clipPath​([PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") it,
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape)
```

Removes lines from a path that lie outside the clipping area and cuts
lines intersecting with the clipping area so the resulting lines
lie within the clipping area.

Parameters:
`it` - The iterator of the path to clip.
`shape` - The clipping area to clip with.
Returns:
The clipped path.
- #### clipPath

```
public static [GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") clipPath​([GeneralPath](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/GeneralPath.html?is-external=true "class or interface in java.awt.geom") path,
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") shape)
```

Removes lines from a path that lie outside the clipping area and cuts
lines intersecting with the clipping area so the resulting lines
lie within the clipping area.

Parameters:
`path` - The path to clip.
`shape` - The clipping area to clip with.
Returns:
The clipped path.