# WorldType (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/WorldType.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[WorldType](WorldType.html "enum in net.runelite.api")>
+ - net.runelite.api.WorldType

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[WorldType](WorldType.html "enum in net.runelite.api")>`

---

```
public enum WorldType
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[WorldType](WorldType.html "enum in net.runelite.api")>
```

An enumeration of possible world types.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BETA\_WORLD](#BETA_WORLD)` | Beta world. |
| `[BOUNTY](#BOUNTY)` | Bounty world type. |
| `[DEADMAN](#DEADMAN)` | Deadman world type. |
| `[EOC\_ONLY](#EOC_ONLY)` | |
| `[FRESH\_START\_WORLD](#FRESH_START_WORLD)` | Fresh start world type |
| `[HIGH\_RISK](#HIGH_RISK)` | High risk world type. |
| `[LAST\_MAN\_STANDING](#LAST_MAN_STANDING)` | Last man standing world type. |
| `[LEGACY\_ONLY](#LEGACY_ONLY)` | |
| `[MEMBERS](#MEMBERS)` | Members world type. |
| `[NOSAVE\_MODE](#NOSAVE_MODE)` | Beta worlds without profiles that are saved. |
| `[PVP](#PVP)` | Pvp world type. |
| `[PVP\_ARENA](#PVP_ARENA)` | PVP arena world type. |
| `[QUEST\_SPEEDRUNNING](#QUEST_SPEEDRUNNING)` | Quest speedrunning |
| `[SEASONAL](#SEASONAL)` | Seasonal world type for leagues and seasonal deadman. |
| `[SKILL\_TOTAL](#SKILL_TOTAL)` | Skill total world type. |
| `[TOURNAMENT\_WORLD](#TOURNAMENT_WORLD)` | Tournament world type |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")>` | `[fromMask](#fromMask(int))​(int mask)` | Create enum set of world types from mask. |
| `static boolean` | `[isPvpWorld](#isPvpWorld(java.util.Collection))​([Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> worldTypes)` | Checks whether a world having a [`Collection`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util") of [`WorldType`](WorldType.html "enum in net.runelite.api")s is a PVP world. |
| `static int` | `[toMask](#toMask(java.util.EnumSet))​([EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> types)` | Create mask from enum set of world types. |
| `static [WorldType](WorldType.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [WorldType](WorldType.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### MEMBERS

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") MEMBERS
```

Members world type.
- #### PVP

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") PVP
```

Pvp world type.
- #### BOUNTY

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") BOUNTY
```

Bounty world type.
- #### PVP\_ARENA

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") PVP_ARENA
```

PVP arena world type.
- #### SKILL\_TOTAL

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") SKILL_TOTAL
```

Skill total world type.
- #### QUEST\_SPEEDRUNNING

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") QUEST_SPEEDRUNNING
```

Quest speedrunning
- #### HIGH\_RISK

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") HIGH_RISK
```

High risk world type.
- #### LAST\_MAN\_STANDING

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") LAST_MAN_STANDING
```

Last man standing world type.
- #### BETA\_WORLD

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") BETA_WORLD
```

Beta world.
- #### LEGACY\_ONLY

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") LEGACY_ONLY
```
- #### EOC\_ONLY

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") EOC_ONLY
```
- #### NOSAVE\_MODE

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") NOSAVE_MODE
```

Beta worlds without profiles that are saved.
- #### TOURNAMENT\_WORLD

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") TOURNAMENT_WORLD
```

Tournament world type
- #### FRESH\_START\_WORLD

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") FRESH_START_WORLD
```

Fresh start world type
- #### DEADMAN

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") DEADMAN
```

Deadman world type.
- #### SEASONAL

```
public static final [WorldType](WorldType.html "enum in net.runelite.api") SEASONAL
```

Seasonal world type for leagues and seasonal deadman.

+ ### Method Detail

- #### values

```
public static [WorldType](WorldType.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (WorldType c : WorldType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [WorldType](WorldType.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### fromMask

```
public static [EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> fromMask​(int mask)
```

Create enum set of world types from mask.

Parameters:
`mask` - the mask
Returns:
the enum set
- #### toMask

```
public static int toMask​([EnumSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/EnumSet.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> types)
```

Create mask from enum set of world types.

Parameters:
`types` - the types
Returns:
the int containing all mask
- #### isPvpWorld

```
public static boolean isPvpWorld​([Collection](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util")<[WorldType](WorldType.html "enum in net.runelite.api")> worldTypes)
```

Checks whether a world having a [`Collection`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util") of [`WorldType`](WorldType.html "enum in net.runelite.api")s is a PVP world.

Parameters:
`worldTypes` - A [`Collection`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collection.html?is-external=true "class or interface in java.util") of [`WorldType`](WorldType.html "enum in net.runelite.api")s describing the given world.
Returns:
True if the given worldtypes of the world are a PVP world, false otherwise.
See Also:
[`Client.getWorldType()`](Client.html#getWorldType())