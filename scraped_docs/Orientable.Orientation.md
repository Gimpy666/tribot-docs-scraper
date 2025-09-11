# Orientable.Orientation (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/Orientable.Orientation.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* java.lang.Object
* + org.tribot.script.sdk.interfaces.Orientable.Orientation

* Enclosing interface:
[Orientable](Orientable.html "interface in org.tribot.script.sdk.interfaces")

---

```
public static final class Orientable.Orientation
extends java.lang.Object
```

Represents the orientation of an entity

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")` | Represents a cardinal direction (and the four inter-cardinal directions) |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Orientation](#%3Cinit%3E(int))​(int angle)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `int` | `[getAngle](#getAngle())()` | |
| `[Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces")` | `[getClosestDirection](#getClosestDirection())()` | The closest cardinal direction to this orientation |
| `int` | `[hashCode](#hashCode())()` | |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

- #### Orientation

```
public Orientation​(int angle)
```

+ ### Method Detail

- #### getClosestDirection

```
public [Orientable.Orientation.Direction](Orientable.Orientation.Direction.html "enum in org.tribot.script.sdk.interfaces") getClosestDirection()
```

The closest cardinal direction to this orientation

Returns:
the closest cardinal direction to this orientation
- #### getAngle

```
public int getAngle()
```
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`