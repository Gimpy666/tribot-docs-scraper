# VarPlayer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/VarPlayer.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.VarPlayer

* ---

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public final class VarPlayer
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Deprecated.
Server controlled "content-developer" integers.

VarPlayers are stored per RuneScape player save, and synchronized
from the server to the client. The client can change them preemptively
if it thinks they will change the next tick as a lag-hiding measure.
The client CANNOT directly make the server change a varp.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[AGILITY\_GOAL\_END](#AGILITY_GOAL_END)` | Deprecated. |
| `static int` | `[AGILITY\_GOAL\_START](#AGILITY_GOAL_START)` | Deprecated. |
| `static int` | `[AREA\_EFFECT\_VOLUME](#AREA_EFFECT_VOLUME)` | Deprecated. |
| `static int` | `[ATTACK\_GOAL\_END](#ATTACK_GOAL_END)` | Deprecated.
Experience tracker goal end. |
| `static int` | `[ATTACK\_GOAL\_START](#ATTACK_GOAL_START)` | Deprecated.
Experience tracker goal start. |
| `static int` | `[ATTACK\_STYLE](#ATTACK_STYLE)` | Deprecated. |
| `static int` | `[BANK\_TAB](#BANK_TAB)` | Deprecated. |
| `static int` | `[BIRD\_HOUSE\_MEADOW\_NORTH](#BIRD_HOUSE_MEADOW_NORTH)` | Deprecated.
Bird house states |
| `static int` | `[BIRD\_HOUSE\_MEADOW\_SOUTH](#BIRD_HOUSE_MEADOW_SOUTH)` | Deprecated. |
| `static int` | `[BIRD\_HOUSE\_VALLEY\_NORTH](#BIRD_HOUSE_VALLEY_NORTH)` | Deprecated. |
| `static int` | `[BIRD\_HOUSE\_VALLEY\_SOUTH](#BIRD_HOUSE_VALLEY_SOUTH)` | Deprecated. |
| `static int` | `[BUFF\_BAR\_WC\_GROUP\_BONUS](#BUFF_BAR_WC_GROUP_BONUS)` | Deprecated.
Determines whether the woodcutting group bonus should be displayed on the buff bar or not. |
| `static int` | `[CANNON\_AMMO](#CANNON_AMMO)` | Deprecated. |
| `static int` | `[CANNON\_COORD](#CANNON_COORD)` | Deprecated. |
| `static int` | `[CANNON\_STATE](#CANNON_STATE)` | Deprecated. |
| `static int` | `[CHARGE\_GOD\_SPELL](#CHARGE_GOD_SPELL)` | Deprecated.
Charge spell duration
Value \* 2 = Remaining game ticks on buff
E.g. |
| `static int` | `[CLOG\_LOGGED](#CLOG_LOGGED)` | Deprecated. |
| `static int` | `[CLOG\_TOTAL](#CLOG_TOTAL)` | Deprecated. |
| `static int` | `[CONSTRUCTION\_GOAL\_END](#CONSTRUCTION_GOAL_END)` | Deprecated. |
| `static int` | `[CONSTRUCTION\_GOAL\_START](#CONSTRUCTION_GOAL_START)` | Deprecated. |
| `static int` | `[COOKING\_GOAL\_END](#COOKING_GOAL_END)` | Deprecated. |
| `static int` | `[COOKING\_GOAL\_START](#COOKING_GOAL_START)` | Deprecated. |
| `static int` | `[CRAFTING\_GOAL\_END](#CRAFTING_GOAL_END)` | Deprecated. |
| `static int` | `[CRAFTING\_GOAL\_START](#CRAFTING_GOAL_START)` | Deprecated. |
| `static int` | `[CURRENT\_GE\_ITEM](#CURRENT_GE_ITEM)` | Deprecated.
Item currently active in the creation of a buy or sell offer |
| `static int` | `[DEFENCE\_GOAL\_END](#DEFENCE_GOAL_END)` | Deprecated. |
| `static int` | `[DEFENCE\_GOAL\_START](#DEFENCE_GOAL_START)` | Deprecated. |
| `static int` | `[DISEASE\_VALUE](#DISEASE_VALUE)` | Deprecated.
Seems to start at 50(10 splash) and goes down by 1 every 30 seconds |
| `static int` | `[DIZANAS\_QUIVER\_ITEM\_COUNT](#DIZANAS_QUIVER_ITEM_COUNT)` | Deprecated.
The amount of ammo in Dizana's quiver's inventory slot. |
| `static int` | `[DIZANAS\_QUIVER\_ITEM\_ID](#DIZANAS_QUIVER_ITEM_ID)` | Deprecated.
The item ID of the ammo in Dizana's quiver inventory slot. |
| `static int` | `[ESSENCE\_POUCH\_GIANT\_DEGRADE](#ESSENCE_POUCH_GIANT_DEGRADE)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_LARGE\_DEGRADE](#ESSENCE_POUCH_LARGE_DEGRADE)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_MEDIUM\_DEGRADE](#ESSENCE_POUCH_MEDIUM_DEGRADE)` | Deprecated.
Runecraft Essence Pouch degrade states |
| `static int` | `[FARMING\_GOAL\_END](#FARMING_GOAL_END)` | Deprecated. |
| `static int` | `[FARMING\_GOAL\_START](#FARMING_GOAL_START)` | Deprecated. |
| `static int` | `[FIREMAKING\_GOAL\_END](#FIREMAKING_GOAL_END)` | Deprecated. |
| `static int` | `[FIREMAKING\_GOAL\_START](#FIREMAKING_GOAL_START)` | Deprecated. |
| `static int` | `[FISHING\_GOAL\_END](#FISHING_GOAL_END)` | Deprecated. |
| `static int` | `[FISHING\_GOAL\_START](#FISHING_GOAL_START)` | Deprecated. |
| `static int` | `[FLETCHING\_GOAL\_END](#FLETCHING_GOAL_END)` | Deprecated. |
| `static int` | `[FLETCHING\_GOAL\_START](#FLETCHING_GOAL_START)` | Deprecated. |
| `static int` | `[HERBLORE\_GOAL\_END](#HERBLORE_GOAL_END)` | Deprecated. |
| `static int` | `[HERBLORE\_GOAL\_START](#HERBLORE_GOAL_START)` | Deprecated. |
| `static int` | `[HITPOINTS\_GOAL\_END](#HITPOINTS_GOAL_END)` | Deprecated. |
| `static int` | `[HITPOINTS\_GOAL\_START](#HITPOINTS_GOAL_START)` | Deprecated. |
| `static int` | `[HP\_HUD\_NPC\_ID](#HP_HUD_NPC_ID)` | Deprecated.
`NpcID` for the HP HUD |
| `static int` | `[HUNTER\_GOAL\_END](#HUNTER_GOAL_END)` | Deprecated. |
| `static int` | `[HUNTER\_GOAL\_START](#HUNTER_GOAL_START)` | Deprecated. |
| `static int` | `[IN\_RAID\_PARTY](#IN_RAID_PARTY)` | Deprecated.
The ID of the party. |
| `static int` | `[LAST\_HOME\_TELEPORT](#LAST_HOME_TELEPORT)` | Deprecated.
The difference, measured in minutes, between the time home teleport spell was last used and midnight, January 1, 1970 UTC. |
| `static int` | `[LAST\_MINIGAME\_TELEPORT](#LAST_MINIGAME_TELEPORT)` | Deprecated.
The difference, measured in minutes, between the time minigame teleport was last used and midnight, January 1, 1970 UTC. |
| `static int` | `[MAGIC\_GOAL\_END](#MAGIC_GOAL_END)` | Deprecated. |
| `static int` | `[MAGIC\_GOAL\_START](#MAGIC_GOAL_START)` | Deprecated. |
| `static int` | `[MEMBERSHIP\_DAYS](#MEMBERSHIP_DAYS)` | Deprecated. |
| `static int` | `[MINING\_GOAL\_END](#MINING_GOAL_END)` | Deprecated. |
| `static int` | `[MINING\_GOAL\_START](#MINING_GOAL_START)` | Deprecated. |
| `static int` | `[MOUSE\_BUTTONS](#MOUSE_BUTTONS)` | Deprecated.
0 = 2 buttons, 1 = 1 button |
| `static int` | `[MUSIC\_VOLUME](#MUSIC_VOLUME)` | Deprecated. |
| `static int` | `[NMZ\_REWARD\_POINTS](#NMZ_REWARD_POINTS)` | Deprecated. |
| `static int` | `[POISON](#POISON)` | Deprecated.
The poisoned status of the player, with negative values indicating the duration of poison or venom protection and
positive values representing the amount of poison or venom damage the player will be taking. |
| `static int` | `[PRAYER\_GOAL\_END](#PRAYER_GOAL_END)` | Deprecated. |
| `static int` | `[PRAYER\_GOAL\_START](#PRAYER_GOAL_START)` | Deprecated. |
| `static int` | `[QUEST\_POINTS](#QUEST_POINTS)` | Deprecated. |
| `static int` | `[RAIDS\_PERSONAL\_POINTS](#RAIDS_PERSONAL_POINTS)` | Deprecated. |
| `static int` | `[RANGED\_GOAL\_END](#RANGED_GOAL_END)` | Deprecated. |
| `static int` | `[RANGED\_GOAL\_START](#RANGED_GOAL_START)` | Deprecated. |
| `static int` | `[RUNECRAFT\_GOAL\_END](#RUNECRAFT_GOAL_END)` | Deprecated. |
| `static int` | `[RUNECRAFT\_GOAL\_START](#RUNECRAFT_GOAL_START)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_AUTO](#SETTINGS_OPAQUE_CHAT_AUTO)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_BROADCAST](#SETTINGS_OPAQUE_CHAT_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_CHALLENGE\_REQUEST](#SETTINGS_OPAQUE_CHAT_CHALLENGE_REQUEST)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_CLAN](#SETTINGS_OPAQUE_CHAT_CLAN)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_CLAN\_BROADCAST](#SETTINGS_OPAQUE_CHAT_CLAN_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_FRIEND](#SETTINGS_OPAQUE_CHAT_FRIEND)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_GUEST\_CLAN](#SETTINGS_OPAQUE_CHAT_GUEST_CLAN)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_IRON\_GROUP\_BROADCAST](#SETTINGS_OPAQUE_CHAT_IRON_GROUP_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_IRON\_GROUP\_CHAT](#SETTINGS_OPAQUE_CHAT_IRON_GROUP_CHAT)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_PRIVATE](#SETTINGS_OPAQUE_CHAT_PRIVATE)` | Deprecated. |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_PUBLIC](#SETTINGS_OPAQUE_CHAT_PUBLIC)` | Deprecated.
Colors for chat messages |
| `static int` | `[SETTINGS\_OPAQUE\_CHAT\_TRADE\_REQUEST](#SETTINGS_OPAQUE_CHAT_TRADE_REQUEST)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_AUTO](#SETTINGS_TRANSPARENT_CHAT_AUTO)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_BROADCAST](#SETTINGS_TRANSPARENT_CHAT_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_CHALLENGE\_REQUEST](#SETTINGS_TRANSPARENT_CHAT_CHALLENGE_REQUEST)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_CLAN](#SETTINGS_TRANSPARENT_CHAT_CLAN)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_CLAN\_BROADCAST](#SETTINGS_TRANSPARENT_CHAT_CLAN_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_FRIEND](#SETTINGS_TRANSPARENT_CHAT_FRIEND)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_GUEST\_CLAN](#SETTINGS_TRANSPARENT_CHAT_GUEST_CLAN)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_IRON\_GROUP\_BROADCAST](#SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_BROADCAST)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_IRON\_GROUP\_CHAT](#SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_CHAT)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_PRIVATE](#SETTINGS_TRANSPARENT_CHAT_PRIVATE)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_PUBLIC](#SETTINGS_TRANSPARENT_CHAT_PUBLIC)` | Deprecated. |
| `static int` | `[SETTINGS\_TRANSPARENT\_CHAT\_TRADE\_REQUEST](#SETTINGS_TRANSPARENT_CHAT_TRADE_REQUEST)` | Deprecated. |
| `static int` | `[SLAYER\_GOAL\_END](#SLAYER_GOAL_END)` | Deprecated. |
| `static int` | `[SLAYER\_GOAL\_START](#SLAYER_GOAL_START)` | Deprecated. |
| `static int` | `[SLAYER\_TASK\_CREATURE](#SLAYER_TASK_CREATURE)` | Deprecated.
Currently assigned slayer task if SLAYER\_TASK\_SIZE is greater than 0. |
| `static int` | `[SLAYER\_TASK\_LOCATION](#SLAYER_TASK_LOCATION)` | Deprecated.
Assigned slayer task location. |
| `static int` | `[SLAYER\_TASK\_SIZE](#SLAYER_TASK_SIZE)` | Deprecated.
Number of slayer creatures remaining on the assigned task |
| `static int` | `[SLAYER\_UNLOCK\_1](#SLAYER_UNLOCK_1)` | Deprecated.
Slayer unlock bitfields |
| `static int` | `[SLAYER\_UNLOCK\_2](#SLAYER_UNLOCK_2)` | Deprecated. |
| `static int` | `[SMITHING\_GOAL\_END](#SMITHING_GOAL_END)` | Deprecated. |
| `static int` | `[SMITHING\_GOAL\_START](#SMITHING_GOAL_START)` | Deprecated. |
| `static int` | `[SOUND\_EFFECT\_VOLUME](#SOUND_EFFECT_VOLUME)` | Deprecated. |
| `static int` | `[SPECIAL\_ATTACK\_ENABLED](#SPECIAL_ATTACK_ENABLED)` | Deprecated. |
| `static int` | `[SPECIAL\_ATTACK\_PERCENT](#SPECIAL_ATTACK_PERCENT)` | Deprecated. |
| `static int` | `[STRENGTH\_GOAL\_END](#STRENGTH_GOAL_END)` | Deprecated. |
| `static int` | `[STRENGTH\_GOAL\_START](#STRENGTH_GOAL_START)` | Deprecated. |
| `static int` | `[THIEVING\_GOAL\_END](#THIEVING_GOAL_END)` | Deprecated. |
| `static int` | `[THIEVING\_GOAL\_START](#THIEVING_GOAL_START)` | Deprecated. |
| `static int` | `[THRONE\_OF\_MISCELLANIA](#THRONE_OF_MISCELLANIA)` | Deprecated.
0 : not started
greater than 0 : in progress
greater than 99 : completed |
| `static int` | `[WOODCUTTING\_GOAL\_END](#WOODCUTTING_GOAL_END)` | Deprecated. |
| `static int` | `[WOODCUTTING\_GOAL\_START](#WOODCUTTING_GOAL_START)` | Deprecated. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[VarPlayer](#%3Cinit%3E())()` | Deprecated. |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### CANNON\_STATE

```
public static final int CANNON_STATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CANNON_STATE)
- #### CANNON\_AMMO

```
public static final int CANNON_AMMO
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CANNON_AMMO)
- #### CANNON\_COORD

```
public static final int CANNON_COORD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CANNON_COORD)
- #### ATTACK\_STYLE

```
public static final int ATTACK_STYLE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ATTACK_STYLE)
- #### QUEST\_POINTS

