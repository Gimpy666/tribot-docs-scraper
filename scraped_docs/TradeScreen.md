# TradeScreen (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/TradeScreen.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.TradeScreen

* ---

```
public class TradeScreen
extends java.lang.Object
```

Utilities for interacting with the "trading" interface that appears for player-to-player trades.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[TradeScreen.MyPlayer](TradeScreen.MyPlayer.html "class in org.tribot.script.sdk")` | My player's trade screen information |
| `static class` | `[TradeScreen.OtherPlayer](TradeScreen.OtherPlayer.html "class in org.tribot.script.sdk")` | The other player's trade screen information |
| `static class` | `[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")` | The trade window stage |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[TradeScreen](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[accept](#accept())()` | Clicks the accept button on either the first or second trade window, and will wait for the trade interface to
change. |
| `static boolean` | `[close](#close())()` | Closes the trading window, and waits for the window to close. |
| `static java.util.Optional<[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")>` | `[getStage](#getStage())()` | Gets the stage of the current trade. |
| `static boolean` | `[isDelayed](#isDelayed())()` | Checks accepting is delayed because something was changed recently in the trade |
| `static boolean` | `[offer](#offer(int,int))​(int itemId,
int amount)` | Offers the items whose ID matches the specified ID to the first trade window. |
| `static boolean` | `[offerAll](#offerAll(int))​(int itemId)` | Offers the items whose ID matches the specified ID to the first trade window. |
| `static boolean` | `[remove](#remove(int,int))​(int itemId,
int amount)` | Removes the offered items whose ID matches the specified ID to the first trade window. |
| `static boolean` | `[removeAll](#removeAll(int))​(int itemId)` | Removes the items whose ID matches the specified ID to the first trade window. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### TradeScreen

```
public TradeScreen()
```

+ ### Method Detail

- #### getStage

```
public static java.util.Optional<[TradeScreen.Stage](TradeScreen.Stage.html "enum in org.tribot.script.sdk")> getStage()
```

Gets the stage of the current trade.

Returns:
The current stage. Empty if not in the trading screen.
- #### isDelayed

```
public static boolean isDelayed()
```

Checks accepting is delayed because something was changed recently in the trade

Returns:
true if accepting is delayed due to a recent change, false otherwise
- #### accept

```
public static boolean accept()
```

Clicks the accept button on either the first or second trade window, and will wait for the trade interface to
change. Will only accept one trade window at a time.

Returns:
True if successfully accepted the trade; false otherwise.
- #### close

```
public static boolean close()
```

Closes the trading window, and waits for the window to close.

Returns:
True if successful. False otherwise.
- #### offer

```
public static boolean offer​(int itemId,
int amount)
```

Offers the items whose ID matches the specified ID to the first trade window.

Parameters:
`itemId` - The ID of the item you wish to offer.
`amount` - The amount of the item to offer.
Returns:
True if all of the items were offered, and if at least one item was offered; false otherwise.
- #### offerAll

```
public static boolean offerAll​(int itemId)
```

Offers the items whose ID matches the specified ID to the first trade window.

Parameters:
`itemId` - The ID of the item you wish to offer.
Returns:
True if all of the items were offered; false otherwise.
- #### remove

```
public static boolean remove​(int itemId,
int amount)
```

Removes the offered items whose ID matches the specified ID to the first trade window.

Parameters:
`itemId` - The ID of the item you wish to remove.
`amount` - The amount of the item to remove.
Returns:
True if all of the items were removed, and if at least one item was removed; false otherwise.
- #### removeAll

```
public static boolean removeAll​(int itemId)
```

Removes the items whose ID matches the specified ID to the first trade window.

Parameters:
`itemId` - The ID of the item you wish to remove.
Returns:
True if all of the items were removed; false otherwise.