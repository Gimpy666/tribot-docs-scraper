# Varbits (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Varbits.html

**Package:** Packagenet.runelite.api

**Description:** These are the expected values:
 0 = No bars being processed
 1 = Ores are being processed on the conveyor belt, bar dispenser cannot be checked
 2 = Bars are cooling down
 3 = Bars can be collected...

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.Varbits

* ---

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public final class Varbits
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Deprecated.
Server controlled "content-developer" integers.

See Also:
`These differ from a in that VarBits can be
less than 32 bits. One or more VarBits can be assigned to a
backing VarPlayer, each with a static range of bits that it is
allowed to access. This allows a more compact representation
of small values, like booleans`

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[ACCOUNT\_TYPE](#ACCOUNT_TYPE)` | Deprecated.
The player's account type. |
| `static int` | `[ANTIFIRE](#ANTIFIRE)` | Deprecated.
Antifire timer
Number of game ticks remaining on antifire in intervals of 30; for a value X there are 30 \* X game ticks remaining. |
| `static int` | `[AUTOWEED](#AUTOWEED)` | Deprecated.
Automatically weed farming patches |
| `static int` | `[BA\_GC](#BA_GC)` | Deprecated. |
| `static int` | `[BANK\_ITEM\_OPTIONS](#BANK_ITEM_OPTIONS)` | Deprecated. |
| `static int` | `[BANK\_LEAVEPLACEHOLDERS](#BANK_LEAVEPLACEHOLDERS)` | Deprecated. |
| `static int` | `[BANK\_QUANTITY\_TYPE](#BANK_QUANTITY_TYPE)` | Deprecated. |
| `static int` | `[BANK\_REARRANGE\_MODE](#BANK_REARRANGE_MODE)` | Deprecated. |
| `static int` | `[BANK\_REQUESTEDQUANTITY](#BANK_REQUESTEDQUANTITY)` | Deprecated. |
| `static int` | `[BANK\_TAB\_EIGHT\_COUNT](#BANK_TAB_EIGHT_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_FIVE\_COUNT](#BANK_TAB_FIVE_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_FOUR\_COUNT](#BANK_TAB_FOUR_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_NINE\_COUNT](#BANK_TAB_NINE_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_ONE\_COUNT](#BANK_TAB_ONE_COUNT)` | Deprecated.
Amount of items in each bank tab |
| `static int` | `[BANK\_TAB\_SEVEN\_COUNT](#BANK_TAB_SEVEN_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_SIX\_COUNT](#BANK_TAB_SIX_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_THREE\_COUNT](#BANK_TAB_THREE_COUNT)` | Deprecated. |
| `static int` | `[BANK\_TAB\_TWO\_COUNT](#BANK_TAB_TWO_COUNT)` | Deprecated. |
| `static int` | `[BAR\_DISPENSER](#BAR_DISPENSER)` | Deprecated.
Blast Furnace Bar Dispenser |
| `static int` | `[BARROWS\_KILLED\_AHRIM](#BARROWS_KILLED_AHRIM)` | Deprecated.
Barrows |
| `static int` | `[BARROWS\_KILLED\_DHAROK](#BARROWS_KILLED_DHAROK)` | Deprecated. |
| `static int` | `[BARROWS\_KILLED\_GUTHAN](#BARROWS_KILLED_GUTHAN)` | Deprecated. |
| `static int` | `[BARROWS\_KILLED\_KARIL](#BARROWS_KILLED_KARIL)` | Deprecated. |
| `static int` | `[BARROWS\_KILLED\_TORAG](#BARROWS_KILLED_TORAG)` | Deprecated. |
| `static int` | `[BARROWS\_KILLED\_VERAC](#BARROWS_KILLED_VERAC)` | Deprecated. |
| `static int` | `[BARROWS\_NPCS\_SLAIN](#BARROWS_NPCS_SLAIN)` | Deprecated. |
| `static int` | `[BARROWS\_REWARD\_POTENTIAL](#BARROWS_REWARD_POTENTIAL)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_ADAMANTITE\_BAR](#BLAST_FURNACE_ADAMANTITE_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_ADAMANTITE\_ORE](#BLAST_FURNACE_ADAMANTITE_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_BRONZE\_BAR](#BLAST_FURNACE_BRONZE_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_COAL](#BLAST_FURNACE_COAL)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_COFFER](#BLAST_FURNACE_COFFER)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_COPPER\_ORE](#BLAST_FURNACE_COPPER_ORE)` | Deprecated.
Blast Furnace |
| `static int` | `[BLAST\_FURNACE\_GOLD\_BAR](#BLAST_FURNACE_GOLD_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_GOLD\_ORE](#BLAST_FURNACE_GOLD_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_IRON\_BAR](#BLAST_FURNACE_IRON_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_IRON\_ORE](#BLAST_FURNACE_IRON_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_MITHRIL\_BAR](#BLAST_FURNACE_MITHRIL_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_MITHRIL\_ORE](#BLAST_FURNACE_MITHRIL_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_RUNITE\_BAR](#BLAST_FURNACE_RUNITE_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_RUNITE\_ORE](#BLAST_FURNACE_RUNITE_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_SILVER\_BAR](#BLAST_FURNACE_SILVER_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_SILVER\_ORE](#BLAST_FURNACE_SILVER_ORE)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_STEEL\_BAR](#BLAST_FURNACE_STEEL_BAR)` | Deprecated. |
| `static int` | `[BLAST\_FURNACE\_TIN\_ORE](#BLAST_FURNACE_TIN_ORE)` | Deprecated. |
| `static int` | `[BLAST\_MINE\_ADAMANTITE](#BLAST_MINE_ADAMANTITE)` | Deprecated. |
| `static int` | `[BLAST\_MINE\_COAL](#BLAST_MINE_COAL)` | Deprecated.
Blast Mine |
| `static int` | `[BLAST\_MINE\_GOLD](#BLAST_MINE_GOLD)` | Deprecated. |
| `static int` | `[BLAST\_MINE\_MITHRIL](#BLAST_MINE_MITHRIL)` | Deprecated. |
| `static int` | `[BLAST\_MINE\_RUNITE](#BLAST_MINE_RUNITE)` | Deprecated. |
| `static int` | `[BOSS\_HEALTH\_CURRENT](#BOSS_HEALTH_CURRENT)` | Deprecated.
Boss health bar info |
| `static int` | `[BOSS\_HEALTH\_MAXIMUM](#BOSS_HEALTH_MAXIMUM)` | Deprecated. |
| `static int` | `[BOSS\_HEALTH\_OVERLAY](#BOSS_HEALTH_OVERLAY)` | Deprecated.
Show boss health overlay setting
0 = on
1 = off |
| `static int` | `[BUFF\_GOADING\_POTION](#BUFF_GOADING_POTION)` | Deprecated. |
| `static int` | `[BUFF\_PRAYER\_REGENERATION](#BUFF_PRAYER_REGENERATION)` | Deprecated. |
| `static int` | `[BUFF\_STAT\_BOOST](#BUFF_STAT_BOOST)` | Deprecated.
How many salt stat boost refreshes the player has remaining. |
| `static int` | `[BURTHORPE\_SLAYER\_MASTER](#BURTHORPE_SLAYER_MASTER)` | Deprecated.
The slayer master which is present at Burthorpe. |
| `static int` | `[CHAT\_SCROLLBAR\_ON\_LEFT](#CHAT_SCROLLBAR_ON_LEFT)` | Deprecated.
If scrollbar in resizable mode chat is on the left |
| `static int` | `[COLLECTION\_LOG\_NOTIFICATION](#COLLECTION_LOG_NOTIFICATION)` | Deprecated.
Collection Log notification settings whenever a new item is added |
| `static int` | `[COLOSSAL\_WYRM\_COURSE\_ADVANCED](#COLOSSAL_WYRM_COURSE_ADVANCED)` | Deprecated.
The player's progress value for the colossal wyrm advanced agility course. |
| `static int` | `[COLOSSAL\_WYRM\_COURSE\_BASIC](#COLOSSAL_WYRM_COURSE_BASIC)` | Deprecated.
The player's progress value for the colossal wyrm advanced basic course. |
| `static int` | `[COLOSSEUM\_DOOM](#COLOSSEUM_DOOM)` | Deprecated.
The amount of Doom stacks received in the Fortis Colosseum. |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_EASY](#COMBAT_ACHIEVEMENT_TIER_EASY)` | Deprecated.
Combat Achievement tier completion variables

2 = completed |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_ELITE](#COMBAT_ACHIEVEMENT_TIER_ELITE)` | Deprecated. |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_GRANDMASTER](#COMBAT_ACHIEVEMENT_TIER_GRANDMASTER)` | Deprecated. |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_HARD](#COMBAT_ACHIEVEMENT_TIER_HARD)` | Deprecated. |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_MASTER](#COMBAT_ACHIEVEMENT_TIER_MASTER)` | Deprecated. |
| `static int` | `[COMBAT\_ACHIEVEMENT\_TIER\_MEDIUM](#COMBAT_ACHIEVEMENT_TIER_MEDIUM)` | Deprecated. |
| `static int` | `[COMBAT\_ACHIEVEMENTS\_POPUP](#COMBAT_ACHIEVEMENTS_POPUP)` | Deprecated.
Combat Achievements popup settings whenever a new task is completed |
| `static int` | `[COMBAT\_TASK\_EASY](#COMBAT_TASK_EASY)` | Deprecated. |
| `static int` | `[COMBAT\_TASK\_ELITE](#COMBAT_TASK_ELITE)` | Deprecated. |
| `static int` | `[COMBAT\_TASK\_GRANDMASTER](#COMBAT_TASK_GRANDMASTER)` | Deprecated. |
| `static int` | `[COMBAT\_TASK\_HARD](#COMBAT_TASK_HARD)` | Deprecated. |
| `static int` | `[COMBAT\_TASK\_MASTER](#COMBAT_TASK_MASTER)` | Deprecated. |
| `static int` | `[COMBAT\_TASK\_MEDIUM](#COMBAT_TASK_MEDIUM)` | Deprecated. |
| `static int` | `[CORP\_DAMAGE](#CORP_DAMAGE)` | Deprecated.
Corp beast damage |
| `static int` | `[CORRUPTION\_COOLDOWN](#CORRUPTION_COOLDOWN)` | Deprecated. |
| `static int` | `[COX\_OVERLOAD\_REFRESHES\_REMAINING](#COX_OVERLOAD_REFRESHES_REMAINING)` | Deprecated.
How many Chambers of Xeric overload refreshes the player has remaining. |
| `static int` | `[CURRENT\_BANK\_TAB](#CURRENT_BANK_TAB)` | Deprecated. |
| `static int` | `[CURSE\_OF\_THE\_MOONS](#CURSE_OF_THE_MOONS)` | Deprecated.
The amount of Curse of the Moons stacks received when fighting the Blue Moon or Eclipse Moon. |
| `static int` | `[DAILY\_ARROWS\_STATE](#DAILY_ARROWS_STATE)` | Deprecated. |
| `static int` | `[DAILY\_BONEMEAL\_STATE](#DAILY_BONEMEAL_STATE)` | Deprecated.
This varbit tracks how much bonemeal has been redeemed from Robin
The player gets 13 for each diary completed above and including Medium, for a maxiumum of 39 |
| `static int` | `[DAILY\_DYNAMITE\_COLLECTED](#DAILY_DYNAMITE_COLLECTED)` | Deprecated. |
| `static int` | `[DAILY\_ESSENCE\_COLLECTED](#DAILY_ESSENCE_COLLECTED)` | Deprecated. |
| `static int` | `[DAILY\_FLAX\_STATE](#DAILY_FLAX_STATE)` | Deprecated. |
| `static int` | `[DAILY\_HERB\_BOXES\_COLLECTED](#DAILY_HERB_BOXES_COLLECTED)` | Deprecated.
Daily Tasks =Collection availability) |
| `static int` | `[DAILY\_RUNES\_COLLECTED](#DAILY_RUNES_COLLECTED)` | Deprecated. |
| `static int` | `[DAILY\_SAND\_COLLECTED](#DAILY_SAND_COLLECTED)` | Deprecated. |
| `static int` | `[DAILY\_STAVES\_COLLECTED](#DAILY_STAVES_COLLECTED)` | Deprecated. |
| `static int` | `[DEATH\_CHARGE](#DEATH_CHARGE)` | Deprecated. |
| `static int` | `[DEATH\_CHARGE\_COOLDOWN](#DEATH_CHARGE_COOLDOWN)` | Deprecated. |
| `static int` | `[DEFENSIVE\_CASTING\_MODE](#DEFENSIVE_CASTING_MODE)` | Deprecated.
Defensive casting mode |
| `static int` | `[DIARY\_ARDOUGNE\_EASY](#DIARY_ARDOUGNE_EASY)` | Deprecated.
Diary Entries |
| `static int` | `[DIARY\_ARDOUGNE\_ELITE](#DIARY_ARDOUGNE_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_ARDOUGNE\_HARD](#DIARY_ARDOUGNE_HARD)` | Deprecated. |
| `static int` | `[DIARY\_ARDOUGNE\_MEDIUM](#DIARY_ARDOUGNE_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_DESERT\_EASY](#DIARY_DESERT_EASY)` | Deprecated. |
| `static int` | `[DIARY\_DESERT\_ELITE](#DIARY_DESERT_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_DESERT\_HARD](#DIARY_DESERT_HARD)` | Deprecated. |
| `static int` | `[DIARY\_DESERT\_MEDIUM](#DIARY_DESERT_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_FALADOR\_EASY](#DIARY_FALADOR_EASY)` | Deprecated. |
| `static int` | `[DIARY\_FALADOR\_ELITE](#DIARY_FALADOR_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_FALADOR\_HARD](#DIARY_FALADOR_HARD)` | Deprecated. |
| `static int` | `[DIARY\_FALADOR\_MEDIUM](#DIARY_FALADOR_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_FREMENNIK\_EASY](#DIARY_FREMENNIK_EASY)` | Deprecated. |
| `static int` | `[DIARY\_FREMENNIK\_ELITE](#DIARY_FREMENNIK_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_FREMENNIK\_HARD](#DIARY_FREMENNIK_HARD)` | Deprecated. |
| `static int` | `[DIARY\_FREMENNIK\_MEDIUM](#DIARY_FREMENNIK_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_KANDARIN\_EASY](#DIARY_KANDARIN_EASY)` | Deprecated. |
| `static int` | `[DIARY\_KANDARIN\_ELITE](#DIARY_KANDARIN_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_KANDARIN\_HARD](#DIARY_KANDARIN_HARD)` | Deprecated. |
| `static int` | `[DIARY\_KANDARIN\_MEDIUM](#DIARY_KANDARIN_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_KARAMJA\_EASY](#DIARY_KARAMJA_EASY)` | Deprecated. |
| `static int` | `[DIARY\_KARAMJA\_ELITE](#DIARY_KARAMJA_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_KARAMJA\_HARD](#DIARY_KARAMJA_HARD)` | Deprecated. |
| `static int` | `[DIARY\_KARAMJA\_MEDIUM](#DIARY_KARAMJA_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_KOUREND\_EASY](#DIARY_KOUREND_EASY)` | Deprecated. |
| `static int` | `[DIARY\_KOUREND\_ELITE](#DIARY_KOUREND_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_KOUREND\_HARD](#DIARY_KOUREND_HARD)` | Deprecated. |
| `static int` | `[DIARY\_KOUREND\_MEDIUM](#DIARY_KOUREND_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_LUMBRIDGE\_EASY](#DIARY_LUMBRIDGE_EASY)` | Deprecated. |
| `static int` | `[DIARY\_LUMBRIDGE\_ELITE](#DIARY_LUMBRIDGE_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_LUMBRIDGE\_HARD](#DIARY_LUMBRIDGE_HARD)` | Deprecated. |
| `static int` | `[DIARY\_LUMBRIDGE\_MEDIUM](#DIARY_LUMBRIDGE_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_MORYTANIA\_EASY](#DIARY_MORYTANIA_EASY)` | Deprecated. |
| `static int` | `[DIARY\_MORYTANIA\_ELITE](#DIARY_MORYTANIA_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_MORYTANIA\_HARD](#DIARY_MORYTANIA_HARD)` | Deprecated. |
| `static int` | `[DIARY\_MORYTANIA\_MEDIUM](#DIARY_MORYTANIA_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_VARROCK\_EASY](#DIARY_VARROCK_EASY)` | Deprecated. |
| `static int` | `[DIARY\_VARROCK\_ELITE](#DIARY_VARROCK_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_VARROCK\_HARD](#DIARY_VARROCK_HARD)` | Deprecated. |
| `static int` | `[DIARY\_VARROCK\_MEDIUM](#DIARY_VARROCK_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_WESTERN\_EASY](#DIARY_WESTERN_EASY)` | Deprecated. |
| `static int` | `[DIARY\_WESTERN\_ELITE](#DIARY_WESTERN_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_WESTERN\_HARD](#DIARY_WESTERN_HARD)` | Deprecated. |
| `static int` | `[DIARY\_WESTERN\_MEDIUM](#DIARY_WESTERN_MEDIUM)` | Deprecated. |
| `static int` | `[DIARY\_WILDERNESS\_EASY](#DIARY_WILDERNESS_EASY)` | Deprecated. |
| `static int` | `[DIARY\_WILDERNESS\_ELITE](#DIARY_WILDERNESS_ELITE)` | Deprecated. |
| `static int` | `[DIARY\_WILDERNESS\_HARD](#DIARY_WILDERNESS_HARD)` | Deprecated. |
| `static int` | `[DIARY\_WILDERNESS\_MEDIUM](#DIARY_WILDERNESS_MEDIUM)` | Deprecated. |
| `static int` | `[DISABLE\_LEVEL\_UP\_INTERFACE](#DISABLE_LEVEL_UP_INTERFACE)` | Deprecated.
Whether the level up interface is disabled |
| `static int` | `[DIVINE\_BASTION](#DIVINE_BASTION)` | Deprecated. |
| `static int` | `[DIVINE\_BATTLEMAGE](#DIVINE_BATTLEMAGE)` | Deprecated. |
| `static int` | `[DIVINE\_MAGIC](#DIVINE_MAGIC)` | Deprecated. |
| `static int` | `[DIVINE\_RANGING](#DIVINE_RANGING)` | Deprecated. |
| `static int` | `[DIVINE\_SUPER\_ATTACK](#DIVINE_SUPER_ATTACK)` | Deprecated.
Divine effect timers
Number of game ticks remaining on a divine effect. |
| `static int` | `[DIVINE\_SUPER\_COMBAT](#DIVINE_SUPER_COMBAT)` | Deprecated. |
| `static int` | `[DIVINE\_SUPER\_DEFENCE](#DIVINE_SUPER_DEFENCE)` | Deprecated. |
| `static int` | `[DIVINE\_SUPER\_STRENGTH](#DIVINE_SUPER_STRENGTH)` | Deprecated. |
| `static int` | `[DRAGONFIRE\_SHIELD\_COOLDOWN](#DRAGONFIRE_SHIELD_COOLDOWN)` | Deprecated.
Dragonfire shield cooldown |
| `static int` | `[DRIFT\_NET\_COLLECT](#DRIFT_NET_COLLECT)` | Deprecated.
Drift net collect interface |
| `static int` | `[EQUIPPED\_WEAPON\_TYPE](#EQUIPPED_WEAPON_TYPE)` | Deprecated.
Equipped weapon type |
| `static int` | `[ESSENCE\_POUCH\_COLOSSAL\_AMOUNT](#ESSENCE_POUCH_COLOSSAL_AMOUNT)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_COLOSSAL\_DEGRADE](#ESSENCE_POUCH_COLOSSAL_DEGRADE)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_GIANT\_AMOUNT](#ESSENCE_POUCH_GIANT_AMOUNT)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_LARGE\_AMOUNT](#ESSENCE_POUCH_LARGE_AMOUNT)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_MEDIUM\_AMOUNT](#ESSENCE_POUCH_MEDIUM_AMOUNT)` | Deprecated. |
| `static int` | `[ESSENCE\_POUCH\_SMALL\_AMOUNT](#ESSENCE_POUCH_SMALL_AMOUNT)` | Deprecated.
Essence pouches |
| `static int` | `[EXPERIENCE\_DROP\_COLOR](#EXPERIENCE_DROP_COLOR)` | Deprecated.
Experience drop color |
| `static int` | `[EXPERIENCE\_TRACKER\_COUNTER](#EXPERIENCE_TRACKER_COUNTER)` | Deprecated. |
| `static int` | `[EXPERIENCE\_TRACKER\_POSITION](#EXPERIENCE_TRACKER_POSITION)` | Deprecated.
Experience tracker |
| `static int` | `[EXPERIENCE\_TRACKER\_PROGRESS\_BAR](#EXPERIENCE_TRACKER_PROGRESS_BAR)` | Deprecated. |
| `static int` | `[EXPLORER\_RING\_ALCHS](#EXPLORER_RING_ALCHS)` | Deprecated. |
| `static int` | `[EXPLORER\_RING\_ALCHTYPE](#EXPLORER_RING_ALCHTYPE)` | Deprecated.
Explorer ring |
| `static int` | `[EXPLORER\_RING\_RUNENERGY](#EXPLORER_RING_RUNENERGY)` | Deprecated. |
| `static int` | `[EXPLORER\_RING\_TELEPORTS](#EXPLORER_RING_TELEPORTS)` | Deprecated. |
| `static int` | `[FAIR\_RING\_LAST\_DESTINATION](#FAIR_RING_LAST_DESTINATION)` | Deprecated.
Fairy Ring |
| `static int` | `[FAIRY\_RIGH\_DIAL\_ILJK](#FAIRY_RIGH_DIAL_ILJK)` | Deprecated. |
| `static int` | `[FAIRY\_RING\_DIAL\_ADCB](#FAIRY_RING_DIAL_ADCB)` | Deprecated. |
| `static int` | `[FAIRY\_RING\_DIAL\_PSRQ](#FAIRY_RING_DIAL_PSRQ)` | Deprecated. |
| `static int` | `[FARMERS\_AFFINITY](#FARMERS_AFFINITY)` | Deprecated.
Farmer's Affinity effect timer
Number of game ticks remaining on Farmer's Affinity effect in intervals of 20; for a value X there are 20 \* X game ticks remaining. |
| `static int` | `[FARMING\_4771](#FARMING_4771)` | Deprecated.
Transmog controllers for farming |
| `static int` | `[FARMING\_4772](#FARMING_4772)` | Deprecated. |
| `static int` | `[FARMING\_4773](#FARMING_4773)` | Deprecated. |
| `static int` | `[FARMING\_4774](#FARMING_4774)` | Deprecated. |
| `static int` | `[FARMING\_4775](#FARMING_4775)` | Deprecated. |
| `static int` | `[FARMING\_7904](#FARMING_7904)` | Deprecated. |
| `static int` | `[FARMING\_7905](#FARMING_7905)` | Deprecated. |
| `static int` | `[FARMING\_7906](#FARMING_7906)` | Deprecated. |
| `static int` | `[FARMING\_7907](#FARMING_7907)` | Deprecated. |
| `static int` | `[FARMING\_7908](#FARMING_7908)` | Deprecated. |
| `static int` | `[FARMING\_7909](#FARMING_7909)` | Deprecated. |
| `static int` | `[FARMING\_7910](#FARMING_7910)` | Deprecated. |
| `static int` | `[FARMING\_7911](#FARMING_7911)` | Deprecated. |
| `static int` | `[FARMING\_7912](#FARMING_7912)` | Deprecated. |
| `static int` | `[FIRE\_PIT\_GIANT\_MOLE](#FIRE_PIT_GIANT_MOLE)` | Deprecated.
Making Friends with My Arm fire pits |
| `static int` | `[FIRE\_PIT\_LUMBRIDGE\_SWAMP](#FIRE_PIT_LUMBRIDGE_SWAMP)` | Deprecated. |
| `static int` | `[FIRE\_PIT\_MOS\_LE\_HARMLESS](#FIRE_PIT_MOS_LE_HARMLESS)` | Deprecated. |
| `static int` | `[FISHING\_TRAWLER\_ACTIVITY](#FISHING_TRAWLER_ACTIVITY)` | Deprecated.
Fishing Trawler
FISHING\_TRAWLER\_ACTIVITY Expected values: 0-255 |
| `static int` | `[FOSSIL\_ISLAND\_WYVERN\_DISABLE](#FOSSIL_ISLAND_WYVERN_DISABLE)` | Deprecated. |
| `static int` | `[GE\_OFFER\_CREATION\_TYPE](#GE_OFFER_CREATION_TYPE)` | Deprecated.
Type of GE offer currently being created
0 = buy
1 = sell |
| `static int` | `[GOD\_WARS\_ALTAR\_COOLDOWN](#GOD_WARS_ALTAR_COOLDOWN)` | Deprecated.
Cooldown timer remaining before eligible to restore at a god wars dungeon altar. |
| `static int` | `[GRAPES\_4953](#GRAPES_4953)` | Deprecated.
Transmog controllers for grapes |
| `static int` | `[GRAPES\_4954](#GRAPES_4954)` | Deprecated. |
| `static int` | `[GRAPES\_4955](#GRAPES_4955)` | Deprecated. |
| `static int` | `[GRAPES\_4956](#GRAPES_4956)` | Deprecated. |
| `static int` | `[GRAPES\_4957](#GRAPES_4957)` | Deprecated. |
| `static int` | `[GRAPES\_4958](#GRAPES_4958)` | Deprecated. |
| `static int` | `[GRAPES\_4959](#GRAPES_4959)` | Deprecated. |
| `static int` | `[GRAPES\_4960](#GRAPES_4960)` | Deprecated. |
| `static int` | `[GRAPES\_4961](#GRAPES_4961)` | Deprecated. |
| `static int` | `[GRAPES\_4962](#GRAPES_4962)` | Deprecated. |
| `static int` | `[GRAPES\_4963](#GRAPES_4963)` | Deprecated. |
| `static int` | `[GRAPES\_4964](#GRAPES_4964)` | Deprecated. |
| `static int` | `[HB\_FINISH](#HB_FINISH)` | Deprecated. |
| `static int` | `[HB\_STARTED](#HB_STARTED)` | Deprecated.
Started hunting Herbiboar. |
| `static int` | `[HB\_TRAIL\_31303](#HB_TRAIL_31303)` | Deprecated.
Herbiboar Trails |
| `static int` | `[HB\_TRAIL\_31306](#HB_TRAIL_31306)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31309](#HB_TRAIL_31309)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31312](#HB_TRAIL_31312)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31315](#HB_TRAIL_31315)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31318](#HB_TRAIL_31318)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31321](#HB_TRAIL_31321)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31324](#HB_TRAIL_31324)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31327](#HB_TRAIL_31327)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31330](#HB_TRAIL_31330)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31333](#HB_TRAIL_31333)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31336](#HB_TRAIL_31336)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31339](#HB_TRAIL_31339)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31342](#HB_TRAIL_31342)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31345](#HB_TRAIL_31345)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31348](#HB_TRAIL_31348)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31351](#HB_TRAIL_31351)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31354](#HB_TRAIL_31354)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31357](#HB_TRAIL_31357)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31360](#HB_TRAIL_31360)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31363](#HB_TRAIL_31363)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31366](#HB_TRAIL_31366)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31369](#HB_TRAIL_31369)` | Deprecated. |
| `static int` | `[HB\_TRAIL\_31372](#HB_TRAIL_31372)` | Deprecated. |
| `static int` | `[HEAL\_GROUP\_COOLDOWN](#HEAL_GROUP_COOLDOWN)` | Deprecated.
Spell cooldowns |
| `static int` | `[IMBUED\_HEART\_COOLDOWN](#IMBUED_HEART_COOLDOWN)` | Deprecated.
Imbued Heart cooldown
Number of game tick remaining on cooldown in intervals of 10; for a value X there are 10 \* X game ticks remaining. |
| `static int` | `[IN\_GAME\_BA](#IN_GAME_BA)` | Deprecated.
Barbarian Assault |
| `static int` | `[IN\_LMS](#IN_LMS)` | Deprecated. |
| `static int` | `[IN\_RAID](#IN_RAID)` | Deprecated.
Raids |
| `static int` | `[IN\_WILDERNESS](#IN_WILDERNESS)` | Deprecated.
0 = Outside wilderness
1 = In wilderness |
| `static int` | `[JARVIS\_GRAVESTONE](#JARVIS_GRAVESTONE)` | Deprecated.
The state of Jarvis' gravestone. |
| `static int` | `[KINGDOM\_APPROVAL](#KINGDOM_APPROVAL)` | Deprecated.
Kingdom of Miscellania Management
Kingdom Approval is represented as a 7-bit unsigned integer; 127 corresponds to 100% approval |
| `static int` | `[KINGDOM\_COFFER](#KINGDOM_COFFER)` | Deprecated. |
| `static int` | `[KOUREND\_FAVOR\_ARCEUUS](#KOUREND_FAVOR_ARCEUUS)` | Deprecated.
Kourend house favours |
| `static int` | `[KOUREND\_FAVOR\_HOSIDIUS](#KOUREND_FAVOR_HOSIDIUS)` | Deprecated. |
| `static int` | `[KOUREND\_FAVOR\_LOVAKENGJ](#KOUREND_FAVOR_LOVAKENGJ)` | Deprecated. |
| `static int` | `[KOUREND\_FAVOR\_PISCARILIUS](#KOUREND_FAVOR_PISCARILIUS)` | Deprecated. |
| `static int` | `[KOUREND\_FAVOR\_SHAYZIEN](#KOUREND_FAVOR_SHAYZIEN)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_1](#LEAGUE_RELIC_1)` | Deprecated.
League relics |
| `static int` | `[LEAGUE\_RELIC\_2](#LEAGUE_RELIC_2)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_3](#LEAGUE_RELIC_3)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_4](#LEAGUE_RELIC_4)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_5](#LEAGUE_RELIC_5)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_6](#LEAGUE_RELIC_6)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_7](#LEAGUE_RELIC_7)` | Deprecated. |
| `static int` | `[LEAGUE\_RELIC\_8](#LEAGUE_RELIC_8)` | Deprecated. |
| `static int` | `[LEAGUES\_MAGIC\_COMBAT\_MASTERY\_LEVEL](#LEAGUES_MAGIC_COMBAT_MASTERY_LEVEL)` | Deprecated. |
| `static int` | `[LEAGUES\_MELEE\_COMBAT\_MASTERY\_LEVEL](#LEAGUES_MELEE_COMBAT_MASTERY_LEVEL)` | Deprecated. |
| `static int` | `[LEAGUES\_RANGED\_COMBAT\_MASTERY\_LEVEL](#LEAGUES_RANGED_COMBAT_MASTERY_LEVEL)` | Deprecated. |
| `static int` | `[LEPRECHAUNS\_LUCK](#LEPRECHAUNS_LUCK)` | Deprecated. |
| `static int` | `[LIQUID\_ADERNALINE\_ACTIVE](#LIQUID_ADERNALINE_ACTIVE)` | Deprecated.
If the player has liquid adrenaline buff active |
| `static int` | `[MAGIC\_IMBUE](#MAGIC_IMBUE)` | Deprecated.
Magic imbue timer
Number of game ticks remaining on magic imbue effect in intervals of 10; for a value X there are 10 \* X game ticks remaining. |
| `static int` | `[MENAPHITE\_REMEDY](#MENAPHITE_REMEDY)` | Deprecated.
If the player has Menaphite remedy effect active. |
| `static int` | `[MOONLIGHT\_POTION](#MOONLIGHT_POTION)` | Deprecated.
Moonlight potion timer. |
| `static int` | `[MULTICOMBAT\_AREA](#MULTICOMBAT_AREA)` | Deprecated.
Multicombat area |
| `static int` | `[MUTED\_AREA\_EFFECT\_VOLUME](#MUTED_AREA_EFFECT_VOLUME)` | Deprecated. |
| `static int` | `[MUTED\_MUSIC\_VOLUME](#MUTED_MUSIC_VOLUME)` | Deprecated.
Muted volume restore values |
| `static int` | `[MUTED\_SOUND\_EFFECT\_VOLUME](#MUTED_SOUND_EFFECT_VOLUME)` | Deprecated. |
| `static int` | `[NMZ\_ABSORPTION](#NMZ_ABSORPTION)` | Deprecated.
Nightmare Zone |
| `static int` | `[NMZ\_OVERLOAD\_REFRESHES\_REMAINING](#NMZ_OVERLOAD_REFRESHES_REMAINING)` | Deprecated.
How many NMZ overload refreshes the player has remaining. |
| `static int` | `[NMZ\_POINTS](#NMZ_POINTS)` | Deprecated. |
| `static int` | `[NORTH\_NET\_CATCH\_COUNT](#NORTH_NET_CATCH_COUNT)` | Deprecated.
Drift net catch count |
| `static int` | `[NORTH\_NET\_STATUS](#NORTH_NET_STATUS)` | Deprecated.
Drift net status |
| `static int` | `[OXYGEN\_LEVEL](#OXYGEN_LEVEL)` | Deprecated.
The varbit that stores the oxygen percentage for player |
| `static int` | `[PARASITE](#PARASITE)` | Deprecated.
Parasite infection status during nightmare of ashihama bossfight |
| `static int` | `[PRAYER\_AUGURY](#PRAYER_AUGURY)` | Deprecated. |
| `static int` | `[PRAYER\_BURST\_OF\_STRENGTH](#PRAYER_BURST_OF_STRENGTH)` | Deprecated. |
| `static int` | `[PRAYER\_CHIVALRY](#PRAYER_CHIVALRY)` | Deprecated. |
| `static int` | `[PRAYER\_CLARITY\_OF\_THOUGHT](#PRAYER_CLARITY_OF_THOUGHT)` | Deprecated. |
| `static int` | `[PRAYER\_DEADEYE](#PRAYER_DEADEYE)` | Deprecated. |
| `static int` | `[PRAYER\_DEADEYE\_UNLOCKED](#PRAYER_DEADEYE_UNLOCKED)` | Deprecated. |
| `static int` | `[PRAYER\_EAGLE\_EYE](#PRAYER_EAGLE_EYE)` | Deprecated. |
| `static int` | `[PRAYER\_HAWK\_EYE](#PRAYER_HAWK_EYE)` | Deprecated. |
| `static int` | `[PRAYER\_IMPROVED\_REFLEXES](#PRAYER_IMPROVED_REFLEXES)` | Deprecated. |
| `static int` | `[PRAYER\_INCREDIBLE\_REFLEXES](#PRAYER_INCREDIBLE_REFLEXES)` | Deprecated. |
| `static int` | `[PRAYER\_MYSTIC\_LORE](#PRAYER_MYSTIC_LORE)` | Deprecated. |
| `static int` | `[PRAYER\_MYSTIC\_MIGHT](#PRAYER_MYSTIC_MIGHT)` | Deprecated. |
| `static int` | `[PRAYER\_MYSTIC\_VIGOUR](#PRAYER_MYSTIC_VIGOUR)` | Deprecated. |
| `static int` | `[PRAYER\_MYSTIC\_VIGOUR\_UNLOCKED](#PRAYER_MYSTIC_VIGOUR_UNLOCKED)` | Deprecated. |
| `static int` | `[PRAYER\_MYSTIC\_WILL](#PRAYER_MYSTIC_WILL)` | Deprecated. |
| `static int` | `[PRAYER\_PIETY](#PRAYER_PIETY)` | Deprecated. |
| `static int` | `[PRAYER\_PRESERVE](#PRAYER_PRESERVE)` | Deprecated. |
| `static int` | `[PRAYER\_PROTECT\_FROM\_MAGIC](#PRAYER_PROTECT_FROM_MAGIC)` | Deprecated. |
| `static int` | `[PRAYER\_PROTECT\_FROM\_MELEE](#PRAYER_PROTECT_FROM_MELEE)` | Deprecated. |
| `static int` | `[PRAYER\_PROTECT\_FROM\_MISSILES](#PRAYER_PROTECT_FROM_MISSILES)` | Deprecated. |
| `static int` | `[PRAYER\_PROTECT\_ITEM](#PRAYER_PROTECT_ITEM)` | Deprecated. |
| `static int` | `[PRAYER\_RAPID\_HEAL](#PRAYER_RAPID_HEAL)` | Deprecated. |
| `static int` | `[PRAYER\_RAPID\_RESTORE](#PRAYER_RAPID_RESTORE)` | Deprecated. |
| `static int` | `[PRAYER\_REDEMPTION](#PRAYER_REDEMPTION)` | Deprecated. |
| `static int` | `[PRAYER\_RETRIBUTION](#PRAYER_RETRIBUTION)` | Deprecated. |
| `static int` | `[PRAYER\_RIGOUR](#PRAYER_RIGOUR)` | Deprecated. |
| `static int` | `[PRAYER\_ROCK\_SKIN](#PRAYER_ROCK_SKIN)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_ANCIENT\_SIGHT](#PRAYER_RP_ANCIENT_SIGHT)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_ANCIENT\_STRENGTH](#PRAYER_RP_ANCIENT_STRENGTH)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_ANCIENT\_WILL](#PRAYER_RP_ANCIENT_WILL)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_ANNIHILATE](#PRAYER_RP_ANNIHILATE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_BERSERKER](#PRAYER_RP_BERSERKER)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_CRUORS\_VOW](#PRAYER_RP_CRUORS_VOW)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_DAMPEN\_MAGIC](#PRAYER_RP_DAMPEN_MAGIC)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_DAMPEN\_MELEE](#PRAYER_RP_DAMPEN_MELEE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_DAMPEN\_RANGED](#PRAYER_RP_DAMPEN_RANGED)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_DECIMATE](#PRAYER_RP_DECIMATE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_FUMUS\_VOW](#PRAYER_RP_FUMUS_VOW)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_GLACIES\_VOW](#PRAYER_RP_GLACIES_VOW)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_INTENSIFY](#PRAYER_RP_INTENSIFY)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_METABOLISE](#PRAYER_RP_METABOLISE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_PROTECT\_ITEM](#PRAYER_RP_PROTECT_ITEM)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_PURGE](#PRAYER_RP_PURGE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_REBUKE](#PRAYER_RP_REBUKE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_REJUVENATION](#PRAYER_RP_REJUVENATION)` | Deprecated.
Ruinous Powers |
| `static int` | `[PRAYER\_RP\_RUINOUS\_GRACE](#PRAYER_RP_RUINOUS_GRACE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_TRINITAS](#PRAYER_RP_TRINITAS)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_UMBRA\_VOW](#PRAYER_RP_UMBRA_VOW)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_VAPORISE](#PRAYER_RP_VAPORISE)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_VINDICATION](#PRAYER_RP_VINDICATION)` | Deprecated. |
| `static int` | `[PRAYER\_RP\_WRATH](#PRAYER_RP_WRATH)` | Deprecated. |
| `static int` | `[PRAYER\_SHARP\_EYE](#PRAYER_SHARP_EYE)` | Deprecated. |
| `static int` | `[PRAYER\_SMITE](#PRAYER_SMITE)` | Deprecated. |
| `static int` | `[PRAYER\_STEEL\_SKIN](#PRAYER_STEEL_SKIN)` | Deprecated. |
| `static int` | `[PRAYER\_SUPERHUMAN\_STRENGTH](#PRAYER_SUPERHUMAN_STRENGTH)` | Deprecated. |
| `static int` | `[PRAYER\_THICK\_SKIN](#PRAYER_THICK_SKIN)` | Deprecated. |
| `static int` | `[PRAYER\_ULTIMATE\_STRENGTH](#PRAYER_ULTIMATE_STRENGTH)` | Deprecated. |
| `static int` | `[PRAYERBOOK](#PRAYERBOOK)` | Deprecated. |
| `static int` | `[PVP\_SPEC\_ORB](#PVP_SPEC_ORB)` | Deprecated.
Whether the player is in a PvP area |
| `static int` | `[PYRAMID\_PLUNDER\_ROOM](#PYRAMID_PLUNDER_ROOM)` | Deprecated. |
| `static int` | `[PYRAMID\_PLUNDER\_ROOM\_LOCATION](#PYRAMID_PLUNDER_ROOM_LOCATION)` | Deprecated.
Pyramid plunder |
| `static int` | `[PYRAMID\_PLUNDER\_THIEVING\_LEVEL](#PYRAMID_PLUNDER_THIEVING_LEVEL)` | Deprecated. |
| `static int` | `[PYRAMID\_PLUNDER\_TIMER](#PYRAMID_PLUNDER_TIMER)` | Deprecated. |
| `static int` | `[QUEST\_DS2](#QUEST_DS2)` | Deprecated.
Dragon slayer 2 quest status |
| `static int` | `[QUEST\_TAB](#QUEST_TAB)` | Deprecated.
The active tab within the quest interface |
| `static int` | `[QUEST\_THE\_HAND\_IN\_THE\_SAND](#QUEST_THE_HAND_IN_THE_SAND)` | Deprecated.
The Hand in the Sand quest status |
| `static int` | `[QUICK\_PRAYER](#QUICK_PRAYER)` | Deprecated.
Prayers |
| `static int` | `[RAID\_STATE](#RAID_STATE)` | Deprecated. |
| `static int` | `[RESURRECT\_THRALL](#RESURRECT_THRALL)` | Deprecated. |
| `static int` | `[RESURRECT\_THRALL\_COOLDOWN](#RESURRECT_THRALL_COOLDOWN)` | Deprecated. |
| `static int` | `[RING\_OF\_ENDURANCE\_EFFECT](#RING_OF_ENDURANCE_EFFECT)` | Deprecated.
Ring of endurance effect timer, stamina duration extended from using the ring of endurance
Number of game ticks remaining on ring of endurance effect in intervals of 10; for a value X there are 10 \* X game ticks remaining. |
| `static int` | `[RUN\_SLOWED\_DEPLETION\_ACTIVE](#RUN_SLOWED_DEPLETION_ACTIVE)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT1](#RUNE_POUCH_AMOUNT1)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT2](#RUNE_POUCH_AMOUNT2)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT3](#RUNE_POUCH_AMOUNT3)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT4](#RUNE_POUCH_AMOUNT4)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT5](#RUNE_POUCH_AMOUNT5)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_AMOUNT6](#RUNE_POUCH_AMOUNT6)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_RUNE1](#RUNE_POUCH_RUNE1)` | Deprecated.
Runepouch |
| `static int` | `[RUNE\_POUCH\_RUNE2](#RUNE_POUCH_RUNE2)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_RUNE3](#RUNE_POUCH_RUNE3)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_RUNE4](#RUNE_POUCH_RUNE4)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_RUNE5](#RUNE_POUCH_RUNE5)` | Deprecated. |
| `static int` | `[RUNE\_POUCH\_RUNE6](#RUNE_POUCH_RUNE6)` | Deprecated. |
| `static int` | `[SACK\_NUMBER](#SACK_NUMBER)` | Deprecated.
Motherlode mine sack |
| `static int` | `[SACK\_UPGRADED](#SACK_UPGRADED)` | Deprecated. |
| `static int` | `[SCURRIUS\_FOOD\_PILE\_COOLDOWN](#SCURRIUS_FOOD_PILE_COOLDOWN)` | Deprecated.
Cooldown timer remaining before being able to eat from the piles of food in Scurrius's lair. |
| `static int` | `[SHADOW\_VEIL](#SHADOW_VEIL)` | Deprecated. |
| `static int` | `[SHADOW\_VEIL\_COOLDOWN](#SHADOW_VEIL_COOLDOWN)` | Deprecated. |
| `static int` | `[SHOW\_PVP\_KDR\_STATS](#SHOW_PVP_KDR_STATS)` | Deprecated.
Whether the PVP kill-death stats widget should be drawn while in the wilderness or in PVP worlds. |
| `static int` | `[SIDE\_PANELS](#SIDE_PANELS)` | Deprecated.
Options |
| `static int` | `[SLAYER\_POINTS](#SLAYER_POINTS)` | Deprecated. |
| `static int` | `[SLAYER\_TASK\_BOSS](#SLAYER_TASK_BOSS)` | Deprecated.
The assigned boss for boss slayer. |
| `static int` | `[SLAYER\_TASK\_STREAK](#SLAYER_TASK_STREAK)` | Deprecated. |
| `static int` | `[SOUTH\_NET\_CATCH\_COUNT](#SOUTH_NET_CATCH_COUNT)` | Deprecated. |
| `static int` | `[SOUTH\_NET\_STATUS](#SOUTH_NET_STATUS)` | Deprecated. |
| `static int` | `[SPELLBOOK](#SPELLBOOK)` | Deprecated. |
| `static int` | `[SPELLBOOK\_SUBMENU](#SPELLBOOK_SUBMENU)` | Deprecated. |
| `static int` | `[SPELLBOOK\_SWAP](#SPELLBOOK_SWAP)` | Deprecated.
If the player has a spellbook swap active |
| `static int` | `[SPICY\_STEW\_BROWN\_SPICES](#SPICY_STEW_BROWN_SPICES)` | Deprecated. |
| `static int` | `[SPICY\_STEW\_ORANGE\_SPICES](#SPICY_STEW_ORANGE_SPICES)` | Deprecated. |
| `static int` | `[SPICY\_STEW\_RED\_SPICES](#SPICY_STEW_RED_SPICES)` | Deprecated.
Spicy stew ingredients |
| `static int` | `[SPICY\_STEW\_YELLOW\_SPICES](#SPICY_STEW_YELLOW_SPICES)` | Deprecated. |
| `static int` | `[STAMINA\_EFFECT](#STAMINA_EFFECT)` | Deprecated.
Stamina effect timer
Number of game ticks remaining on stamina effect in intervals of 10; for a value X there are 10 \* X game ticks remaining. |
| `static int` | `[SUPER\_ANTIFIRE](#SUPER_ANTIFIRE)` | Deprecated.
Super Antifire timer
Number of game ticks remaining on super antifire in intervals of 20; for a value X there are 20 \* X game ticks remaining. |
| `static int` | `[SUPERIOR\_ENABLED](#SUPERIOR_ENABLED)` | Deprecated.
Toggleable slayer unlocks |
| `static int` | `[TELEBLOCK](#TELEBLOCK)` | Deprecated.
State of Teleblock spell effects on the player |
| `static int` | `[THEATRE\_OF\_BLOOD](#THEATRE_OF_BLOOD)` | Deprecated.
Theatre of Blood 1=In Party, 2=Inside/Spectator, 3=Dead Spectating |
| `static int` | `[THEATRE\_OF\_BLOOD\_ORB1](#THEATRE_OF_BLOOD_ORB1)` | Deprecated.
Theatre of Blood orb healths
0=hide 1-27=% of health - 27 is 100% health and 1 is 0% health, 30=dead |
| `static int` | `[THEATRE\_OF\_BLOOD\_ORB2](#THEATRE_OF_BLOOD_ORB2)` | Deprecated. |
| `static int` | `[THEATRE\_OF\_BLOOD\_ORB3](#THEATRE_OF_BLOOD_ORB3)` | Deprecated. |
| `static int` | `[THEATRE\_OF\_BLOOD\_ORB4](#THEATRE_OF_BLOOD_ORB4)` | Deprecated. |
| `static int` | `[THEATRE\_OF\_BLOOD\_ORB5](#THEATRE_OF_BLOOD_ORB5)` | Deprecated. |
| `static int` | `[TITHE\_FARM\_POINTS](#TITHE_FARM_POINTS)` | Deprecated. |
| `static int` | `[TITHE\_FARM\_SACK\_AMOUNT](#TITHE_FARM_SACK_AMOUNT)` | Deprecated.
Tithe Farm |
| `static int` | `[TITHE\_FARM\_SACK\_ICON](#TITHE_FARM_SACK_ICON)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_0\_HEALTH](#TOA_MEMBER_0_HEALTH)` | Deprecated.
Tombs of Amascut orb healths
0=hide 1-27=% of health - 27 is 100% health and 1 is 0% health, 30=dead |
| `static int` | `[TOA\_MEMBER\_1\_HEALTH](#TOA_MEMBER_1_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_2\_HEALTH](#TOA_MEMBER_2_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_3\_HEALTH](#TOA_MEMBER_3_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_4\_HEALTH](#TOA_MEMBER_4_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_5\_HEALTH](#TOA_MEMBER_5_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_6\_HEALTH](#TOA_MEMBER_6_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_MEMBER\_7\_HEALTH](#TOA_MEMBER_7_HEALTH)` | Deprecated. |
| `static int` | `[TOA\_RAID\_DAMAGE](#TOA_RAID_DAMAGE)` | Deprecated. |
| `static int` | `[TOA\_RAID\_LEVEL](#TOA_RAID_LEVEL)` | Deprecated. |
| `static int` | `[TOTAL\_POINTS](#TOTAL_POINTS)` | Deprecated. |
| `static int` | `[TRANSPARENT\_CHATBOX](#TRANSPARENT_CHATBOX)` | Deprecated. |
| `static int` | `[VENGEANCE\_ACTIVE](#VENGEANCE_ACTIVE)` | Deprecated.
Spell activeness |
| `static int` | `[VENGEANCE\_COOLDOWN](#VENGEANCE_COOLDOWN)` | Deprecated. |
| `static int` | `[VIGGORA\_LOCATION](#VIGGORA_LOCATION)` | Deprecated.
During and after Curse of the Empty Lord, Viggora can be located in one of three locations,
which is uniquely and permanently set for each player. |
| `static int` | `[WARD\_OF\_ARCEUUS\_COOLDOWN](#WARD_OF_ARCEUUS_COOLDOWN)` | Deprecated. |
| `static int` | `[WIKI\_ENTITY\_LOOKUP](#WIKI_ENTITY_LOOKUP)` | Deprecated.
Whether the vanilla wiki entity lookup is displayed under the minimap |
| `static int` | `[WINTERTODT\_TIMER](#WINTERTODT_TIMER)` | Deprecated. |
| `static int` | `[WINTERTODT\_WARMTH](#WINTERTODT_WARMTH)` | Deprecated. |
| `static int` | `[WORLDHOPPER\_FAVORITE\_1](#WORLDHOPPER_FAVORITE_1)` | Deprecated. |
| `static int` | `[WORLDHOPPER\_FAVORITE\_2](#WORLDHOPPER_FAVORITE_2)` | Deprecated. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Varbits](#%3Cinit%3E())()` | Deprecated. |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### TRANSPARENT\_CHATBOX

```
public static final int TRANSPARENT_CHATBOX
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TRANSPARENT_CHATBOX)
- #### RUN\_SLOWED\_DEPLETION\_ACTIVE

```
public static final int RUN_SLOWED_DEPLETION_ACTIVE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUN_SLOWED_DEPLETION_ACTIVE)
- #### STAMINA\_EFFECT

