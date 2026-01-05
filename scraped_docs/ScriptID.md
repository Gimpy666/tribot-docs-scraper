# ScriptID (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ScriptID.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.ScriptID

* ---

```
public final class ScriptID
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[ACCOUNT\_SUMMARY\_SECTION\_FORMAT](#ACCOUNT_SUMMARY_SECTION_FORMAT)` | |
| `static int` | `[ACCOUNT\_SUMMARY\_TEXT\_FORMAT](#ACCOUNT_SUMMARY_TEXT_FORMAT)` | |
| `static int` | `[ADD\_OVERLAYTIMER\_LOC](#ADD_OVERLAYTIMER_LOC)` | Called to add a loc overlay timer

loc coord
loc id
loc type
overlay type
overlay ticks
|
| `static int` | `[BANK\_DEPOSITBOX\_INIT](#BANK_DEPOSITBOX_INIT)` | |
| `static int` | `[BANKMAIN\_BUILD](#BANKMAIN_BUILD)` | Main layout script for the bank

int (WidgetID) \* 17, various widgets making up the bank interface
|
| `static int` | `[BANKMAIN\_DRAGSCROLL](#BANKMAIN_DRAGSCROLL)` | |
| `static int` | `[BANKMAIN\_FINISHBUILDING](#BANKMAIN_FINISHBUILDING)` | |
| `static int` | `[BANKMAIN\_INIT](#BANKMAIN_INIT)` | |
| `static int` | `[BANKMAIN\_SEARCH\_REFRESH](#BANKMAIN_SEARCH_REFRESH)` | Called in an onTimer, determines whether to layout the bank during a search

int (WidgetID) \* 16, various widgets making up the bank interface
|
| `static int` | `[BANKMAIN\_SEARCH\_TOGGLE](#BANKMAIN_SEARCH_TOGGLE)` | Toggles the bank search

int 1 (must be 1 or script immediately returns)

Also takes 17 widget IDs corresponding to various bank widgets. |
| `static int` | `[BANKMAIN\_SEARCHING](#BANKMAIN_SEARCHING)` | |
| `static int` | `[BANKMAIN\_SIZE\_CHECK](#BANKMAIN_SIZE_CHECK)` | |
| `static int` | `[BUILD\_CHATBOX](#BUILD_CHATBOX)` | Rebuilds the chatbox |
| `static int` | `[CAMERA\_DO\_ZOOM](#CAMERA_DO_ZOOM)` | Handles zoom input

Updates the VarClientInts (73, 74) to this same value

int Reset zoom position for fixed viewport mode
int Reset zoom position for resizable viewport mode
|
| `static int` | `[CAMERA\_SET\_ZOOM\_LIMITS](#CAMERA_SET_ZOOM_LIMITS)` | |
| `static int` | `[CHAT\_PROMPT\_INIT](#CHAT_PROMPT_INIT)` | Builds the chatbox input widget |
| `static int` | `[CHAT\_SEND](#CHAT_SEND)` | Sends a chat message

String Message to send
int modes
int (clan type)
int (boolean) use target
int set target
|
| `static int` | `[CHAT\_TEXT\_INPUT\_REBUILD](#CHAT_TEXT_INPUT_REBUILD)` | Rebuilds the text input widget inside the chat interface

String Message Prefix. |
| `static int` | `[CHATBOX\_KEYINPUT\_MATCHED](#CHATBOX_KEYINPUT_MATCHED)` | |
| `static int` | `[CLAN\_SIDEPANEL\_DRAW](#CLAN_SIDEPANEL_DRAW)` | Builds the widget that holds all of the players inside a clan chat |
| `static int` | `[COLLECTION\_DRAW\_LIST](#COLLECTION_DRAW_LIST)` | |
| `static int` | `[COMBAT\_INTERFACE\_SETUP](#COMBAT_INTERFACE_SETUP)` | Called to build the combat interface |
| `static int` | `[DIARY\_UPDATE\_LINECOUNT](#DIARY_UPDATE_LINECOUNT)` | Updates the Diary interface's scrollbar

