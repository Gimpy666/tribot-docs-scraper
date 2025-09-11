# Prayer (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Prayer.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + java.lang.Enum<[Prayer](Prayer.html "enum in org.tribot.script.sdk")>
+ - org.tribot.script.sdk.Prayer

* All Implemented Interfaces:
`java.io.Serializable`, `java.lang.Comparable<[Prayer](Prayer.html "enum in org.tribot.script.sdk")>`

---

```
public enum Prayer
extends java.lang.Enum<[Prayer](Prayer.html "enum in org.tribot.script.sdk")>
```

A prayer listed under the prayer tab

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AUGURY](#AUGURY)` | |
| `[BURST\_OF\_STRENGTH](#BURST_OF_STRENGTH)` | |
| `[CHIVALRY](#CHIVALRY)` | |
| `[CLARITY\_OF\_THOUGHT](#CLARITY_OF_THOUGHT)` | |
| `[DEADEYE](#DEADEYE)` | |
| `[EAGLE\_EYE](#EAGLE_EYE)` | |
| `[HAWK\_EYE](#HAWK_EYE)` | |
| `[IMPROVED\_REFLEXES](#IMPROVED_REFLEXES)` | |
| `[INCREDIBLE\_REFLEXES](#INCREDIBLE_REFLEXES)` | |
| `[MYSTIC\_LORE](#MYSTIC_LORE)` | |
| `[MYSTIC\_MIGHT](#MYSTIC_MIGHT)` | |
| `[MYSTIC\_VIGOUR](#MYSTIC_VIGOUR)` | |
| `[MYSTIC\_WILL](#MYSTIC_WILL)` | |
| `[PIETY](#PIETY)` | |
| `[PRESERVE](#PRESERVE)` | |
| `[PROTECT\_FROM\_MAGIC](#PROTECT_FROM_MAGIC)` | |
| `[PROTECT\_FROM\_MELEE](#PROTECT_FROM_MELEE)` | |
| `[PROTECT\_FROM\_MISSILES](#PROTECT_FROM_MISSILES)` | |
| `[PROTECT\_ITEMS](#PROTECT_ITEMS)` | |
| `[RAPID\_HEAL](#RAPID_HEAL)` | |
| `[RAPID\_RESTORE](#RAPID_RESTORE)` | |
| `[REDEMPTION](#REDEMPTION)` | |
| `[RETRIBUTION](#RETRIBUTION)` | |
| `[RIGOUR](#RIGOUR)` | |
| `[ROCK\_SKIN](#ROCK_SKIN)` | |
| `[SHARP\_EYE](#SHARP_EYE)` | |
| `[SMITE](#SMITE)` | |
| `[STEEL\_SKIN](#STEEL_SKIN)` | |
| `[SUPERHUMAN\_STRENGTH](#SUPERHUMAN_STRENGTH)` | |
| `[THICK\_SKIN](#THICK_SKIN)` | |
| `[ULTIMATE\_STRENGTH](#ULTIMATE_STRENGTH)` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[disable](#disable())()` | Attempts to disable this prayer |
| `static boolean` | `[disableAll](#disableAll(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Attempts to disable the specified prayers |
| `static boolean` | `[disableQuickPrayer](#disableQuickPrayer())()` | Attmpts to disable quick prayer |
| `boolean` | `[enable](#enable())()` | Attempts to enable this prayer |
| `static boolean` | `[enableAll](#enableAll(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Attempts to enable the specified prayers |
| `static boolean` | `[enableQuickPrayer](#enableQuickPrayer())()` | Attempts to enable quick prayer |
| `boolean` | `[flick](#flick(int))​(int delayMs)` | Attempts to flick this prayer, leaving it active for the specified delay in milliseconds |
| `static java.util.List<[Prayer](Prayer.html "enum in org.tribot.script.sdk")>` | `[getActivePrayers](#getActivePrayers())()` | Gets all active prayers |
| `java.lang.String` | `[getName](#getName())()` | Gets the prayer name |
| `static int` | `[getPrayerPoints](#getPrayerPoints())()` | Gets the current amount of prayer points |
| `int` | `[getRequiredLevel](#getRequiredLevel())()` | Gets the required prayer level for this prayer |
| `static java.util.List<[Prayer](Prayer.html "enum in org.tribot.script.sdk")>` | `[getSelectedQuickPrayers](#getSelectedQuickPrayers())()` | Gets the prayers that will be enabled when quick prayer is enabled |
| `static boolean` | `[isAllDisabled](#isAllDisabled(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Checks if all the specified prayers are disabled |
| `static boolean` | `[isAllEnabled](#isAllEnabled(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Checks if all the specified prayers are enabled |
| `boolean` | `[isEnabled](#isEnabled())()` | Checks if the prayer is currently enabled |
| `static boolean` | `[isQuickPrayerEnabled](#isQuickPrayerEnabled())()` | Checks if quick prayer is currently enabled |
| `boolean` | `[isQuickPrayerSet](#isQuickPrayerSet())()` | Checks if this prayer is set as a prayer that will be activated when quick prayer is activated |
| `static boolean` | `[isQuickPrayersSelected](#isQuickPrayersSelected(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Gets whether or not all of the passed prayers are currently selected as quick prayers |
| `boolean` | `[isUnlocked](#isUnlocked())()` | Checks if this prayer is unlocked (ex. |
| `static boolean` | `[selectQuickPrayers](#selectQuickPrayers(org.tribot.script.sdk.Prayer...))​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)` | Attempts to set the specified quick prayers as prayers that will be active when quick prayer is enabled |
| `static [Prayer](Prayer.html "enum in org.tribot.script.sdk")` | `[valueOf](#valueOf(java.lang.String))​(java.lang.String name)` | Returns the enum constant of this type with the specified name. |
| `static [Prayer](Prayer.html "enum in org.tribot.script.sdk")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
- ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

- #### THICK\_SKIN

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") THICK_SKIN
```
- #### BURST\_OF\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") BURST_OF_STRENGTH
```
- #### CLARITY\_OF\_THOUGHT

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") CLARITY_OF_THOUGHT
```
- #### SHARP\_EYE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") SHARP_EYE
```
- #### MYSTIC\_WILL

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") MYSTIC_WILL
```
- #### ROCK\_SKIN

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") ROCK_SKIN
```
- #### SUPERHUMAN\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") SUPERHUMAN_STRENGTH
```
- #### IMPROVED\_REFLEXES

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") IMPROVED_REFLEXES
```
- #### RAPID\_RESTORE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") RAPID_RESTORE
```
- #### RAPID\_HEAL

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") RAPID_HEAL
```
- #### PROTECT\_ITEMS

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PROTECT_ITEMS
```
- #### HAWK\_EYE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") HAWK_EYE
```
- #### MYSTIC\_LORE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") MYSTIC_LORE
```
- #### STEEL\_SKIN

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") STEEL_SKIN
```
- #### ULTIMATE\_STRENGTH

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") ULTIMATE_STRENGTH
```
- #### INCREDIBLE\_REFLEXES

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") INCREDIBLE_REFLEXES
```
- #### PROTECT\_FROM\_MAGIC

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PROTECT_FROM_MAGIC
```
- #### PROTECT\_FROM\_MISSILES

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PROTECT_FROM_MISSILES
```
- #### PROTECT\_FROM\_MELEE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PROTECT_FROM_MELEE
```
- #### EAGLE\_EYE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") EAGLE_EYE
```
- #### MYSTIC\_MIGHT

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") MYSTIC_MIGHT
```
- #### RETRIBUTION

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") RETRIBUTION
```
- #### REDEMPTION

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") REDEMPTION
```
- #### SMITE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") SMITE
```
- #### PRESERVE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PRESERVE
```
- #### CHIVALRY

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") CHIVALRY
```
- #### PIETY

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") PIETY
```
- #### RIGOUR

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") RIGOUR
```
- #### AUGURY

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") AUGURY
```
- #### MYSTIC\_VIGOUR

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") MYSTIC_VIGOUR
```
- #### DEADEYE

```
public static final [Prayer](Prayer.html "enum in org.tribot.script.sdk") DEADEYE
```

+ ### Method Detail

- #### values

```
public static [Prayer](Prayer.html "enum in org.tribot.script.sdk")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (Prayer c : Prayer.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [Prayer](Prayer.html "enum in org.tribot.script.sdk") valueOf​(java.lang.String name)
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
- #### getName

```
public java.lang.String getName()
```

Gets the prayer name

Returns:
the prayer name
- #### isEnabled

```
public boolean isEnabled()
```

Checks if the prayer is currently enabled

Returns:
true if currently enabled, false otherwise
- #### isQuickPrayerSet

```
public boolean isQuickPrayerSet()
```

Checks if this prayer is set as a prayer that will be activated when quick prayer is activated

Returns:
true if this prayer is set as a quick prayer, false otherwise
- #### enable

```
public boolean enable()
```

Attempts to enable this prayer

Returns:
true if enabled successfully, false otherwise
- #### disable

```
public boolean disable()
```

Attempts to disable this prayer

Returns:
true if disabled succesfully, false otherwise
- #### getRequiredLevel

```
public int getRequiredLevel()
```

Gets the required prayer level for this prayer

Returns:
the required prayer level for this prayer
- #### flick

```
public boolean flick​(int delayMs)
```

Attempts to flick this prayer, leaving it active for the specified delay in milliseconds

Parameters:
`delayMs` - the delay in milliseconds
Returns:
true if flicked successfully, false otherwise
- #### isUnlocked

```
public boolean isUnlocked()
```

Checks if this prayer is unlocked (ex. [`RIGOUR`](#RIGOUR) requires activating some scroll ingame).
If the prayer doesn't require anything specific to unlock it then it will always be unlocked.

Returns:
true if this prayer is unlocked, false otherwise
- #### isAllEnabled

```
public static boolean isAllEnabled​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Checks if all the specified prayers are enabled

Parameters:
`prayers` - the specified prayers
Returns:
true if all the specified prayers are enabled, false otherwise
- #### isAllDisabled

```
public static boolean isAllDisabled​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Checks if all the specified prayers are disabled

Parameters:
`prayers` - the specified prayers
Returns:
true if all the specified prayers are dsiabled, false otherwise
- #### enableAll

```
public static boolean enableAll​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Attempts to enable the specified prayers

Parameters:
`prayers` - the prayers to enable
Returns:
true if all prayers were enabled, false otherwise
- #### disableAll

```
public static boolean disableAll​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Attempts to disable the specified prayers

Parameters:
`prayers` - the prayers to disable
Returns:
true if all prayers were disabled, false otherwise
- #### getPrayerPoints

```
public static int getPrayerPoints()
```

Gets the current amount of prayer points

Returns:
the current prayer points available
- #### getActivePrayers

```
public static java.util.List<[Prayer](Prayer.html "enum in org.tribot.script.sdk")> getActivePrayers()
```

Gets all active prayers

Returns:
the active prayers
- #### getSelectedQuickPrayers

```
public static java.util.List<[Prayer](Prayer.html "enum in org.tribot.script.sdk")> getSelectedQuickPrayers()
```

Gets the prayers that will be enabled when quick prayer is enabled

Returns:
the prayers that are set as quick prayers
- #### isQuickPrayerEnabled

```
public static boolean isQuickPrayerEnabled()
```

Checks if quick prayer is currently enabled

Returns:
true if quick prayer is enabled, false otherwise
- #### enableQuickPrayer

```
public static boolean enableQuickPrayer()
```

Attempts to enable quick prayer

Returns:
true if successful, false otherwise
- #### selectQuickPrayers

```
public static boolean selectQuickPrayers​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Attempts to set the specified quick prayers as prayers that will be active when quick prayer is enabled

Parameters:
`prayers` - the prayers to set
Returns:
true if successful, false otherwise
- #### disableQuickPrayer

```
public static boolean disableQuickPrayer()
```

Attmpts to disable quick prayer

Returns:
true if successful, false otherwise
- #### isQuickPrayersSelected

```
public static boolean isQuickPrayersSelected​([Prayer](Prayer.html "enum in org.tribot.script.sdk")... prayers)
```

Gets whether or not all of the passed prayers are currently selected as quick prayers

Parameters:
`prayers` - The prayers to check
Returns:
True if all the prayers are selected as quick prayers, false otherwise.