```
public static final int STAMINA_EFFECT
```

Deprecated.
Stamina effect timer
Number of game ticks remaining on stamina effect in intervals of 10; for a value X there are 10 \* X game ticks remaining.
The stamina effect expires once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.STAMINA_EFFECT)
- #### ANTIFIRE

```
public static final int ANTIFIRE
```

Deprecated.
Antifire timer
Number of game ticks remaining on antifire in intervals of 30; for a value X there are 30 \* X game ticks remaining.
The antifire expires once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ANTIFIRE)
- #### SUPER\_ANTIFIRE

```
public static final int SUPER_ANTIFIRE
```

Deprecated.
Super Antifire timer
Number of game ticks remaining on super antifire in intervals of 20; for a value X there are 20 \* X game ticks remaining.
The super antifire expires once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SUPER_ANTIFIRE)
- #### MAGIC\_IMBUE

```
public static final int MAGIC_IMBUE
```

Deprecated.
Magic imbue timer
Number of game ticks remaining on magic imbue effect in intervals of 10; for a value X there are 10 \* X game ticks remaining.
The magic imbue effect expires once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MAGIC_IMBUE)
- #### DIVINE\_SUPER\_ATTACK

```
public static final int DIVINE_SUPER_ATTACK
```

Deprecated.
Divine effect timers
Number of game ticks remaining on a divine effect.
A potion that combines multiple effects will set the varbits for the individual effects as well as its own effect.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_SUPER_ATTACK)
- #### DIVINE\_SUPER\_STRENGTH

