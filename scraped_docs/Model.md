# Model (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/Model.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.Model

* ---

```
public class Model
extends java.lang.Object
```

Represents an entity model viewable on the game screen, such as a player or game object

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Model](#%3Cinit%3E(org.tribot.api2007.types.RSModel))​(org.tribot.api2007.types.RSModel model)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `java.util.Optional<java.awt.Polygon>` | `[getBounds](#getBounds())()` | Gets the polygon model bounds on the game screen |
| `int` | `[getBoundsArea](#getBoundsArea())()` | Gets the total area of this model |
| `java.util.Optional<java.awt.Point>` | `[getCenterPoint](#getCenterPoint())()` | Gets the center point of this model |
| `java.util.Optional<java.awt.Shape>` | `[getClickArea](#getClickArea())()` | Gets the click area of this model. |
| `int` | `[getIndexCount](#getIndexCount())()` | Gets the number of indices in the model |
| `java.util.List<java.awt.Point>` | `[getPoints](#getPoints())()` | Gets the points in this model |
| `int` | `[getVertexCount](#getVertexCount())()` | Gets the number of vertices in the model |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

- #### Model

```
public Model​(org.tribot.api2007.types.RSModel model)
```

+ ### Method Detail

- #### getBounds

```
public java.util.Optional<java.awt.Polygon> getBounds()
```

Gets the polygon model bounds on the game screen

Returns:
the polygon model bounds on the game screen
- #### getClickArea

```
public java.util.Optional<java.awt.Shape> getClickArea()
```

Gets the click area of this model. This click area is where the mouse can move to for a menu action to be added for this entity.

Returns:
the click area of this model
- #### getPoints

```
public java.util.List<java.awt.Point> getPoints()
```

Gets the points in this model

Returns:
the points in this model
- #### getCenterPoint

```
public java.util.Optional<java.awt.Point> getCenterPoint()
```

Gets the center point of this model

Returns:
the center point of this model
- #### getIndexCount

```
public int getIndexCount()
```

Gets the number of indices in the model

Returns:
the number of indices in the model
- #### getVertexCount

```
public int getVertexCount()
```

Gets the number of vertices in the model

Returns:
the number of vertices in the model
- #### getBoundsArea

```
public int getBoundsArea()
```

Gets the total area of this model

Returns:
the total area of this model
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`