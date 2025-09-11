# ObjectDefinition (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/definitions/ObjectDefinition.html

**Package:** Packageorg.tribot.script.sdk.types.definitions

---

* java.lang.Object
* + org.tribot.script.sdk.types.definitions.ObjectDefinition

* ---

```
public class ObjectDefinition
extends java.lang.Object
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ObjectDefinition](#%3Cinit%3E(org.tribot.api2007.types.RSObjectDefinition))​(org.tribot.api2007.types.RSObjectDefinition definition)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[blocksProjectiles](#blocksProjectiles())()` | Gets whether or not the object can block projectiles. |
| `static java.util.Optional<[ObjectDefinition](ObjectDefinition.html "class in org.tribot.script.sdk.types.definitions")>` | `[get](#get(int))​(int id)` | Gets the object definition for the object with the specified ID. |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | |
| `int` | `[getHeight](#getHeight())()` | Gets the height in tiles of this object. |
| `short[]` | `[getModifiedColors](#getModifiedColors())()` | |
| `java.lang.String` | `[getName](#getName())()` | |
| `int` | `[getWidth](#getWidth())()` | Gets the width in tiles of this object. |
| `boolean` | `[isWalkable](#isWalkable())()` | Gets whether or not this object can be walked over |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ObjectDefinition

```
public ObjectDefinition​(org.tribot.api2007.types.RSObjectDefinition definition)
```

+ ### Method Detail

- #### getName

```
public java.lang.String getName()
```
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```
- #### getWidth

```
public int getWidth()
```

Gets the width in tiles of this object.
- #### getHeight

```
public int getHeight()
```

Gets the height in tiles of this object.
- #### blocksProjectiles

```
public boolean blocksProjectiles()
```

Gets whether or not the object can block projectiles.
- #### isWalkable

```
public boolean isWalkable()
```

Gets whether or not this object can be walked over
- #### getModifiedColors

```
public short[] getModifiedColors()
```
- #### get

```
public static java.util.Optional<[ObjectDefinition](ObjectDefinition.html "class in org.tribot.script.sdk.types.definitions")> get​(int id)
```

Gets the object definition for the object with the specified ID. If this operation fails, the optional will be
empty.