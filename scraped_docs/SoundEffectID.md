# SoundEffectID (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/SoundEffectID.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.SoundEffectID

* ---

```
public final class SoundEffectID
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

Utility class used for mapping sound effect IDs.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[ATTACK\_HIT](#ATTACK_HIT)` | |
| `static int` | `[BURY\_BONES](#BURY_BONES)` | |
| `static int` | `[CLOSE\_DOOR](#CLOSE_DOOR)` | |
| `static int` | `[COOK\_WOOSH](#COOK_WOOSH)` | |
| `static int` | `[FIRE\_WOOSH](#FIRE_WOOSH)` | |
| `static int` | `[GE\_ADD\_OFFER\_DINGALING](#GE_ADD_OFFER_DINGALING)` | |
| `static int` | `[GE\_COIN\_TINKLE](#GE_COIN_TINKLE)` | |
| `static int` | `[GE\_COLLECT\_BLOOP](#GE_COLLECT_BLOOP)` | |
| `static int` | `[GE\_DECREMENT\_PLOP](#GE_DECREMENT_PLOP)` | |
| `static int` | `[GE\_INCREMENT\_PLOP](#GE_INCREMENT_PLOP)` | |
| `static int` | `[ITEM\_DROP](#ITEM_DROP)` | |
| `static int` | `[ITEM\_PICKUP](#ITEM_PICKUP)` | |
| `static int` | `[MAGIC\_SPLASH\_BOING](#MAGIC_SPLASH_BOING)` | |
| `static int` | `[MINING\_TINK](#MINING_TINK)` | |
| `static int` | `[NPC\_TELEPORT\_WOOSH](#NPC_TELEPORT_WOOSH)` | Used for random event NPCs spawning, and the imp teleport. |
| `static int` | `[OPEN\_DOOR](#OPEN_DOOR)` | |
| `static int` | `[PICK\_PLANT\_BLOOP](#PICK_PLANT_BLOOP)` | |
| `static int` | `[PRAYER\_ACTIVATE\_BURST\_OF\_STRENGTH](#PRAYER_ACTIVATE_BURST_OF_STRENGTH)` | |
| `static int` | `[PRAYER\_ACTIVATE\_CHIVALRY](#PRAYER_ACTIVATE_CHIVALRY)` | |
| `static int` | `[PRAYER\_ACTIVATE\_CLARITY\_OF\_THOUGHT](#PRAYER_ACTIVATE_CLARITY_OF_THOUGHT)` | |
| `static int` | `[PRAYER\_ACTIVATE\_DEADEYE](#PRAYER_ACTIVATE_DEADEYE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_EAGLE\_EYE](#PRAYER_ACTIVATE_EAGLE_EYE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_HAWK\_EYE](#PRAYER_ACTIVATE_HAWK_EYE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_IMPROVED\_REFLEXES](#PRAYER_ACTIVATE_IMPROVED_REFLEXES)` | |
| `static int` | `[PRAYER\_ACTIVATE\_INCREDIBLE\_REFLEXES](#PRAYER_ACTIVATE_INCREDIBLE_REFLEXES)` | |
| `static int` | `[PRAYER\_ACTIVATE\_MYSTIC\_LORE](#PRAYER_ACTIVATE_MYSTIC_LORE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_MYSTIC\_MIGHT](#PRAYER_ACTIVATE_MYSTIC_MIGHT)` | |
| `static int` | `[PRAYER\_ACTIVATE\_MYSTIC\_VIGOUR](#PRAYER_ACTIVATE_MYSTIC_VIGOUR)` | |
| `static int` | `[PRAYER\_ACTIVATE\_MYSTIC\_WILL\_AUGURY](#PRAYER_ACTIVATE_MYSTIC_WILL_AUGURY)` | |
| `static int` | `[PRAYER\_ACTIVATE\_PIETY](#PRAYER_ACTIVATE_PIETY)` | |
| `static int` | `[PRAYER\_ACTIVATE\_PROTECT\_FROM\_MAGIC](#PRAYER_ACTIVATE_PROTECT_FROM_MAGIC)` | |
| `static int` | `[PRAYER\_ACTIVATE\_PROTECT\_FROM\_MELEE](#PRAYER_ACTIVATE_PROTECT_FROM_MELEE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_PROTECT\_FROM\_MISSILES](#PRAYER_ACTIVATE_PROTECT_FROM_MISSILES)` | |
| `static int` | `[PRAYER\_ACTIVATE\_PROTECT\_ITEM](#PRAYER_ACTIVATE_PROTECT_ITEM)` | |
| `static int` | `[PRAYER\_ACTIVATE\_RAPID\_HEAL](#PRAYER_ACTIVATE_RAPID_HEAL)` | |
| `static int` | `[PRAYER\_ACTIVATE\_RAPID\_RESTORE\_PRESERVE](#PRAYER_ACTIVATE_RAPID_RESTORE_PRESERVE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_REDEMPTION](#PRAYER_ACTIVATE_REDEMPTION)` | |
| `static int` | `[PRAYER\_ACTIVATE\_RETRIBUTION](#PRAYER_ACTIVATE_RETRIBUTION)` | |
| `static int` | `[PRAYER\_ACTIVATE\_ROCK\_SKIN](#PRAYER_ACTIVATE_ROCK_SKIN)` | |
| `static int` | `[PRAYER\_ACTIVATE\_SHARP\_EYE\_RIGOUR](#PRAYER_ACTIVATE_SHARP_EYE_RIGOUR)` | |
| `static int` | `[PRAYER\_ACTIVATE\_SMITE](#PRAYER_ACTIVATE_SMITE)` | |
| `static int` | `[PRAYER\_ACTIVATE\_STEEL\_SKIN](#PRAYER_ACTIVATE_STEEL_SKIN)` | |
| `static int` | `[PRAYER\_ACTIVATE\_SUPERHUMAN\_STRENGTH](#PRAYER_ACTIVATE_SUPERHUMAN_STRENGTH)` | |
| `static int` | `[PRAYER\_ACTIVATE\_THICK\_SKIN](#PRAYER_ACTIVATE_THICK_SKIN)` | |
| `static int` | `[PRAYER\_ACTIVATE\_ULTIMATE\_STRENGTH](#PRAYER_ACTIVATE_ULTIMATE_STRENGTH)` | |
| `static int` | `[PRAYER\_DEACTIVE\_VWOOP](#PRAYER_DEACTIVE_VWOOP)` | |
| `static int` | `[PRAYER\_DEPLETE\_TWINKLE](#PRAYER_DEPLETE_TWINKLE)` | |
| `static int` | `[SMITH\_ANVIL\_TINK](#SMITH_ANVIL_TINK)` | |
| `static int` | `[SMITH\_ANVIL\_TONK](#SMITH_ANVIL_TONK)` | |
| `static int` | `[TAKE\_DAMAGE\_SPLAT](#TAKE_DAMAGE_SPLAT)` | |
| `static int` | `[TELEPORT\_VWOOP](#TELEPORT_VWOOP)` | |
| `static int` | `[TINDER\_STRIKE](#TINDER_STRIKE)` | |
| `static int` | `[TOWN\_CRIER\_BELL\_DING](#TOWN_CRIER_BELL_DING)` | |
| `static int` | `[TOWN\_CRIER\_BELL\_DONG](#TOWN_CRIER_BELL_DONG)` | |
| `static int` | `[TOWN\_CRIER\_SHOUT\_SQUEAK](#TOWN_CRIER_SHOUT_SQUEAK)` | |
| `static int` | `[TREE\_CHOP](#TREE_CHOP)` | |
| `static int` | `[TREE\_FALLING](#TREE_FALLING)` | |
| `static int` | `[UI\_BOOP](#UI_BOOP)` | |
| `static int` | `[ZERO\_DAMAGE\_SPLAT](#ZERO_DAMAGE_SPLAT)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[SoundEffectID](#%3Cinit%3E())()` | |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### UI\_BOOP