int (boolean) Reset scroll position
int Number of lines
|
| `static int` | `[DOM\_LOOT\_CLAIM](#DOM_LOOT_CLAIM)` | |
| `static int` | `[EQUIPMENT\_SET\_STAT\_BONUS\_SETUP](#EQUIPMENT_SET_STAT_BONUS_SETUP)` | |
| `static int` | `[FAIRYRINGS\_SORT\_UPDATE](#FAIRYRINGS_SORT_UPDATE)` | |
| `static int` | `[FRIENDS\_CHAT\_CHANNEL\_REBUILD](#FRIENDS_CHAT_CHANNEL_REBUILD)` | Builds the widget that holds all of the players inside a friends chat |
| `static int` | `[FRIENDS\_CHAT\_SEND\_KICK](#FRIENDS_CHAT_SEND_KICK)` | Attempts to kick the specified player from the friends chat

String Players in-game name
|
| `static int` | `[FRIENDS\_UPDATE](#FRIENDS_UPDATE)` | Called when the friends list is updated

int (WidgetID) Friends list "full container"
int (WidgetID) Friends list sort by name button
int (WidgetID) Friends list sort by last world change button
int (WidgetID) Friends list sort by world button
int (WidgetID) Friends list legacy sort button
int (WidgetID) Friends list names container
int (WidgetID) Friends list scroll bar
int (WidgetID) Friends list "loading please wait" text
int (WidgetID) Friends list player previous name holder
|
| `static int` | `[GE\_ITEM\_SEARCH](#GE_ITEM_SEARCH)` | Builds the grand exchange item search widget |
| `static int` | `[GE\_OFFERS\_SETUP\_BUILD](#GE_OFFERS_SETUP_BUILD)` | Builds the widget for making an offer in Grand Exchange |
| `static int` | `[GROUP\_IRONMAN\_STORAGE\_BUILD](#GROUP_IRONMAN_STORAGE_BUILD)` | |
| `static int` | `[HP\_HUD\_UPDATE](#HP_HUD_UPDATE)` | |
| `static int` | `[IGNORE\_UPDATE](#IGNORE_UPDATE)` | Called when the ignore list is updated

int (WidgetID) Ignore list "full container"
int (WidgetID) Ignore list sort by name button
int (WidgetID) Ignore list legacy sort button
int (WidgetID) Ignore list names container
int (WidgetID) Ignore list scroll bar
int (WidgetID) Ignore list "loading please wait" text
int (WidgetID) Ignore list player previous name holder
|
| `static int` | `[INTERFACE\_INV\_DRAW\_SLOT\_BIG](#INTERFACE_INV_DRAW_SLOT_BIG)` | |
| `static int` | `[INVENTORY\_DRAWITEM](#INVENTORY_DRAWITEM)` | |
| `static int` | `[LOOTTRACKER\_ADD\_LOOT](#LOOTTRACKER_ADD_LOOT)` | |
| `static int` | `[MAGIC\_SPELLBOOK\_INITIALISESPELLS](#MAGIC_SPELLBOOK_INITIALISESPELLS)` | |
| `static int` | `[MESSAGE\_LAYER\_CLOSE](#MESSAGE_LAYER_CLOSE)` | Closes the chatbox input

int (boolean) Clear the current text
int (boolean) Restore to chat view
int (boolean) Submit close to server
|
| `static int` | `[MESSAGE\_LAYER\_OPEN](#MESSAGE_LAYER_OPEN)` | Readies the chatbox panel for things like the chatbox input
Inverse of MESSAGE\_LAYER\_CLOSE

int (InputType) message layer type we are changing to
|
| `static int` | `[MOTHERLODE\_HUD\_UPDATE](#MOTHERLODE_HUD_UPDATE)` | |
| `static int` | `[NOTIFICATION\_DELAY](#NOTIFICATION_DELAY)` | Draws the active notification in full size for a specified number of client ticks. |
| `static int` | `[NOTIFICATION\_START](#NOTIFICATION_START)` | Draws the active notification in increasing sizes (increasing horizontally first, then vertically) to show a
starting animation. |
| `static int` | `[NULL](#NULL)` | Deprecated. |
| `static int` | `[OPEN\_PRIVATE\_MESSAGE\_INTERFACE](#OPEN_PRIVATE_MESSAGE_INTERFACE)` | Opens the Private Message chat interface

Jagex refers to this script as `meslayer_mode6`

