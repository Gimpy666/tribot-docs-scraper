# Camera.RotationMethod (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Camera.RotationMethod.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Camera.RotationMethod

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")>`

Enclosing class:
[Camera](Camera.html "class in org.tribot.script.sdk")

---

```
public static enum Camera.RotationMethod
extends java.lang.Enum<[Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")>
```

A rotation method for moving the camera

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[DEFAULT](#DEFAULT)` | Default to tribot's player-specific preferences to assign camera rotation method |
| `[KEYS](#KEYS)` | Only use the keyboard keys to change the camera |
| `[MOUSE](#MOUSE)` | Only use the middle mouse button to change the camera |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### KEYS

```
public static final [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") KEYS
```

Only use the keyboard keys to change the camera
- #### MOUSE

```
public static final [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") MOUSE
```

Only use the middle mouse button to change the camera
- #### DEFAULT

```
public static final [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") DEFAULT
```

Default to tribot's player-specific preferences to assign camera rotation method

+ ### Method Detail

- #### values

```
public static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Camera.RotationMethod c : Camera.RotationMethod.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Camera.RotationMethod](Camera.RotationMethod.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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