```
public static final int QUEST_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.QUEST_POINTS)
- #### DISEASE\_VALUE

```
public static final int DISEASE_VALUE
```

Deprecated.
Seems to start at 50(10 splash) and goes down by 1 every 30 seconds

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.DISEASE_VALUE)
- #### BANK\_TAB

```
public static final int BANK_TAB
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BANK_TAB)
- #### MEMBERSHIP\_DAYS

```
public static final int MEMBERSHIP_DAYS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MEMBERSHIP_DAYS)
- #### SPECIAL\_ATTACK\_PERCENT

```
public static final int SPECIAL_ATTACK_PERCENT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SPECIAL_ATTACK_PERCENT)
- #### SPECIAL\_ATTACK\_ENABLED

```
public static final int SPECIAL_ATTACK_ENABLED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SPECIAL_ATTACK_ENABLED)
- #### IN\_RAID\_PARTY

```
public static final int IN_RAID_PARTY
```

Deprecated.
The ID of the party. This Var is only set in the raid bank area and the raid lobby

This gets set to -1 when the raid starts. This is first set when the first player of the friends chat forms a party
on the recruiting board and it changes again when the first person actually enters the raid.

-1 : Not in a party or in the middle of an ongoing raid
Anything else : This means that your friends chat has a raid party being formed and has not started yet

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.IN_RAID_PARTY)
- #### NMZ\_REWARD\_POINTS

```
public static final int NMZ_REWARD_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.NMZ_REWARD_POINTS)
- #### POISON

