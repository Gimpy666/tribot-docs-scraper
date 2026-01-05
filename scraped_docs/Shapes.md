# Shapes (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/geometry/Shapes.html

**Package:** Packagenet.runelite.api.geometry

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.geometry.Shapes<T>

* All Implemented Interfaces:
`[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`

---

```
public class Shapes<T extends [Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")>
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
implements [Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Shapes](#%3Cinit%3E(java.util.List))​([List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[T](Shapes.html "type parameter in Shapes")> shapes)` | |
| `[Shapes](#%3Cinit%3E(T...))​([T](Shapes.html "type parameter in Shapes")... shape)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[contains](#contains(double,double))​(double x,
double y)` | |
| `boolean` | `[contains](#contains(double,double,double,double))​(double x,
double y,
double w,
double h)` | |
| `boolean` | `[contains](#contains(java.awt.geom.Point2D))​([Point2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.html?is-external=true "class or interface in java.awt.geom") p)` | |
| `boolean` | `[contains](#contains(java.awt.geom.Rectangle2D))​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)` | |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getBounds](#getBounds())()` | |
| `[Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom")` | `[getBounds2D](#getBounds2D())()` | |
| `[PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom")` | `[getPathIterator](#getPathIterator(java.awt.geom.AffineTransform))​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at)` | |
| `[PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom")` | `[getPathIterator](#getPathIterator(java.awt.geom.AffineTransform,double))​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at,
double flatness)` | |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[T](Shapes.html "type parameter in Shapes")>` | `[getShapes](#getShapes())()` | |
| `boolean` | `[intersects](#intersects(double,double,double,double))​(double x,
double y,
double w,
double h)` | |
| `boolean` | `[intersects](#intersects(java.awt.geom.Rectangle2D))​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### Shapes

```
public Shapes​([T](Shapes.html "type parameter in Shapes")... shape)
```
- #### Shapes

```
public Shapes​([List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[T](Shapes.html "type parameter in Shapes")> shapes)
```

+ ### Method Detail

- #### getBounds

```
public [Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt") getBounds()
```

Specified by:
`[getBounds](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#getBounds() "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### getBounds2D

```
public [Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") getBounds2D()
```

Specified by:
`[getBounds2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#getBounds2D() "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### contains

```
public boolean contains​(double x,
double y)
```

Specified by:
`[contains](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#contains(double,double) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### contains

```
public boolean contains​([Point2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.html?is-external=true "class or interface in java.awt.geom") p)
```

Specified by:
`[contains](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#contains(java.awt.geom.Point2D) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### intersects

```
public boolean intersects​(double x,
double y,
double w,
double h)
```

Specified by:
`[intersects](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#intersects(double,double,double,double) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### intersects

```
public boolean intersects​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)
```

Specified by:
`[intersects](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#intersects(java.awt.geom.Rectangle2D) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### contains

```
public boolean contains​(double x,
double y,
double w,
double h)
```

Specified by:
`[contains](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#contains(double,double,double,double) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### contains

```
public boolean contains​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)
```

Specified by:
`[contains](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#contains(java.awt.geom.Rectangle2D) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### getPathIterator

```
public [PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") getPathIterator​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at)
```

Specified by:
`[getPathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#getPathIterator(java.awt.geom.AffineTransform) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### getPathIterator

```
public [PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom") getPathIterator​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at,
double flatness)
```

Specified by:
`[getPathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true#getPathIterator(java.awt.geom.AffineTransform,double) "class or interface in java.awt")` in interface `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`
- #### getShapes

```
public [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[T](Shapes.html "type parameter in Shapes")> getShapes()
```