```
public static final int DIVINE_SUPER_STRENGTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_SUPER_STRENGTH)
- #### DIVINE\_SUPER\_DEFENCE

```
public static final int DIVINE_SUPER_DEFENCE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_SUPER_DEFENCE)
- #### DIVINE\_RANGING

```
public static final int DIVINE_RANGING
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_RANGING)
- #### DIVINE\_MAGIC

```
public static final int DIVINE_MAGIC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_MAGIC)
- #### DIVINE\_SUPER\_COMBAT

```
public static final int DIVINE_SUPER_COMBAT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_SUPER_COMBAT)
- #### DIVINE\_BASTION

```
public static final int DIVINE_BASTION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_BASTION)
- #### DIVINE\_BATTLEMAGE

```
public static final int DIVINE_BATTLEMAGE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIVINE_BATTLEMAGE)
- #### MOONLIGHT\_POTION

```
public static final int MOONLIGHT_POTION
```

Deprecated.
Moonlight potion timer.
When at least 70 herblore, the moonlight potion's defense effect will be removed when this timer runs out.
If the player drinks a dose of moonlight potion while already under its effects, desync between
Varbits.MOONLIGHT\_POTION and Varbits.DIVINE\_SUPER\_DEFENCE can occur, with the latter being 1 tick greater.
In case of desync, the moonlight defence effect will be removed once Varbits.DIVINE\_SUPER\_DEFENCE becomes 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MOONLIGHT_POTION)
- #### RING\_OF\_ENDURANCE\_EFFECT

```
public static final int RING_OF_ENDURANCE_EFFECT
```

Deprecated.
Ring of endurance effect timer, stamina duration extended from using the ring of endurance
Number of game ticks remaining on ring of endurance effect in intervals of 10; for a value X there are 10 \* X game ticks remaining.
Unequipping the ring of endurance will cause this to change to 0.
When this reaches 0, [`STAMINA_EFFECT`](#STAMINA_EFFECT) will begin counting down.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RING_OF_ENDURANCE_EFFECT)
- #### CHAT\_SCROLLBAR\_ON\_LEFT

```
public static final int CHAT_SCROLLBAR_ON_LEFT
```

Deprecated.
If scrollbar in resizable mode chat is on the left

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.CHAT_SCROLLBAR_ON_LEFT)
- #### ESSENCE\_POUCH\_SMALL\_AMOUNT

```
public static final int ESSENCE_POUCH_SMALL_AMOUNT
```

Deprecated.
Essence pouches

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_SMALL_AMOUNT)
- #### ESSENCE\_POUCH\_MEDIUM\_AMOUNT

```
public static final int ESSENCE_POUCH_MEDIUM_AMOUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_MEDIUM_AMOUNT)
- #### ESSENCE\_POUCH\_LARGE\_AMOUNT

