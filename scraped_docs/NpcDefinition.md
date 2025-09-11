# NpcDefinition (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/definitions/NpcDefinition.html

**Package:** Packageorg.tribot.script.sdk.types.definitions

---

* java.lang.Object
* + org.tribot.script.sdk.types.definitions.NpcDefinition

* All Implemented Interfaces:
`[Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class NpcDefinition
extends java.lang.Object
implements [Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces"), [Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[NpcDefinition](#%3Cinit%3E(org.tribot.api2007.types.RSNPCDefinition))​(org.tribot.api2007.types.RSNPCDefinition npcDefinition)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[NpcDefinition](NpcDefinition.html "class in org.tribot.script.sdk.types.definitions")>` | `[get](#get(int))​(int id)` | |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | |
| `int` | `[getCombatLevel](#getCombatLevel())()` | |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |
| `int` | `[getSize](#getSize())()` | |
| `boolean` | `[isPet](#isPet())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### NpcDefinition

```
public NpcDefinition​(org.tribot.api2007.types.RSNPCDefinition npcDefinition)
```

+ ### Method Detail

- #### getId

```
public int getId()
```

Description copied from interface: `[Identifiable](../../interfaces/Identifiable.html#getId())`
Gets the ID of the entity

Specified by:
`[getId](../../interfaces/Identifiable.html#getId())` in interface `[Identifiable](../../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getName

```
public java.lang.String getName()
```

Description copied from interface: `[Named](../../interfaces/Named.html#getName())`
Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Specified by:
`[getName](../../interfaces/Named.html#getName())` in interface `[Named](../../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The name of the entity
- #### getCombatLevel

```
public int getCombatLevel()
```
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```
- #### isPet

```
public boolean isPet()
```
- #### getSize

```
public int getSize()
```
- #### get

```
public static java.util.Optional<[NpcDefinition](NpcDefinition.html "class in org.tribot.script.sdk.types.definitions")> get​(int id)
```