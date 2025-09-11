# Mouse (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Mouse.html

**Package:** Packageorg.tribot.script.sdk.input

---

* java.lang.Object
* + org.tribot.script.sdk.input.Mouse

* ---

```
public class Mouse
extends java.lang.Object
```

Utilities related to the virtual mouse.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")` | Represents an entity clicking method |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Mouse](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input")` | `[getClickMethod](#getClickMethod())()` | Gets the set click method. |
| `static int` | `[getSpeed](#getSpeed())()` | Gets the set mouse speed. |
| `static boolean` | `[isOnScreen](#isOnScreen())()` | Determines if the mouse is on screen or not. |
| `static void` | `[leaveScreen](#leaveScreen())()` | Makes the mouse move offscreen. |
| `static void` | `[setClickMethod](#setClickMethod(org.tribot.script.sdk.input.Mouse.ClickMethod))​([Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") clickMethod)` | Sets the click method. |
| `static void` | `[setSpeed](#setSpeed(int))​(int speed)` | Sets the mouse speed. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Mouse

```
public Mouse()
```

+ ### Method Detail

- #### isOnScreen

```
public static boolean isOnScreen()
```

Determines if the mouse is on screen or not.

Returns:
True if on screen. False otherwise.
- #### leaveScreen

```
public static void leaveScreen()
```

Makes the mouse move offscreen.
- #### getSpeed

```
public static int getSpeed()
```

Gets the set mouse speed. Default is 100. Higher number means faster mouse.
- #### setSpeed

```
public static void setSpeed​(int speed)
```

Sets the mouse speed. Default is 100. Higher number means faster mouse.
- #### getClickMethod

```
public static [Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") getClickMethod()
```

Gets the set click method.
- #### setClickMethod

```
public static void setClickMethod​([Mouse.ClickMethod](Mouse.ClickMethod.html "enum in org.tribot.script.sdk.input") clickMethod)
```

Sets the click method.

Parameters:
`clickMethod` - The method to use for clicking.