```
public static final int ESSENCE_POUCH_LARGE_AMOUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_LARGE_AMOUNT)
- #### ESSENCE\_POUCH\_GIANT\_AMOUNT

```
public static final int ESSENCE_POUCH_GIANT_AMOUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_GIANT_AMOUNT)
- #### ESSENCE\_POUCH\_COLOSSAL\_AMOUNT

```
public static final int ESSENCE_POUCH_COLOSSAL_AMOUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_COLOSSAL_AMOUNT)
- #### ESSENCE\_POUCH\_COLOSSAL\_DEGRADE

```
public static final int ESSENCE_POUCH_COLOSSAL_DEGRADE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ESSENCE_POUCH_COLOSSAL_DEGRADE)
- #### RUNE\_POUCH\_RUNE1

```
public static final int RUNE_POUCH_RUNE1
```

Deprecated.
Runepouch

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE1)
- #### RUNE\_POUCH\_RUNE2

```
public static final int RUNE_POUCH_RUNE2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE2)
- #### RUNE\_POUCH\_RUNE3

```
public static final int RUNE_POUCH_RUNE3
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE3)
- #### RUNE\_POUCH\_RUNE4

```
public static final int RUNE_POUCH_RUNE4
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE4)
- #### RUNE\_POUCH\_RUNE5

```
public static final int RUNE_POUCH_RUNE5
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE5)
- #### RUNE\_POUCH\_RUNE6

```
public static final int RUNE_POUCH_RUNE6
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_RUNE6)
- #### RUNE\_POUCH\_AMOUNT1

```
public static final int RUNE_POUCH_AMOUNT1
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT1)
- #### RUNE\_POUCH\_AMOUNT2

```
public static final int RUNE_POUCH_AMOUNT2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT2)
- #### RUNE\_POUCH\_AMOUNT3

```
public static final int RUNE_POUCH_AMOUNT3
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT3)
- #### RUNE\_POUCH\_AMOUNT4

```
public static final int RUNE_POUCH_AMOUNT4
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT4)
- #### RUNE\_POUCH\_AMOUNT5

```
public static final int RUNE_POUCH_AMOUNT5
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT5)
- #### RUNE\_POUCH\_AMOUNT6

```
public static final int RUNE_POUCH_AMOUNT6
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RUNE_POUCH_AMOUNT6)
- #### PRAYER\_DEADEYE\_UNLOCKED

```
public static final int PRAYER_DEADEYE_UNLOCKED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_DEADEYE_UNLOCKED)
- #### PRAYER\_MYSTIC\_VIGOUR\_UNLOCKED

```
public static final int PRAYER_MYSTIC_VIGOUR_UNLOCKED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_MYSTIC_VIGOUR_UNLOCKED)
- #### QUICK\_PRAYER

```
public static final int QUICK_PRAYER
```

Deprecated.
Prayers

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.QUICK_PRAYER)
- #### PRAYER\_THICK\_SKIN

```
public static final int PRAYER_THICK_SKIN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_THICK_SKIN)
- #### PRAYER\_BURST\_OF\_STRENGTH

```
public static final int PRAYER_BURST_OF_STRENGTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_BURST_OF_STRENGTH)
- #### PRAYER\_CLARITY\_OF\_THOUGHT

```
public static final int PRAYER_CLARITY_OF_THOUGHT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_CLARITY_OF_THOUGHT)
- #### PRAYER\_SHARP\_EYE

```
public static final int PRAYER_SHARP_EYE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_SHARP_EYE)
- #### PRAYER\_MYSTIC\_WILL

```
public static final int PRAYER_MYSTIC_WILL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_MYSTIC_WILL)
- #### PRAYER\_ROCK\_SKIN