```
public static final int POISON
```

Deprecated.
The poisoned status of the player, with negative values indicating the duration of poison or venom protection and
positive values representing the amount of poison or venom damage the player will be taking.

* (-inf, -38): Venom immune for a duration of `(abs(val) - 38) * 30` game ticks (18 seconds per
poison tick), after which point the value will have increased to `-38` and be representing poison
immunity rather than venom immunity
* [-38, 0): Poison immune for a duration of `abs(val) * 30` game ticks (18 seconds per poison tick)
* 0: Not poisoned or immune to poison
* [1, 100]: Poisoned for an amount of `ceil(val / 5.0f)`
* [1000000, inf): Venomed for an amount of `min(20, (val - 999997) * 2)`, that is, an amount starting
at 6 damage, increasing by 2 each time the value increases by one, and capped at 20

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.POISON)
- #### THRONE\_OF\_MISCELLANIA

```
public static final int THRONE_OF_MISCELLANIA
```

Deprecated.
0 : not started
greater than 0 : in progress
greater than 99 : completed

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.THRONE_OF_MISCELLANIA)
- #### CURRENT\_GE\_ITEM

```
public static final int CURRENT_GE_ITEM
```

Deprecated.
Item currently active in the creation of a buy or sell offer

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CURRENT_GE_ITEM)
- #### ATTACK\_GOAL\_START

