# SimplePolygon (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/geometry/SimplePolygon.html

**Package:** Packagenet.runelite.api.geometry

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.geometry.SimplePolygon

* All Implemented Interfaces:
`[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")`

---

```
public class SimplePolygon
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
implements [Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")
```

A simple list of vertices that can be append or prepended to

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `protected int` | `[left](#left)` | |
| `protected int` | `[right](#right)` | |
| `protected int[]` | `[x](#x)` | |
| `protected int[]` | `[y](#y)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[SimplePolygon](#%3Cinit%3E())()` | |
| `[SimplePolygon](#%3Cinit%3E(int%5B%5D,int%5B%5D,int))​(int[] x,
int[] y,
int length)` | |
| `[SimplePolygon](#%3Cinit%3E(int%5B%5D,int%5B%5D,int,int))​(int[] x,
int[] y,
int left,
int right)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `void` | `[appendTo](#appendTo(net.runelite.api.geometry.SimplePolygon))​([SimplePolygon](SimplePolygon.html "class in net.runelite.api.geometry") other)` | |
| `boolean` | `[contains](#contains(double,double))​(double cx,
double cy)` | |
| `boolean` | `[contains](#contains(double,double,double,double))​(double x,
double y,
double w,
double h)` | |
| `boolean` | `[contains](#contains(java.awt.geom.Point2D))​([Point2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Point2D.html?is-external=true "class or interface in java.awt.geom") p)` | |
| `boolean` | `[contains](#contains(java.awt.geom.Rectangle2D))​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)` | |
| `void` | `[copyTo](#copyTo(int%5B%5D,int%5B%5D,int))​(int[] xDest,
int[] yDest,
int offset)` | |
| `protected void` | `[expandLeft](#expandLeft(int))​(int grow)` | |
| `protected void` | `[expandRight](#expandRight(int))​(int grow)` | |
| `[Rectangle](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Rectangle.html?is-external=true "class or interface in java.awt")` | `[getBounds](#getBounds())()` | |
| `[Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom")` | `[getBounds2D](#getBounds2D())()` | |
| `int` | `[getLeft](#getLeft())()` | |
| `[PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom")` | `[getPathIterator](#getPathIterator(java.awt.geom.AffineTransform))​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at)` | |
| `[PathIterator](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/PathIterator.html?is-external=true "class or interface in java.awt.geom")` | `[getPathIterator](#getPathIterator(java.awt.geom.AffineTransform,double))​([AffineTransform](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/AffineTransform.html?is-external=true "class or interface in java.awt.geom") at,
double flatness)` | |
| `int` | `[getRight](#getRight())()` | |
| `int[]` | `[getX](#getX())()` | |
| `int` | `[getX](#getX(int))​(int index)` | |
| `int[]` | `[getY](#getY())()` | |
| `int` | `[getY](#getY(int))​(int index)` | |
| `boolean` | `[intersects](#intersects(double,double,double,double))​(double x0,
double y0,
double w,
double h)` | |
| `boolean` | `[intersects](#intersects(java.awt.geom.Rectangle2D))​([Rectangle2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/geom/Rectangle2D.html?is-external=true "class or interface in java.awt.geom") r)` | |
| `void` | `[intersectWithConvex](#intersectWithConvex(net.runelite.api.geometry.SimplePolygon))​([SimplePolygon](SimplePolygon.html "class in net.runelite.api.geometry") convex)` | Clips the polygon with the passed convex polygon |
| `void` | `[popLeft](#popLeft())()` | |
| `void` | `[popRight](#popRight())()` | |
| `void` | `[pushLeft](#pushLeft(int,int))​(int xCoord,
int yCoord)` | |
| `void` | `[pushRight](#pushRight(int,int))​(int xCoord,
int yCoord)` | |
| `void` | `[reverse](#reverse())()` | |
| `void` | `[setLeft](#setLeft(int))​(int left)` | |
| `void` | `[setRight](#setRight(int))​(int right)` | |
| `void` | `[setX](#setX(int%5B%5D))​(int[] x)` | |
| `void` | `[setY](#setY(int%5B%5D))​(int[] y)` | |
| `int` | `[size](#size())()` | |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")>` | `[toRuneLitePointList](#toRuneLitePointList())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### x

```
protected int[] x
```
- #### y

```
protected int[] y
```
- #### left

```
protected int left
```
- #### right

```
protected int right
```

+ ### Constructor Detail

- #### SimplePolygon

```
public SimplePolygon()
```
- #### SimplePolygon

```
public SimplePolygon​(int[] x,
int[] y,
int length)
```
- #### SimplePolygon

```
public SimplePolygon​(int[] x,
int[] y,
int left,
int right)
```

+ ### Method Detail

- #### pushLeft

```
public void pushLeft​(int xCoord,
int yCoord)
```
- #### popLeft

```
public void popLeft()
```
- #### expandLeft

```
protected void expandLeft​(int grow)
```
- #### pushRight

```
public void pushRight​(int xCoord,
int yCoord)
```
- #### popRight

```
public void popRight()
```
- #### expandRight

```
protected void expandRight​(int grow)
```
- #### getX

```
public int getX​(int index)
```
- #### getY

```
public int getY​(int index)
```
- #### size

```
public int size()
```
- #### toRuneLitePointList

```
public [List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[Point](../Point.html "class in net.runelite.api")> toRuneLitePointList()
```
- #### copyTo

```
public void copyTo​(int[] xDest,
int[] yDest,
int offset)
```
- #### appendTo

```
public void appendTo​([SimplePolygon](SimplePolygon.html "class in net.runelite.api.geometry") other)
```
- #### reverse

```
public void reverse()
```
- #### intersectWithConvex

```
public void intersectWithConvex​([SimplePolygon](SimplePolygon.html "class in net.runelite.api.geometry") convex)
```

Clips the polygon with the passed convex polygon
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
public boolean contains​(double cx,
double cy)
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
public boolean intersects​(double x0,
double y0,
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
- #### getX

```
public int[] getX()
```
- #### getY

```
public int[] getY()
```
- #### getLeft

```
public int getLeft()
```
- #### getRight

```
public int getRight()
```
- #### setX

```
public void setX​(int[] x)
```
- #### setY

```
public void setY​(int[] y)
```
- #### setLeft

```
public void setLeft​(int left)
```
- #### setRight

```
public void setRight​(int right)
```