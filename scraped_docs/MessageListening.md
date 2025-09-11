# MessageListening (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/MessageListening.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.MessageListening

* ---

```
public class MessageListening
extends java.lang.Object
```

Contains methods to register listeners to listen to specific message types.
The listeners will be cleaned up after the script runs automatically.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[MessageListening](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[addClanMessageListener](#addClanMessageListener(org.tribot.script.sdk.interfaces.ClanMessageListener))​([ClanMessageListener](interfaces/ClanMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new clan message listener |
| `static void` | `[addDuelRequestListener](#addDuelRequestListener(org.tribot.script.sdk.interfaces.DuelRequestListener))​([DuelRequestListener](interfaces/DuelRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new duel request listener |
| `static void` | `[addPlayerMessageListener](#addPlayerMessageListener(org.tribot.script.sdk.interfaces.PlayerMessageListener))​([PlayerMessageListener](interfaces/PlayerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new player message listener |
| `static void` | `[addPrivateMessageListener](#addPrivateMessageListener(org.tribot.script.sdk.interfaces.PrivateMessageListener))​([PrivateMessageListener](interfaces/PrivateMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new private message listener |
| `static void` | `[addServerMessageListener](#addServerMessageListener(org.tribot.script.sdk.interfaces.ServerMessageListener))​([ServerMessageListener](interfaces/ServerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new server message listener |
| `static void` | `[addTradeRequestListener](#addTradeRequestListener(org.tribot.script.sdk.interfaces.TradeRequestListener))​([TradeRequestListener](interfaces/TradeRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Registers a new trade request listener |
| `static void` | `[removeClanMessageListener](#removeClanMessageListener(org.tribot.script.sdk.interfaces.ClanMessageListener))​([ClanMessageListener](interfaces/ClanMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a clan message listener |
| `static void` | `[removeDuelRequestListener](#removeDuelRequestListener(org.tribot.script.sdk.interfaces.DuelRequestListener))​([DuelRequestListener](interfaces/DuelRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a duel request listener |
| `static void` | `[removePlayerMessageListener](#removePlayerMessageListener(org.tribot.script.sdk.interfaces.PlayerMessageListener))​([PlayerMessageListener](interfaces/PlayerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a player message listener |
| `static void` | `[removePrivateMessageListener](#removePrivateMessageListener(org.tribot.script.sdk.interfaces.PrivateMessageListener))​([PrivateMessageListener](interfaces/PrivateMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a private message listener |
| `static void` | `[removeServerMessageListener](#removeServerMessageListener(org.tribot.script.sdk.interfaces.ServerMessageListener))​([ServerMessageListener](interfaces/ServerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a server message listener |
| `static void` | `[removeTradeRequestListener](#removeTradeRequestListener(org.tribot.script.sdk.interfaces.TradeRequestListener))​([TradeRequestListener](interfaces/TradeRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)` | Removes a trade request listener |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### MessageListening

```
public MessageListening()
```

+ ### Method Detail

- #### addClanMessageListener

```
public static void addClanMessageListener​([ClanMessageListener](interfaces/ClanMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new clan message listener

Parameters:
`listener` - the clan message listener
- #### removeClanMessageListener

```
public static void removeClanMessageListener​([ClanMessageListener](interfaces/ClanMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a clan message listener

Parameters:
`listener` - the listener to remove
- #### addDuelRequestListener

```
public static void addDuelRequestListener​([DuelRequestListener](interfaces/DuelRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new duel request listener

Parameters:
`listener` - the duel request listener
- #### removeDuelRequestListener

```
public static void removeDuelRequestListener​([DuelRequestListener](interfaces/DuelRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a duel request listener

Parameters:
`listener` - the listener to remove
- #### addPlayerMessageListener

```
public static void addPlayerMessageListener​([PlayerMessageListener](interfaces/PlayerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new player message listener

Parameters:
`listener` - the player message listener
- #### removePlayerMessageListener

```
public static void removePlayerMessageListener​([PlayerMessageListener](interfaces/PlayerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a player message listener

Parameters:
`listener` - the listener to remove
- #### addPrivateMessageListener

```
public static void addPrivateMessageListener​([PrivateMessageListener](interfaces/PrivateMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new private message listener

Parameters:
`listener` - the private message listener
- #### removePrivateMessageListener

```
public static void removePrivateMessageListener​([PrivateMessageListener](interfaces/PrivateMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a private message listener

Parameters:
`listener` - the listener to remove
- #### addServerMessageListener

```
public static void addServerMessageListener​([ServerMessageListener](interfaces/ServerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new server message listener

Parameters:
`listener` - the server message listener
- #### removeServerMessageListener

```
public static void removeServerMessageListener​([ServerMessageListener](interfaces/ServerMessageListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a server message listener

Parameters:
`listener` - the listener to remove
- #### addTradeRequestListener

```
public static void addTradeRequestListener​([TradeRequestListener](interfaces/TradeRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Registers a new trade request listener

Parameters:
`listener` - the trade request listener
- #### removeTradeRequestListener

```
public static void removeTradeRequestListener​([TradeRequestListener](interfaces/TradeRequestListener.html "interface in org.tribot.script.sdk.interfaces") listener)
```

Removes a trade request listener

Parameters:
`listener` - the listener to remove