```
public static final int ATTACK_GOAL_START
```

Deprecated.
Experience tracker goal start.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ATTACK_GOAL_START)
- #### STRENGTH\_GOAL\_START

```
public static final int STRENGTH_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.STRENGTH_GOAL_START)
- #### RANGED\_GOAL\_START

```
public static final int RANGED_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.RANGED_GOAL_START)
- #### MAGIC\_GOAL\_START

```
public static final int MAGIC_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MAGIC_GOAL_START)
- #### DEFENCE\_GOAL\_START

```
public static final int DEFENCE_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.DEFENCE_GOAL_START)
- #### HITPOINTS\_GOAL\_START

```
public static final int HITPOINTS_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HITPOINTS_GOAL_START)
- #### PRAYER\_GOAL\_START

```
public static final int PRAYER_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.PRAYER_GOAL_START)
- #### AGILITY\_GOAL\_START

```
public static final int AGILITY_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.AGILITY_GOAL_START)
- #### HERBLORE\_GOAL\_START

```
public static final int HERBLORE_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HERBLORE_GOAL_START)
- #### THIEVING\_GOAL\_START

```
public static final int THIEVING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.THIEVING_GOAL_START)
- #### CRAFTING\_GOAL\_START

```
public static final int CRAFTING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CRAFTING_GOAL_START)
- #### RUNECRAFT\_GOAL\_START