String Player to send private message to
|
| `static int` | `[ORBS\_UPDATE\_RUNENERGY](#ORBS_UPDATE_RUNENERGY)` | |
| `static int` | `[POPUP\_OVERLAY\_YESNO\_INIT](#POPUP_OVERLAY_YESNO_INIT)` | |
| `static int` | `[POTIONSTORE\_BUILD](#POTIONSTORE_BUILD)` | |
| `static int` | `[POTIONSTORE\_DOSE\_CHANGE](#POTIONSTORE_DOSE_CHANGE)` | |
| `static int` | `[POTIONSTORE\_DOSES](#POTIONSTORE_DOSES)` | |
| `static int` | `[POTIONSTORE\_WITHDRAW\_DOSES](#POTIONSTORE_WITHDRAW_DOSES)` | |
| `static int` | `[PRAYER\_REDRAW](#PRAYER_REDRAW)` | |
| `static int` | `[PRAYER\_UPDATEBUTTON](#PRAYER_UPDATEBUTTON)` | |
| `static int` | `[PRIVMSG](#PRIVMSG)` | Send a private message. |
| `static int` | `[PVP\_WIDGET\_BUILDER](#PVP_WIDGET_BUILDER)` | Called to update the PVP widget (wilderness level/protection) |
| `static int` | `[QUEST\_STATUS\_GET](#QUEST_STATUS_GET)` | Queries the completion state of a quest by its struct id

int (struct) The id of the quest

Returns

int (QuestState) the normalized state of the quest
|
| `static int` | `[QUEST\_UPDATE\_LINECOUNT](#QUEST_UPDATE_LINECOUNT)` | Updates the Quest interface's scrollbar

int (boolean) Reset scroll position
int Number of lines
|
| `static int` | `[QUESTLIST\_INIT](#QUESTLIST_INIT)` | On load listener for building the quest list interface |
| `static int` | `[QUICKPRAYER\_INIT](#QUICKPRAYER_INIT)` | |
| `static int` | `[RAIDS\_STORAGE\_PRIVATE\_ITEMS](#RAIDS_STORAGE_PRIVATE_ITEMS)` | |
| `static int` | `[SEED\_VAULT\_BUILD](#SEED_VAULT_BUILD)` | |
| `static int` | `[SETTINGS\_SLIDER\_CHOOSE\_ONOP](#SETTINGS_SLIDER_CHOOSE_ONOP)` | Chooses the click handler for a [`ParamID.SETTING_SLIDER_CUSTOM_ONOP`](ParamID.html#SETTING_SLIDER_CUSTOM_ONOP) = 1 settings slider

The active widget is set to the track created by [`ParamID.SETTING_FOREGROUND_CLICKZONE`](ParamID.html#SETTING_FOREGROUND_CLICKZONE)

int [`ParamID.SETTING_ID`](ParamID.html#SETTING_ID)
int (WidgetID) Slider handle ID
int (widget index) Slider handle index
int track width
int y offset
int x offset
int (WidgetID) drag parent
|
| `static int` | `[SETTINGS\_ZOOM\_SLIDER\_ONDRAG](#SETTINGS_ZOOM_SLIDER_ONDRAG)` | Drag callback for the camera zoom slider in the settings. |
| `static int` | `[SPLITPM\_CHANGED](#SPLITPM_CHANGED)` | Rebuilds the chatbox and the pmbox |
| `static int` | `[TOB\_HUD\_SOTETSEG\_FADE](#TOB_HUD_SOTETSEG_FADE)` | Transitions the tob hud into the white flash that happens when sotetseg teleports the players to the maze. |
| `static int` | `[TOPLEVEL\_REDRAW](#TOPLEVEL_REDRAW)` | Called to build the toplevel interface |
| `static int` | `[TOPLEVEL\_RESIZE\_CUSTOMISE](#TOPLEVEL_RESIZE_CUSTOMISE)` | |
| `static int` | `[TRADE\_MAIN\_INIT](#TRADE_MAIN_INIT)` | Initializes the trade interface |
| `static int` | `[UPDATE\_SCROLLBAR](#UPDATE_SCROLLBAR)` | Updates the scrollbar handle and container to the new height of the content container

int (WidgetID) Scrollbar's widget ID
int (WidgetID) Container widget ID
int how far down to scroll
|
| `static int` | `[WATSON\_STASH\_UNIT\_CHECK](#WATSON_STASH_UNIT_CHECK)` | Checks the state of the given stash unit. |
| `static int` | `[WIKI\_ICON\_UPDATE](#WIKI_ICON_UPDATE)` | Position and size the wiki button, as well as hide/unhide it |
| `static int` | `[WORLDMAP\_LOADMAP](#WORLDMAP_LOADMAP)` | |
| `static int` | `[XPDROP\_DISABLED](#XPDROP_DISABLED)` | Creates a disabled experience drop

int (Skill ordinal) Sets what icon to use
int Amount of exp to drop
|
| `static int` | `[XPDROPS\_SETDROPSIZE](#XPDROPS_SETDROPSIZE)` | Called to set position of an xpdrop text and sprite(s)

XP drop parent component
|
| `static int` | `[ZOOM\_SLIDER\_ONDRAG](#ZOOM_SLIDER_ONDRAG)` | Drag callback for the camera zoom slider in the options side panel. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[ScriptID](#%3Cinit%3E())()` | |

+ ### Method Summary

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### UPDATE\_SCROLLBAR

```
@ScriptArguments(integer=3)
public static final int UPDATE_SCROLLBAR
```

Updates the scrollbar handle and container to the new height of the content container

* int (WidgetID) Scrollbar's widget ID
* int (WidgetID) Container widget ID
* int how far down to scroll

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.UPDATE_SCROLLBAR)
- #### CHAT\_SEND

```
@ScriptArguments(integer=4,
string=1)
public static final int CHAT_SEND
```

Sends a chat message

* String Message to send
* int modes
* int (clan type)
* int (boolean) use target
* int set target

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CHAT_SEND)
- #### SPLITPM\_CHANGED

```
@ScriptArguments
public static final int SPLITPM_CHANGED
```

Rebuilds the chatbox and the pmbox

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.SPLITPM_CHANGED)
- #### BUILD\_CHATBOX

```
@ScriptArguments
public static final int BUILD_CHATBOX
```

Rebuilds the chatbox

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BUILD_CHATBOX)
- #### OPEN\_PRIVATE\_MESSAGE\_INTERFACE

