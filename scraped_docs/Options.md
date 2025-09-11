# Options (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Options.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Options

* ---

```
public class Options
extends java.lang.Object
```

Utilities for getting information related to what's in the Options Tab and Minimap HUD. Also provides ways to change
and toggle settings.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Options.AttackOption](Options.AttackOption.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Options.ChatboxScrollPosition](Options.ChatboxScrollPosition.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Options.HouseDoor](Options.HouseDoor.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")` | |
| `static class` | `[Options.Tab](Options.Tab.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Options](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static boolean` | `[closeAllSettings](#closeAllSettings())()` | |
| `static boolean` | `[closeHouseOptionsTab](#closeHouseOptionsTab())()` | Closes House Options Tab |
| `static [Options.HouseDoor](Options.HouseDoor.html "enum in org.tribot.script.sdk")` | `[getHouseDoorState](#getHouseDoorState())()` | |
| `static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk")` | `[getResizableModeType](#getResizableModeType())()` | Gets the resizable game mode type (fixed, resizable classic, resizable modern) |
| `static int` | `[getRunEnergy](#getRunEnergy())()` | Deprecated. |
| `static [Options.ChatboxScrollPosition](Options.ChatboxScrollPosition.html "enum in org.tribot.script.sdk")` | `[getScrollbarRightPosition](#getScrollbarRightPosition())()` | Determines whether the option to set scroll-bars as right-aligned is enabled. |
| `static boolean` | `[isAcceptAidEnabled](#isAcceptAidEnabled())()` | |
| `static boolean` | `[isAcceptTradeDelayEnabled](#isAcceptTradeDelayEnabled())()` | Determine if accept trade delay is enabled |
| `static boolean` | `[isAllSettingsOpen](#isAllSettingsOpen())()` | |
| `static boolean` | `[isAnySoundOn](#isAnySoundOn())()` | Determines if any sounds is on or off |
| `static boolean` | `[isAreaSoundOn](#isAreaSoundOn())()` | Determines if Area sound is on or off. |
| `static boolean` | `[isClickThroughChatboxEnabled](#isClickThroughChatboxEnabled())()` | Determines whether the option to set the chat-box as click-through is enabled. |
| `static boolean` | `[isDataOrbsEnabled](#isDataOrbsEnabled())()` | Determines whether the option to display data-orbs (the UIs on the side of the mini-map) is enabled. |
| `static boolean` | `[isDisableLevelUpInterfaceEnabled](#isDisableLevelUpInterfaceEnabled())()` | Determine if disable level up interface is enabled |
| `static boolean` | `[isEscapeClosingEnabled](#isEscapeClosingEnabled())()` | |
| `static boolean` | `[isFollowerOptionsLowerDownEnabled](#isFollowerOptionsLowerDownEnabled())()` | Determines whether the option to show follower (summoning) options lower down is enabled. |
| `static boolean` | `[isGrandExchangeBuyWarningEnabled](#isGrandExchangeBuyWarningEnabled())()` | Determine if grand exchange buy warning is enabled |
| `static boolean` | `[isGrandExchangeSellWarningEnabled](#isGrandExchangeSellWarningEnabled())()` | Determine if grand exchange sell warning is enabled |
| `static boolean` | `[isHouseOptionsTabOpen](#isHouseOptionsTabOpen())()` | Determine if house options tab is open |
| `static boolean` | `[isHouseTeleportInsideEnabled](#isHouseTeleportInsideEnabled())()` | Determine if house teleport inside is on or off |
| `static boolean` | `[isMouseCameraEnabled](#isMouseCameraEnabled())()` | Determines whether the option to use the middle mouse button to adjust the camera is enabled. |
| `static boolean` | `[isMouseScrollZoomEnabled](#isMouseScrollZoomEnabled())()` | Determines whether the option to allow viewport zooming via mouse wheel scrolling is enabled. |
| `static boolean` | `[isMusicSoundOn](#isMusicSoundOn())()` | Determines if Music is on or off. |
| `static boolean` | `[isMusicUnlockMessageEnabled](#isMusicUnlockMessageEnabled())()` | Determine if music unlock message is on or off |
| `static boolean` | `[isPrayerTooltipEnabled](#isPrayerTooltipEnabled())()` | Determines whether the option to use prayer tool-tips is enabled. |
| `static boolean` | `[isResizableModeEnabled](#isResizableModeEnabled())()` | Determines if the resizable mode setting is enabled. |
| `static boolean` | `[isRoofsEnabled](#isRoofsEnabled())()` | Checks if roofs are currently enabled (roofs are being drawn) |
| `static boolean` | `[isRunEnabled](#isRunEnabled())()` | Determines if the run setting is enabled. |
| `static boolean` | `[isShiftClickDropEnabled](#isShiftClickDropEnabled())()` | Determines if the shift-click drop setting is enabled. |
| `static boolean` | `[isShowActivityAdviserEnabled](#isShowActivityAdviserEnabled())()` | Determine if activity adviser is enabled |
| `static boolean` | `[isSidePanelsEnabled](#isSidePanelsEnabled())()` | Determines whether the option to set side panels on is enabled. |
| `static boolean` | `[isSidePanelsHotkeyOpeningEnabled](#isSidePanelsHotkeyOpeningEnabled())()` | Determines whether the option to use hot-keys to open side panels is enabled. |
| `static boolean` | `[isSoundEffectsOn](#isSoundEffectsOn())()` | Determines if Sound effect is on or off. |
| `static boolean` | `[isSpecialAttackTooltipEnabled](#isSpecialAttackTooltipEnabled())()` | Determines whether the option to use special attack tool-tips is enabled. |
| `static boolean` | `[isStatsPanelXpEnabled](#isStatsPanelXpEnabled())()` | Determines whether the option to set the stats panel XP til next level is enabled. |
| `static boolean` | `[isTransparentChatboxEnabled](#isTransparentChatboxEnabled())()` | Determines whether the option to set the chat-box transparent is enabled. |
| `static boolean` | `[isTransparentSidePanelsEnabled](#isTransparentSidePanelsEnabled())()` | Determines whether the option to set side panels as transparent is enabled. |
| `static boolean` | `[isWorldSwitcherConfirmationEnabled](#isWorldSwitcherConfirmationEnabled())()` | Determine if world switch confirmations are enabled |
| `static boolean` | `[isXpDropsEnabled](#isXpDropsEnabled())()` | Determines whether the option to show XP drops is enabled. |
| `static boolean` | `[isZoomWithScrollEnabled](#isZoomWithScrollEnabled())()` | Determine if zoom with mouse scroll is on or off |
| `static boolean` | `[openHouseOptionsTab](#openHouseOptionsTab())()` | Opens House Options Tab |
| `static boolean` | `[setAcceptAid](#setAcceptAid(boolean))​(boolean acceptAid)` | |
| `static boolean` | `[setClickThroughChatboxEnabled](#setClickThroughChatboxEnabled(boolean))​(boolean enable)` | Sets the option for clicking through the chat-box. |
| `static boolean` | `[setDataOrbsEnabled](#setDataOrbsEnabled(boolean))​(boolean enable)` | Sets the option for showing data-orbs. |
| `static boolean` | `[setFollowerOptionsLowerDownEnabled](#setFollowerOptionsLowerDownEnabled(boolean))​(boolean enable)` | Sets the option controlling whether follower (summoning) options are first/last. |
| `static boolean` | `[setHouseDoorState](#setHouseDoorState(org.tribot.script.sdk.Options.HouseDoor))​([Options.HouseDoor](Options.HouseDoor.html "enum in org.tribot.script.sdk") houseDoor)` | |
| `static boolean` | `[setHouseTeleportInsideEnabled](#setHouseTeleportInsideEnabled(boolean))​(boolean enable)` | Set house teleport inside on or off |
| `static boolean` | `[setMouseCameraEnabled](#setMouseCameraEnabled(boolean))​(boolean enable)` | Sets the option for using the middle mouse button to adjust the camera. |
| `static boolean` | `[setMouseScrollZoomEnabled](#setMouseScrollZoomEnabled(boolean))​(boolean enable)` | Sets the option for allowing viewport zooming using the mouse wheel. |
| `static boolean` | `[setMusicUnlockMessageEnabled](#setMusicUnlockMessageEnabled(boolean))​(boolean enable)` | Turns music unlock message on or off. |
| `static boolean` | `[setPrayerTooltipEnabled](#setPrayerTooltipEnabled(boolean))​(boolean enable)` | Sets the option for prayer tool-tips. |
| `static boolean` | `[setRemoveRoofsEnabled](#setRemoveRoofsEnabled(boolean))​(boolean enable)` | Configures the setting to remove roofs |
| `static boolean` | `[setResizableModeType](#setResizableModeType(org.tribot.script.sdk.Options.ResizableType))​([Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") resizableType)` | Sets the resizable display type |
| `static boolean` | `[setRunEnabled](#setRunEnabled(boolean))​(boolean runEnabled)` | Turns run on or off. |
| `static boolean` | `[setScrollbarPosition](#setScrollbarPosition(org.tribot.script.sdk.Options.ChatboxScrollPosition))​([Options.ChatboxScrollPosition](Options.ChatboxScrollPosition.html "enum in org.tribot.script.sdk") position)` | Sets the option for scroll-bar alignment. |
| `static boolean` | `[setShiftClickDrop](#setShiftClickDrop(boolean))​(boolean enabled)` | Turns the shift-click drop setting on or off. |
| `static boolean` | `[setSidePanelsEnabled](#setSidePanelsEnabled(boolean))​(boolean enable)` | Sets the option for use of side panels. |
| `static boolean` | `[setSidePanelsHotkeyOpeningEnabled](#setSidePanelsHotkeyOpeningEnabled(boolean))​(boolean enable)` | Sets the option for using hot-keys to open side panels. |
| `static boolean` | `[setSpecialAttackTooltipEnabled](#setSpecialAttackTooltipEnabled(boolean))​(boolean enable)` | Sets the option for special attack tool-tips. |
| `static boolean` | `[setStatsPanelXpEnabled](#setStatsPanelXpEnabled(boolean))​(boolean enable)` | Sets the option for showing XP til next level in the stats panel. |
| `static boolean` | `[setTransparentChatboxEnabled](#setTransparentChatboxEnabled(boolean))​(boolean enable)` | Sets the option for chat-box transparency. |
| `static boolean` | `[setTransparentSidePanelsEnabled](#setTransparentSidePanelsEnabled(boolean))​(boolean enable)` | Sets the option for side panel transparency. |
| `static boolean` | `[setXpDropsEnabled](#setXpDropsEnabled(boolean))​(boolean enable)` | Sets the option for showing XP drops. |
| `static boolean` | `[setZoomWithScrollEnabled](#setZoomWithScrollEnabled(boolean))​(boolean enable)` | Turns zoom with mouse scroll on or off. |
| `static boolean` | `[turnAllSoundsOff](#turnAllSoundsOff())()` | Turn all sounds off |
| `static boolean` | `[turnAreaSoundOff](#turnAreaSoundOff())()` | Turn area sound off |
| `static boolean` | `[turnMusicOff](#turnMusicOff())()` | Turn music off |
| `static boolean` | `[turnSoundEffectsOff](#turnSoundEffectsOff())()` | Turn sound effect off |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Options

```
public Options()
```

+ ### Method Detail

- #### isAllSettingsOpen

```
public static boolean isAllSettingsOpen()
```
- #### closeAllSettings

```
public static boolean closeAllSettings()
```
- #### isEscapeClosingEnabled

```
public static boolean isEscapeClosingEnabled()
```
- #### isAcceptAidEnabled

```
public static boolean isAcceptAidEnabled()
```
- #### setAcceptAid

```
public static boolean setAcceptAid​(boolean acceptAid)
```
- #### isShiftClickDropEnabled

```
public static boolean isShiftClickDropEnabled()
```

Determines if the shift-click drop setting is enabled.

Returns:
True if the setting is enabled. False otherwise.
- #### setShiftClickDrop

```
public static boolean setShiftClickDrop​(boolean enabled)
```

Turns the shift-click drop setting on or off.

Parameters:
`enabled` - Whether to turn the setting on (true) or off (false).
Returns:
If the click to toggle the setting was successful.
- #### isResizableModeEnabled

```
public static boolean isResizableModeEnabled()
```

Determines if the resizable mode setting is enabled.

Returns:
True if the setting is enabled. False otherwise.
- #### isRoofsEnabled

```
public static boolean isRoofsEnabled()
```

Checks if roofs are currently enabled (roofs are being drawn)

Returns:
true if roofs are enabled (being drawn), false otherwise
- #### setRemoveRoofsEnabled

```
public static boolean setRemoveRoofsEnabled​(boolean enable)
```

Configures the setting to remove roofs

Parameters:
`enable` - true to disable roofs, false to enable
Returns:
true if the option was successfully set, false otherwise
- #### isRunEnabled

```
public static boolean isRunEnabled()
```

Determines if the run setting is enabled. If it is, the character will run instead of walk.

Returns:
True if run is enabled. False otherwise.
- #### getRunEnergy

```
@Deprecated
public static int getRunEnergy()
```

Deprecated.
Gets the current run energy of the player character.

Returns:
The current run energy (0-100)
See Also:
[`moved to a more intuitive location`](MyPlayer.html#getRunEnergy())
- #### setRunEnabled

```
public static boolean setRunEnabled​(boolean runEnabled)
```

Turns run on or off.

Parameters:
`runEnabled` - Whether to turn run on (true) or off (false).
Returns:
If the click to toggle the setting was successful.
- #### getResizableModeType

```
public static [Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") getResizableModeType()
```

Gets the resizable game mode type (fixed, resizable classic, resizable modern)

Returns:
the resizable game mode type
- #### setResizableModeType

```
public static boolean setResizableModeType​([Options.ResizableType](Options.ResizableType.html "enum in org.tribot.script.sdk") resizableType)
```

Sets the resizable display type

Parameters:
`resizableType` - the resizable type
Returns:
true if the resizable type was set successfully, false otherwise
- #### isMusicSoundOn

```
public static boolean isMusicSoundOn()
```

Determines if Music is on or off.

Returns:
True if the Music is enabled. False otherwise.
- #### isSoundEffectsOn

```
public static boolean isSoundEffectsOn()
```

Determines if Sound effect is on or off.

Returns:
True if the Music is enabled. False otherwise.
- #### isAreaSoundOn

```
public static boolean isAreaSoundOn()
```

Determines if Area sound is on or off.

Returns:
True if the Music is enabled. False otherwise.
- #### turnMusicOff

```
public static boolean turnMusicOff()
```

Turn music off

Returns:
True if the music is Off. False otherwise.
- #### turnSoundEffectsOff

```
public static boolean turnSoundEffectsOff()
```

Turn sound effect off

Returns:
True if the sound effect is Off. False otherwise.
- #### turnAreaSoundOff

```
public static boolean turnAreaSoundOff()
```

Turn area sound off

Returns:
True if the area sound is Off. False otherwise.
- #### isDataOrbsEnabled

```
public static boolean isDataOrbsEnabled()
```

Determines whether the option to display data-orbs (the UIs on the side of the mini-map) is enabled.

Returns:
True if enabled; false otherwise.
- #### isMouseCameraEnabled

```
public static boolean isMouseCameraEnabled()
```

Determines whether the option to use the middle mouse button to adjust the camera is enabled.

Returns:
True if enabled; false otherwise.
- #### isTransparentChatboxEnabled

```
public static boolean isTransparentChatboxEnabled()
```

Determines whether the option to set the chat-box transparent is enabled.

Returns:
True if enabled; false otherwise.
- #### isClickThroughChatboxEnabled

```
public static boolean isClickThroughChatboxEnabled()
```

Determines whether the option to set the chat-box as click-through is enabled.

Returns:
True if enabled; false otherwise.
- #### isSidePanelsEnabled

```
public static boolean isSidePanelsEnabled()
```

Determines whether the option to set side panels on is enabled.

Returns:
True if enabled; false otherwise.
- #### isSidePanelsHotkeyOpeningEnabled

```
public static boolean isSidePanelsHotkeyOpeningEnabled()
```

Determines whether the option to use hot-keys to open side panels is enabled.

Returns:
True if enabled; false otherwise.
- #### isTransparentSidePanelsEnabled

```
public static boolean isTransparentSidePanelsEnabled()
```

Determines whether the option to set side panels as transparent is enabled.

Returns:
True if enabled; false otherwise.
- #### getScrollbarRightPosition

```
public static [Options.ChatboxScrollPosition](Options.ChatboxScrollPosition.html "enum in org.tribot.script.sdk") getScrollbarRightPosition()
```

Determines whether the option to set scroll-bars as right-aligned is enabled.

Returns:
True if enabled (scroll-bars on the right); false otherwise (scroll-bars on the left).
- #### isStatsPanelXpEnabled

```
public static boolean isStatsPanelXpEnabled()
```

Determines whether the option to set the stats panel XP til next level is enabled.

Returns:
True if enabled; false otherwise.
- #### isPrayerTooltipEnabled

```
public static boolean isPrayerTooltipEnabled()
```

Determines whether the option to use prayer tool-tips is enabled.

Returns:
True if enabled; false otherwise.
- #### isSpecialAttackTooltipEnabled

```
public static boolean isSpecialAttackTooltipEnabled()
```

Determines whether the option to use special attack tool-tips is enabled.

Returns:
True if enabled; false otherwise.
- #### isXpDropsEnabled

```
public static boolean isXpDropsEnabled()
```

Determines whether the option to show XP drops is enabled.

Returns:
True if enabled; false otherwise.
- #### isMouseScrollZoomEnabled

```
public static boolean isMouseScrollZoomEnabled()
```

Determines whether the option to allow viewport zooming via mouse wheel scrolling is enabled.

Returns:
True if enabled; false otherwise.
- #### isFollowerOptionsLowerDownEnabled

```
public static boolean isFollowerOptionsLowerDownEnabled()
```

Determines whether the option to show follower (summoning) options lower down is enabled.

Returns:
True if enabled; false otherwise.
- #### setDataOrbsEnabled

```
public static boolean setDataOrbsEnabled​(boolean enable)
```

Sets the option for showing data-orbs.

Parameters:
`enable` - True to enable use data-orbs; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setMouseCameraEnabled

```
public static boolean setMouseCameraEnabled​(boolean enable)
```

Sets the option for using the middle mouse button to adjust the camera.

Parameters:
`enable` - True to enable use the middle mouse button to adjust the camera; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setTransparentChatboxEnabled

```
public static boolean setTransparentChatboxEnabled​(boolean enable)
```

Sets the option for chat-box transparency.

Parameters:
`enable` - True to enable transparency; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setClickThroughChatboxEnabled

```
public static boolean setClickThroughChatboxEnabled​(boolean enable)
```

Sets the option for clicking through the chat-box.

Parameters:
`enable` - True to enable click-through; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setSidePanelsEnabled

```
public static boolean setSidePanelsEnabled​(boolean enable)
```

Sets the option for use of side panels.

Parameters:
`enable` - True to enable side panels; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setSidePanelsHotkeyOpeningEnabled

```
public static boolean setSidePanelsHotkeyOpeningEnabled​(boolean enable)
```

Sets the option for using hot-keys to open side panels.

Parameters:
`enable` - True to enable hot-key opening; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setTransparentSidePanelsEnabled

```
public static boolean setTransparentSidePanelsEnabled​(boolean enable)
```

Sets the option for side panel transparency.

Parameters:
`enable` - True to enable transparency; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setScrollbarPosition

```
public static boolean setScrollbarPosition​([Options.ChatboxScrollPosition](Options.ChatboxScrollPosition.html "enum in org.tribot.script.sdk") position)
```

Sets the option for scroll-bar alignment.

Parameters:
`position` - the scroll position
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setStatsPanelXpEnabled

```
public static boolean setStatsPanelXpEnabled​(boolean enable)
```

Sets the option for showing XP til next level in the stats panel.

Parameters:
`enable` - True to enable showing XP til next level; false to disable it.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setPrayerTooltipEnabled

```
public static boolean setPrayerTooltipEnabled​(boolean enable)
```

Sets the option for prayer tool-tips.

Parameters:
`enable` - True to enable use of prayer tool-tips; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setSpecialAttackTooltipEnabled

```
public static boolean setSpecialAttackTooltipEnabled​(boolean enable)
```

Sets the option for special attack tool-tips.

Parameters:
`enable` - True to enable use of special attack tool-tips; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setXpDropsEnabled

```
public static boolean setXpDropsEnabled​(boolean enable)
```

Sets the option for showing XP drops.

Parameters:
`enable` - True to enable the displaying of XP drops; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setMouseScrollZoomEnabled

```
public static boolean setMouseScrollZoomEnabled​(boolean enable)
```

Sets the option for allowing viewport zooming using the mouse wheel.

Parameters:
`enable` - True to enable the mouse wheel to zoom in/out; false to disable.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### setFollowerOptionsLowerDownEnabled

```
public static boolean setFollowerOptionsLowerDownEnabled​(boolean enable)
```

Sets the option controlling whether follower (summoning) options are first/last.

Parameters:
`enable` - True to show follower options first; false to show them last.
Returns:
True if the option was successfully set; false if it was not for some unknown reason.
- #### isAnySoundOn

```
public static boolean isAnySoundOn()
```

Determines if any sounds is on or off

Returns:
True if any sound is on. False otherwise
- #### turnAllSoundsOff

```
public static boolean turnAllSoundsOff()
```

Turn all sounds off

Returns:
True if all sound are Off. False otherwise.
- #### isZoomWithScrollEnabled

```
public static boolean isZoomWithScrollEnabled()
```

Determine if zoom with mouse scroll is on or off

Returns:
True if zoom with mouse scroll is on. False otherwise.
- #### setZoomWithScrollEnabled

```
public static boolean setZoomWithScrollEnabled​(boolean enable)
```

Turns zoom with mouse scroll on or off.

Parameters:
`enable` - Whether to turn zoom with mouse scroll on (true) or off (false).
Returns:
If the click to toggle the setting was successful.
- #### isMusicUnlockMessageEnabled

```
public static boolean isMusicUnlockMessageEnabled()
```

Determine if music unlock message is on or off

Returns:
True if music unlock message is on. False otherwise.
- #### setMusicUnlockMessageEnabled

```
public static boolean setMusicUnlockMessageEnabled​(boolean enable)
```

Turns music unlock message on or off.

Parameters:
`enable` - Whether to turn music unlock message on (true) or off (false).
Returns:
If the click to toggle the setting was successful.
- #### isWorldSwitcherConfirmationEnabled

```
public static boolean isWorldSwitcherConfirmationEnabled()
```

Determine if world switch confirmations are enabled

Returns:
True if world switcher confirmations is on. False otherwise.
- #### isHouseOptionsTabOpen

```
public static boolean isHouseOptionsTabOpen()
```

Determine if house options tab is open

Returns:
True if house options tab is open. False otherwise.
- #### openHouseOptionsTab

```
public static boolean openHouseOptionsTab()
```

Opens House Options Tab

Returns:
True if House Options Tab is opened successfully. False otherwise.
- #### closeHouseOptionsTab

```
public static boolean closeHouseOptionsTab()
```

Closes House Options Tab

Returns:
True if House Options Tab is closed successfully. False otherwise.
- #### isHouseTeleportInsideEnabled

```
public static boolean isHouseTeleportInsideEnabled()
```

Determine if house teleport inside is on or off

Returns:
True if house teleport inside is on. False otherwise.
- #### setHouseTeleportInsideEnabled

```
public static boolean setHouseTeleportInsideEnabled​(boolean enable)
```

Set house teleport inside on or off

Parameters:
`enable` - Whether to turn house teleport inside on (true) or off (false).
Returns:
If the click to toggle the setting was successful.
- #### isAcceptTradeDelayEnabled

```
public static boolean isAcceptTradeDelayEnabled()
```

Determine if accept trade delay is enabled

Returns:
True if accept trade delay is enabled. False otherwise.
- #### isShowActivityAdviserEnabled

```
public static boolean isShowActivityAdviserEnabled()
```

Determine if activity adviser is enabled

Returns:
True if activity adviser is enabled. False otherwise.
- #### isDisableLevelUpInterfaceEnabled

```
public static boolean isDisableLevelUpInterfaceEnabled()
```

Determine if disable level up interface is enabled

Returns:
True if disable level up interface is enabled. False otherwise.
- #### isGrandExchangeBuyWarningEnabled

```
public static boolean isGrandExchangeBuyWarningEnabled()
```

Determine if grand exchange buy warning is enabled

Returns:
True if grand exchange buy warning is enabled. False otherwise.
- #### isGrandExchangeSellWarningEnabled

```
public static boolean isGrandExchangeSellWarningEnabled()
```

Determine if grand exchange sell warning is enabled

Returns:
True if grand exchange sell warning is enabled. False otherwise.
- #### getHouseDoorState

```
public static [Options.HouseDoor](Options.HouseDoor.html "enum in org.tribot.script.sdk") getHouseDoorState()
```
- #### setHouseDoorState

```
public static boolean setHouseDoorState​([Options.HouseDoor](Options.HouseDoor.html "enum in org.tribot.script.sdk") houseDoor)
```