```
public static final int RUNECRAFT_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.RUNECRAFT_GOAL_START)
- #### MINING\_GOAL\_START

```
public static final int MINING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MINING_GOAL_START)
- #### SMITHING\_GOAL\_START

```
public static final int SMITHING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SMITHING_GOAL_START)
- #### FISHING\_GOAL\_START

```
public static final int FISHING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FISHING_GOAL_START)
- #### COOKING\_GOAL\_START

```
public static final int COOKING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.COOKING_GOAL_START)
- #### FIREMAKING\_GOAL\_START

```
public static final int FIREMAKING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FIREMAKING_GOAL_START)
- #### WOODCUTTING\_GOAL\_START

```
public static final int WOODCUTTING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.WOODCUTTING_GOAL_START)
- #### FLETCHING\_GOAL\_START

```
public static final int FLETCHING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FLETCHING_GOAL_START)
- #### SLAYER\_GOAL\_START

```
public static final int SLAYER_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_GOAL_START)
- #### FARMING\_GOAL\_START

```
public static final int FARMING_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FARMING_GOAL_START)
- #### CONSTRUCTION\_GOAL\_START

```
public static final int CONSTRUCTION_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CONSTRUCTION_GOAL_START)
- #### HUNTER\_GOAL\_START

```
public static final int HUNTER_GOAL_START
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HUNTER_GOAL_START)
- #### ATTACK\_GOAL\_END

```
public static final int ATTACK_GOAL_END
```

Deprecated.
Experience tracker goal end.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ATTACK_GOAL_END)
- #### STRENGTH\_GOAL\_END

```
public static final int STRENGTH_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.STRENGTH_GOAL_END)
- #### RANGED\_GOAL\_END

```
public static final int RANGED_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.RANGED_GOAL_END)
- #### MAGIC\_GOAL\_END

```
public static final int MAGIC_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MAGIC_GOAL_END)
- #### DEFENCE\_GOAL\_END

```
public static final int DEFENCE_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.DEFENCE_GOAL_END)
- #### HITPOINTS\_GOAL\_END

