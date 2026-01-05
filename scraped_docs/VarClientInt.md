# VarClientInt (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/VarClientInt.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.VarClientInt

* ---

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public final class VarClientInt
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Deprecated.
Use `VarClientID`

Client side only, content-developer integers

VarCInts are stored entirely in memory, or locally on a user's
machine in the preferences2.dat file depending on how Jagex
configured the variable

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[BANK\_SCROLL](#BANK_SCROLL)` | Deprecated. |
| `static int` | `[BLOCK\_KEYPRESS](#BLOCK_KEYPRESS)` | Deprecated.
time to block keypresses til |
| `static int` | `[CAMERA\_ZOOM\_FIXED\_VIEWPORT](#CAMERA_ZOOM_FIXED_VIEWPORT)` | Deprecated.
The game sets this to the same value as [`CAMERA_ZOOM_RESIZABLE_VIEWPORT`](#CAMERA_ZOOM_RESIZABLE_VIEWPORT) |
| `static int` | `[CAMERA\_ZOOM\_RESIZABLE\_VIEWPORT](#CAMERA_ZOOM_RESIZABLE_VIEWPORT)` | Deprecated. |
| `static int` | `[INPUT\_TYPE](#INPUT_TYPE)` | Deprecated.
Current message layer mode |
| `static int` | `[INVENTORY\_TAB](#INVENTORY_TAB)` | Deprecated. |
| `static int` | `[MEMBERSHIP\_STATUS](#MEMBERSHIP_STATUS)` | Deprecated. |
| `static int` | `[TOOLTIP\_TIMEOUT](#TOOLTIP_TIMEOUT)` | Deprecated. |
| `static int` | `[TOOLTIP\_VISIBLE](#TOOLTIP_VISIBLE)` | Deprecated.
0 = no tooltip displayed
1 = tooltip displaying |
| `static int` | `[WORLD\_MAP\_SEARCH\_FOCUSED](#WORLD_MAP_SEARCH_FOCUSED)` | Deprecated. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[VarClientInt](#%3Cinit%3E())()` | Deprecated. |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### TOOLTIP\_TIMEOUT

```
public static final int TOOLTIP_TIMEOUT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.TOOLTIP_TIMEOUT)
- #### TOOLTIP\_VISIBLE

```
public static final int TOOLTIP_VISIBLE
```

Deprecated.
0 = no tooltip displayed
1 = tooltip displaying

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.TOOLTIP_VISIBLE)
- #### INPUT\_TYPE

```
public static final int INPUT_TYPE
```

Deprecated.
Current message layer mode

See Also:
[`InputType`](vars/InputType.html "enum in net.runelite.api.vars"),
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.INPUT_TYPE)
- #### BANK\_SCROLL

```
public static final int BANK_SCROLL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.BANK_SCROLL)
- #### CAMERA\_ZOOM\_FIXED\_VIEWPORT

```
public static final int CAMERA_ZOOM_FIXED_VIEWPORT
```

Deprecated.
The game sets this to the same value as [`CAMERA_ZOOM_RESIZABLE_VIEWPORT`](#CAMERA_ZOOM_RESIZABLE_VIEWPORT)

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.CAMERA_ZOOM_FIXED_VIEWPORT)
- #### CAMERA\_ZOOM\_RESIZABLE\_VIEWPORT

```
public static final int CAMERA_ZOOM_RESIZABLE_VIEWPORT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.CAMERA_ZOOM_RESIZABLE_VIEWPORT)
- #### MEMBERSHIP\_STATUS

```
public static final int MEMBERSHIP_STATUS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.MEMBERSHIP_STATUS)
- #### INVENTORY\_TAB

```
public static final int INVENTORY_TAB
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.INVENTORY_TAB)
- #### BLOCK\_KEYPRESS

```
public static final int BLOCK_KEYPRESS
```

Deprecated.
time to block keypresses til

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.BLOCK_KEYPRESS)
- #### WORLD\_MAP\_SEARCH\_FOCUSED

```
public static final int WORLD_MAP_SEARCH_FOCUSED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarClientInt.WORLD_MAP_SEARCH_FOCUSED)

+ ### Constructor Detail

- #### VarClientInt

```
public VarClientInt()
```

Deprecated.