```
@ScriptArguments(string=1)
public static final int OPEN_PRIVATE_MESSAGE_INTERFACE
```

Opens the Private Message chat interface

Jagex refers to this script as `meslayer_mode6`

* String Player to send private message to

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.OPEN_PRIVATE_MESSAGE_INTERFACE)
- #### CHAT\_TEXT\_INPUT\_REBUILD

```
@ScriptArguments(string=1)
public static final int CHAT_TEXT_INPUT_REBUILD
```

Rebuilds the text input widget inside the chat interface

* String Message Prefix. Only used inside the GE search interfaces

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CHAT_TEXT_INPUT_REBUILD)
- #### MESSAGE\_LAYER\_CLOSE

```
@ScriptArguments(integer=3)
public static final int MESSAGE_LAYER_CLOSE
```

Closes the chatbox input

* int (boolean) Clear the current text
* int (boolean) Restore to chat view
* int (boolean) Submit close to server

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.MESSAGE_LAYER_CLOSE)
- #### MESSAGE\_LAYER\_OPEN

```
@ScriptArguments(integer=1)
public static final int MESSAGE_LAYER_OPEN
```

Readies the chatbox panel for things like the chatbox input
Inverse of MESSAGE\_LAYER\_CLOSE

* int (InputType) message layer type we are changing to

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.MESSAGE_LAYER_OPEN)
- #### CHAT\_PROMPT\_INIT

```
@ScriptArguments
public static final int CHAT_PROMPT_INIT
```

Builds the chatbox input widget

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CHAT_PROMPT_INIT)
- #### WATSON\_STASH\_UNIT\_CHECK

```
@ScriptArguments(integer=4)
public static final int WATSON_STASH_UNIT_CHECK
```

Checks the state of the given stash unit.

* int (loc) The stash unit object id
* int Bitpacked stash unit states
* int Bitpacked stash unit states 2
* int Bitpacked stash unit states 3

Returns a pair of booleans indicating if the stash unit is built and if it is filled

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.WATSON_STASH_UNIT_CHECK)
- #### QUEST\_STATUS\_GET

```
@ScriptArguments(integer=1)
public static final int QUEST_STATUS_GET
```