```
public static final int HITPOINTS_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HITPOINTS_GOAL_END)
- #### PRAYER\_GOAL\_END

```
public static final int PRAYER_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.PRAYER_GOAL_END)
- #### AGILITY\_GOAL\_END

```
public static final int AGILITY_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.AGILITY_GOAL_END)
- #### HERBLORE\_GOAL\_END

```
public static final int HERBLORE_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HERBLORE_GOAL_END)
- #### THIEVING\_GOAL\_END

```
public static final int THIEVING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.THIEVING_GOAL_END)
- #### CRAFTING\_GOAL\_END

```
public static final int CRAFTING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CRAFTING_GOAL_END)
- #### RUNECRAFT\_GOAL\_END

```
public static final int RUNECRAFT_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.RUNECRAFT_GOAL_END)
- #### MINING\_GOAL\_END

```
public static final int MINING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MINING_GOAL_END)
- #### SMITHING\_GOAL\_END

```
public static final int SMITHING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SMITHING_GOAL_END)
- #### FISHING\_GOAL\_END

```
public static final int FISHING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FISHING_GOAL_END)
- #### COOKING\_GOAL\_END

```
public static final int COOKING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.COOKING_GOAL_END)
- #### FIREMAKING\_GOAL\_END

```
public static final int FIREMAKING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FIREMAKING_GOAL_END)
- #### WOODCUTTING\_GOAL\_END

```
public static final int WOODCUTTING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.WOODCUTTING_GOAL_END)
- #### FLETCHING\_GOAL\_END

```
public static final int FLETCHING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FLETCHING_GOAL_END)
- #### SLAYER\_GOAL\_END

```
public static final int SLAYER_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_GOAL_END)
- #### FARMING\_GOAL\_END

```
public static final int FARMING_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.FARMING_GOAL_END)
- #### CONSTRUCTION\_GOAL\_END

```
public static final int CONSTRUCTION_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CONSTRUCTION_GOAL_END)
- #### HUNTER\_GOAL\_END

```
public static final int HUNTER_GOAL_END
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HUNTER_GOAL_END)
- #### BIRD\_HOUSE\_MEADOW\_NORTH

```
public static final int BIRD_HOUSE_MEADOW_NORTH
```

Deprecated.
Bird house states

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BIRD_HOUSE_MEADOW_NORTH)
- #### BIRD\_HOUSE\_MEADOW\_SOUTH

```
public static final int BIRD_HOUSE_MEADOW_SOUTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BIRD_HOUSE_MEADOW_SOUTH)
- #### BIRD\_HOUSE\_VALLEY\_NORTH

```
public static final int BIRD_HOUSE_VALLEY_NORTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BIRD_HOUSE_VALLEY_NORTH)
- #### BIRD\_HOUSE\_VALLEY\_SOUTH

```
public static final int BIRD_HOUSE_VALLEY_SOUTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BIRD_HOUSE_VALLEY_SOUTH)
- #### SLAYER\_UNLOCK\_1

```
public static final int SLAYER_UNLOCK_1
```

Deprecated.
Slayer unlock bitfields

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_UNLOCK_1)
- #### SLAYER\_UNLOCK\_2

```
public static final int SLAYER_UNLOCK_2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_UNLOCK_2)
- #### MUSIC\_VOLUME

```
public static final int MUSIC_VOLUME
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MUSIC_VOLUME)
- #### SOUND\_EFFECT\_VOLUME

```
public static final int SOUND_EFFECT_VOLUME
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SOUND_EFFECT_VOLUME)
- #### AREA\_EFFECT\_VOLUME

```
public static final int AREA_EFFECT_VOLUME
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.AREA_EFFECT_VOLUME)
- #### MOUSE\_BUTTONS

```
public static final int MOUSE_BUTTONS
```

Deprecated.
0 = 2 buttons, 1 = 1 button

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.MOUSE_BUTTONS)
- #### HP\_HUD\_NPC\_ID

```
public static final int HP_HUD_NPC_ID
```

Deprecated.
`NpcID` for the HP HUD

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.HP_HUD_NPC_ID)
- #### CLOG\_LOGGED

```
public static final int CLOG_LOGGED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CLOG_LOGGED)
- #### CLOG\_TOTAL

