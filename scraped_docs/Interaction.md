# Interaction (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Interaction.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Interaction

* ---

```
public class Interaction
extends java.lang.Object
```

Utilities for easily interacting with game entities

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Interaction](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[interactGroundItem](#interactGroundItem(int,java.lang.String))​(int itemId,
java.lang.String action)` | Interacts with the best nearby ground item using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactGroundItem](#interactGroundItem(java.lang.String,java.lang.String))​(java.lang.String itemName,
java.lang.String action)` | Interacts with the best nearby ground item using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactNpc](#interactNpc(int,java.lang.String))​(int npcId,
java.lang.String action)` | Interacts with the best nearby npc using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactNpc](#interactNpc(java.lang.String,java.lang.String))​(java.lang.String npcName,
java.lang.String action)` | Interacts with the best nearby npc using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactObj](#interactObj(int,java.lang.String))​(int objId,
java.lang.String action)` | Interacts with the best nearby object using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactObj](#interactObj(java.lang.String,java.lang.String))​(java.lang.String objName,
java.lang.String action)` | Interacts with the best nearby object using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban") |
| `static boolean` | `[interactPlayer](#interactPlayer(java.lang.String,java.lang.String))​(java.lang.String playerName,
java.lang.String action)` | Interacts with the specified player using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String)) |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Interaction

```
public Interaction()
```

+ ### Method Detail

- #### interactNpc

```
public static boolean interactNpc​(java.lang.String npcName,
java.lang.String action)
```

Interacts with the best nearby npc using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`npcName` - the npc name
`action` - the npc action
Returns:
true if interacted with successfully, false otherwise
- #### interactNpc

```
public static boolean interactNpc​(int npcId,
java.lang.String action)
```

Interacts with the best nearby npc using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`npcId` - the npc id
`action` - the npc action
Returns:
true if interacted with successfully, false otherwise
- #### interactObj

```
public static boolean interactObj​(java.lang.String objName,
java.lang.String action)
```

Interacts with the best nearby object using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`objName` - the object name
`action` - the object action
Returns:
true if interacted with successfully, false otherwise
- #### interactObj

```
public static boolean interactObj​(int objId,
java.lang.String action)
```

Interacts with the best nearby object using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`objId` - the object id
`action` - the object action
Returns:
true if interacted with successfully, false otherwise
- #### interactPlayer

```
public static boolean interactPlayer​(java.lang.String playerName,
java.lang.String action)
```

Interacts with the specified player using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))

Parameters:
`playerName` - the player name
`action` - the player action
Returns:
true if interacted with successfully, false otherwise
- #### interactGroundItem

```
public static boolean interactGroundItem​(java.lang.String itemName,
java.lang.String action)
```

Interacts with the best nearby ground item using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`itemName` - the item name
`action` - the item action
Returns:
true if interacted with successfully, false otherwise
- #### interactGroundItem

```
public static boolean interactGroundItem​(int itemId,
java.lang.String action)
```

Interacts with the best nearby ground item using [`Interactable.interact(String)`](interfaces/Interactable.html#interact(java.lang.String))
according to [`PreferredTargetSelector`](antiban/PreferredTargetSelector.html "class in org.tribot.script.sdk.antiban")

Parameters:
`itemId` - the item id
`action` - the item action
Returns:
true if interacted with successfully, false otherwise