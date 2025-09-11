# Combat (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Combat.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Combat

* ---

```
public class Combat
extends java.lang.Object
```

Contains utility methods for interacting with the combat tab and obtaining other combat related information

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")` | An attack style that is selectable on the combat tab |
| `static class` | `[Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk")` | A spell that can be autocast |
| `static class` | `[Combat.WeaponType](Combat.WeaponType.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Combat](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[activateSpecialAttack](#activateSpecialAttack())()` | Attempts to activate special attack, using the spec orb if able |
| `static boolean` | `[activateSpecialAttack](#activateSpecialAttack(boolean))​(boolean orb)` | Attempts to activate special attack |
| `static boolean` | `[canUseSpecialAttack](#canUseSpecialAttack())()` | Checks if we have enough special attack energy to use a special attack |
| `static java.util.Optional<[Player](types/Player.html "class in org.tribot.script.sdk.types")>` | `[getAttackingPlayer](#getAttackingPlayer())()` | Gets the player that we are attacking |
| `static java.util.Optional<java.lang.Integer>` | `[getAttackStyleIndexFor](#getAttackStyleIndexFor(org.tribot.script.sdk.Combat.AttackStyle))​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)` | Gets the current attack style index for the specified attack style |
| `static java.util.List<java.lang.String>` | `[getAttackStyleNames](#getAttackStyleNames())()` | Gets the available attack actions (the text on the combat style tabs). |
| `static java.util.Optional<[Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk")>` | `[getAutocastSpell](#getAutocastSpell())()` | Gets the currently selected autocast spell |
| `static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk")` | `[getCurrentAttackStyle](#getCurrentAttackStyle())()` | Gets the current [`Combat.AttackStyle`](Combat.AttackStyle.html "enum in org.tribot.script.sdk") |
| `static int` | `[getSelectedAttackStyleIndex](#getSelectedAttackStyleIndex())()` | Gets the selected attack style index |
| `static int` | `[getSpecialAttackPercent](#getSpecialAttackPercent())()` | Gets the current amount of special attack available (out of 100) |
| `static java.util.Optional<java.lang.String>` | `[getWeaponName](#getWeaponName())()` | Gets the current weapon name |
| `static int` | `[getWeaponSpecialAttackPercent](#getWeaponSpecialAttackPercent())()` | Gets the special attack percent required for the current weapon |
| `static int` | `[getWeaponSpecialAttackPercent](#getWeaponSpecialAttackPercent(int))​(int id)` | Gets the special attack percent required for the specified weapon |
| `static [Combat.WeaponType](Combat.WeaponType.html "enum in org.tribot.script.sdk")` | `[getWeaponType](#getWeaponType())()` | Gets the current weapon type |
| `static int` | `[getWildernessLevel](#getWildernessLevel())()` | Gets the level of wilderness the player character is in, based on WorldTile position. |
| `static boolean` | `[isAttackStyleAvailable](#isAttackStyleAvailable(org.tribot.script.sdk.Combat.AttackStyle))​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)` | Checks if the specified attack style is currently available |
| `static boolean` | `[isAttackStyleSet](#isAttackStyleSet(org.tribot.script.sdk.Combat.AttackStyle))​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)` | Checks if the specified attack style is currently set |
| `static boolean` | `[isAutoRetaliateOn](#isAutoRetaliateOn())()` | Checks if auto retaliate is on |
| `static boolean` | `[isDefensiveAutocasting](#isDefensiveAutocasting())()` | Checks if we are defensive autocasting |
| `static boolean` | `[isInMultiCombat](#isInMultiCombat())()` | Checks if we are in a multi combat zone |
| `static boolean` | `[isInWilderness](#isInWilderness())()` | Determines if the player character is in the wilderness. |
| `static boolean` | `[isSpecialAttackEnabled](#isSpecialAttackEnabled())()` | Checks if special attack is enabled (ex. |
| `static boolean` | `[isSpecOrbDisabled](#isSpecOrbDisabled())()` | Checks if the spec orb is disabled due to being in a PvP zone |
| `static boolean` | `[isWeaponSpecialAttackAvailable](#isWeaponSpecialAttackAvailable())()` | Checks if the currently equipped weapon supports special attacks |
| `static boolean` | `[setAttackByIndex](#setAttackByIndex(int))​(int index)` | Attempts to select the specified combat style index if not already selected |
| `static boolean` | `[setAttackByName](#setAttackByName(java.lang.String))​(java.lang.String actionName)` | Attempts to select the specified attack action if not already selected. |
| `static boolean` | `[setAttackStyle](#setAttackStyle(org.tribot.script.sdk.Combat.AttackStyle))​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)` | Sets the specified attack style |
| `static boolean` | `[setAutocastSpell](#setAutocastSpell(org.tribot.script.sdk.Combat.AutocastableSpell))​([Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk") spell)` | Attempts to autocast the specified autocastable spell, not using defensive |
| `static boolean` | `[setAutocastSpell](#setAutocastSpell(org.tribot.script.sdk.Combat.AutocastableSpell,boolean))​([Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk") spell,
boolean defensive)` | Attempts to autocast the specified autocastable spell |
| `static boolean` | `[setAutoRetaliate](#setAutoRetaliate(boolean))​(boolean active)` | Attempts to enable or disable auto retaliate |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Combat

```
public Combat()
```

+ ### Method Detail

- #### getWeaponName

```
public static java.util.Optional<java.lang.String> getWeaponName()
```

Gets the current weapon name

Returns:
the current weapon name
- #### setAttackByName

```
public static boolean setAttackByName​(java.lang.String actionName)
```

Attempts to select the specified attack action if not already selected.

Parameters:
`actionName` - the action to select. Will select the first action which matches this parameter
Returns:
true if successful, false otherwise
- #### setAttackByIndex

```
public static boolean setAttackByIndex​(int index)
```

Attempts to select the specified combat style index if not already selected

Parameters:
`index` - The index to select (0-3)
Returns:
true if successful; false otherwise
- #### getSelectedAttackStyleIndex

```
public static int getSelectedAttackStyleIndex()
```

Gets the selected attack style index

Returns:
the selected attack style index
- #### getAttackStyleNames

```
public static java.util.List<java.lang.String> getAttackStyleNames()
```

Gets the available attack actions (the text on the combat style tabs). Example: Chop, Hack, Smash, Block

Returns:
the available attack actions
- #### isAutoRetaliateOn

```
public static boolean isAutoRetaliateOn()
```

Checks if auto retaliate is on

Returns:
true if auto retaliate is on, false otherwise
- #### setAutoRetaliate

```
public static boolean setAutoRetaliate​(boolean active)
```

Attempts to enable or disable auto retaliate

Parameters:
`active` - true to enable auto retaliate, false to disable
Returns:
true if successful, false otherwise
- #### getSpecialAttackPercent

```
public static int getSpecialAttackPercent()
```

Gets the current amount of special attack available (out of 100)

Returns:
the current amount of special attack energy available
- #### activateSpecialAttack

```
public static boolean activateSpecialAttack()
```

Attempts to activate special attack, using the spec orb if able

Returns:
true if successful, false otherwise
- #### canUseSpecialAttack

```
public static boolean canUseSpecialAttack()
```

Checks if we have enough special attack energy to use a special attack

Returns:
true if the current weapon supports special attacks and we have enough special attack energy to use it
- #### isWeaponSpecialAttackAvailable

```
public static boolean isWeaponSpecialAttackAvailable()
```

Checks if the currently equipped weapon supports special attacks

Returns:
true if the currently equipped weapon supports special attacks, false otherwise
- #### activateSpecialAttack

```
public static boolean activateSpecialAttack​(boolean orb)
```

Attempts to activate special attack

Parameters:
`orb` - true to click the orb by the minimap, false to use the combat tab
Returns:
true if successful, false otherwise
- #### isSpecialAttackEnabled

```
public static boolean isSpecialAttackEnabled()
```

Checks if special attack is enabled (ex. the next attack will be a special attack)

Returns:
true if special attack is currently enabled, false otherwise
- #### getWeaponSpecialAttackPercent

```
public static int getWeaponSpecialAttackPercent()
```

Gets the special attack percent required for the current weapon

Returns:
the special attack percent required for the current weapon
- #### getWeaponSpecialAttackPercent

```
public static int getWeaponSpecialAttackPercent​(int id)
```

Gets the special attack percent required for the specified weapon

Parameters:
`id` - the specified weapon id
Returns:
the special attack percent required for the specified weapon
- #### isInMultiCombat

```
public static boolean isInMultiCombat()
```

Checks if we are in a multi combat zone

Returns:
true if we are in a multi combat zone, false otherwise
- #### isInWilderness

```
public static boolean isInWilderness()
```

Determines if the player character is in the wilderness.

Returns:
True if in the wilderness. False otherwise.
- #### getWildernessLevel

```
public static int getWildernessLevel()
```

Gets the level of wilderness the player character is in, based on WorldTile position.

Returns:
The wilderness level. 0 if not in the wilderness.
- #### isSpecOrbDisabled

```
public static boolean isSpecOrbDisabled()
```

Checks if the spec orb is disabled due to being in a PvP zone

Returns:
true if the spec orb is disabled due to being in a PvP zone, false otherwise
- #### getAttackingPlayer

```
public static java.util.Optional<[Player](types/Player.html "class in org.tribot.script.sdk.types")> getAttackingPlayer()
```

Gets the player that we are attacking

Returns:
the player that we are attacking
- #### getCurrentAttackStyle

```
public static [Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") getCurrentAttackStyle()
```

Gets the current [`Combat.AttackStyle`](Combat.AttackStyle.html "enum in org.tribot.script.sdk")

Returns:
the current attack style
- #### getAttackStyleIndexFor

```
public static java.util.Optional<java.lang.Integer> getAttackStyleIndexFor​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)
```

Gets the current attack style index for the specified attack style

Parameters:
`style` - the attack style
Returns:
the attack style index, or an empty optional if the specified attack style isn't available
- #### getWeaponType

```
public static [Combat.WeaponType](Combat.WeaponType.html "enum in org.tribot.script.sdk") getWeaponType()
```

Gets the current weapon type

Returns:
the current weapon type
- #### isAttackStyleSet

```
public static boolean isAttackStyleSet​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)
```

Checks if the specified attack style is currently set

Parameters:
`style` - the attack style
Returns:
true if the specified attack style is currently set, false otherwise
- #### isAttackStyleAvailable

```
public static boolean isAttackStyleAvailable​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)
```

Checks if the specified attack style is currently available

Parameters:
`style` - the attack style
Returns:
true if the attack style is currently available, false otherwise
- #### setAttackStyle

```
public static boolean setAttackStyle​([Combat.AttackStyle](Combat.AttackStyle.html "enum in org.tribot.script.sdk") style)
```

Sets the specified attack style

Parameters:
`style` - the attack style to set
Returns:
true if successful, false otherwise
- #### isDefensiveAutocasting

```
public static boolean isDefensiveAutocasting()
```

Checks if we are defensive autocasting

Returns:
true if we are defensive autocasting, false otherwise
- #### setAutocastSpell

```
public static boolean setAutocastSpell​([Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk") spell)
```

Attempts to autocast the specified autocastable spell, not using defensive

Parameters:
`spell` - the spell to autocast
Returns:
true if successful, false otherwise
- #### setAutocastSpell

```
public static boolean setAutocastSpell​([Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk") spell,
boolean defensive)
```

Attempts to autocast the specified autocastable spell

Parameters:
`spell` - the spell to autocast
`defensive` - true to use defensive autocasting, false otherwise
Returns:
true is successful, false otherwise
- #### getAutocastSpell

```
public static java.util.Optional<[Combat.AutocastableSpell](Combat.AutocastableSpell.html "enum in org.tribot.script.sdk")> getAutocastSpell()
```

Gets the currently selected autocast spell

Returns:
the currently selected autocast spell