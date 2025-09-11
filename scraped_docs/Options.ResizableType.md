# Options.ResizableType (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Options.ResizableType.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Options.ResizableType

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Options](Options.html "class in org.tribot.script.sdk")

---

```
public static enum Options.ResizableType
extends java.lang.Enum<[Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")>
```

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[FIXED](#FIXED)` | |
| `[RESIZABLE\_CLASSIC](#RESIZABLE_CLASSIC)` | |
| `[RESIZABLE\_MODERN](#RESIZABLE_MODERN)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `java.lang.String` | `[getText](#getText())()` | |
| `java.lang.String` | `[toString](#toString())()` | |
| `static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### FIXED

```
public static final [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") FIXED
```
- #### RESIZABLE\_CLASSIC

```
public static final [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") RESIZABLE_CLASSIC
```
- #### RESIZABLE\_MODERN

```
public static final [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") RESIZABLE_MODERN
```

+ ### Method Detail

- #### values

```
public static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Options.ResizableType c : Options.ResizableType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Enum<[Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")>`
- #### getText

```
public java.lang.String getText()
```