```
public static final int PRAYER_ROCK_SKIN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_ROCK_SKIN)
- #### PRAYER\_SUPERHUMAN\_STRENGTH

```
public static final int PRAYER_SUPERHUMAN_STRENGTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_SUPERHUMAN_STRENGTH)
- #### PRAYER\_IMPROVED\_REFLEXES

```
public static final int PRAYER_IMPROVED_REFLEXES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_IMPROVED_REFLEXES)
- #### PRAYER\_RAPID\_RESTORE

```
public static final int PRAYER_RAPID_RESTORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RAPID_RESTORE)
- #### PRAYER\_RAPID\_HEAL

```
public static final int PRAYER_RAPID_HEAL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RAPID_HEAL)
- #### PRAYER\_PROTECT\_ITEM

```
public static final int PRAYER_PROTECT_ITEM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PROTECT_ITEM)
- #### PRAYER\_HAWK\_EYE

```
public static final int PRAYER_HAWK_EYE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_HAWK_EYE)
- #### PRAYER\_MYSTIC\_LORE

```
public static final int PRAYER_MYSTIC_LORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_MYSTIC_LORE)
- #### PRAYER\_STEEL\_SKIN

```
public static final int PRAYER_STEEL_SKIN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_STEEL_SKIN)
- #### PRAYER\_ULTIMATE\_STRENGTH

```
public static final int PRAYER_ULTIMATE_STRENGTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_ULTIMATE_STRENGTH)
- #### PRAYER\_INCREDIBLE\_REFLEXES

```
public static final int PRAYER_INCREDIBLE_REFLEXES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_INCREDIBLE_REFLEXES)
- #### PRAYER\_PROTECT\_FROM\_MAGIC

```
public static final int PRAYER_PROTECT_FROM_MAGIC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PROTECT_FROM_MAGIC)
- #### PRAYER\_PROTECT\_FROM\_MISSILES

```
public static final int PRAYER_PROTECT_FROM_MISSILES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PROTECT_FROM_MISSILES)
- #### PRAYER\_PROTECT\_FROM\_MELEE

```
public static final int PRAYER_PROTECT_FROM_MELEE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PROTECT_FROM_MELEE)
- #### PRAYER\_EAGLE\_EYE

```
public static final int PRAYER_EAGLE_EYE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_EAGLE_EYE)
- #### PRAYER\_MYSTIC\_MIGHT

```
public static final int PRAYER_MYSTIC_MIGHT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_MYSTIC_MIGHT)
- #### PRAYER\_RETRIBUTION

```
public static final int PRAYER_RETRIBUTION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RETRIBUTION)
- #### PRAYER\_REDEMPTION

```
public static final int PRAYER_REDEMPTION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_REDEMPTION)
- #### PRAYER\_SMITE

```
public static final int PRAYER_SMITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_SMITE)
- #### PRAYER\_CHIVALRY

```
public static final int PRAYER_CHIVALRY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_CHIVALRY)
- #### PRAYER\_PIETY

```
public static final int PRAYER_PIETY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PIETY)
- #### PRAYER\_PRESERVE

```
public static final int PRAYER_PRESERVE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_PRESERVE)
- #### PRAYER\_RIGOUR

```
public static final int PRAYER_RIGOUR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RIGOUR)
- #### PRAYER\_AUGURY

```
public static final int PRAYER_AUGURY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_AUGURY)
- #### PRAYER\_DEADEYE

```
public static final int PRAYER_DEADEYE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_DEADEYE)
- #### PRAYER\_MYSTIC\_VIGOUR

```
public static final int PRAYER_MYSTIC_VIGOUR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_MYSTIC_VIGOUR)
- #### PRAYER\_RP\_REJUVENATION

```
public static final int PRAYER_RP_REJUVENATION
```

Deprecated.
Ruinous Powers

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_REJUVENATION)
- #### PRAYER\_RP\_ANCIENT\_STRENGTH

```
public static final int PRAYER_RP_ANCIENT_STRENGTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_ANCIENT_STRENGTH)
- #### PRAYER\_RP\_ANCIENT\_SIGHT

```
public static final int PRAYER_RP_ANCIENT_SIGHT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_ANCIENT_SIGHT)
- #### PRAYER\_RP\_ANCIENT\_WILL

```
public static final int PRAYER_RP_ANCIENT_WILL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_ANCIENT_WILL)
- #### PRAYER\_RP\_PROTECT\_ITEM

```
public static final int PRAYER_RP_PROTECT_ITEM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_PROTECT_ITEM)
- #### PRAYER\_RP\_RUINOUS\_GRACE

```
public static final int PRAYER_RP_RUINOUS_GRACE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_RUINOUS_GRACE)
- #### PRAYER\_RP\_DAMPEN\_MAGIC

```
public static final int PRAYER_RP_DAMPEN_MAGIC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_DAMPEN_MAGIC)
- #### PRAYER\_RP\_DAMPEN\_RANGED

```
public static final int PRAYER_RP_DAMPEN_RANGED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_DAMPEN_RANGED)
- #### PRAYER\_RP\_DAMPEN\_MELEE

```
public static final int PRAYER_RP_DAMPEN_MELEE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_DAMPEN_MELEE)
- #### PRAYER\_RP\_TRINITAS

```
public static final int PRAYER_RP_TRINITAS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_TRINITAS)
- #### PRAYER\_RP\_BERSERKER

```
public static final int PRAYER_RP_BERSERKER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_BERSERKER)
- #### PRAYER\_RP\_PURGE

```
public static final int PRAYER_RP_PURGE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_PURGE)
- #### PRAYER\_RP\_METABOLISE

```
public static final int PRAYER_RP_METABOLISE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_METABOLISE)
- #### PRAYER\_RP\_REBUKE

```
public static final int PRAYER_RP_REBUKE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_REBUKE)
- #### PRAYER\_RP\_VINDICATION

```
public static final int PRAYER_RP_VINDICATION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_VINDICATION)
- #### PRAYER\_RP\_DECIMATE

```
public static final int PRAYER_RP_DECIMATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_DECIMATE)
- #### PRAYER\_RP\_ANNIHILATE

```
public static final int PRAYER_RP_ANNIHILATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_ANNIHILATE)
- #### PRAYER\_RP\_VAPORISE

```
public static final int PRAYER_RP_VAPORISE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_VAPORISE)
- #### PRAYER\_RP\_FUMUS\_VOW

```
public static final int PRAYER_RP_FUMUS_VOW
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_FUMUS_VOW)
- #### PRAYER\_RP\_UMBRA\_VOW

```
public static final int PRAYER_RP_UMBRA_VOW
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_UMBRA_VOW)
- #### PRAYER\_RP\_CRUORS\_VOW

```
public static final int PRAYER_RP_CRUORS_VOW
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_CRUORS_VOW)
- #### PRAYER\_RP\_GLACIES\_VOW

```
public static final int PRAYER_RP_GLACIES_VOW
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_GLACIES_VOW)
- #### PRAYER\_RP\_WRATH

```
public static final int PRAYER_RP_WRATH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_WRATH)
- #### PRAYER\_RP\_INTENSIFY

```
public static final int PRAYER_RP_INTENSIFY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYER_RP_INTENSIFY)
- #### DIARY\_ARDOUGNE\_EASY

```
public static final int DIARY_ARDOUGNE_EASY
```

Deprecated.
Diary Entries

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_ARDOUGNE_EASY)
- #### DIARY\_ARDOUGNE\_MEDIUM

```
public static final int DIARY_ARDOUGNE_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_ARDOUGNE_MEDIUM)
- #### DIARY\_ARDOUGNE\_HARD

```
public static final int DIARY_ARDOUGNE_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_ARDOUGNE_HARD)
- #### DIARY\_ARDOUGNE\_ELITE

```
public static final int DIARY_ARDOUGNE_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_ARDOUGNE_ELITE)
- #### DIARY\_DESERT\_EASY

```
public static final int DIARY_DESERT_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_DESERT_EASY)
- #### DIARY\_DESERT\_MEDIUM

```
public static final int DIARY_DESERT_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_DESERT_MEDIUM)
- #### DIARY\_DESERT\_HARD

```
public static final int DIARY_DESERT_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_DESERT_HARD)
- #### DIARY\_DESERT\_ELITE

```
public static final int DIARY_DESERT_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_DESERT_ELITE)
- #### DIARY\_FALADOR\_EASY

```
public static final int DIARY_FALADOR_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FALADOR_EASY)
- #### DIARY\_FALADOR\_MEDIUM

```
public static final int DIARY_FALADOR_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FALADOR_MEDIUM)
- #### DIARY\_FALADOR\_HARD

```
public static final int DIARY_FALADOR_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FALADOR_HARD)
- #### DIARY\_FALADOR\_ELITE

```
public static final int DIARY_FALADOR_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FALADOR_ELITE)
- #### DIARY\_FREMENNIK\_EASY

```
public static final int DIARY_FREMENNIK_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FREMENNIK_EASY)
- #### DIARY\_FREMENNIK\_MEDIUM

```
public static final int DIARY_FREMENNIK_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FREMENNIK_MEDIUM)
- #### DIARY\_FREMENNIK\_HARD

```
public static final int DIARY_FREMENNIK_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FREMENNIK_HARD)
- #### DIARY\_FREMENNIK\_ELITE

```
public static final int DIARY_FREMENNIK_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_FREMENNIK_ELITE)
- #### DIARY\_KANDARIN\_EASY

```
public static final int DIARY_KANDARIN_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KANDARIN_EASY)
- #### DIARY\_KANDARIN\_MEDIUM

```
public static final int DIARY_KANDARIN_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KANDARIN_MEDIUM)
- #### DIARY\_KANDARIN\_HARD

```
public static final int DIARY_KANDARIN_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KANDARIN_HARD)
- #### DIARY\_KANDARIN\_ELITE

```
public static final int DIARY_KANDARIN_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KANDARIN_ELITE)
- #### DIARY\_KARAMJA\_EASY

```
public static final int DIARY_KARAMJA_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KARAMJA_EASY)
- #### DIARY\_KARAMJA\_MEDIUM

```
public static final int DIARY_KARAMJA_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KARAMJA_MEDIUM)
- #### DIARY\_KARAMJA\_HARD

```
public static final int DIARY_KARAMJA_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KARAMJA_HARD)
- #### DIARY\_KARAMJA\_ELITE

```
public static final int DIARY_KARAMJA_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KARAMJA_ELITE)
- #### DIARY\_KOUREND\_EASY

```
public static final int DIARY_KOUREND_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KOUREND_EASY)
- #### DIARY\_KOUREND\_MEDIUM

```
public static final int DIARY_KOUREND_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KOUREND_MEDIUM)
- #### DIARY\_KOUREND\_HARD

```
public static final int DIARY_KOUREND_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KOUREND_HARD)
- #### DIARY\_KOUREND\_ELITE

```
public static final int DIARY_KOUREND_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_KOUREND_ELITE)
- #### DIARY\_LUMBRIDGE\_EASY

```
public static final int DIARY_LUMBRIDGE_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_LUMBRIDGE_EASY)
- #### DIARY\_LUMBRIDGE\_MEDIUM

```
public static final int DIARY_LUMBRIDGE_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_LUMBRIDGE_MEDIUM)
- #### DIARY\_LUMBRIDGE\_HARD

```
public static final int DIARY_LUMBRIDGE_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_LUMBRIDGE_HARD)
- #### DIARY\_LUMBRIDGE\_ELITE

```
public static final int DIARY_LUMBRIDGE_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_LUMBRIDGE_ELITE)
- #### DIARY\_MORYTANIA\_EASY

```
public static final int DIARY_MORYTANIA_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_MORYTANIA_EASY)
- #### DIARY\_MORYTANIA\_MEDIUM

```
public static final int DIARY_MORYTANIA_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_MORYTANIA_MEDIUM)
- #### DIARY\_MORYTANIA\_HARD

```
public static final int DIARY_MORYTANIA_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_MORYTANIA_HARD)
- #### DIARY\_MORYTANIA\_ELITE

```
public static final int DIARY_MORYTANIA_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_MORYTANIA_ELITE)
- #### DIARY\_VARROCK\_EASY

```
public static final int DIARY_VARROCK_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_VARROCK_EASY)
- #### DIARY\_VARROCK\_MEDIUM

```
public static final int DIARY_VARROCK_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_VARROCK_MEDIUM)
- #### DIARY\_VARROCK\_HARD

```
public static final int DIARY_VARROCK_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_VARROCK_HARD)
- #### DIARY\_VARROCK\_ELITE

```
public static final int DIARY_VARROCK_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_VARROCK_ELITE)
- #### DIARY\_WESTERN\_EASY

```
public static final int DIARY_WESTERN_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WESTERN_EASY)
- #### DIARY\_WESTERN\_MEDIUM

```
public static final int DIARY_WESTERN_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WESTERN_MEDIUM)
- #### DIARY\_WESTERN\_HARD

```
public static final int DIARY_WESTERN_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WESTERN_HARD)
- #### DIARY\_WESTERN\_ELITE

```
public static final int DIARY_WESTERN_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WESTERN_ELITE)
- #### DIARY\_WILDERNESS\_EASY

```
public static final int DIARY_WILDERNESS_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WILDERNESS_EASY)
- #### DIARY\_WILDERNESS\_MEDIUM

```
public static final int DIARY_WILDERNESS_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WILDERNESS_MEDIUM)
- #### DIARY\_WILDERNESS\_HARD

```
public static final int DIARY_WILDERNESS_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WILDERNESS_HARD)
- #### DIARY\_WILDERNESS\_ELITE

```
public static final int DIARY_WILDERNESS_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DIARY_WILDERNESS_ELITE)
- #### KOUREND\_FAVOR\_ARCEUUS

```
public static final int KOUREND_FAVOR_ARCEUUS
```

Deprecated.
Kourend house favours

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KOUREND_FAVOR_ARCEUUS)
- #### KOUREND\_FAVOR\_HOSIDIUS

```
public static final int KOUREND_FAVOR_HOSIDIUS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KOUREND_FAVOR_HOSIDIUS)
- #### KOUREND\_FAVOR\_LOVAKENGJ

```
public static final int KOUREND_FAVOR_LOVAKENGJ
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KOUREND_FAVOR_LOVAKENGJ)
- #### KOUREND\_FAVOR\_PISCARILIUS

```
public static final int KOUREND_FAVOR_PISCARILIUS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KOUREND_FAVOR_PISCARILIUS)
- #### KOUREND\_FAVOR\_SHAYZIEN

```
public static final int KOUREND_FAVOR_SHAYZIEN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KOUREND_FAVOR_SHAYZIEN)
- #### EQUIPPED\_WEAPON\_TYPE

```
public static final int EQUIPPED_WEAPON_TYPE
```