Queries the completion state of a quest by its struct id

* int (struct) The id of the quest
Returns

* int (QuestState) the normalized state of the quest

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.QUEST_STATUS_GET)
- #### QUEST\_UPDATE\_LINECOUNT

```
@ScriptArguments(integer=2)
public static final int QUEST_UPDATE_LINECOUNT
```

Updates the Quest interface's scrollbar

* int (boolean) Reset scroll position
* int Number of lines

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.QUEST_UPDATE_LINECOUNT)
- #### DIARY\_UPDATE\_LINECOUNT

```
@ScriptArguments(integer=2)
public static final int DIARY_UPDATE_LINECOUNT
```

Updates the Diary interface's scrollbar

* int (boolean) Reset scroll position
* int Number of lines

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.DIARY_UPDATE_LINECOUNT)
- #### CAMERA\_DO\_ZOOM

```
@ScriptArguments(integer=2)
public static final int CAMERA_DO_ZOOM
```

Handles zoom input

Updates the VarClientInts (73, 74) to this same value

* int Reset zoom position for fixed viewport mode
* int Reset zoom position for resizable viewport mode

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CAMERA_DO_ZOOM)
- #### NULL

```
@ScriptArguments
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final int NULL
```

Deprecated.
Does nothing

This is used to eat events when you want a menu action attached to it
because you need an op listener attached to it for it to work

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.NULL)
- #### PRIVMSG

```
@ScriptArguments(string=2)
public static final int PRIVMSG
```

Send a private message.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.PRIVMSG)
- #### XPDROP\_DISABLED

```
@ScriptArguments(integer=2)
public static final int XPDROP_DISABLED
```

Creates a disabled experience drop

* int (Skill ordinal) Sets what icon to use
* int Amount of exp to drop

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.XPDROP_DISABLED)
- #### FRIENDS\_CHAT\_SEND\_KICK

```
@ScriptArguments(string=1)
public static final int FRIENDS_CHAT_SEND_KICK
```

Attempts to kick the specified player from the friends chat

* String Players in-game name

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.FRIENDS_CHAT_SEND_KICK)
- #### FRIENDS\_CHAT\_CHANNEL\_REBUILD

```
@ScriptArguments(integer=15)
public static final int FRIENDS_CHAT_CHANNEL_REBUILD
```

Builds the widget that holds all of the players inside a friends chat

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.FRIENDS_CHAT_CHANNEL_REBUILD)
- #### CLAN\_SIDEPANEL\_DRAW

```
@ScriptArguments(integer=7)
public static final int CLAN_SIDEPANEL_DRAW
```

Builds the widget that holds all of the players inside a clan chat

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CLAN_SIDEPANEL_DRAW)
- #### GE\_OFFERS\_SETUP\_BUILD

```
@ScriptArguments(integer=17)
public static final int GE_OFFERS_SETUP_BUILD
```

Builds the widget for making an offer in Grand Exchange

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.GE_OFFERS_SETUP_BUILD)
- #### GE\_ITEM\_SEARCH

```
@ScriptArguments(integer=3)
public static final int GE_ITEM_SEARCH
```

Builds the grand exchange item search widget

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.GE_ITEM_SEARCH)
- #### QUESTLIST\_INIT

```
@ScriptArguments(integer=8)
public static final int QUESTLIST_INIT
```

On load listener for building the quest list interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.QUESTLIST_INIT)
- #### FRIENDS\_UPDATE

```
@ScriptArguments(integer=9)
public static final int FRIENDS_UPDATE
```

Called when the friends list is updated

* int (WidgetID) Friends list "full container"
* int (WidgetID) Friends list sort by name button
* int (WidgetID) Friends list sort by last world change button
* int (WidgetID) Friends list sort by world button
* int (WidgetID) Friends list legacy sort button
* int (WidgetID) Friends list names container
* int (WidgetID) Friends list scroll bar
* int (WidgetID) Friends list "loading please wait" text
* int (WidgetID) Friends list player previous name holder

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.FRIENDS_UPDATE)
- #### IGNORE\_UPDATE

```
@ScriptArguments(integer=7)
public static final int IGNORE_UPDATE
```

Called when the ignore list is updated

