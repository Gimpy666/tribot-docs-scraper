# MenuAction (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/MenuAction.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[MenuAction](MenuAction.html "enum in net.runelite.api")>
+ - net.runelite.api.MenuAction

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[MenuAction](MenuAction.html "enum in net.runelite.api")>`

---

```
public enum MenuAction
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[MenuAction](MenuAction.html "enum in net.runelite.api")>
```

An enumeration of right-click menu actions.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[CANCEL](#CANCEL)` | Menu action triggered by canceling a menu. |
| `[CC\_OP](#CC_OP)` | Menu action for normal priority child component actions. |
| `[CC\_OP\_LOW\_PRIORITY](#CC_OP_LOW_PRIORITY)` | Menu action for low priority child component actions. |
| `[EXAMINE\_ITEM](#EXAMINE_ITEM)` | Deprecated. |
| `[EXAMINE\_ITEM\_GROUND](#EXAMINE_ITEM_GROUND)` | Menu action triggered by examining item on ground. |
| `[EXAMINE\_NPC](#EXAMINE_NPC)` | Menu action triggered by examining an NPC. |
| `[EXAMINE\_OBJECT](#EXAMINE_OBJECT)` | Menu action triggered by examining an object. |
| `[EXAMINE\_WORLD\_ENTITY](#EXAMINE_WORLD_ENTITY)` | |
| `[GAME\_OBJECT\_FIFTH\_OPTION](#GAME_OBJECT_FIFTH_OPTION)` | Fifth menu action for a game object. |
| `[GAME\_OBJECT\_FIRST\_OPTION](#GAME_OBJECT_FIRST_OPTION)` | First menu action for a game object. |
| `[GAME\_OBJECT\_FOURTH\_OPTION](#GAME_OBJECT_FOURTH_OPTION)` | Fourth menu action for a game object. |
| `[GAME\_OBJECT\_SECOND\_OPTION](#GAME_OBJECT_SECOND_OPTION)` | Second menu action for a game object. |
| `[GAME\_OBJECT\_THIRD\_OPTION](#GAME_OBJECT_THIRD_OPTION)` | Third menu action for a game object. |
| `[GROUND\_ITEM\_FIFTH\_OPTION](#GROUND_ITEM_FIFTH_OPTION)` | Fifth menu action for an item on the ground. |
| `[GROUND\_ITEM\_FIRST\_OPTION](#GROUND_ITEM_FIRST_OPTION)` | First menu action for an item on the ground. |
| `[GROUND\_ITEM\_FOURTH\_OPTION](#GROUND_ITEM_FOURTH_OPTION)` | Fourth menu action for an item on the ground. |
| `[GROUND\_ITEM\_SECOND\_OPTION](#GROUND_ITEM_SECOND_OPTION)` | Second menu action for an item on the ground. |
| `[GROUND\_ITEM\_THIRD\_OPTION](#GROUND_ITEM_THIRD_OPTION)` | Third menu action for an item on the ground. |
| `[ITEM\_FIFTH\_OPTION](#ITEM_FIFTH_OPTION)` | Deprecated. |
| `[ITEM\_FIRST\_OPTION](#ITEM_FIRST_OPTION)` | Deprecated. |
| `[ITEM\_FOURTH\_OPTION](#ITEM_FOURTH_OPTION)` | Deprecated. |
| `[ITEM\_SECOND\_OPTION](#ITEM_SECOND_OPTION)` | Deprecated. |
| `[ITEM\_THIRD\_OPTION](#ITEM_THIRD_OPTION)` | Deprecated. |
| `[ITEM\_USE](#ITEM_USE)` | Deprecated. |
| `[ITEM\_USE\_ON\_GAME\_OBJECT](#ITEM_USE_ON_GAME_OBJECT)` | Deprecated. |
| `[ITEM\_USE\_ON\_GROUND\_ITEM](#ITEM_USE_ON_GROUND_ITEM)` | Deprecated. |
| `[ITEM\_USE\_ON\_ITEM](#ITEM_USE_ON_ITEM)` | Deprecated. |
| `[ITEM\_USE\_ON\_NPC](#ITEM_USE_ON_NPC)` | Deprecated. |
| `[ITEM\_USE\_ON\_PLAYER](#ITEM_USE_ON_PLAYER)` | Deprecated. |
| `[NPC\_FIFTH\_OPTION](#NPC_FIFTH_OPTION)` | Fifth menu action for an NPC. |
| `[NPC\_FIRST\_OPTION](#NPC_FIRST_OPTION)` | First menu action for an NPC. |
| `[NPC\_FOURTH\_OPTION](#NPC_FOURTH_OPTION)` | Fourth menu action for an NPC. |
| `[NPC\_SECOND\_OPTION](#NPC_SECOND_OPTION)` | Second menu action for an NPC. |
| `[NPC\_THIRD\_OPTION](#NPC_THIRD_OPTION)` | Third menu action for an NPC. |
| `[PLAYER\_EIGHTH\_OPTION](#PLAYER_EIGHTH_OPTION)` | |
| `[PLAYER\_FIFTH\_OPTION](#PLAYER_FIFTH_OPTION)` | |
| `[PLAYER\_FIRST\_OPTION](#PLAYER_FIRST_OPTION)` | |
| `[PLAYER\_FOURTH\_OPTION](#PLAYER_FOURTH_OPTION)` | |
| `[PLAYER\_SECOND\_OPTION](#PLAYER_SECOND_OPTION)` | |
| `[PLAYER\_SEVENTH\_OPTION](#PLAYER_SEVENTH_OPTION)` | |
| `[PLAYER\_SIXTH\_OPTION](#PLAYER_SIXTH_OPTION)` | |
| `[PLAYER\_THIRD\_OPTION](#PLAYER_THIRD_OPTION)` | |
| `[RUNELITE](#RUNELITE)` | Menu action injected by runelite for its menu items. |
| `[RUNELITE\_HIGH\_PRIORITY](#RUNELITE_HIGH_PRIORITY)` | Menu action for high priority runelite options |
| `[RUNELITE\_INFOBOX](#RUNELITE_INFOBOX)` | Menu action for InfoBox menu entries |
| `[RUNELITE\_LOW\_PRIORITY](#RUNELITE_LOW_PRIORITY)` | Like [`RUNELITE`](#RUNELITE), except clicking always forces the menu open. |
| `[RUNELITE\_OVERLAY](#RUNELITE_OVERLAY)` | Menu action injected by runelite for overlay menu items. |
| `[RUNELITE\_OVERLAY\_CONFIG](#RUNELITE_OVERLAY_CONFIG)` | Menu action for configuring runelite overlays. |
| `[RUNELITE\_PLAYER](#RUNELITE_PLAYER)` | Menu action injected by runelite for menu items which target
a player and have its identifier set to a player index. |
| `[RUNELITE\_WIDGET](#RUNELITE_WIDGET)` | RuneLite menu that is a widge. |
| `[SET\_HEADING](#SET_HEADING)` | |
| `[UNKNOWN](#UNKNOWN)` | Menu action triggered when the id is not defined in this class. |
| `[WALK](#WALK)` | Menu action for walking. |
| `[WIDGET\_CLOSE](#WIDGET_CLOSE)` | Performs an ifclose. |
| `[WIDGET\_CONTINUE](#WIDGET_CONTINUE)` | Performs a Continue |
| `[WIDGET\_FIFTH\_OPTION](#WIDGET_FIFTH_OPTION)` | Fifth menu action for a widget. |
| `[WIDGET\_FIRST\_OPTION](#WIDGET_FIRST_OPTION)` | First menu action for a widget. |
| `[WIDGET\_FOURTH\_OPTION](#WIDGET_FOURTH_OPTION)` | Fourth menu action for a widget. |
| `[WIDGET\_SECOND\_OPTION](#WIDGET_SECOND_OPTION)` | Second menu action for a widget. |
| `[WIDGET\_TARGET](#WIDGET_TARGET)` | Select the widget for targeting other widgets/entites etc. |
| `[WIDGET\_TARGET\_ON\_GAME\_OBJECT](#WIDGET_TARGET_ON_GAME_OBJECT)` | Menu action for using a widget on a tile object (GameObject or GroundObject). |
| `[WIDGET\_TARGET\_ON\_GROUND\_ITEM](#WIDGET_TARGET_ON_GROUND_ITEM)` | Menu action for using a widget on an item on the ground. |
| `[WIDGET\_TARGET\_ON\_NPC](#WIDGET_TARGET_ON_NPC)` | Menu action for using a widget on an NPC. |
| `[WIDGET\_TARGET\_ON\_PLAYER](#WIDGET_TARGET_ON_PLAYER)` | Menu action for using a widget on a player. |
| `[WIDGET\_TARGET\_ON\_WIDGET](#WIDGET_TARGET_ON_WIDGET)` | Using a widget on another widget |
| `[WIDGET\_THIRD\_OPTION](#WIDGET_THIRD_OPTION)` | Third menu action for a widget. |
| `[WIDGET\_TYPE\_1](#WIDGET_TYPE_1)` | Interaction with widget (type 1). |
| `[WIDGET\_TYPE\_4](#WIDGET_TYPE_4)` | Interaction with widget (type 4). |
| `[WIDGET\_TYPE\_5](#WIDGET_TYPE_5)` | Interaction with widget (type 5). |
| `[WIDGET\_USE\_ON\_ITEM](#WIDGET_USE_ON_ITEM)` | Deprecated. |
| `[WORLD\_ENTITY\_FIFTH\_OPTION](#WORLD_ENTITY_FIFTH_OPTION)` | |
| `[WORLD\_ENTITY\_FIRST\_OPTION](#WORLD_ENTITY_FIRST_OPTION)` | |
| `[WORLD\_ENTITY\_FOURTH\_OPTION](#WORLD_ENTITY_FOURTH_OPTION)` | |
| `[WORLD\_ENTITY\_SECOND\_OPTION](#WORLD_ENTITY_SECOND_OPTION)` | |
| `[WORLD\_ENTITY\_THIRD\_OPTION](#WORLD_ENTITY_THIRD_OPTION)` | |

+ ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static int` | `[MENU\_ACTION\_DEPRIORITIZE\_OFFSET](#MENU_ACTION_DEPRIORITIZE_OFFSET)` | |
| `static [MenuAction](MenuAction.html "enum in net.runelite.api")` | `[PLAYER\_EIGTH\_OPTION](#PLAYER_EIGTH_OPTION)` | Deprecated. |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | |
| `static [MenuAction](MenuAction.html "enum in net.runelite.api")` | `[of](#of(int))​(int id)` | |
| `static [MenuAction](MenuAction.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [MenuAction](MenuAction.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### ITEM\_USE\_ON\_GAME\_OBJECT

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE_ON_GAME_OBJECT
```

Deprecated.
Menu action for using an item in your inventory on a tile object (GameObject or GroundObject).
- #### WIDGET\_TARGET\_ON\_GAME\_OBJECT

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET_ON_GAME_OBJECT
```

Menu action for using a widget on a tile object (GameObject or GroundObject).
- #### GAME\_OBJECT\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GAME_OBJECT_FIRST_OPTION
```

First menu action for a game object.
- #### GAME\_OBJECT\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GAME_OBJECT_SECOND_OPTION
```

Second menu action for a game object.
- #### GAME\_OBJECT\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GAME_OBJECT_THIRD_OPTION
```

Third menu action for a game object.
- #### GAME\_OBJECT\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GAME_OBJECT_FOURTH_OPTION
```

Fourth menu action for a game object.
- #### GAME\_OBJECT\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GAME_OBJECT_FIFTH_OPTION
```

Fifth menu action for a game object.
- #### ITEM\_USE\_ON\_NPC

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE_ON_NPC
```

Deprecated.
Menu action for using an item in your inventory on an NPC.
- #### WIDGET\_TARGET\_ON\_NPC

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET_ON_NPC
```

Menu action for using a widget on an NPC.
- #### NPC\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") NPC_FIRST_OPTION
```

First menu action for an NPC.
- #### NPC\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") NPC_SECOND_OPTION
```

Second menu action for an NPC.
- #### NPC\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") NPC_THIRD_OPTION
```

Third menu action for an NPC.
- #### NPC\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") NPC_FOURTH_OPTION
```

Fourth menu action for an NPC.
- #### NPC\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") NPC_FIFTH_OPTION
```

Fifth menu action for an NPC.
- #### ITEM\_USE\_ON\_PLAYER

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE_ON_PLAYER
```

Deprecated.
Menu action for using an item on a player.
- #### WIDGET\_TARGET\_ON\_PLAYER

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET_ON_PLAYER
```

Menu action for using a widget on a player.
- #### ITEM\_USE\_ON\_GROUND\_ITEM

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE_ON_GROUND_ITEM
```

Deprecated.
Menu action for using an item on an item on the ground.
- #### WIDGET\_TARGET\_ON\_GROUND\_ITEM

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET_ON_GROUND_ITEM
```

Menu action for using a widget on an item on the ground.
- #### GROUND\_ITEM\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GROUND_ITEM_FIRST_OPTION
```

First menu action for an item on the ground.
- #### GROUND\_ITEM\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GROUND_ITEM_SECOND_OPTION
```

Second menu action for an item on the ground.
- #### GROUND\_ITEM\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GROUND_ITEM_THIRD_OPTION
```

Third menu action for an item on the ground.
- #### GROUND\_ITEM\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GROUND_ITEM_FOURTH_OPTION
```

Fourth menu action for an item on the ground.
- #### GROUND\_ITEM\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") GROUND_ITEM_FIFTH_OPTION
```

Fifth menu action for an item on the ground.
- #### WALK

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WALK
```

Menu action for walking.
- #### WIDGET\_TYPE\_1

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TYPE_1
```

Interaction with widget (type 1).
- #### WIDGET\_TARGET

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET
```

Select the widget for targeting other widgets/entites etc.

See Also:
[`Client.getSelectedWidget()`](Client.html#getSelectedWidget())
- #### WIDGET\_CLOSE

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_CLOSE
```

Performs an ifclose.
- #### WIDGET\_TYPE\_4

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TYPE_4
```

Interaction with widget (type 4).
- #### WIDGET\_TYPE\_5

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TYPE_5
```

Interaction with widget (type 5).
- #### WIDGET\_CONTINUE

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_CONTINUE
```

Performs a Continue
- #### ITEM\_USE\_ON\_ITEM

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE_ON_ITEM
```

Deprecated.
Menu action when using an item on another item
- #### WIDGET\_USE\_ON\_ITEM

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_USE_ON_ITEM
```

Deprecated.
Menu action when using a component on an item
- #### ITEM\_FIRST\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_FIRST_OPTION
```

Deprecated.
First menu action for an item.
- #### ITEM\_SECOND\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_SECOND_OPTION
```

Deprecated.
Second menu action for an item.
- #### ITEM\_THIRD\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_THIRD_OPTION
```

Deprecated.
Third menu action for an item.
- #### ITEM\_FOURTH\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_FOURTH_OPTION
```

Deprecated.
Fourth menu action for an item.
- #### ITEM\_FIFTH\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_FIFTH_OPTION
```

Deprecated.
Fifth menu action for an item.
- #### ITEM\_USE

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") ITEM_USE
```

Deprecated.
Menu action to use an item.
- #### WIDGET\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_FIRST_OPTION
```

First menu action for a widget.
- #### WIDGET\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_SECOND_OPTION
```

Second menu action for a widget.
- #### WIDGET\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_THIRD_OPTION
```

Third menu action for a widget.
- #### WIDGET\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_FOURTH_OPTION
```

Fourth menu action for a widget.
- #### WIDGET\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_FIFTH_OPTION
```

Fifth menu action for a widget.
- #### PLAYER\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_FIRST_OPTION
```
- #### PLAYER\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_SECOND_OPTION
```
- #### PLAYER\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_THIRD_OPTION
```
- #### PLAYER\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_FOURTH_OPTION
```
- #### PLAYER\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_FIFTH_OPTION
```
- #### PLAYER\_SIXTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_SIXTH_OPTION
```
- #### PLAYER\_SEVENTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_SEVENTH_OPTION
```
- #### PLAYER\_EIGHTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_EIGHTH_OPTION
```
- #### CC\_OP

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") CC_OP
```

Menu action for normal priority child component actions.
- #### WIDGET\_TARGET\_ON\_WIDGET

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WIDGET_TARGET_ON_WIDGET
```

Using a widget on another widget
- #### SET\_HEADING

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") SET_HEADING
```
- #### WORLD\_ENTITY\_FIRST\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WORLD_ENTITY_FIRST_OPTION
```
- #### WORLD\_ENTITY\_SECOND\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WORLD_ENTITY_SECOND_OPTION
```
- #### WORLD\_ENTITY\_THIRD\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WORLD_ENTITY_THIRD_OPTION
```
- #### WORLD\_ENTITY\_FOURTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WORLD_ENTITY_FOURTH_OPTION
```
- #### WORLD\_ENTITY\_FIFTH\_OPTION

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") WORLD_ENTITY_FIFTH_OPTION
```
- #### RUNELITE\_WIDGET

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_WIDGET
```

RuneLite menu that is a widge.

See Also:
[`MenuEntry.getWidget()`](MenuEntry.html#getWidget())
- #### RUNELITE\_HIGH\_PRIORITY

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_HIGH_PRIORITY
```

Menu action for high priority runelite options
- #### EXAMINE\_OBJECT

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") EXAMINE_OBJECT
```

Menu action triggered by examining an object.
- #### EXAMINE\_NPC

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") EXAMINE_NPC
```

Menu action triggered by examining an NPC.
- #### EXAMINE\_ITEM\_GROUND

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") EXAMINE_ITEM_GROUND
```

Menu action triggered by examining item on ground.
- #### EXAMINE\_ITEM

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") EXAMINE_ITEM
```

Deprecated.
Menu action triggered by examining item in inventory.
- #### CANCEL

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") CANCEL
```

Menu action triggered by canceling a menu.
- #### CC\_OP\_LOW\_PRIORITY

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") CC_OP_LOW_PRIORITY
```

Menu action for low priority child component actions.
- #### EXAMINE\_WORLD\_ENTITY

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") EXAMINE_WORLD_ENTITY
```
- #### RUNELITE

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE
```

Menu action injected by runelite for its menu items.
- #### RUNELITE\_OVERLAY

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_OVERLAY
```

Menu action injected by runelite for overlay menu items.
- #### RUNELITE\_OVERLAY\_CONFIG

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_OVERLAY_CONFIG
```

Menu action for configuring runelite overlays.
- #### RUNELITE\_PLAYER

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_PLAYER
```

Menu action injected by runelite for menu items which target
a player and have its identifier set to a player index.
- #### RUNELITE\_INFOBOX

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_INFOBOX
```

Menu action for InfoBox menu entries
- #### RUNELITE\_LOW\_PRIORITY

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") RUNELITE_LOW_PRIORITY
```

Like [`RUNELITE`](#RUNELITE), except clicking always forces the menu open.
- #### UNKNOWN

```
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") UNKNOWN
```

Menu action triggered when the id is not defined in this class.

+ ### Field Detail

- #### MENU\_ACTION\_DEPRIORITIZE\_OFFSET

```
public static final int MENU_ACTION_DEPRIORITIZE_OFFSET
```

See Also:
[Constant Field Values](../../../constant-values.html#net.runelite.api.MenuAction.MENU_ACTION_DEPRIORITIZE_OFFSET)
- #### PLAYER\_EIGTH\_OPTION

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public static final [MenuAction](MenuAction.html "enum in net.runelite.api") PLAYER_EIGTH_OPTION
```

Deprecated.

+ ### Method Detail

- #### values

```
public static [MenuAction](MenuAction.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (MenuAction c : MenuAction.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [MenuAction](MenuAction.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html?is-external=true "class or interface in java.lang")` - if this enum type has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/NullPointerException.html?is-external=true "class or interface in java.lang")` - if the argument is null
- #### getId

```
public int getId()
```
- #### of

```
public static [MenuAction](MenuAction.html "enum in net.runelite.api") of​(int id)
```