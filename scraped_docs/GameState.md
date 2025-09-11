# GameState (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/GameState.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.GameState

* ---

```
public class GameState
extends java.lang.Object
```

Utilities for inspecting the client game state

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GameState.State](GameState.State.html "enum in org.tribot.script.sdk")` | A current state of the game, such as loading, at login screen, or logged in. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[GameState](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static int` | `[getFps](#getFps())()` | Gets the current fps. |
| `static java.util.Optional<[LocalTile](types/LocalTile.html "class in org.tribot.script.sdk.types")>` | `[getHintArrowPosition](#getHintArrowPosition())()` | Gets the tile that the hint arrow is pointing to. |
| `static int` | `[getLoopCycle](#getLoopCycle())()` | Gets the runescape client's current loop cycle. |
| `static int` | `[getMinimapRotation](#getMinimapRotation())()` | Gets the rotation of the minimap |
| `static java.lang.String` | `[getSelectedItemName](#getSelectedItemName())()` | Gets the name of the selected item if there is one. |
| `static int` | `[getSetting](#getSetting(int))​(int index)` | Pulls Setting value from the client with the given index. |
| `static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk")` | `[getState](#getState())()` | Gets the current state of the game |
| `static java.lang.String` | `[getUpText](#getUpText())()` | Gets the game's "uptext" that appears in the top left corner of the screen. |
| `static int` | `[getVarbit](#getVarbit(int))​(int id)` | Pulls org.tribot.script.sdk.VarBit value from the client with the given varbit ID. |
| `static java.util.Optional<java.lang.Object>` | `[getVarc](#getVarc(int))​(int index)` | Gets the client-side variable at the specified index |
| `static java.util.Optional<java.lang.Integer>` | `[getVarcInt](#getVarcInt(int))​(int index)` | Gets the client-side variable at the specified index as an int |
| `static java.util.Optional<java.lang.String>` | `[getVarcString](#getVarcString(int))​(int index)` | Gets the client-side variable at the specified index as a string |
| `static int` | `[getViewportHeight](#getViewportHeight())()` | Determines the height of the viewport (OSRS scene render). |
| `static int` | `[getViewportWidth](#getViewportWidth())()` | Determines the width of the viewport (OSRS scene render). |
| `static boolean` | `[isAnyItemSelected](#isAnyItemSelected())()` | Determines if an inventory item is selected (highlighted). |
| `static boolean` | `[isGravestoneActive](#isGravestoneActive())()` | Checks if a gravestone is active |
| `static boolean` | `[isInBuildingMode](#isInBuildingMode())()` | Determines if the game is in "building mode", which can be toggled when in your own Player Owned House. |
| `static boolean` | `[isInInstance](#isInInstance())()` | Checks if we are in an instance |
| `static boolean` | `[isLoading](#isLoading())()` | Checks if the game is loading the current player. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### GameState

```
public GameState()
```

+ ### Method Detail

- #### getVarbit

```
public static int getVarbit​(int id)
```

Pulls org.tribot.script.sdk.VarBit value from the client with the given varbit ID.

Helpful VarBits: https://github.com/runelite/runelite/blob/master/runelite-api/src/main/java/net/runelite/api/Varbits.java
- #### getVarc

```
public static java.util.Optional<java.lang.Object> getVarc​(int index)
```

Gets the client-side variable at the specified index

Parameters:
`index` - the client-side variable index
Returns:
the client-side variable at the specified index
- #### getVarcString

```
public static java.util.Optional<java.lang.String> getVarcString​(int index)
```

Gets the client-side variable at the specified index as a string

Parameters:
`index` - the client-side variable index
Returns:
the client-side variable at the specified index as a string
- #### getVarcInt

```
public static java.util.Optional<java.lang.Integer> getVarcInt​(int index)
```

Gets the client-side variable at the specified index as an int

Parameters:
`index` - the client-side variable index
Returns:
the client-side variable at the specified index as an int
- #### getSetting

```
public static int getSetting​(int index)
```

Pulls Setting value from the client with the given index.
- #### getViewportHeight

```
public static int getViewportHeight()
```

Determines the height of the viewport (OSRS scene render).

Returns:
The height, in number of pixels.
- #### getViewportWidth

```
public static int getViewportWidth()
```

Determines the width of the viewport (OSRS scene render).

Returns:
The width, in number of pixels.
- #### getUpText

```
public static java.lang.String getUpText()
```

Gets the game's "uptext" that appears in the top left corner of the screen.

Returns:
The uptext string. Blank if there is no uptext.
- #### isAnyItemSelected

```
public static boolean isAnyItemSelected()
```

Determines if an inventory item is selected (highlighted).

Returns:
True if any item is selected. False otherwise.
- #### getSelectedItemName

```
public static java.lang.String getSelectedItemName()
```

Gets the name of the selected item if there is one.

Returns:
The name of the selected item. Blank if no item is selected.
- #### getMinimapRotation

```
public static int getMinimapRotation()
```

Gets the rotation of the minimap
- #### getHintArrowPosition

```
public static java.util.Optional<[LocalTile](types/LocalTile.html "class in org.tribot.script.sdk.types")> getHintArrowPosition()
```

Gets the tile that the hint arrow is pointing to.

Returns:
An Optional of the tile. Empty if there is no hint arrow.
- #### isLoading

```
public static boolean isLoading()
```

Checks if the game is loading the current player. This occurs when logging in and the runescape client is loading the player's data from the server.

Returns:
true if the game is loading the current player, false otherwise
- #### isInInstance

```
public static boolean isInInstance()
```

Checks if we are in an instance

Returns:
true if we are in an instanced area, false otherwise
- #### getLoopCycle

```
public static int getLoopCycle()
```

Gets the runescape client's current loop cycle. The client performs a loop cycle at most every 20 milliseconds.

Returns:
the runescape client's current loop cycle
- #### getFps

```
public static int getFps()
```

Gets the current fps. This is what would appear if you typed ::displayfps in-game

Returns:
the current fps
- #### isGravestoneActive

```
public static boolean isGravestoneActive()
```

Checks if a gravestone is active

Returns:
true if a gravestone is active, false otherwise
- #### getState

```
public static [GameState.State](GameState.State.html "enum in org.tribot.script.sdk") getState()
```

Gets the current state of the game

Returns:
the current state of the game
- #### isInBuildingMode

```
public static boolean isInBuildingMode()
```

Determines if the game is in "building mode", which can be toggled when in your own Player Owned House.

Returns:
True if in building mode. False otherwise.