* int (WidgetID) Ignore list "full container"
* int (WidgetID) Ignore list sort by name button
* int (WidgetID) Ignore list legacy sort button
* int (WidgetID) Ignore list names container
* int (WidgetID) Ignore list scroll bar
* int (WidgetID) Ignore list "loading please wait" text
* int (WidgetID) Ignore list player previous name holder

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.IGNORE_UPDATE)
- #### BANKMAIN\_SEARCH\_REFRESH

```
@ScriptArguments(integer=17)
public static final int BANKMAIN_SEARCH_REFRESH
```

Called in an onTimer, determines whether to layout the bank during a search

* int (WidgetID) \* 16, various widgets making up the bank interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_SEARCH_REFRESH)
- #### BANKMAIN\_DRAGSCROLL

```
@ScriptArguments(integer=6)
public static final int BANKMAIN_DRAGSCROLL
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_DRAGSCROLL)
- #### PVP\_WIDGET\_BUILDER

```
@ScriptArguments(integer=1)
public static final int PVP_WIDGET_BUILDER
```

Called to update the PVP widget (wilderness level/protection)

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.PVP_WIDGET_BUILDER)
- #### COMBAT\_INTERFACE\_SETUP

```
@ScriptArguments(integer=1)
public static final int COMBAT_INTERFACE_SETUP
```

Called to build the combat interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.COMBAT_INTERFACE_SETUP)
- #### TOPLEVEL\_REDRAW

```
@ScriptArguments(integer=2)
public static final int TOPLEVEL_REDRAW
```

Called to build the toplevel interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.TOPLEVEL_REDRAW)
- #### TOPLEVEL\_RESIZE\_CUSTOMISE

```
@ScriptArguments(integer=2)
public static final int TOPLEVEL_RESIZE_CUSTOMISE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.TOPLEVEL_RESIZE_CUSTOMISE)
- #### XPDROPS\_SETDROPSIZE

```
@ScriptArguments(integer=4,
string=1)
public static final int XPDROPS_SETDROPSIZE
```

Called to set position of an xpdrop text and sprite(s)

* XP drop parent component

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.XPDROPS_SETDROPSIZE)
- #### BANKMAIN\_INIT

```
@ScriptArguments(integer=34)
public static final int BANKMAIN_INIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_INIT)
- #### BANKMAIN\_BUILD

```
@ScriptArguments(integer=17)
public static final int BANKMAIN_BUILD
```

Main layout script for the bank

* int (WidgetID) \* 17, various widgets making up the bank interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_BUILD)
- #### BANKMAIN\_FINISHBUILDING

```
@ScriptArguments(integer=19)
public static final int BANKMAIN_FINISHBUILDING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_FINISHBUILDING)
- #### BANKMAIN\_SEARCHING

```
@ScriptArguments
public static final int BANKMAIN_SEARCHING
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_SEARCHING)
- #### BANKMAIN\_SEARCH\_TOGGLE

```
@ScriptArguments(integer=18)
public static final int BANKMAIN_SEARCH_TOGGLE
```

Toggles the bank search

* int 1 (must be 1 or script immediately returns)

Also takes 17 widget IDs corresponding to various bank widgets.
These can be retrieved from the onInvTransmitListener of BANK\_ITEM\_CONTAINER. Note that this array also
contains the script ID for the bank layout script in the first index

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_SEARCH_TOGGLE)
- #### BANKMAIN\_SIZE\_CHECK

```
@ScriptArguments(integer=6)
public static final int BANKMAIN_SIZE_CHECK
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANKMAIN_SIZE_CHECK)
- #### SETTINGS\_SLIDER\_CHOOSE\_ONOP

```
@ScriptArguments(integer=11,
string=1)
public static final int SETTINGS_SLIDER_CHOOSE_ONOP
```

