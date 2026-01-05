# Experience (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Experience.html

**Package:** Packagenet.runelite.api

**Description:** Skill levels calculated and handled by this class are within (inclusive)
 the range 1-126 rather than 1-99 to account for virtual levels obtained
 when reaching the 200M experience limit....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.Experience

* ---

```
public class Experience
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A utility class used for calculating experience related values.

Skill levels calculated and handled by this class are within (inclusive)
the range 1-126 rather than 1-99 to account for virtual levels obtained
when reaching the 200M experience limit.

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[MAX\_COMBAT\_LEVEL](#MAX_COMBAT_LEVEL)` | The maximum possible combat level. |
| `static int` | `[MAX\_REAL\_LEVEL](#MAX_REAL_LEVEL)` | Maximum effective skill level at 13,034,431 experience. |
| `static int` | `[MAX\_SKILL\_XP](#MAX_SKILL_XP)` | |
| `static int` | `[MAX\_VIRT\_LEVEL](#MAX_VIRT_LEVEL)` | The maximum virtual skill level for any skill (200M experience). |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Experience](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getCombatLevel](#getCombatLevel(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculates a regular combat level. |
| `static double` | `[getCombatLevelPrecise](#getCombatLevelPrecise(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculates a non-virtual high-precision combat level without integer
rounding. |
| `static int` | `[getLevelForXp](#getLevelForXp(int))​(int xp)` | Gets the skill level for the passed total experience. |
| `static int` | `[getNextCombatLevelHpDef](#getNextCombatLevelHpDef(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculate number of hitpoints/defence levels required to increase combat level. |
| `static int` | `[getNextCombatLevelMagic](#getNextCombatLevelMagic(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculate number of magic levels required to increase combat level. |
| `static int` | `[getNextCombatLevelMelee](#getNextCombatLevelMelee(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculate number of attack/strength levels required to increase combat level. |
| `static int` | `[getNextCombatLevelPrayer](#getNextCombatLevelPrayer(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculate number of prayer levels required to increase combat level. |
| `static int` | `[getNextCombatLevelRange](#getNextCombatLevelRange(int,int,int,int,int,int,int))​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)` | Calculate number of ranged levels required to increase combat level. |
| `static int` | `[getXpForLevel](#getXpForLevel(int))​(int level)` | Gets the total experience required to obtain the passed skill
level. |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### MAX\_REAL\_LEVEL

```
public static final int MAX_REAL_LEVEL
```

Maximum effective skill level at 13,034,431 experience.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Experience.MAX_REAL_LEVEL)
- #### MAX\_VIRT\_LEVEL

```
public static final int MAX_VIRT_LEVEL
```

The maximum virtual skill level for any skill (200M experience).

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Experience.MAX_VIRT_LEVEL)
- #### MAX\_SKILL\_XP

```
public static final int MAX_SKILL_XP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Experience.MAX_SKILL_XP)
- #### MAX\_COMBAT\_LEVEL

```
public static final int MAX_COMBAT_LEVEL
```

The maximum possible combat level.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.Experience.MAX_COMBAT_LEVEL)

+ ### Constructor Detail

- #### Experience

```
public Experience()
```

+ ### Method Detail

- #### getXpForLevel

```
public static int getXpForLevel​(int level)
```

Gets the total experience required to obtain the passed skill
level.

Parameters:
`level` - the skill level
Returns:
the required experience for the level
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if skill level is invalid
- #### getLevelForXp

```
public static int getLevelForXp​(int xp)
```

Gets the skill level for the passed total experience.

Parameters:
`xp` - the passed experience (non-negative)
Returns:
the skill level
- #### getCombatLevelPrecise

```
public static double getCombatLevelPrecise​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculates a non-virtual high-precision combat level without integer
rounding.

Combat levels range between 1.15 and ~126.1.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the non-virtual combat level
- #### getCombatLevel

```
public static int getCombatLevel​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculates a regular combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the combat level, rounded down
- #### getNextCombatLevelMelee

```
public static int getNextCombatLevelMelee​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculate number of attack/strength levels required to increase combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the number of levels required
- #### getNextCombatLevelHpDef

```
public static int getNextCombatLevelHpDef​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculate number of hitpoints/defence levels required to increase combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the number of levels required
- #### getNextCombatLevelMagic

```
public static int getNextCombatLevelMagic​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculate number of magic levels required to increase combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the number of levels required
- #### getNextCombatLevelRange

```
public static int getNextCombatLevelRange​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculate number of ranged levels required to increase combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the number of levels required
- #### getNextCombatLevelPrayer

```
public static int getNextCombatLevelPrayer​(int attackLevel,
int strengthLevel,
int defenceLevel,
int hitpointsLevel,
int magicLevel,
int rangeLevel,
int prayerLevel)
```

Calculate number of prayer levels required to increase combat level.

Parameters:
`attackLevel` - the attack level
`strengthLevel` - the strength level
`defenceLevel` - the defence level
`hitpointsLevel` - the hitpoints level
`magicLevel` - the magic level
`rangeLevel` - the range level
`prayerLevel` - the prayer level
Returns:
the number of levels required