# NPCComposition (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/NPCComposition.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[ParamHolder](ParamHolder.html "interface in net.runelite.api")`

---

```
public interface NPCComposition
extends [ParamHolder](ParamHolder.html "interface in net.runelite.api")
```

Information about a specific `NpcID`

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[STAT\_ATTACK](#STAT_ATTACK)` | |
| `static int` | `[STAT\_DEFENCE](#STAT_DEFENCE)` | |
| `static int` | `[STAT\_HITPOINTS](#STAT_HITPOINTS)` | |
| `static int` | `[STAT\_MAGIC](#STAT_MAGIC)` | |
| `static int` | `[STAT\_RANGED](#STAT_RANGED)` | |
| `static int` | `[STAT\_STRENGTH](#STAT_STRENGTH)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[]` | `[getActions](#getActions())()` | The 5 menuops this NPC has when in world. |
| `int[]` | `[getChatheadModels](#getChatheadModels())()` | Gets the model IDs that compose this NPC's chathead. |
| `short[]` | `[getColorToReplace](#getColorToReplace())()` | Get the colors to be replaced on this npc's model for this npc. |
| `short[]` | `[getColorToReplaceWith](#getColorToReplaceWith())()` | Get the colors applied to this npc's model for this npc. |
| `int` | `[getCombatLevel](#getCombatLevel())()` | |
| `int[]` | `[getConfigs](#getConfigs())()` | Get the `NpcID`s of NPCs this can transform into, depending
on a `VarbitID` or `VarPlayerID` |
| `int` | `[getFootprintSize](#getFootprintSize())()` | Get the npc footprint size |
| `int` | `[getHeightScale](#getHeightScale())()` | Vertical scaling of the npc model (1/128th of a tile). |
| `int` | `[getId](#getId())()` | Gets the ID of the NPC. |
| `int[]` | `[getModels](#getModels())()` | Gets the model IDs that compose this NPC. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the NPC. |
| `int` | `[getSize](#getSize())()` | How many tiles wide this NPC is |
| `int[]` | `[getStats](#getStats())()` | Get the npc's stats |
| `int` | `[getWidthScale](#getWidthScale())()` | Horizontal scaling of the npc model (1/128th of a tile). |
| `boolean` | `[isFollower](#isFollower())()` | If the npc is a follower, such as a pet. |
| `boolean` | `[isInteractible](#isInteractible())()` | NPC can be interacting with via menu options |
| `boolean` | `[isMinimapVisible](#isMinimapVisible())()` | Gets whether the NPC is visible on the mini-map. |
| `[NPCComposition](NPCComposition.html "interface in net.runelite.api")` | `[transform](#transform())()` | Get the NPC composition the player's state says this NPC should
transmogrify into. |

- ### Methods inherited from interface net.runelite.api.[ParamHolder](ParamHolder.html "interface in net.runelite.api")

`[getIntValue](ParamHolder.html#getIntValue(int)), [getParams](ParamHolder.html#getParams()), [getStringValue](ParamHolder.html#getStringValue(int)), [setParams](ParamHolder.html#setParams(net.runelite.api.IterableHashTable)), [setValue](ParamHolder.html#setValue(int,int)), [setValue](ParamHolder.html#setValue(int,java.lang.String))`

* + ### Field Detail

- #### STAT\_ATTACK

```
static final int STAT_ATTACK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_ATTACK)
- #### STAT\_DEFENCE

```
static final int STAT_DEFENCE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_DEFENCE)
- #### STAT\_STRENGTH

```
static final int STAT_STRENGTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_STRENGTH)
- #### STAT\_HITPOINTS

```
static final int STAT_HITPOINTS
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_HITPOINTS)
- #### STAT\_RANGED

```
static final int STAT_RANGED
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_RANGED)
- #### STAT\_MAGIC

```
static final int STAT_MAGIC
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.NPCComposition.STAT_MAGIC)

+ ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the NPC.
- #### getModels

```
int[] getModels()
```

Gets the model IDs that compose this NPC.
- #### getChatheadModels

```
@Nullable
int[] getChatheadModels()
```

Gets the model IDs that compose this NPC's chathead.
- #### getActions

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")[] getActions()
```

The 5 menuops this NPC has when in world. Index 0 corresponds to
[`MenuAction.NPC_FIRST_OPTION`](MenuAction.html#NPC_FIRST_OPTION), Index 2 to
[`MenuAction.NPC_SECOND_OPTION`](MenuAction.html#NPC_SECOND_OPTION) and so on.
- #### isInteractible

```
boolean isInteractible()
```

NPC can be interacting with via menu options

Returns:
- #### isMinimapVisible

```
boolean isMinimapVisible()
```

Gets whether the NPC is visible on the mini-map.
- #### getId

```
int getId()
```

Gets the ID of the NPC.

See Also:
`NpcID`
- #### getCombatLevel

```
int getCombatLevel()
```

Returns:
the combat level, -1 if none
- #### getConfigs

```
int[] getConfigs()
```

Get the `NpcID`s of NPCs this can transform into, depending
on a `VarbitID` or `VarPlayerID`
- #### transform

```
[NPCComposition](NPCComposition.html "interface in net.runelite.api") transform()
```

Get the NPC composition the player's state says this NPC should
transmogrify into.

Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if [`getConfigs()`](#getConfigs()) is null
- #### getSize

```
int getSize()
```

How many tiles wide this NPC is
- #### isFollower

```
boolean isFollower()
```

If the npc is a follower, such as a pet. Is affected by the
"Move follower options lower down" setting.

Returns:
- #### getColorToReplace

```
@Nullable
short[] getColorToReplace()
```

Get the colors to be replaced on this npc's model for this npc.

Returns:
the colors to be replaced
See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api")
- #### getColorToReplaceWith

```
@Nullable
short[] getColorToReplaceWith()
```

Get the colors applied to this npc's model for this npc.

Returns:
the colors to replace with
See Also:
[`JagexColor`](JagexColor.html "class in net.runelite.api")
- #### getWidthScale

```
int getWidthScale()
```

Horizontal scaling of the npc model (1/128th of a tile).

Returns:
- #### getHeightScale

```
int getHeightScale()
```

Vertical scaling of the npc model (1/128th of a tile).

Returns:
- #### getFootprintSize

```
int getFootprintSize()
```

Get the npc footprint size

Returns:
- #### getStats

```
int[] getStats()
```

Get the npc's stats

Returns:
See Also:
[`STAT_ATTACK`](#STAT_ATTACK),
[`STAT_DEFENCE`](#STAT_DEFENCE),
[`STAT_STRENGTH`](#STAT_STRENGTH),
[`STAT_HITPOINTS`](#STAT_HITPOINTS),
[`STAT_RANGED`](#STAT_RANGED),
[`STAT_MAGIC`](#STAT_MAGIC)