```
public static final int CLOG_TOTAL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CLOG_TOTAL)
- #### SETTINGS\_OPAQUE\_CHAT\_PUBLIC

```
public static final int SETTINGS_OPAQUE_CHAT_PUBLIC
```

Deprecated.
Colors for chat messages

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_PUBLIC)
- #### SETTINGS\_OPAQUE\_CHAT\_PRIVATE

```
public static final int SETTINGS_OPAQUE_CHAT_PRIVATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_PRIVATE)
- #### SETTINGS\_OPAQUE\_CHAT\_AUTO

```
public static final int SETTINGS_OPAQUE_CHAT_AUTO
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_AUTO)
- #### SETTINGS\_OPAQUE\_CHAT\_BROADCAST

```
public static final int SETTINGS_OPAQUE_CHAT_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_BROADCAST)
- #### SETTINGS\_OPAQUE\_CHAT\_FRIEND

```
public static final int SETTINGS_OPAQUE_CHAT_FRIEND
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_FRIEND)
- #### SETTINGS\_OPAQUE\_CHAT\_CLAN

```
public static final int SETTINGS_OPAQUE_CHAT_CLAN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_CLAN)
- #### SETTINGS\_OPAQUE\_CHAT\_GUEST\_CLAN

```
public static final int SETTINGS_OPAQUE_CHAT_GUEST_CLAN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_GUEST_CLAN)
- #### SETTINGS\_OPAQUE\_CHAT\_CLAN\_BROADCAST

```
public static final int SETTINGS_OPAQUE_CHAT_CLAN_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_CLAN_BROADCAST)
- #### SETTINGS\_OPAQUE\_CHAT\_IRON\_GROUP\_CHAT

```
public static final int SETTINGS_OPAQUE_CHAT_IRON_GROUP_CHAT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_IRON_GROUP_CHAT)
- #### SETTINGS\_OPAQUE\_CHAT\_IRON\_GROUP\_BROADCAST

```
public static final int SETTINGS_OPAQUE_CHAT_IRON_GROUP_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_IRON_GROUP_BROADCAST)
- #### SETTINGS\_OPAQUE\_CHAT\_TRADE\_REQUEST

```
public static final int SETTINGS_OPAQUE_CHAT_TRADE_REQUEST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_TRADE_REQUEST)
- #### SETTINGS\_OPAQUE\_CHAT\_CHALLENGE\_REQUEST

```
public static final int SETTINGS_OPAQUE_CHAT_CHALLENGE_REQUEST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_OPAQUE_CHAT_CHALLENGE_REQUEST)
- #### SETTINGS\_TRANSPARENT\_CHAT\_PUBLIC

```
public static final int SETTINGS_TRANSPARENT_CHAT_PUBLIC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_PUBLIC)
- #### SETTINGS\_TRANSPARENT\_CHAT\_PRIVATE

```
public static final int SETTINGS_TRANSPARENT_CHAT_PRIVATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_PRIVATE)
- #### SETTINGS\_TRANSPARENT\_CHAT\_AUTO

```
public static final int SETTINGS_TRANSPARENT_CHAT_AUTO
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_AUTO)
- #### SETTINGS\_TRANSPARENT\_CHAT\_BROADCAST

```
public static final int SETTINGS_TRANSPARENT_CHAT_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_BROADCAST)
- #### SETTINGS\_TRANSPARENT\_CHAT\_FRIEND

```
public static final int SETTINGS_TRANSPARENT_CHAT_FRIEND
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_FRIEND)
- #### SETTINGS\_TRANSPARENT\_CHAT\_CLAN

```
public static final int SETTINGS_TRANSPARENT_CHAT_CLAN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_CLAN)
- #### SETTINGS\_TRANSPARENT\_CHAT\_GUEST\_CLAN

```
public static final int SETTINGS_TRANSPARENT_CHAT_GUEST_CLAN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_GUEST_CLAN)
- #### SETTINGS\_TRANSPARENT\_CHAT\_CLAN\_BROADCAST

```
public static final int SETTINGS_TRANSPARENT_CHAT_CLAN_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_CLAN_BROADCAST)
- #### SETTINGS\_TRANSPARENT\_CHAT\_IRON\_GROUP\_CHAT

```
public static final int SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_CHAT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_CHAT)
- #### SETTINGS\_TRANSPARENT\_CHAT\_IRON\_GROUP\_BROADCAST

```
public static final int SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_BROADCAST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_IRON_GROUP_BROADCAST)
- #### SETTINGS\_TRANSPARENT\_CHAT\_TRADE\_REQUEST

