# InstanceTemplates (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/InstanceTemplates.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")>
+ - net.runelite.api.InstanceTemplates

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")>`

---

```
public enum InstanceTemplates
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")>
```

An enumeration of possible instance templates and the area they occupy.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[RAIDS\_CRABS](#RAIDS_CRABS)` | |
| `[RAIDS\_END](#RAIDS_END)` | |
| `[RAIDS\_FARMING](#RAIDS_FARMING)` | |
| `[RAIDS\_FARMING2](#RAIDS_FARMING2)` | |
| `[RAIDS\_GUARDIANS](#RAIDS_GUARDIANS)` | |
| `[RAIDS\_ICE\_DEMON](#RAIDS_ICE_DEMON)` | |
| `[RAIDS\_LOBBY](#RAIDS_LOBBY)` | |
| `[RAIDS\_MUTTADILES](#RAIDS_MUTTADILES)` | |
| `[RAIDS\_MYSTICS](#RAIDS_MYSTICS)` | |
| `[RAIDS\_SCAVENGERS](#RAIDS_SCAVENGERS)` | |
| `[RAIDS\_SCAVENGERS2](#RAIDS_SCAVENGERS2)` | |
| `[RAIDS\_SHAMANS](#RAIDS_SHAMANS)` | |
| `[RAIDS\_START](#RAIDS_START)` | |
| `[RAIDS\_TEKTON](#RAIDS_TEKTON)` | |
| `[RAIDS\_THIEVING](#RAIDS_THIEVING)` | |
| `[RAIDS\_TIGHTROPE](#RAIDS_TIGHTROPE)` | |
| `[RAIDS\_VANGUARDS](#RAIDS_VANGUARDS)` | |
| `[RAIDS\_VASA](#RAIDS_VASA)` | |
| `[RAIDS\_VESPULA](#RAIDS_VESPULA)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")` | `[findMatch](#findMatch(int))​(int chunkData)` | Matches chunk data of an instance to the instance it belongs. |
| `int` | `[getBaseX](#getBaseX())()` | The base x-axis coordinate of the instance area. |
| `int` | `[getBaseY](#getBaseY())()` | The base y-axis coordinate of the instance area. |
| `int` | `[getHeight](#getHeight())()` | The height of the instance area. |
| `int` | `[getPlane](#getPlane())()` | The plane the instance is on. |
| `int` | `[getWidth](#getWidth())()` | The width of the instance area. |
| `static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### RAIDS\_LOBBY

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_LOBBY
```
- #### RAIDS\_START

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_START
```
- #### RAIDS\_END

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_END
```
- #### RAIDS\_SCAVENGERS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_SCAVENGERS
```
- #### RAIDS\_SHAMANS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_SHAMANS
```
- #### RAIDS\_VASA

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_VASA
```
- #### RAIDS\_VANGUARDS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_VANGUARDS
```
- #### RAIDS\_ICE\_DEMON

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_ICE_DEMON
```
- #### RAIDS\_THIEVING

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_THIEVING
```
- #### RAIDS\_FARMING

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_FARMING
```
- #### RAIDS\_SCAVENGERS2

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_SCAVENGERS2
```
- #### RAIDS\_MUTTADILES

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_MUTTADILES
```
- #### RAIDS\_MYSTICS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_MYSTICS
```
- #### RAIDS\_TEKTON

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_TEKTON
```
- #### RAIDS\_TIGHTROPE

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_TIGHTROPE
```
- #### RAIDS\_FARMING2

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_FARMING2
```
- #### RAIDS\_GUARDIANS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_GUARDIANS
```
- #### RAIDS\_VESPULA

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_VESPULA
```
- #### RAIDS\_CRABS

```
public static final [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") RAIDS_CRABS
```

+ ### Method Detail

- #### values

```
public static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (InstanceTemplates c : InstanceTemplates.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if this enum type has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if the argument is null
- #### findMatch

```
public static [InstanceTemplates](InstanceTemplates.html "enum in net.runelite.api") findMatch​(int chunkData)
```

Matches chunk data of an instance to the instance it belongs.

Parameters:
`chunkData` - the chunk data
Returns:
the instance the chunk is in
- #### getBaseX

```
public int getBaseX()
```

The base x-axis coordinate of the instance area.
- #### getBaseY

```
public int getBaseY()
```

The base y-axis coordinate of the instance area.
- #### getPlane

```
public int getPlane()
```

The plane the instance is on.
- #### getWidth

```
public int getWidth()
```

The width of the instance area.
- #### getHeight

```
public int getHeight()
```

The height of the instance area.