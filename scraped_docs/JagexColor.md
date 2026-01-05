# JagexColor (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/JagexColor.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.JagexColor

* ---

```
public final class JagexColor
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[HUE\_MAX](#HUE_MAX)` | |
| `static int` | `[LUMINANCE\_MAX](#LUMINANCE_MAX)` | |
| `static int` | `[SATURATION\_MAX](#SATURATION_MAX)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[JagexColor](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[formatHSL](#formatHSL(short))​(short hsl)` | |
| `static short` | `[packHSL](#packHSL(int,int,int))​(int hue,
int saturation,
int luminance)` | |
| `static short` | `[rgbToHSL](#rgbToHSL(int,double))​(int rgb,
double brightness)` | |
| `static int` | `[unpackHue](#unpackHue(short))​(short hsl)` | |
| `static int` | `[unpackLuminance](#unpackLuminance(short))​(short hsl)` | |
| `static int` | `[unpackSaturation](#unpackSaturation(short))​(short hsl)` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### HUE\_MAX

```
public static final int HUE_MAX
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.JagexColor.HUE_MAX)
- #### SATURATION\_MAX

```
public static final int SATURATION_MAX
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.JagexColor.SATURATION_MAX)
- #### LUMINANCE\_MAX

```
public static final int LUMINANCE_MAX
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.JagexColor.LUMINANCE_MAX)

+ ### Constructor Detail

- #### JagexColor

```
public JagexColor()
```

+ ### Method Detail

- #### packHSL

```
public static short packHSL​(int hue,
int saturation,
int luminance)
```
- #### unpackHue

```
public static int unpackHue​(short hsl)
```
- #### unpackSaturation

```
public static int unpackSaturation​(short hsl)
```
- #### unpackLuminance

```
public static int unpackLuminance​(short hsl)
```
- #### formatHSL

```
public static [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") formatHSL​(short hsl)
```
- #### rgbToHSL

```
public static short rgbToHSL​(int rgb,
double brightness)
```