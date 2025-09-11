# MyPlayer (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MyPlayer.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.MyPlayer

* ---

```
public class MyPlayer
extends java.lang.Object
```

Static convenience methods for the local player.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")` | An account type |
| `static class` | `[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")` | The various states of teleblock
0 = not currently active
0 - 100 = not active, but immune
100 - 600 = currently active |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[MyPlayer](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static java.util.Optional<[Player](types/Player.html "class in org.tribot.script.sdk.types")>` | `[get](#get())()` | Gets the [`Player`](types/Player.html "class in org.tribot.script.sdk.types") that corresponds to the local player |
| `static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk")` | `[getAccountType](#getAccountType())()` | Gets the account type of the local player |
| `static int` | `[getAnimation](#getAnimation())()` | Gets the animation of local player |
| `static int` | `[getCombatLevel](#getCombatLevel())()` | Gets the local player's combat level |
| `static int` | `[getCurrentHealth](#getCurrentHealth())()` | Gets the current health of the local player |
| `static double` | `[getCurrentHealthPercent](#getCurrentHealthPercent())()` | Gets the local player's health percent out of 100 |
| `static java.util.Optional<[WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")>` | `[getDestination](#getDestination())()` | Gets the player's destination. |
| `static int` | `[getMaxHealth](#getMaxHealth())()` | Gets the max health of the local player |
| `static int` | `[getMembershipDaysRemaining](#getMembershipDaysRemaining())()` | Gets the remaining membership days of the local player |
| `static int` | `[getPoisonDamage](#getPoisonDamage())()` | Gets the amount of poison damage the current player is taking (how much damage the player will take next poison hit) |
| `static [WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")` | `[getPosition](#getPosition())()` | Deprecated.
see [`getTile()`](#getTile()) for the same functionality
|
| `static int` | `[getQuestPoints](#getQuestPoints())()` | Gets the local player's quest points |
| `static int` | `[getRunEnergy](#getRunEnergy())()` | Gets the current run energy of the player character. |
| `static java.util.Optional<[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")>` | `[getTeleblockState](#getTeleblockState())()` | Gets the current teleblock state of the player |
| `static [WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the tile of the local player |
| `static int` | `[getTotalLevel](#getTotalLevel())()` | Gets the total level of the local player |
| `static java.lang.String` | `[getUsername](#getUsername())()` | Gets the username of the local player |
| `static int` | `[getVenomDamage](#getVenomDamage())()` | Gets the amount of venom damage the current player is taking (how much damage the player will take next venom hit) |
| `static int` | `[getWeight](#getWeight())()` | Gets the current weight of the player. |
| `static boolean` | `[isAnimating](#isAnimating())()` | Checks if the local player is animating |
| `static boolean` | `[isDiseased](#isDiseased())()` | Checks if the local player is diseased |
| `static boolean` | `[isHealthBarVisible](#isHealthBarVisible())()` | Checks if the local player's health bar is visible |
| `static boolean` | `[isMember](#isMember())()` | Checks if the current player is a member |
| `static boolean` | `[isMoving](#isMoving())()` | Checks if the local player is moving |
| `static boolean` | `[isPoisoned](#isPoisoned())()` | Checks if the local player is poisoned |
| `static boolean` | `[isPoisonImmune](#isPoisonImmune())()` | Checks if the local player is poison immune |
| `static boolean` | `[isStaminaActive](#isStaminaActive())()` | Checks if a stamina potion is currently active |
| `static boolean` | `[isVenomed](#isVenomed())()` | Checks if the local player is venomed |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### MyPlayer

```
public MyPlayer()
```

+ ### Method Detail

- #### get

```
public static java.util.Optional<[Player](types/Player.html "class in org.tribot.script.sdk.types")> get()
```

Gets the [`Player`](types/Player.html "class in org.tribot.script.sdk.types") that corresponds to the local player

Returns:
the local player
- #### getUsername

```
public static java.lang.String getUsername()
```

Gets the username of the local player

Returns:
the username of the local player
- #### getPosition

```
@Deprecated
public static [WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types") getPosition()
```

Deprecated.
see [`getTile()`](#getTile()) for the same functionality

Gets the position of the local player

Returns:
the position of the local player
- #### getTile

```
public static [WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Gets the tile of the local player

Returns:
the tile of the local player
- #### isAnimating

```
public static boolean isAnimating()
```

Checks if the local player is animating

Returns:
true if animating, false otherwise
- #### getAnimation

```
public static int getAnimation()
```

Gets the animation of local player

Returns:
animation of the local player
- #### isMoving

```
public static boolean isMoving()
```

Checks if the local player is moving

Returns:
true if moving, false otherwise
- #### isPoisoned

```
public static boolean isPoisoned()
```

Checks if the local player is poisoned

Returns:
true if poisoned, false otherwise
- #### isVenomed

```
public static boolean isVenomed()
```

Checks if the local player is venomed

Returns:
true if venomed, false otherwise
- #### isDiseased

```
public static boolean isDiseased()
```

Checks if the local player is diseased

Returns:
true if diseased, false otherwise
- #### isPoisonImmune

```
public static boolean isPoisonImmune()
```

Checks if the local player is poison immune

Returns:
true if poison immune, false otherwise
- #### getPoisonDamage

```
public static int getPoisonDamage()
```

Gets the amount of poison damage the current player is taking (how much damage the player will take next poison hit)

Returns:
the current poison damage, 0 if not poisoned
- #### getVenomDamage

```
public static int getVenomDamage()
```

Gets the amount of venom damage the current player is taking (how much damage the player will take next venom hit)

Returns:
the current venom damage, 0 if not venomed
- #### getCurrentHealth

```
public static int getCurrentHealth()
```

Gets the current health of the local player

Returns:
the current health of the local player
- #### getMaxHealth

```
public static int getMaxHealth()
```

Gets the max health of the local player

Returns:
the max health of the local player
- #### getCurrentHealthPercent

```
public static double getCurrentHealthPercent()
```

Gets the local player's health percent out of 100

Returns:
the local player's health percent out of 100
- #### isHealthBarVisible

```
public static boolean isHealthBarVisible()
```

Checks if the local player's health bar is visible

Returns:
true if the local player's health bar is visible, false otherwise
- #### getCombatLevel

```
public static int getCombatLevel()
```

Gets the local player's combat level

Returns:
the local player's combat level
- #### getQuestPoints

```
public static int getQuestPoints()
```

Gets the local player's quest points

Returns:
the local player's quest points
See Also:
[`Quest`](Quest.html "enum in org.tribot.script.sdk")
- #### getAccountType

```
public static [MyPlayer.AccountType](MyPlayer.AccountType.html "enum in org.tribot.script.sdk") getAccountType()
```

Gets the account type of the local player

Returns:
the account type of the local player
- #### getMembershipDaysRemaining

```
public static int getMembershipDaysRemaining()
```

Gets the remaining membership days of the local player

Returns:
the remaining membership days
- #### isMember

```
public static boolean isMember()
```

Checks if the current player is a member

Returns:
true if the current player is a member, false otherwise
- #### getDestination

```
public static java.util.Optional<[WorldTile](types/WorldTile.html "class in org.tribot.script.sdk.types")> getDestination()
```

Gets the player's destination. This is the red flag seen in the minimap when clicking a tile.

Returns:
the player's destination tile
- #### getTotalLevel

```
public static int getTotalLevel()
```

Gets the total level of the local player

Returns:
the total level of the local player
- #### isStaminaActive

```
public static boolean isStaminaActive()
```

Checks if a stamina potion is currently active

Returns:
true if a stamina potion is active, false otherwise
- #### getRunEnergy

```
public static int getRunEnergy()
```

Gets the current run energy of the player character.

Returns:
The current run energy (0-100)
- #### getWeight

```
public static int getWeight()
```

Gets the current weight of the player.

Returns:
The current weight of the player in kg.
- #### getTeleblockState

```
public static java.util.Optional<[MyPlayer.TeleblockState](MyPlayer.TeleblockState.html "enum in org.tribot.script.sdk")> getTeleblockState()
```

Gets the current teleblock state of the player

Returns:
the current teleblock state of the player