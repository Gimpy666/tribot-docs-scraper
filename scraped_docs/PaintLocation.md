# PaintLocation (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/template/basic/PaintLocation.html

**Package:** Packageorg.tribot.script.sdk.painting.template.basic

---

* java.lang.Object
* + java.lang.Enum<[PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")>
+ - org.tribot.script.sdk.painting.template.basic.PaintLocation

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")>`

---

```
public enum PaintLocation
extends java.lang.Enum<[PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")>
```

Contains preset paint locations for [`BasicPaintTemplate`](BasicPaintTemplate.html "class in org.tribot.script.sdk.painting.template.basic")

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BOTTOM\_LEFT\_CHATBOX](#BOTTOM_LEFT_CHATBOX)` | |
| `[BOTTOM\_LEFT\_VIEWPORT](#BOTTOM_LEFT_VIEWPORT)` | |
| `[BOTTOM\_RIGHT\_CHATBOX](#BOTTOM_RIGHT_CHATBOX)` | |
| `[BOTTOM\_RIGHT\_VIEWPORT](#BOTTOM_RIGHT_VIEWPORT)` | |
| `[INVENTORY\_AREA](#INVENTORY_AREA)` | |
| `[TOP\_LEFT\_CHATBOX](#TOP_LEFT_CHATBOX)` | |
| `[TOP\_LEFT\_VIEWPORT](#TOP_LEFT_VIEWPORT)` | |
| `[TOP\_RIGHT\_CHATBOX](#TOP_RIGHT_CHATBOX)` | |
| `[TOP\_RIGHT\_VIEWPORT](#TOP_RIGHT_VIEWPORT)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### BOTTOM\_LEFT\_VIEWPORT

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") BOTTOM_LEFT_VIEWPORT
```
- #### BOTTOM\_RIGHT\_VIEWPORT

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") BOTTOM_RIGHT_VIEWPORT
```
- #### TOP\_LEFT\_VIEWPORT

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") TOP_LEFT_VIEWPORT
```
- #### TOP\_RIGHT\_VIEWPORT

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") TOP_RIGHT_VIEWPORT
```
- #### TOP\_LEFT\_CHATBOX

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") TOP_LEFT_CHATBOX
```
- #### TOP\_RIGHT\_CHATBOX

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") TOP_RIGHT_CHATBOX
```
- #### BOTTOM\_LEFT\_CHATBOX

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") BOTTOM_LEFT_CHATBOX
```
- #### BOTTOM\_RIGHT\_CHATBOX

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") BOTTOM_RIGHT_CHATBOX
```
- #### INVENTORY\_AREA

```
public static final [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") INVENTORY_AREA
```

+ ### Method Detail

- #### values

```
public static [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (PaintLocation c : PaintLocation.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") valueOf​(java.lang.String name)
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