```
public static final int UI_BOOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.UI_BOOP)
- #### GE\_INCREMENT\_PLOP

```
public static final int GE_INCREMENT_PLOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.GE_INCREMENT_PLOP)
- #### GE\_DECREMENT\_PLOP

```
public static final int GE_DECREMENT_PLOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.GE_DECREMENT_PLOP)
- #### GE\_ADD\_OFFER\_DINGALING

```
public static final int GE_ADD_OFFER_DINGALING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.GE_ADD_OFFER_DINGALING)
- #### GE\_COLLECT\_BLOOP

```
public static final int GE_COLLECT_BLOOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.GE_COLLECT_BLOOP)
- #### GE\_COIN\_TINKLE

```
public static final int GE_COIN_TINKLE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.GE_COIN_TINKLE)
- #### CLOSE\_DOOR

```
public static final int CLOSE_DOOR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.CLOSE_DOOR)
- #### OPEN\_DOOR

```
public static final int OPEN_DOOR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.OPEN_DOOR)
- #### ITEM\_DROP

```
public static final int ITEM_DROP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.ITEM_DROP)
- #### ITEM\_PICKUP

```
public static final int ITEM_PICKUP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.ITEM_PICKUP)
- #### PICK\_PLANT\_BLOOP

```
public static final int PICK_PLANT_BLOOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PICK_PLANT_BLOOP)
- #### BURY\_BONES

```
public static final int BURY_BONES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.BURY_BONES)
- #### TINDER\_STRIKE