```
public static final int SETTINGS_TRANSPARENT_CHAT_TRADE_REQUEST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_TRADE_REQUEST)
- #### SETTINGS\_TRANSPARENT\_CHAT\_CHALLENGE\_REQUEST

```
public static final int SETTINGS_TRANSPARENT_CHAT_CHALLENGE_REQUEST
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SETTINGS_TRANSPARENT_CHAT_CHALLENGE_REQUEST)
- #### LAST\_HOME\_TELEPORT

```
public static final int LAST_HOME_TELEPORT
```

Deprecated.
The difference, measured in minutes, between the time home teleport spell was last used and midnight, January 1, 1970 UTC.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.LAST_HOME_TELEPORT)
- #### CHARGE\_GOD\_SPELL

```
public static final int CHARGE_GOD_SPELL
```

Deprecated.
Charge spell duration
Value \* 2 = Remaining game ticks on buff
E.g. value of 50 means buff will expire in 100 ticks.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.CHARGE_GOD_SPELL)
- #### LAST\_MINIGAME\_TELEPORT

```
public static final int LAST_MINIGAME_TELEPORT
```

Deprecated.
The difference, measured in minutes, between the time minigame teleport was last used and midnight, January 1, 1970 UTC.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.LAST_MINIGAME_TELEPORT)
- #### SLAYER\_TASK\_SIZE

```
public static final int SLAYER_TASK_SIZE
```

Deprecated.
Number of slayer creatures remaining on the assigned task

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_TASK_SIZE)
- #### SLAYER\_TASK\_CREATURE

```
public static final int SLAYER_TASK_CREATURE
```

Deprecated.
Currently assigned slayer task if SLAYER\_TASK\_SIZE is greater than 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_TASK_CREATURE)
- #### SLAYER\_TASK\_LOCATION

```
public static final int SLAYER_TASK_LOCATION
```

Deprecated.
Assigned slayer task location.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.SLAYER_TASK_LOCATION)
- #### BUFF\_BAR\_WC\_GROUP\_BONUS

```
public static final int BUFF_BAR_WC_GROUP_BONUS
```

Deprecated.
Determines whether the woodcutting group bonus should be displayed on the buff bar or not.
96 = displayed (including the woodcutting guild).
0 = not displayed (after login until cutting a tree except normal trees or trees grown through farming).
-1 = not displayed (including normal trees or trees grown through farming).

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.BUFF_BAR_WC_GROUP_BONUS)
- #### DIZANAS\_QUIVER\_ITEM\_COUNT

```
public static final int DIZANAS_QUIVER_ITEM_COUNT
```

Deprecated.
The amount of ammo in Dizana's quiver's inventory slot.
0 means the quiver is empty.

See Also:
[`DIZANAS_QUIVER_ITEM_ID`](#DIZANAS_QUIVER_ITEM_ID),
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.DIZANAS_QUIVER_ITEM_COUNT)
- #### DIZANAS\_QUIVER\_ITEM\_ID

```
public static final int DIZANAS_QUIVER_ITEM_ID
```

Deprecated.
The item ID of the ammo in Dizana's quiver inventory slot.
-1 means the quiver is empty.

See Also:
[`DIZANAS_QUIVER_ITEM_COUNT`](#DIZANAS_QUIVER_ITEM_COUNT),
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.DIZANAS_QUIVER_ITEM_ID)
- #### ESSENCE\_POUCH\_MEDIUM\_DEGRADE

```
public static final int ESSENCE_POUCH_MEDIUM_DEGRADE
```

Deprecated.
Runecraft Essence Pouch degrade states

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ESSENCE_POUCH_MEDIUM_DEGRADE)
- #### ESSENCE\_POUCH\_LARGE\_DEGRADE

```
public static final int ESSENCE_POUCH_LARGE_DEGRADE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ESSENCE_POUCH_LARGE_DEGRADE)
- #### ESSENCE\_POUCH\_GIANT\_DEGRADE

```
public static final int ESSENCE_POUCH_GIANT_DEGRADE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.ESSENCE_POUCH_GIANT_DEGRADE)
- #### RAIDS\_PERSONAL\_POINTS

```
public static final int RAIDS_PERSONAL_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.VarPlayer.RAIDS_PERSONAL_POINTS)

+ ### Constructor Detail

- #### VarPlayer

```
public VarPlayer()
```

Deprecated.