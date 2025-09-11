# World.Type (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/World.Type.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + java.lang.Enum<[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")>
+ - org.tribot.script.sdk.types.World.Type

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")>`

Enclosing class:
[World](World.html "class in org.tribot.script.sdk.types")

---

```
public static enum World.Type
extends java.lang.Enum<[World.Type](World.Type.html "enum in org.tribot.script.sdk.types")>
```

Represents the types that a world can have. A world can have 0 or more types.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[BETA\_WORLD](#BETA_WORLD)` | |
| `[BOUNTY](#BOUNTY)` | |
| `[DEADMAN](#DEADMAN)` | |
| `[DEADMAN\_TOURNAMENT](#DEADMAN_TOURNAMENT)` | Deprecated, for removal: This API element is subject to removal in a future version. |
| `[FRESH\_START\_WORLD](#FRESH_START_WORLD)` | |
| `[HIGH\_RISK](#HIGH_RISK)` | |
| `[LAST\_MAN\_STANDING](#LAST_MAN_STANDING)` | |
| `[LEAGUE](#LEAGUE)` | |
| `[MEMBERS](#MEMBERS)` | |
| `[NOSAVE\_MODE](#NOSAVE_MODE)` | |
| `[PVP](#PVP)` | |
| `[PVP\_ARENA](#PVP_ARENA)` | |
| `[QUEST\_SPEEDRUNNING](#QUEST_SPEEDRUNNING)` | |
| `[SKILL\_TOTAL](#SKILL_TOTAL)` | |
| `[TOURNAMENT](#TOURNAMENT)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [World.Type](World.Type.html "enum in org.tribot.script.sdk.types")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [World.Type](World.Type.html "enum in org.tribot.script.sdk.types")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### MEMBERS

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") MEMBERS
```
- #### PVP

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") PVP
```
- #### BOUNTY

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") BOUNTY
```
- #### PVP\_ARENA

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") PVP_ARENA
```
- #### SKILL\_TOTAL

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") SKILL_TOTAL
```
- #### QUEST\_SPEEDRUNNING

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") QUEST_SPEEDRUNNING
```
- #### HIGH\_RISK

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") HIGH_RISK
```
- #### LAST\_MAN\_STANDING

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") LAST_MAN_STANDING
```
- #### BETA\_WORLD

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") BETA_WORLD
```
- #### NOSAVE\_MODE

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") NOSAVE_MODE
```
- #### TOURNAMENT

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") TOURNAMENT
```
- #### DEADMAN\_TOURNAMENT

```
@Deprecated(forRemoval=true)
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") DEADMAN_TOURNAMENT
```

Deprecated, for removal: This API element is subject to removal in a future version.
- #### FRESH\_START\_WORLD

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") FRESH_START_WORLD
```
- #### DEADMAN

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") DEADMAN
```
- #### LEAGUE

```
public static final [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") LEAGUE
```

+ ### Method Detail

- #### values

```
public static [World.Type](World.Type.html "enum in org.tribot.script.sdk.types")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (World.Type c : World.Type.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [World.Type](World.Type.html "enum in org.tribot.script.sdk.types") valueOf​(java.lang.String name)
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