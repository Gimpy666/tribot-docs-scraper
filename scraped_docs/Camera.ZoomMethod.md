# Camera.ZoomMethod (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Camera.ZoomMethod.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Camera.ZoomMethod

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Camera](Camera.html "class in org.tribot.script.sdk")

---

```
public static enum Camera.ZoomMethod
extends java.lang.Enum<[Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DEFAULT](#DEFAULT)` | Default to tribot's player-specific preferences to assign camera rotation method |
| `[MOUSE\_SCROLL](#MOUSE_SCROLL)` | Only use the mouse scroll wheel to adjust zoom |
| `[OPTIONS\_TAB](#OPTIONS_TAB)` | Only use the options tab to adjust zoom |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### OPTIONS\_TAB

```
public static final [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") OPTIONS_TAB
```

Only use the options tab to adjust zoom
- #### MOUSE\_SCROLL

```
public static final [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") MOUSE_SCROLL
```

Only use the mouse scroll wheel to adjust zoom
- #### DEFAULT

```
public static final [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") DEFAULT
```

Default to tribot's player-specific preferences to assign camera rotation method

+ ### Method Detail

- #### values

```
public static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Camera.ZoomMethod c : Camera.ZoomMethod.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Camera.ZoomMethod](Camera.ZoomMethod.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
`java.lang.NullPointerException` - if the argument is null