Deprecated.
Equipped weapon type

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EQUIPPED_WEAPON_TYPE)
- #### DEFENSIVE\_CASTING\_MODE

```
public static final int DEFENSIVE_CASTING_MODE
```

Deprecated.
Defensive casting mode

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DEFENSIVE_CASTING_MODE)
- #### SIDE\_PANELS

```
public static final int SIDE_PANELS
```

Deprecated.
Options

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SIDE_PANELS)
- #### HB\_TRAIL\_31303

```
public static final int HB_TRAIL_31303
```

Deprecated.
Herbiboar Trails

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31303)
- #### HB\_TRAIL\_31306

```
public static final int HB_TRAIL_31306
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31306)
- #### HB\_TRAIL\_31309

```
public static final int HB_TRAIL_31309
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31309)
- #### HB\_TRAIL\_31312

```
public static final int HB_TRAIL_31312
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31312)
- #### HB\_TRAIL\_31315

```
public static final int HB_TRAIL_31315
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31315)
- #### HB\_TRAIL\_31318

```
public static final int HB_TRAIL_31318
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31318)
- #### HB\_TRAIL\_31321

```
public static final int HB_TRAIL_31321
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31321)
- #### HB\_TRAIL\_31324

```
public static final int HB_TRAIL_31324
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31324)
- #### HB\_TRAIL\_31327

```
public static final int HB_TRAIL_31327
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31327)
- #### HB\_TRAIL\_31330

```
public static final int HB_TRAIL_31330
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31330)
- #### HB\_TRAIL\_31333

```
public static final int HB_TRAIL_31333
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31333)
- #### HB\_TRAIL\_31336

```
public static final int HB_TRAIL_31336
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31336)
- #### HB\_TRAIL\_31339

```
public static final int HB_TRAIL_31339
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31339)
- #### HB\_TRAIL\_31342

```
public static final int HB_TRAIL_31342
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31342)
- #### HB\_TRAIL\_31345

```
public static final int HB_TRAIL_31345
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31345)
- #### HB\_TRAIL\_31348

```
public static final int HB_TRAIL_31348
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31348)
- #### HB\_TRAIL\_31351

```
public static final int HB_TRAIL_31351
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31351)
- #### HB\_TRAIL\_31354

```
public static final int HB_TRAIL_31354
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31354)
- #### HB\_TRAIL\_31357

```
public static final int HB_TRAIL_31357
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31357)
- #### HB\_TRAIL\_31360

```
public static final int HB_TRAIL_31360
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31360)
- #### HB\_TRAIL\_31363

```
public static final int HB_TRAIL_31363
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31363)
- #### HB\_TRAIL\_31366

```
public static final int HB_TRAIL_31366
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31366)
- #### HB\_TRAIL\_31369

```
public static final int HB_TRAIL_31369
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31369)
- #### HB\_TRAIL\_31372

```
public static final int HB_TRAIL_31372
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_TRAIL_31372)
- #### HB\_FINISH

```
public static final int HB_FINISH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_FINISH)
- #### HB\_STARTED

```
public static final int HB_STARTED
```

Deprecated.
Started hunting Herbiboar.

NOTE: This value remains at 0 even after starting a Herbiboar trail up until searching the first object along the
hunting path.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HB_STARTED)
- #### IN\_GAME\_BA

```
public static final int IN_GAME_BA
```

Deprecated.
Barbarian Assault

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.IN_GAME_BA)
- #### BA\_GC

```
public static final int BA_GC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BA_GC)
- #### IN\_WILDERNESS

```
public static final int IN_WILDERNESS
```

Deprecated.
0 = Outside wilderness
1 = In wilderness

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.IN_WILDERNESS)
- #### FISHING\_TRAWLER\_ACTIVITY

```
public static final int FISHING_TRAWLER_ACTIVITY
```

Deprecated.
Fishing Trawler
FISHING\_TRAWLER\_ACTIVITY Expected values: 0-255

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FISHING_TRAWLER_ACTIVITY)
- #### BAR\_DISPENSER

```
public static final int BAR_DISPENSER
```

Deprecated.
Blast Furnace Bar Dispenser

These are the expected values:
0 = No bars being processed
1 = Ores are being processed on the conveyor belt, bar dispenser cannot be checked
2 = Bars are cooling down
3 = Bars can be collected

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BAR_DISPENSER)
- #### SACK\_NUMBER

```
public static final int SACK_NUMBER
```

Deprecated.
Motherlode mine sack

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SACK_NUMBER)
- #### SACK\_UPGRADED

```
public static final int SACK_UPGRADED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SACK_UPGRADED)
- #### EXPERIENCE\_TRACKER\_POSITION

```
public static final int EXPERIENCE_TRACKER_POSITION
```

Deprecated.
Experience tracker

EXPERIENCE\_TRACKER\_POSITION expected values:
0 = Right
1 = Middle
2 = Left

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPERIENCE_TRACKER_POSITION)
- #### EXPERIENCE\_TRACKER\_COUNTER

```
public static final int EXPERIENCE_TRACKER_COUNTER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPERIENCE_TRACKER_COUNTER)
- #### EXPERIENCE\_TRACKER\_PROGRESS\_BAR

```
public static final int EXPERIENCE_TRACKER_PROGRESS_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPERIENCE_TRACKER_PROGRESS_BAR)
- #### EXPERIENCE\_DROP\_COLOR

```
public static final int EXPERIENCE_DROP_COLOR
```

Deprecated.
Experience drop color

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPERIENCE_DROP_COLOR)
- #### TITHE\_FARM\_SACK\_AMOUNT

```
public static final int TITHE_FARM_SACK_AMOUNT
```

Deprecated.
Tithe Farm

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TITHE_FARM_SACK_AMOUNT)
- #### TITHE\_FARM\_SACK\_ICON

```
public static final int TITHE_FARM_SACK_ICON
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TITHE_FARM_SACK_ICON)
- #### TITHE\_FARM\_POINTS

```
public static final int TITHE_FARM_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TITHE_FARM_POINTS)
- #### BLAST\_MINE\_COAL

```
public static final int BLAST_MINE_COAL
```

Deprecated.
Blast Mine

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_MINE_COAL)
- #### BLAST\_MINE\_GOLD

```
public static final int BLAST_MINE_GOLD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_MINE_GOLD)
- #### BLAST\_MINE\_MITHRIL

```
public static final int BLAST_MINE_MITHRIL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_MINE_MITHRIL)
- #### BLAST\_MINE\_ADAMANTITE

```
public static final int BLAST_MINE_ADAMANTITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_MINE_ADAMANTITE)
- #### BLAST\_MINE\_RUNITE

```
public static final int BLAST_MINE_RUNITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_MINE_RUNITE)
- #### IN\_RAID

```
public static final int IN_RAID
```

Deprecated.
Raids

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.IN_RAID)
- #### TOTAL\_POINTS

```
public static final int TOTAL_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOTAL_POINTS)
- #### RAID\_STATE

```
public static final int RAID_STATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RAID_STATE)
- #### FIRE\_PIT\_GIANT\_MOLE

```
public static final int FIRE_PIT_GIANT_MOLE
```

Deprecated.
Making Friends with My Arm fire pits

Expected values:
0 = Not built
1 = Built

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FIRE_PIT_GIANT_MOLE)
- #### FIRE\_PIT\_LUMBRIDGE\_SWAMP

```
public static final int FIRE_PIT_LUMBRIDGE_SWAMP
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FIRE_PIT_LUMBRIDGE_SWAMP)
- #### FIRE\_PIT\_MOS\_LE\_HARMLESS

```
public static final int FIRE_PIT_MOS_LE_HARMLESS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FIRE_PIT_MOS_LE_HARMLESS)
- #### THEATRE\_OF\_BLOOD

```
public static final int THEATRE_OF_BLOOD
```

Deprecated.
Theatre of Blood 1=In Party, 2=Inside/Spectator, 3=Dead Spectating

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD)
- #### THEATRE\_OF\_BLOOD\_ORB1

```
public static final int THEATRE_OF_BLOOD_ORB1
```

Deprecated.
Theatre of Blood orb healths
0=hide 1-27=% of health - 27 is 100% health and 1 is 0% health, 30=dead

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD_ORB1)
- #### THEATRE\_OF\_BLOOD\_ORB2

```
public static final int THEATRE_OF_BLOOD_ORB2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD_ORB2)
- #### THEATRE\_OF\_BLOOD\_ORB3

```
public static final int THEATRE_OF_BLOOD_ORB3
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD_ORB3)
- #### THEATRE\_OF\_BLOOD\_ORB4

```
public static final int THEATRE_OF_BLOOD_ORB4
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD_ORB4)
- #### THEATRE\_OF\_BLOOD\_ORB5

```
public static final int THEATRE_OF_BLOOD_ORB5
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.THEATRE_OF_BLOOD_ORB5)
- #### NMZ\_ABSORPTION

```
public static final int NMZ_ABSORPTION
```

Deprecated.
Nightmare Zone

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.NMZ_ABSORPTION)
- #### NMZ\_POINTS

```
public static final int NMZ_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.NMZ_POINTS)
- #### BLAST\_FURNACE\_COPPER\_ORE

```
public static final int BLAST_FURNACE_COPPER_ORE
```

Deprecated.
Blast Furnace

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_COPPER_ORE)
- #### BLAST\_FURNACE\_TIN\_ORE

```
public static final int BLAST_FURNACE_TIN_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_TIN_ORE)
- #### BLAST\_FURNACE\_IRON\_ORE

```
public static final int BLAST_FURNACE_IRON_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_IRON_ORE)
- #### BLAST\_FURNACE\_COAL

```
public static final int BLAST_FURNACE_COAL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_COAL)
- #### BLAST\_FURNACE\_MITHRIL\_ORE

```
public static final int BLAST_FURNACE_MITHRIL_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_MITHRIL_ORE)
- #### BLAST\_FURNACE\_ADAMANTITE\_ORE

```
public static final int BLAST_FURNACE_ADAMANTITE_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_ADAMANTITE_ORE)
- #### BLAST\_FURNACE\_RUNITE\_ORE

```
public static final int BLAST_FURNACE_RUNITE_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_RUNITE_ORE)
- #### BLAST\_FURNACE\_SILVER\_ORE

```
public static final int BLAST_FURNACE_SILVER_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_SILVER_ORE)
- #### BLAST\_FURNACE\_GOLD\_ORE

```
public static final int BLAST_FURNACE_GOLD_ORE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_GOLD_ORE)
- #### BLAST\_FURNACE\_BRONZE\_BAR

```
public static final int BLAST_FURNACE_BRONZE_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_BRONZE_BAR)
- #### BLAST\_FURNACE\_IRON\_BAR

```
public static final int BLAST_FURNACE_IRON_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_IRON_BAR)
- #### BLAST\_FURNACE\_STEEL\_BAR

```
public static final int BLAST_FURNACE_STEEL_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_STEEL_BAR)
- #### BLAST\_FURNACE\_MITHRIL\_BAR

```
public static final int BLAST_FURNACE_MITHRIL_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_MITHRIL_BAR)
- #### BLAST\_FURNACE\_ADAMANTITE\_BAR

```
public static final int BLAST_FURNACE_ADAMANTITE_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_ADAMANTITE_BAR)
- #### BLAST\_FURNACE\_RUNITE\_BAR

```
public static final int BLAST_FURNACE_RUNITE_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_RUNITE_BAR)
- #### BLAST\_FURNACE\_SILVER\_BAR

```
public static final int BLAST_FURNACE_SILVER_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_SILVER_BAR)
- #### BLAST\_FURNACE\_GOLD\_BAR

```
public static final int BLAST_FURNACE_GOLD_BAR
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_GOLD_BAR)
- #### BLAST\_FURNACE\_COFFER

```
public static final int BLAST_FURNACE_COFFER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BLAST_FURNACE_COFFER)
- #### PYRAMID\_PLUNDER\_ROOM\_LOCATION

```
public static final int PYRAMID_PLUNDER_ROOM_LOCATION
```

Deprecated.
Pyramid plunder

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PYRAMID_PLUNDER_ROOM_LOCATION)
- #### PYRAMID\_PLUNDER\_TIMER

```
public static final int PYRAMID_PLUNDER_TIMER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PYRAMID_PLUNDER_TIMER)
- #### PYRAMID\_PLUNDER\_THIEVING\_LEVEL

```
public static final int PYRAMID_PLUNDER_THIEVING_LEVEL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PYRAMID_PLUNDER_THIEVING_LEVEL)
- #### PYRAMID\_PLUNDER\_ROOM

```
public static final int PYRAMID_PLUNDER_ROOM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PYRAMID_PLUNDER_ROOM)
- #### BARROWS\_KILLED\_AHRIM

```
public static final int BARROWS_KILLED_AHRIM
```

Deprecated.
Barrows

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_AHRIM)
- #### BARROWS\_KILLED\_DHAROK

```
public static final int BARROWS_KILLED_DHAROK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_DHAROK)
- #### BARROWS\_KILLED\_GUTHAN

```
public static final int BARROWS_KILLED_GUTHAN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_GUTHAN)
- #### BARROWS\_KILLED\_KARIL

```
public static final int BARROWS_KILLED_KARIL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_KARIL)
- #### BARROWS\_KILLED\_TORAG

```
public static final int BARROWS_KILLED_TORAG
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_TORAG)
- #### BARROWS\_KILLED\_VERAC

```
public static final int BARROWS_KILLED_VERAC
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_KILLED_VERAC)
- #### BARROWS\_REWARD\_POTENTIAL

```
public static final int BARROWS_REWARD_POTENTIAL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_REWARD_POTENTIAL)
- #### BARROWS\_NPCS\_SLAIN

```
public static final int BARROWS_NPCS_SLAIN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BARROWS_NPCS_SLAIN)
- #### SPICY\_STEW\_RED\_SPICES

```
public static final int SPICY_STEW_RED_SPICES
```

Deprecated.
Spicy stew ingredients

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPICY_STEW_RED_SPICES)
- #### SPICY\_STEW\_YELLOW\_SPICES

```
public static final int SPICY_STEW_YELLOW_SPICES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPICY_STEW_YELLOW_SPICES)
- #### SPICY\_STEW\_BROWN\_SPICES

```
public static final int SPICY_STEW_BROWN_SPICES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPICY_STEW_BROWN_SPICES)
- #### SPICY\_STEW\_ORANGE\_SPICES

```
public static final int SPICY_STEW_ORANGE_SPICES
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPICY_STEW_ORANGE_SPICES)
- #### MULTICOMBAT\_AREA

```
public static final int MULTICOMBAT_AREA
```

Deprecated.
Multicombat area

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MULTICOMBAT_AREA)
- #### KINGDOM\_APPROVAL

```
public static final int KINGDOM_APPROVAL
```

Deprecated.
Kingdom of Miscellania Management
Kingdom Approval is represented as a 7-bit unsigned integer; 127 corresponds to 100% approval

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KINGDOM_APPROVAL)
- #### KINGDOM\_COFFER

```
public static final int KINGDOM_COFFER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.KINGDOM_COFFER)
- #### QUEST\_THE\_HAND\_IN\_THE\_SAND