Chooses the click handler for a [`ParamID.SETTING_SLIDER_CUSTOM_ONOP`](ParamID.html#SETTING_SLIDER_CUSTOM_ONOP) = 1 settings slider

The active widget is set to the track created by [`ParamID.SETTING_FOREGROUND_CLICKZONE`](ParamID.html#SETTING_FOREGROUND_CLICKZONE)

* int [`ParamID.SETTING_ID`](ParamID.html#SETTING_ID)
* int (WidgetID) Slider handle ID
* int (widget index) Slider handle index
* int track width
* int y offset
* int x offset
* int (WidgetID) drag parent

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.SETTINGS_SLIDER_CHOOSE_ONOP)
- #### WIKI\_ICON\_UPDATE

```
@ScriptArguments(integer=4)
public static final int WIKI_ICON_UPDATE
```

Position and size the wiki button, as well as hide/unhide it

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.WIKI_ICON_UPDATE)
- #### ZOOM\_SLIDER\_ONDRAG

```
@ScriptArguments(integer=3)
public static final int ZOOM_SLIDER_ONDRAG
```

Drag callback for the camera zoom slider in the options side panel.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.ZOOM_SLIDER_ONDRAG)
- #### SETTINGS\_ZOOM\_SLIDER\_ONDRAG

```
@ScriptArguments(integer=6)
public static final int SETTINGS_ZOOM_SLIDER_ONDRAG
```

Drag callback for the camera zoom slider in the settings.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.SETTINGS_ZOOM_SLIDER_ONDRAG)
- #### COLLECTION\_DRAW\_LIST

```
@ScriptArguments(integer=8)
public static final int COLLECTION_DRAW_LIST
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.COLLECTION_DRAW_LIST)
- #### NOTIFICATION\_START

```
@ScriptArguments(integer=3)
public static final int NOTIFICATION_START
```

Draws the active notification in increasing sizes (increasing horizontally first, then vertically) to show a
starting animation.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.NOTIFICATION_START)
- #### NOTIFICATION\_DELAY

```
@ScriptArguments(integer=1)
public static final int NOTIFICATION_DELAY
```

Draws the active notification in full size for a specified number of client ticks. In essence, delayed between
the open and close animations.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.NOTIFICATION_DELAY)
- #### GROUP\_IRONMAN\_STORAGE\_BUILD

```
@ScriptArguments(integer=7)
public static final int GROUP_IRONMAN_STORAGE_BUILD
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.GROUP_IRONMAN_STORAGE_BUILD)
- #### INVENTORY\_DRAWITEM

```
@ScriptArguments(integer=6)
public static final int INVENTORY_DRAWITEM
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.INVENTORY_DRAWITEM)
- #### TRADE\_MAIN\_INIT

```
@ScriptArguments(integer=6)
public static final int TRADE_MAIN_INIT
```

Initializes the trade interface

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.TRADE_MAIN_INIT)
- #### TOB\_HUD\_SOTETSEG\_FADE

```
@ScriptArguments(string=1)
public static final int TOB_HUD_SOTETSEG_FADE
```

Transitions the tob hud into the white flash that happens when sotetseg teleports the players to the maze.

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.TOB_HUD_SOTETSEG_FADE)
- #### RAIDS\_STORAGE\_PRIVATE\_ITEMS

```
@ScriptArguments(integer=3)
public static final int RAIDS_STORAGE_PRIVATE_ITEMS
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.RAIDS_STORAGE_PRIVATE_ITEMS)
- #### HP\_HUD\_UPDATE

```
@ScriptArguments(integer=12)
public static final int HP_HUD_UPDATE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.HP_HUD_UPDATE)
- #### ORBS\_UPDATE\_RUNENERGY

```
@ScriptArguments(integer=7)
public static final int ORBS_UPDATE_RUNENERGY
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.ORBS_UPDATE_RUNENERGY)
- #### WORLDMAP\_LOADMAP

```
@ScriptArguments(integer=9)
public static final int WORLDMAP_LOADMAP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.WORLDMAP_LOADMAP)
- #### PRAYER\_UPDATEBUTTON

```
@ScriptArguments(integer=5)
public static final int PRAYER_UPDATEBUTTON
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.PRAYER_UPDATEBUTTON)
- #### PRAYER\_REDRAW

```
@ScriptArguments(integer=9,
string=2)
public static final int PRAYER_REDRAW
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.PRAYER_REDRAW)
- #### QUICKPRAYER\_INIT

```
@ScriptArguments(integer=3)
public static final int QUICKPRAYER_INIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.QUICKPRAYER_INIT)
- #### ADD\_OVERLAYTIMER\_LOC

```
@ScriptArguments(integer=7)
public static final int ADD_OVERLAYTIMER_LOC
```

Called to add a loc overlay timer

