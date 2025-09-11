# Screenshot (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Screenshot.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Screenshot

* ---

```
public class Screenshot
extends java.lang.Object
```

Utility methods for taking screenshots of the game

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Screenshot](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.awt.image.BufferedImage` | `[capture](#capture())()` | Obtains an image of the current game screen, without script paint included |
| `static java.awt.image.BufferedImage` | `[captureWithPaint](#captureWithPaint())()` | Obtains an image of the current game screen, with script paint included |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Screenshot

```
public Screenshot()
```

+ ### Method Detail

- #### capture

```
public static java.awt.image.BufferedImage capture()
```

Obtains an image of the current game screen, without script paint included

Returns:
a buffered image of the game screen
- #### captureWithPaint

```
public static java.awt.image.BufferedImage captureWithPaint()
```

Obtains an image of the current game screen, with script paint included

Returns:
a buffered image of the game screen, with script paint included