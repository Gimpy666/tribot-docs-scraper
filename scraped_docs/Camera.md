# Camera (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Camera.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Camera

* ---

```
public class Camera
extends java.lang.Object
```

Utilities for controlling the camera in game.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")` | A rotation method for moving the camera |
| `static class` | `[Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Camera](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getAngle](#getAngle())()` | Gets the camera angle. |
| `static int` | `[getRotation](#getRotation())()` | Gets the camera rotation, in degrees. |
| `static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")` | `[getRotationMethod](#getRotationMethod())()` | Gets the camera rotation method |
| `static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")` | `[getZoomMethod](#getZoomMethod())()` | Gets the camera zoom method to use when calling [`setZoomPercent(double)`](#setZoomPercent(double)). |
| `static double` | `[getZoomPercent](#getZoomPercent())()` | Gets the level of zoom the camera is in. |
| `static boolean` | `[resetZoomPercent](#resetZoomPercent())()` | Resets the zoom percent by clicking the 'Restore Default Zoom' action in the options tab |
| `static void` | `[setAngle](#setAngle(int))​(int angle)` | Sets the camera angle. |
| `static void` | `[setRotation](#setRotation(int))​(int degrees)` | Sets the camera rotation to the specified degrees. |
| `static void` | `[setRotationMethod](#setRotationMethod(org.tribot.script.sdk.Camera.RotationMethod))​([Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") method)` | Sets the rotation method |
| `static void` | `[setZoomMethod](#setZoomMethod(org.tribot.script.sdk.Camera.ZoomMethod))​([Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") zoomMethod)` | Sets the camera zoom method to use when calling [`setZoomPercent(double)`](#setZoomPercent(double)) |
| `static boolean` | `[setZoomPercent](#setZoomPercent(double))​(double zoomPercent)` | Attempts to set the camera zoom within the options tab. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Camera

```
public Camera()
```

+ ### Method Detail

- #### setRotationMethod

```
public static void setRotationMethod​([Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") method)
```

Sets the rotation method

Parameters:
`method` - the camera rotation method
- #### getRotationMethod

```
public static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") getRotationMethod()
```

Gets the camera rotation method

Returns:
the camera rotation method
- #### getZoomMethod

```
public static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") getZoomMethod()
```

Gets the camera zoom method to use when calling [`setZoomPercent(double)`](#setZoomPercent(double)).
Default is randomly based on a player preference generated through [`PlayerPreferences`](antiban/PlayerPreferences.html "class in org.tribot.script.sdk.antiban").

Returns:
the [`Camera.ZoomMethod`](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")
- #### setZoomMethod

```
public static void setZoomMethod​([Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") zoomMethod)
```

Sets the camera zoom method to use when calling [`setZoomPercent(double)`](#setZoomPercent(double))

Parameters:
`zoomMethod` - the [`Camera.ZoomMethod`](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")
- #### getZoomPercent

```
public static double getZoomPercent()
```

Gets the level of zoom the camera is in.

Returns:
The zoom level percentage (0.0 - 100.0)
- #### setZoomPercent

```
public static boolean setZoomPercent​(double zoomPercent)
```

Attempts to set the camera zoom within the options tab.
Note that this will set the zoom percent to roughly the specified zoom percent, it may not be exact

Parameters:
`zoomPercent` - the camera zoom percent (0.0 - 100.0)
Returns:
true if the zoom was set successfully, false otherwise
- #### resetZoomPercent

```
public static boolean resetZoomPercent()
```

Resets the zoom percent by clicking the 'Restore Default Zoom' action in the options tab

Returns:
true if the zoom was reset successfully, false otherwise
- #### getRotation

```
public static int getRotation()
```

Gets the camera rotation, in degrees.

Returns:
The rotation (0 - 360)
- #### setRotation

```
public static void setRotation​(int degrees)
```

Sets the camera rotation to the specified degrees.

Parameters:
`degrees` - The degrees in rotation.
- #### getAngle

```
public static int getAngle()
```

Gets the camera angle.

Returns:
The angle (0 - 100)
- #### setAngle

```
public static void setAngle​(int angle)
```

Sets the camera angle.

Parameters:
`angle` - The angle to set the camera to (0 - 100).