# Painting (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/Painting.html

**Package:** Packageorg.tribot.script.sdk.painting

---

* java.lang.Object
* + org.tribot.script.sdk.painting.Painting

* ---

```
public class Painting
extends java.lang.Object
```

Utilities for painting over the game screen

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Painting](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static void` | `[addPaint](#addPaint(java.util.function.Consumer))​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)` | Adds a paint listener to draw on the canvas |
| `static void` | `[clearPaint](#clearPaint())()` | Removes all paint listeners |
| `static void` | `[removePaint](#removePaint(java.util.function.Consumer))​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)` | Removes a paint listener |
| `static void` | `[setMousePaint](#setMousePaint(org.tribot.script.sdk.painting.MousePaint))​([MousePaint](MousePaint.html "interface in org.tribot.script.sdk.painting") mousePaint)` | Sets the mouse paint function for the script to draw on the OSRS canvas based on mouse position |
| `static void` | `[setMouseSplinePaint](#setMouseSplinePaint(org.tribot.script.sdk.painting.MouseSplinePaint))​([MouseSplinePaint](MouseSplinePaint.html "interface in org.tribot.script.sdk.painting") mouseSplinePaint)` | Sets the mouse paint function for the script to draw on the OSRS canvas based on mouse spline |
| `static void` | `[setPaint](#setPaint(java.util.function.Consumer))​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)` | Deprecated.
see [`addPaint(Consumer)`](#addPaint(java.util.function.Consumer))
|

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Painting

```
public Painting()
```

+ ### Method Detail

- #### setPaint

```
@Deprecated
public static void setPaint​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)
```

Deprecated.
see [`addPaint(Consumer)`](#addPaint(java.util.function.Consumer))

Sets the paint function for the script to draw on the OSRS canvas.

Parameters:
`graphicsConsumer` - A consumer meant to draw on the Graphics object.
- #### addPaint

```
public static void addPaint​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)
```

Adds a paint listener to draw on the canvas

Parameters:
`graphicsConsumer` - A consumer meant to draw on the Graphics object.
- #### clearPaint

```
public static void clearPaint()
```

Removes all paint listeners
- #### removePaint

```
public static void removePaint​(java.util.function.Consumer<java.awt.Graphics2D> graphicsConsumer)
```

Removes a paint listener

Parameters:
`graphicsConsumer` - A consumer that was used to draw on the Graphics object.
- #### setMousePaint

```
public static void setMousePaint​([MousePaint](MousePaint.html "interface in org.tribot.script.sdk.painting") mousePaint)
```

Sets the mouse paint function for the script to draw on the OSRS canvas based on mouse position
- #### setMouseSplinePaint

```
public static void setMouseSplinePaint​([MouseSplinePaint](MouseSplinePaint.html "interface in org.tribot.script.sdk.painting") mouseSplinePaint)
```

Sets the mouse paint function for the script to draw on the OSRS canvas based on mouse spline