* loc coord
* loc id
* loc type
* overlay type
* overlay ticks

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.ADD_OVERLAYTIMER_LOC)
- #### ACCOUNT\_SUMMARY\_TEXT\_FORMAT

```
@ScriptArguments(integer=7,
string=1)
public static final int ACCOUNT_SUMMARY_TEXT_FORMAT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.ACCOUNT_SUMMARY_TEXT_FORMAT)
- #### ACCOUNT\_SUMMARY\_SECTION\_FORMAT

```
@ScriptArguments(integer=10,
string=3)
public static final int ACCOUNT_SUMMARY_SECTION_FORMAT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.ACCOUNT_SUMMARY_SECTION_FORMAT)
- #### CHATBOX\_KEYINPUT\_MATCHED

```
@ScriptArguments(integer=6,
string=2)
public static final int CHATBOX_KEYINPUT_MATCHED
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CHATBOX_KEYINPUT_MATCHED)
- #### EQUIPMENT\_SET\_STAT\_BONUS\_SETUP

```
@ScriptArguments(integer=6)
public static final int EQUIPMENT_SET_STAT_BONUS_SETUP
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.EQUIPMENT_SET_STAT_BONUS_SETUP)
- #### MAGIC\_SPELLBOOK\_INITIALISESPELLS

```
@ScriptArguments(integer=12,
string=2)
public static final int MAGIC_SPELLBOOK_INITIALISESPELLS
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.MAGIC_SPELLBOOK_INITIALISESPELLS)
- #### MOTHERLODE\_HUD\_UPDATE

```
@ScriptArguments(integer=2)
public static final int MOTHERLODE_HUD_UPDATE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.MOTHERLODE_HUD_UPDATE)
- #### POTIONSTORE\_DOSES

```
@ScriptArguments(integer=1)
public static final int POTIONSTORE_DOSES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.POTIONSTORE_DOSES)
- #### POTIONSTORE\_WITHDRAW\_DOSES

```
@ScriptArguments(integer=1)
public static final int POTIONSTORE_WITHDRAW_DOSES
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.POTIONSTORE_WITHDRAW_DOSES)
- #### POTIONSTORE\_BUILD

```
@ScriptArguments
public static final int POTIONSTORE_BUILD
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.POTIONSTORE_BUILD)
- #### POTIONSTORE\_DOSE\_CHANGE

```
@ScriptArguments(integer=3)
public static final int POTIONSTORE_DOSE_CHANGE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.POTIONSTORE_DOSE_CHANGE)
- #### FAIRYRINGS\_SORT\_UPDATE

```
@ScriptArguments(integer=6)
public static final int FAIRYRINGS_SORT_UPDATE
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.FAIRYRINGS_SORT_UPDATE)
- #### POPUP\_OVERLAY\_YESNO\_INIT

```
@ScriptArguments(integer=1,
string=1)
public static final int POPUP_OVERLAY_YESNO_INIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.POPUP_OVERLAY_YESNO_INIT)
- #### BANK\_DEPOSITBOX\_INIT

```
@ScriptArguments(integer=12)
public static final int BANK_DEPOSITBOX_INIT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.BANK_DEPOSITBOX_INIT)
- #### SEED\_VAULT\_BUILD

```
@ScriptArguments(integer=7)
public static final int SEED_VAULT_BUILD
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.SEED_VAULT_BUILD)
- #### LOOTTRACKER\_ADD\_LOOT

```
@ScriptArguments(integer=4)
public static final int LOOTTRACKER_ADD_LOOT
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.LOOTTRACKER_ADD_LOOT)
- #### DOM\_LOOT\_CLAIM

```
@ScriptArguments(integer=1)
public static final int DOM_LOOT_CLAIM
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.DOM_LOOT_CLAIM)
- #### CAMERA\_SET\_ZOOM\_LIMITS

```
@ScriptArguments(integer=4)
public static final int CAMERA_SET_ZOOM_LIMITS
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.CAMERA_SET_ZOOM_LIMITS)
- #### INTERFACE\_INV\_DRAW\_SLOT\_BIG

```
@ScriptArguments(integer=6,
string=9)
public static final int INTERFACE_INV_DRAW_SLOT_BIG
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.ScriptID.INTERFACE_INV_DRAW_SLOT_BIG)

+ ### Constructor Detail

- #### ScriptID

```
public ScriptID()
```