```
public static final int TINDER_STRIKE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TINDER_STRIKE)
- #### FIRE\_WOOSH

```
public static final int FIRE_WOOSH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.FIRE_WOOSH)
- #### TREE\_FALLING

```
public static final int TREE_FALLING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TREE_FALLING)
- #### TREE\_CHOP

```
public static final int TREE_CHOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TREE_CHOP)
- #### MINING\_TINK

```
public static final int MINING_TINK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.MINING_TINK)
- #### COOK\_WOOSH

```
public static final int COOK_WOOSH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.COOK_WOOSH)
- #### MAGIC\_SPLASH\_BOING

```
public static final int MAGIC_SPLASH_BOING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.MAGIC_SPLASH_BOING)
- #### SMITH\_ANVIL\_TINK

```
public static final int SMITH_ANVIL_TINK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.SMITH_ANVIL_TINK)
- #### SMITH\_ANVIL\_TONK

```
public static final int SMITH_ANVIL_TONK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.SMITH_ANVIL_TONK)
- #### NPC\_TELEPORT\_WOOSH

```
public static final int NPC_TELEPORT_WOOSH
```

Used for random event NPCs spawning, and the imp teleport.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.NPC_TELEPORT_WOOSH)
- #### TELEPORT\_VWOOP

```
public static final int TELEPORT_VWOOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TELEPORT_VWOOP)
- #### ZERO\_DAMAGE\_SPLAT

```
public static final int ZERO_DAMAGE_SPLAT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.ZERO_DAMAGE_SPLAT)
- #### TAKE\_DAMAGE\_SPLAT

```
public static final int TAKE_DAMAGE_SPLAT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TAKE_DAMAGE_SPLAT)
- #### ATTACK\_HIT

```
public static final int ATTACK_HIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.ATTACK_HIT)
- #### PRAYER\_ACTIVATE\_THICK\_SKIN

```
public static final int PRAYER_ACTIVATE_THICK_SKIN
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_THICK_SKIN)
- #### PRAYER\_ACTIVATE\_BURST\_OF\_STRENGTH

```
public static final int PRAYER_ACTIVATE_BURST_OF_STRENGTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_BURST_OF_STRENGTH)
- #### PRAYER\_ACTIVATE\_CLARITY\_OF\_THOUGHT

```
public static final int PRAYER_ACTIVATE_CLARITY_OF_THOUGHT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_CLARITY_OF_THOUGHT)
- #### PRAYER\_ACTIVATE\_SHARP\_EYE\_RIGOUR

```
public static final int PRAYER_ACTIVATE_SHARP_EYE_RIGOUR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_SHARP_EYE_RIGOUR)
- #### PRAYER\_ACTIVATE\_MYSTIC\_WILL\_AUGURY

```
public static final int PRAYER_ACTIVATE_MYSTIC_WILL_AUGURY
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_MYSTIC_WILL_AUGURY)
- #### PRAYER\_ACTIVATE\_ROCK\_SKIN

```
public static final int PRAYER_ACTIVATE_ROCK_SKIN
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_ROCK_SKIN)
- #### PRAYER\_ACTIVATE\_SUPERHUMAN\_STRENGTH

```
public static final int PRAYER_ACTIVATE_SUPERHUMAN_STRENGTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_SUPERHUMAN_STRENGTH)
- #### PRAYER\_ACTIVATE\_IMPROVED\_REFLEXES

```
public static final int PRAYER_ACTIVATE_IMPROVED_REFLEXES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_IMPROVED_REFLEXES)
- #### PRAYER\_ACTIVATE\_RAPID\_RESTORE\_PRESERVE

```
public static final int PRAYER_ACTIVATE_RAPID_RESTORE_PRESERVE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_RAPID_RESTORE_PRESERVE)
- #### PRAYER\_ACTIVATE\_RAPID\_HEAL