```
public static final int QUEST_THE_HAND_IN_THE_SAND
```

Deprecated.
The Hand in the Sand quest status

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.QUEST_THE_HAND_IN_THE_SAND)
- #### QUEST\_DS2

```
public static final int QUEST_DS2
```

Deprecated.
Dragon slayer 2 quest status

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.QUEST_DS2)
- #### DAILY\_HERB\_BOXES\_COLLECTED

```
public static final int DAILY_HERB_BOXES_COLLECTED
```

Deprecated.
Daily Tasks =Collection availability)

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_HERB_BOXES_COLLECTED)
- #### DAILY\_STAVES\_COLLECTED

```
public static final int DAILY_STAVES_COLLECTED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_STAVES_COLLECTED)
- #### DAILY\_ESSENCE\_COLLECTED

```
public static final int DAILY_ESSENCE_COLLECTED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_ESSENCE_COLLECTED)
- #### DAILY\_RUNES\_COLLECTED

```
public static final int DAILY_RUNES_COLLECTED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_RUNES_COLLECTED)
- #### DAILY\_SAND\_COLLECTED

```
public static final int DAILY_SAND_COLLECTED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_SAND_COLLECTED)
- #### DAILY\_FLAX\_STATE

```
public static final int DAILY_FLAX_STATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_FLAX_STATE)
- #### DAILY\_ARROWS\_STATE

```
public static final int DAILY_ARROWS_STATE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_ARROWS_STATE)
- #### DAILY\_BONEMEAL\_STATE

```
public static final int DAILY_BONEMEAL_STATE
```

Deprecated.
This varbit tracks how much bonemeal has been redeemed from Robin
The player gets 13 for each diary completed above and including Medium, for a maxiumum of 39

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_BONEMEAL_STATE)
- #### DAILY\_DYNAMITE\_COLLECTED

```
public static final int DAILY_DYNAMITE_COLLECTED
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DAILY_DYNAMITE_COLLECTED)
- #### FAIR\_RING\_LAST\_DESTINATION

```
public static final int FAIR_RING_LAST_DESTINATION
```

Deprecated.
Fairy Ring

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FAIR_RING_LAST_DESTINATION)
- #### FAIRY\_RING\_DIAL\_ADCB

```
public static final int FAIRY_RING_DIAL_ADCB
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FAIRY_RING_DIAL_ADCB)
- #### FAIRY\_RIGH\_DIAL\_ILJK

```
public static final int FAIRY_RIGH_DIAL_ILJK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FAIRY_RIGH_DIAL_ILJK)
- #### FAIRY\_RING\_DIAL\_PSRQ

```
public static final int FAIRY_RING_DIAL_PSRQ
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FAIRY_RING_DIAL_PSRQ)
- #### FARMING\_4771

```
public static final int FARMING_4771
```

Deprecated.
Transmog controllers for farming

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_4771)
- #### FARMING\_4772

```
public static final int FARMING_4772
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_4772)
- #### FARMING\_4773

```
public static final int FARMING_4773
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_4773)
- #### FARMING\_4774

```
public static final int FARMING_4774
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_4774)
- #### FARMING\_4775

```
public static final int FARMING_4775
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_4775)
- #### FARMING\_7904

```
public static final int FARMING_7904
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7904)
- #### FARMING\_7905

```
public static final int FARMING_7905
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7905)
- #### FARMING\_7906

```
public static final int FARMING_7906
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7906)
- #### FARMING\_7907

```
public static final int FARMING_7907
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7907)
- #### FARMING\_7908

```
public static final int FARMING_7908
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7908)
- #### FARMING\_7909

```
public static final int FARMING_7909
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7909)
- #### FARMING\_7910

```
public static final int FARMING_7910
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7910)
- #### FARMING\_7911

```
public static final int FARMING_7911
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7911)
- #### FARMING\_7912

```
public static final int FARMING_7912
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMING_7912)
- #### GRAPES\_4953

```
public static final int GRAPES_4953
```

Deprecated.
Transmog controllers for grapes

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4953)
- #### GRAPES\_4954

```
public static final int GRAPES_4954
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4954)
- #### GRAPES\_4955

```
public static final int GRAPES_4955
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4955)
- #### GRAPES\_4956

```
public static final int GRAPES_4956
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4956)
- #### GRAPES\_4957

```
public static final int GRAPES_4957
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4957)
- #### GRAPES\_4958

```
public static final int GRAPES_4958
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4958)
- #### GRAPES\_4959

```
public static final int GRAPES_4959
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4959)
- #### GRAPES\_4960

```
public static final int GRAPES_4960
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4960)
- #### GRAPES\_4961

```
public static final int GRAPES_4961
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4961)
- #### GRAPES\_4962

```
public static final int GRAPES_4962
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4962)
- #### GRAPES\_4963

```
public static final int GRAPES_4963
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4963)
- #### GRAPES\_4964

```
public static final int GRAPES_4964
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GRAPES_4964)
- #### AUTOWEED

```
public static final int AUTOWEED
```

Deprecated.
Automatically weed farming patches

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.AUTOWEED)
- #### ACCOUNT\_TYPE

```
public static final int ACCOUNT_TYPE
```

Deprecated.
The player's account type.

0 = normal
1 = ironman
2 = ultimate ironman
3 = hardcore ironman
4 = group ironman
5 = hardcore group ironman
6 = unranked group ironman

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.ACCOUNT_TYPE)
- #### OXYGEN\_LEVEL

```
public static final int OXYGEN_LEVEL
```

Deprecated.
The varbit that stores the oxygen percentage for player

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.OXYGEN_LEVEL)
- #### NORTH\_NET\_STATUS

```
public static final int NORTH_NET_STATUS
```

Deprecated.
Drift net status

Expected values
0 = Unset
1 = Set up
2 = Caught some fish
3 = Full

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.NORTH_NET_STATUS)
- #### SOUTH\_NET\_STATUS

```
public static final int SOUTH_NET_STATUS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SOUTH_NET_STATUS)
- #### NORTH\_NET\_CATCH\_COUNT

```
public static final int NORTH_NET_CATCH_COUNT
```

Deprecated.
Drift net catch count

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.NORTH_NET_CATCH_COUNT)
- #### SOUTH\_NET\_CATCH\_COUNT

```
public static final int SOUTH_NET_CATCH_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SOUTH_NET_CATCH_COUNT)
- #### DRIFT\_NET\_COLLECT

```
public static final int DRIFT_NET_COLLECT
```

Deprecated.
Drift net collect interface

Expected values:
0 = Not open
1 = North interface open
2 = South interface open

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DRIFT_NET_COLLECT)
- #### CORP\_DAMAGE

```
public static final int CORP_DAMAGE
```

Deprecated.
Corp beast damage

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.CORP_DAMAGE)
- #### SUPERIOR\_ENABLED

```
public static final int SUPERIOR_ENABLED
```

Deprecated.
Toggleable slayer unlocks

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SUPERIOR_ENABLED)
- #### FOSSIL\_ISLAND\_WYVERN\_DISABLE

```
public static final int FOSSIL_ISLAND_WYVERN_DISABLE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FOSSIL_ISLAND_WYVERN_DISABLE)
- #### BANK\_REARRANGE\_MODE

```
public static final int BANK_REARRANGE_MODE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_REARRANGE_MODE)
- #### CURRENT\_BANK\_TAB

```
public static final int CURRENT_BANK_TAB
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.CURRENT_BANK_TAB)
- #### BANK\_QUANTITY\_TYPE

```
public static final int BANK_QUANTITY_TYPE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_QUANTITY_TYPE)
- #### BANK\_REQUESTEDQUANTITY

```
public static final int BANK_REQUESTEDQUANTITY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_REQUESTEDQUANTITY)
- #### BANK\_LEAVEPLACEHOLDERS

```
public static final int BANK_LEAVEPLACEHOLDERS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_LEAVEPLACEHOLDERS)
- #### BANK\_ITEM\_OPTIONS

```
public static final int BANK_ITEM_OPTIONS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_ITEM_OPTIONS)
- #### WORLDHOPPER\_FAVORITE\_1

```
public static final int WORLDHOPPER_FAVORITE_1
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WORLDHOPPER_FAVORITE_1)
- #### WORLDHOPPER\_FAVORITE\_2

```
public static final int WORLDHOPPER_FAVORITE_2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WORLDHOPPER_FAVORITE_2)
- #### VENGEANCE\_ACTIVE

```
public static final int VENGEANCE_ACTIVE
```

Deprecated.
Spell activeness

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.VENGEANCE_ACTIVE)
- #### DEATH\_CHARGE

```
public static final int DEATH_CHARGE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DEATH_CHARGE)
- #### RESURRECT\_THRALL

```
public static final int RESURRECT_THRALL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RESURRECT_THRALL)
- #### SHADOW\_VEIL

```
public static final int SHADOW_VEIL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SHADOW_VEIL)
- #### HEAL\_GROUP\_COOLDOWN

```
public static final int HEAL_GROUP_COOLDOWN
```

Deprecated.
Spell cooldowns

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.HEAL_GROUP_COOLDOWN)
- #### VENGEANCE\_COOLDOWN

```
public static final int VENGEANCE_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.VENGEANCE_COOLDOWN)
- #### DEATH\_CHARGE\_COOLDOWN

```
public static final int DEATH_CHARGE_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DEATH_CHARGE_COOLDOWN)
- #### CORRUPTION\_COOLDOWN

```
public static final int CORRUPTION_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.CORRUPTION_COOLDOWN)
- #### RESURRECT\_THRALL\_COOLDOWN

```
public static final int RESURRECT_THRALL_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.RESURRECT_THRALL_COOLDOWN)
- #### SHADOW\_VEIL\_COOLDOWN

```
public static final int SHADOW_VEIL_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SHADOW_VEIL_COOLDOWN)
- #### WARD\_OF\_ARCEUUS\_COOLDOWN

```
public static final int WARD_OF_ARCEUUS_COOLDOWN
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WARD_OF_ARCEUUS_COOLDOWN)
- #### IMBUED\_HEART\_COOLDOWN

```
public static final int IMBUED_HEART_COOLDOWN
```

Deprecated.
Imbued Heart cooldown
Number of game tick remaining on cooldown in intervals of 10; for a value X there are 10 \* X game ticks remaining.
The heart regains its power once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.IMBUED_HEART_COOLDOWN)
- #### DRAGONFIRE\_SHIELD\_COOLDOWN

```
public static final int DRAGONFIRE_SHIELD_COOLDOWN
```

Deprecated.
Dragonfire shield cooldown

Number of game ticks remaining on cooldown in intervals of 8; for a value X there are 8 \* X game ticks remaining.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DRAGONFIRE_SHIELD_COOLDOWN)
- #### BANK\_TAB\_ONE\_COUNT

```
public static final int BANK_TAB_ONE_COUNT
```

Deprecated.
Amount of items in each bank tab

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_ONE_COUNT)
- #### BANK\_TAB\_TWO\_COUNT

```
public static final int BANK_TAB_TWO_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_TWO_COUNT)
- #### BANK\_TAB\_THREE\_COUNT

```
public static final int BANK_TAB_THREE_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_THREE_COUNT)
- #### BANK\_TAB\_FOUR\_COUNT

```
public static final int BANK_TAB_FOUR_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_FOUR_COUNT)
- #### BANK\_TAB\_FIVE\_COUNT

```
public static final int BANK_TAB_FIVE_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_FIVE_COUNT)
- #### BANK\_TAB\_SIX\_COUNT

```
public static final int BANK_TAB_SIX_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_SIX_COUNT)
- #### BANK\_TAB\_SEVEN\_COUNT

```
public static final int BANK_TAB_SEVEN_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_SEVEN_COUNT)
- #### BANK\_TAB\_EIGHT\_COUNT

```
public static final int BANK_TAB_EIGHT_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_EIGHT_COUNT)
- #### BANK\_TAB\_NINE\_COUNT

```
public static final int BANK_TAB_NINE_COUNT
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BANK_TAB_NINE_COUNT)
- #### GE\_OFFER\_CREATION\_TYPE

```
public static final int GE_OFFER_CREATION_TYPE
```

Deprecated.
Type of GE offer currently being created
0 = buy
1 = sell

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GE_OFFER_CREATION_TYPE)
- #### QUEST\_TAB

```
public static final int QUEST_TAB
```

Deprecated.
The active tab within the quest interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.QUEST_TAB)
- #### EXPLORER\_RING\_ALCHTYPE

```
public static final int EXPLORER_RING_ALCHTYPE
```

Deprecated.
Explorer ring

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPLORER_RING_ALCHTYPE)
- #### EXPLORER\_RING\_TELEPORTS

```
public static final int EXPLORER_RING_TELEPORTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPLORER_RING_TELEPORTS)
- #### EXPLORER\_RING\_ALCHS

```
public static final int EXPLORER_RING_ALCHS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPLORER_RING_ALCHS)
- #### EXPLORER\_RING\_RUNENERGY

```
public static final int EXPLORER_RING_RUNENERGY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.EXPLORER_RING_RUNENERGY)
- #### WINTERTODT\_TIMER

```
public static final int WINTERTODT_TIMER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WINTERTODT_TIMER)
- #### LEAGUE\_RELIC\_1

```
public static final int LEAGUE_RELIC_1
```

Deprecated.
League relics

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_1)
- #### LEAGUE\_RELIC\_2

```
public static final int LEAGUE_RELIC_2
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_2)
- #### LEAGUE\_RELIC\_3

```
public static final int LEAGUE_RELIC_3
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_3)
- #### LEAGUE\_RELIC\_4

```
public static final int LEAGUE_RELIC_4
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_4)
- #### LEAGUE\_RELIC\_5

```
public static final int LEAGUE_RELIC_5
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_5)
- #### LEAGUE\_RELIC\_6

```
public static final int LEAGUE_RELIC_6
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_6)
- #### LEAGUE\_RELIC\_7

```
public static final int LEAGUE_RELIC_7
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_7)
- #### LEAGUE\_RELIC\_8

```
public static final int LEAGUE_RELIC_8
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUE_RELIC_8)
- #### MUTED\_MUSIC\_VOLUME

```
public static final int MUTED_MUSIC_VOLUME
```

Deprecated.
Muted volume restore values

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MUTED_MUSIC_VOLUME)
- #### MUTED\_SOUND\_EFFECT\_VOLUME

```
public static final int MUTED_SOUND_EFFECT_VOLUME
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MUTED_SOUND_EFFECT_VOLUME)
- #### MUTED\_AREA\_EFFECT\_VOLUME