```
public static final int PRAYER_ACTIVATE_RAPID_HEAL
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_RAPID_HEAL)
- #### PRAYER\_ACTIVATE\_PROTECT\_ITEM

```
public static final int PRAYER_ACTIVATE_PROTECT_ITEM
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_PROTECT_ITEM)
- #### PRAYER\_ACTIVATE\_HAWK\_EYE

```
public static final int PRAYER_ACTIVATE_HAWK_EYE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_HAWK_EYE)
- #### PRAYER\_ACTIVATE\_MYSTIC\_LORE

```
public static final int PRAYER_ACTIVATE_MYSTIC_LORE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_MYSTIC_LORE)
- #### PRAYER\_ACTIVATE\_STEEL\_SKIN

```
public static final int PRAYER_ACTIVATE_STEEL_SKIN
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_STEEL_SKIN)
- #### PRAYER\_ACTIVATE\_ULTIMATE\_STRENGTH

```
public static final int PRAYER_ACTIVATE_ULTIMATE_STRENGTH
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_ULTIMATE_STRENGTH)
- #### PRAYER\_ACTIVATE\_INCREDIBLE\_REFLEXES

```
public static final int PRAYER_ACTIVATE_INCREDIBLE_REFLEXES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_INCREDIBLE_REFLEXES)
- #### PRAYER\_ACTIVATE\_PROTECT\_FROM\_MAGIC

```
public static final int PRAYER_ACTIVATE_PROTECT_FROM_MAGIC
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_PROTECT_FROM_MAGIC)
- #### PRAYER\_ACTIVATE\_PROTECT\_FROM\_MISSILES

```
public static final int PRAYER_ACTIVATE_PROTECT_FROM_MISSILES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_PROTECT_FROM_MISSILES)
- #### PRAYER\_ACTIVATE\_PROTECT\_FROM\_MELEE

```
public static final int PRAYER_ACTIVATE_PROTECT_FROM_MELEE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_PROTECT_FROM_MELEE)
- #### PRAYER\_ACTIVATE\_EAGLE\_EYE

```
public static final int PRAYER_ACTIVATE_EAGLE_EYE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_EAGLE_EYE)
- #### PRAYER\_ACTIVATE\_DEADEYE

```
public static final int PRAYER_ACTIVATE_DEADEYE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_DEADEYE)
- #### PRAYER\_ACTIVATE\_MYSTIC\_MIGHT

```
public static final int PRAYER_ACTIVATE_MYSTIC_MIGHT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_MYSTIC_MIGHT)
- #### PRAYER\_ACTIVATE\_MYSTIC\_VIGOUR

```
public static final int PRAYER_ACTIVATE_MYSTIC_VIGOUR
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_MYSTIC_VIGOUR)
- #### PRAYER\_ACTIVATE\_RETRIBUTION

```
public static final int PRAYER_ACTIVATE_RETRIBUTION
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_RETRIBUTION)
- #### PRAYER\_ACTIVATE\_REDEMPTION

```
public static final int PRAYER_ACTIVATE_REDEMPTION
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_REDEMPTION)
- #### PRAYER\_ACTIVATE\_SMITE

```
public static final int PRAYER_ACTIVATE_SMITE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_SMITE)
- #### PRAYER\_ACTIVATE\_CHIVALRY

```
public static final int PRAYER_ACTIVATE_CHIVALRY
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_CHIVALRY)
- #### PRAYER\_ACTIVATE\_PIETY

```
public static final int PRAYER_ACTIVATE_PIETY
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_ACTIVATE_PIETY)
- #### PRAYER\_DEACTIVE\_VWOOP

```
public static final int PRAYER_DEACTIVE_VWOOP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_DEACTIVE_VWOOP)
- #### PRAYER\_DEPLETE\_TWINKLE

```
public static final int PRAYER_DEPLETE_TWINKLE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.PRAYER_DEPLETE_TWINKLE)
- #### TOWN\_CRIER\_BELL\_DING

```
public static final int TOWN_CRIER_BELL_DING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TOWN_CRIER_BELL_DING)
- #### TOWN\_CRIER\_BELL\_DONG

```
public static final int TOWN_CRIER_BELL_DONG
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TOWN_CRIER_BELL_DONG)
- #### TOWN\_CRIER\_SHOUT\_SQUEAK

```
public static final int TOWN_CRIER_SHOUT_SQUEAK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.SoundEffectID.TOWN_CRIER_SHOUT_SQUEAK)

+ ### Constructor Detail

- #### SoundEffectID

```
public SoundEffectID()
```