```
public static final int MUTED_AREA_EFFECT_VOLUME
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MUTED_AREA_EFFECT_VOLUME)
- #### PARASITE

```
public static final int PARASITE
```

Deprecated.
Parasite infection status during nightmare of ashihama bossfight

0 = not infected
1 = infected

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PARASITE)
- #### WIKI\_ENTITY\_LOOKUP

```
public static final int WIKI_ENTITY_LOOKUP
```

Deprecated.
Whether the vanilla wiki entity lookup is displayed under the minimap

0 = Enabled
1 = Disabled

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WIKI_ENTITY_LOOKUP)
- #### PVP\_SPEC\_ORB

```
public static final int PVP_SPEC_ORB
```

Deprecated.
Whether the player is in a PvP area

0 = Player is not in PvP area
1 = Player is in PvP area

Note: The name of this varbit comes from historical behavior where
the special attack orb would be disabled in PvP, but this was changed
on 2023-03-09 due to Poll 78. Yet, the varbit still updates as before.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PVP_SPEC_ORB)
- #### COLLECTION\_LOG\_NOTIFICATION

```
public static final int COLLECTION_LOG_NOTIFICATION
```

Deprecated.
Collection Log notification settings whenever a new item is added

0 = no notification
1 = chat notification only
2 = popup notification only
3 = chat and popup

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COLLECTION_LOG_NOTIFICATION)
- #### COMBAT\_ACHIEVEMENTS\_POPUP

```
public static final int COMBAT_ACHIEVEMENTS_POPUP
```

Deprecated.
Combat Achievements popup settings whenever a new task is completed

0 = popup notification enabled
1 = popup notification disabled

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENTS_POPUP)
- #### COMBAT\_ACHIEVEMENT\_TIER\_EASY

```
public static final int COMBAT_ACHIEVEMENT_TIER_EASY
```

Deprecated.
Combat Achievement tier completion variables

2 = completed

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_EASY)
- #### COMBAT\_ACHIEVEMENT\_TIER\_MEDIUM

```
public static final int COMBAT_ACHIEVEMENT_TIER_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_MEDIUM)
- #### COMBAT\_ACHIEVEMENT\_TIER\_HARD

```
public static final int COMBAT_ACHIEVEMENT_TIER_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_HARD)
- #### COMBAT\_ACHIEVEMENT\_TIER\_ELITE

```
public static final int COMBAT_ACHIEVEMENT_TIER_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_ELITE)
- #### COMBAT\_ACHIEVEMENT\_TIER\_MASTER

```
public static final int COMBAT_ACHIEVEMENT_TIER_MASTER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_MASTER)
- #### COMBAT\_ACHIEVEMENT\_TIER\_GRANDMASTER

```
public static final int COMBAT_ACHIEVEMENT_TIER_GRANDMASTER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_ACHIEVEMENT_TIER_GRANDMASTER)
- #### BOSS\_HEALTH\_OVERLAY

```
public static final int BOSS_HEALTH_OVERLAY
```

Deprecated.
Show boss health overlay setting
0 = on
1 = off

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BOSS_HEALTH_OVERLAY)
- #### BOSS\_HEALTH\_CURRENT

```
public static final int BOSS_HEALTH_CURRENT
```

Deprecated.
Boss health bar info

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BOSS_HEALTH_CURRENT)
- #### BOSS\_HEALTH\_MAXIMUM

```
public static final int BOSS_HEALTH_MAXIMUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BOSS_HEALTH_MAXIMUM)
- #### SHOW\_PVP\_KDR\_STATS

```
public static final int SHOW_PVP_KDR_STATS
```

Deprecated.
Whether the PVP kill-death stats widget should be drawn while in the wilderness or in PVP worlds.

0 = Disabled
1 = Enabled

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SHOW_PVP_KDR_STATS)
- #### TELEBLOCK

```
public static final int TELEBLOCK
```

Deprecated.
State of Teleblock spell effects on the player

0 = Teleblock inactive, no immunity
1 <= X <= 100 = Teleblock inactive, remaining ticks of immunity from reapplication of spell effect
101 <= Teleblock active, remaining ticks of blocking effect

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TELEBLOCK)
- #### GOD\_WARS\_ALTAR\_COOLDOWN

```
public static final int GOD_WARS_ALTAR_COOLDOWN
```

Deprecated.
Cooldown timer remaining before eligible to restore at a god wars dungeon altar.
Number of game ticks remaining is in intervals of 100; for a value X there are 100 \* X game ticks remaining.
A player can pray at a god wars altar once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.GOD_WARS_ALTAR_COOLDOWN)
- #### SCURRIUS\_FOOD\_PILE\_COOLDOWN

```
public static final int SCURRIUS_FOOD_PILE_COOLDOWN
```

Deprecated.
Cooldown timer remaining before being able to eat from the piles of food in Scurrius's lair.
Number of game ticks remaining is in intervals of 100; for a value X there are 100 \* X game ticks remaining.
A player can eat from the food piles once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SCURRIUS_FOOD_PILE_COOLDOWN)
- #### FARMERS\_AFFINITY

```
public static final int FARMERS_AFFINITY
```

Deprecated.
Farmer's Affinity effect timer
Number of game ticks remaining on Farmer's Affinity effect in intervals of 20; for a value X there are 20 \* X game ticks remaining.
The Farmer's Affinity expires once this reaches 0.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.FARMERS_AFFINITY)
- #### MENAPHITE\_REMEDY

```
public static final int MENAPHITE_REMEDY
```

Deprecated.
If the player has Menaphite remedy effect active.
This will go down by 1 every 25 ticks (15 seconds) and the player's combat stats will be restored by 6 + 16%.
Set to 20 upon consuming potion.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.MENAPHITE_REMEDY)
- #### BUFF\_STAT\_BOOST

```
public static final int BUFF_STAT_BOOST
```

Deprecated.
How many salt stat boost refreshes the player has remaining.
This will go down by 1 every 25 ticks (15 seconds) and the player's stats will be restored.
Set to 32 upon crushing salts.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BUFF_STAT_BOOST)
- #### LIQUID\_ADERNALINE\_ACTIVE

```
public static final int LIQUID_ADERNALINE_ACTIVE
```

Deprecated.
If the player has liquid adrenaline buff active

0 = inactive
1 = active

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LIQUID_ADERNALINE_ACTIVE)
- #### TOA\_RAID\_LEVEL

```
public static final int TOA_RAID_LEVEL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_RAID_LEVEL)
- #### TOA\_RAID\_DAMAGE

```
public static final int TOA_RAID_DAMAGE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_RAID_DAMAGE)
- #### TOA\_MEMBER\_0\_HEALTH

```
public static final int TOA_MEMBER_0_HEALTH
```

Deprecated.
Tombs of Amascut orb healths
0=hide 1-27=% of health - 27 is 100% health and 1 is 0% health, 30=dead

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_0_HEALTH)
- #### TOA\_MEMBER\_1\_HEALTH

```
public static final int TOA_MEMBER_1_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_1_HEALTH)
- #### TOA\_MEMBER\_2\_HEALTH

```
public static final int TOA_MEMBER_2_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_2_HEALTH)
- #### TOA\_MEMBER\_3\_HEALTH

```
public static final int TOA_MEMBER_3_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_3_HEALTH)
- #### TOA\_MEMBER\_4\_HEALTH

```
public static final int TOA_MEMBER_4_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_4_HEALTH)
- #### TOA\_MEMBER\_5\_HEALTH

```
public static final int TOA_MEMBER_5_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_5_HEALTH)
- #### TOA\_MEMBER\_6\_HEALTH

```
public static final int TOA_MEMBER_6_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_6_HEALTH)
- #### TOA\_MEMBER\_7\_HEALTH

```
public static final int TOA_MEMBER_7_HEALTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.TOA_MEMBER_7_HEALTH)
- #### NMZ\_OVERLOAD\_REFRESHES\_REMAINING

```
public static final int NMZ_OVERLOAD_REFRESHES_REMAINING
```

Deprecated.
How many NMZ overload refreshes the player has remaining.

This will go down by 1 every 25 ticks (15 seconds) and the player's stats will be restored.
Set to 20 upon drinking an overload.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.NMZ_OVERLOAD_REFRESHES_REMAINING)
- #### COX\_OVERLOAD\_REFRESHES\_REMAINING

```
public static final int COX_OVERLOAD_REFRESHES_REMAINING
```

Deprecated.
How many Chambers of Xeric overload refreshes the player has remaining.

This will go down by 1 every 25 ticks (15 seconds) and the player's stats will be restored.
Set to 20 upon drinking an overload.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COX_OVERLOAD_REFRESHES_REMAINING)
- #### SLAYER\_POINTS

```
public static final int SLAYER_POINTS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SLAYER_POINTS)
- #### SLAYER\_TASK\_STREAK

```
public static final int SLAYER_TASK_STREAK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SLAYER_TASK_STREAK)
- #### SLAYER\_TASK\_BOSS

```
public static final int SLAYER_TASK_BOSS
```

Deprecated.
The assigned boss for boss slayer.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SLAYER_TASK_BOSS)
- #### DISABLE\_LEVEL\_UP\_INTERFACE

```
public static final int DISABLE_LEVEL_UP_INTERFACE
```

Deprecated.
Whether the level up interface is disabled

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.DISABLE_LEVEL_UP_INTERFACE)
- #### PRAYERBOOK

```
public static final int PRAYERBOOK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.PRAYERBOOK)
- #### VIGGORA\_LOCATION

```
public static final int VIGGORA_LOCATION
```

Deprecated.
During and after Curse of the Empty Lord, Viggora can be located in one of three locations,
which is uniquely and permanently set for each player.
This varbit determines which location he will appear in, which is useful for a master clue step.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.VIGGORA_LOCATION)
- #### SPELLBOOK\_SWAP

```
public static final int SPELLBOOK_SWAP
```

Deprecated.
If the player has a spellbook swap active

0 = inactive
1 = active

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPELLBOOK_SWAP)
- #### SPELLBOOK

```
public static final int SPELLBOOK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPELLBOOK)
- #### SPELLBOOK\_SUBMENU

```
public static final int SPELLBOOK_SUBMENU
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.SPELLBOOK_SUBMENU)
- #### CURSE\_OF\_THE\_MOONS

```
public static final int CURSE_OF_THE_MOONS
```

Deprecated.
The amount of Curse of the Moons stacks received when fighting the Blue Moon or Eclipse Moon.
The varbit value remains 0 when fighting the Blood Moon.
When fighting the Blue Moon, the player's joints will lock up at 18 stacks, which causes their next attack to be
canceled and 18 stacks to be removed.
When fighting the Eclipse Moon, the stacks increase the chance of a player's attack glancing off the shield of
the Eclipse Moon. Glancing attacks reduce the player's max hit by two times the flat armour of the Eclipse Moon.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.CURSE_OF_THE_MOONS)
- #### COLOSSEUM\_DOOM

```
public static final int COLOSSEUM_DOOM
```

Deprecated.
The amount of Doom stacks received in the Fortis Colosseum.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COLOSSEUM_DOOM)
- #### BUFF\_GOADING\_POTION

```
public static final int BUFF_GOADING_POTION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BUFF_GOADING_POTION)
- #### BUFF\_PRAYER\_REGENERATION

```
public static final int BUFF_PRAYER_REGENERATION
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BUFF_PRAYER_REGENERATION)
- #### COLOSSAL\_WYRM\_COURSE\_BASIC

```
public static final int COLOSSAL_WYRM_COURSE_BASIC
```

Deprecated.
The player's progress value for the colossal wyrm advanced basic course.

Max value = 6;

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COLOSSAL_WYRM_COURSE_BASIC)
- #### COLOSSAL\_WYRM\_COURSE\_ADVANCED

```
public static final int COLOSSAL_WYRM_COURSE_ADVANCED
```

Deprecated.
The player's progress value for the colossal wyrm advanced agility course.

Max value = 6;

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COLOSSAL_WYRM_COURSE_ADVANCED)
- #### WINTERTODT\_WARMTH

```
public static final int WINTERTODT_WARMTH
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.WINTERTODT_WARMTH)
- #### COMBAT\_TASK\_EASY

```
public static final int COMBAT_TASK_EASY
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_EASY)
- #### COMBAT\_TASK\_MEDIUM

```
public static final int COMBAT_TASK_MEDIUM
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_MEDIUM)
- #### COMBAT\_TASK\_HARD

```
public static final int COMBAT_TASK_HARD
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_HARD)
- #### COMBAT\_TASK\_ELITE

```
public static final int COMBAT_TASK_ELITE
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_ELITE)
- #### COMBAT\_TASK\_MASTER

```
public static final int COMBAT_TASK_MASTER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_MASTER)
- #### COMBAT\_TASK\_GRANDMASTER

```
public static final int COMBAT_TASK_GRANDMASTER
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.COMBAT_TASK_GRANDMASTER)
- #### LEPRECHAUNS\_LUCK

```
public static final int LEPRECHAUNS_LUCK
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEPRECHAUNS_LUCK)
- #### LEAGUES\_MELEE\_COMBAT\_MASTERY\_LEVEL

```
public static final int LEAGUES_MELEE_COMBAT_MASTERY_LEVEL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUES_MELEE_COMBAT_MASTERY_LEVEL)
- #### LEAGUES\_RANGED\_COMBAT\_MASTERY\_LEVEL

```
public static final int LEAGUES_RANGED_COMBAT_MASTERY_LEVEL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUES_RANGED_COMBAT_MASTERY_LEVEL)
- #### LEAGUES\_MAGIC\_COMBAT\_MASTERY\_LEVEL

```
public static final int LEAGUES_MAGIC_COMBAT_MASTERY_LEVEL
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.LEAGUES_MAGIC_COMBAT_MASTERY_LEVEL)
- #### BURTHORPE\_SLAYER\_MASTER

```
public static final int BURTHORPE_SLAYER_MASTER
```

Deprecated.
The slayer master which is present at Burthorpe.

0 = Turael
1, 2 = Aya
3 = Null

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.BURTHORPE_SLAYER_MASTER)
- #### JARVIS\_GRAVESTONE

```
public static final int JARVIS_GRAVESTONE
```

Deprecated.
The state of Jarvis' gravestone.

0, 2, 3 = Bush (eg. saved Jarvis, or did not partake in the 2017 Halloween event)
1 = Gravestone

See Also:
[Gravestone (Jarvis) - OSRS Wiki](https://oldschool.runescape.wiki/w/Gravestone_(Jarvis)),
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.JARVIS_GRAVESTONE)
- #### IN\_LMS

```
public static final int IN_LMS
```

Deprecated.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Varbits.IN_LMS)

+ ### Constructor Detail

- #### Varbits

```
public Varbits()
```

Deprecated.