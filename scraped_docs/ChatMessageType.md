# ChatMessageType (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ChatMessageType.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[ChatMessageType](ChatMessageType.html "enum in net.runelite.api")>
+ - net.runelite.api.ChatMessageType

* All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html?is-external=true "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[ChatMessageType](ChatMessageType.html "enum in net.runelite.api")>`

---

```
public enum ChatMessageType
extends [Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[ChatMessageType](ChatMessageType.html "enum in net.runelite.api")>
```

Enumeration of message types that can be received in the chat.

* + ### Enum Constant Summary

Enum Constants | Enum Constant | Description |
| `[AUTOTYPER](#AUTOTYPER)` | An autotyper message from a player. |
| `[BROADCAST](#BROADCAST)` | A game broadcast. |
| `[CHALREQ\_CLANCHAT](#CHALREQ_CLANCHAT)` | Challenge offer for the clan tab |
| `[CHALREQ\_FRIENDSCHAT](#CHALREQ_FRIENDSCHAT)` | A message received when someone sends a friends chat challenge offer. |
| `[CHALREQ\_TRADE](#CHALREQ_TRADE)` | A message received when somebody sends a duel offer. |
| `[CLAN\_CHAT](#CLAN_CHAT)` | A chat message in a clan chat. |
| `[CLAN\_CREATION\_INVITATION](#CLAN_CREATION_INVITATION)` | Clan creation invitation. |
| `[CLAN\_GIM\_CHAT](#CLAN_GIM_CHAT)` | |
| `[CLAN\_GIM\_FORM\_GROUP](#CLAN_GIM_FORM_GROUP)` | |
| `[CLAN\_GIM\_GROUP\_WITH](#CLAN_GIM_GROUP_WITH)` | |
| `[CLAN\_GIM\_MESSAGE](#CLAN_GIM_MESSAGE)` | |
| `[CLAN\_GUEST\_CHAT](#CLAN_GUEST_CHAT)` | A chat message in the guest clan chat. |
| `[CLAN\_GUEST\_MESSAGE](#CLAN_GUEST_MESSAGE)` | A system message in the guest clan chat. |
| `[CLAN\_MESSAGE](#CLAN_MESSAGE)` | A system message in a clan chat. |
| `[CONSOLE](#CONSOLE)` | A game message. |
| `[DIALOG](#DIALOG)` | Chat type for npc and player dialog |
| `[DIDYOUKNOW](#DIDYOUKNOW)` | Did you know?-es |
| `[ENGINE](#ENGINE)` | A message that the game engine sends. |
| `[FRIENDNOTIFICATION](#FRIENDNOTIFICATION)` | Adding player to friend list. |
| `[FRIENDSCHAT](#FRIENDSCHAT)` | A message received in friends chat. |
| `[FRIENDSCHATNOTIFICATION](#FRIENDSCHATNOTIFICATION)` | A message received with information about the current friends chat. |
| `[GAMEMESSAGE](#GAMEMESSAGE)` | A normal game message. |
| `[IGNORENOTIFICATION](#IGNORENOTIFICATION)` | Adding player to ignore list. |
| `[ITEM\_EXAMINE](#ITEM_EXAMINE)` | Examine item description. |
| `[LOGINLOGOUTNOTIFICATION](#LOGINLOGOUTNOTIFICATION)` | A message received when a friend logs in or out. |
| `[MESBOX](#MESBOX)` | Chat type for dialog with a graphic/object |
| `[MODAUTOTYPER](#MODAUTOTYPER)` | An autotyper message from a mod. |
| `[MODCHAT](#MODCHAT)` | A message in the public chat from a moderator |
| `[MODPRIVATECHAT](#MODPRIVATECHAT)` | A private message received from a moderator. |
| `[NPC\_EXAMINE](#NPC_EXAMINE)` | Examine NPC description. |
| `[NPC\_SAY](#NPC_SAY)` | Chat type for some npcs overhead text |
| `[OBJECT\_EXAMINE](#OBJECT_EXAMINE)` | Examine object description. |
| `[PLAYERRELATED](#PLAYERRELATED)` | A message that is relating to the player. |
| `[PRIVATECHAT](#PRIVATECHAT)` | A private message from another player. |
| `[PRIVATECHATOUT](#PRIVATECHATOUT)` | A private message sent to another player. |
| `[PUBLICCHAT](#PUBLICCHAT)` | A message in the public chat. |
| `[SNAPSHOTFEEDBACK](#SNAPSHOTFEEDBACK)` | An abuse report submitted. |
| `[SPAM](#SPAM)` | A message that was filtered. |
| `[TENSECTIMEOUT](#TENSECTIMEOUT)` | A message that times out after 10 seconds. |
| `[TRADE](#TRADE)` | A message received when completing a trade or a duel |
| `[TRADE\_SENT](#TRADE_SENT)` | A trade request being sent. |
| `[TRADEREQ](#TRADEREQ)` | A message received when somebody sends a trade offer. |
| `[UNKNOWN](#UNKNOWN)` | An unknown message type. |
| `[WELCOME](#WELCOME)` | The "Welcome to RuneScape" message |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `int` | `[getType](#getType())()` | |
| `static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api")` | `[of](#of(int))​(int type)` | Utility method that maps the type value to its respective
[`ChatMessageType`](ChatMessageType.html "enum in net.runelite.api") value. |
| `static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api")` | `[valueOf](#valueOf(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Returns the enum constant of this type with the specified name. |
| `static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api")[]` | `[values](#values())()` | Returns an array containing the constants of this enum type, in
the order they are declared. |

- ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#clone() "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#compareTo(E) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#finalize() "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#getDeclaringClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#hashCode() "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#name() "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#ordinal() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#toString() "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true#valueOf(java.lang.Class,java.lang.String) "class or interface in java.lang")`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Enum Constant Detail

- #### GAMEMESSAGE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") GAMEMESSAGE
```

A normal game message.
- #### MODCHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") MODCHAT
```

A message in the public chat from a moderator
- #### PUBLICCHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") PUBLICCHAT
```

A message in the public chat.
- #### PRIVATECHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") PRIVATECHAT
```

A private message from another player.
- #### ENGINE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") ENGINE
```

A message that the game engine sends.
- #### LOGINLOGOUTNOTIFICATION

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") LOGINLOGOUTNOTIFICATION
```

A message received when a friend logs in or out.
- #### PRIVATECHATOUT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") PRIVATECHATOUT
```

A private message sent to another player.
- #### MODPRIVATECHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") MODPRIVATECHAT
```

A private message received from a moderator.
- #### FRIENDSCHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") FRIENDSCHAT
```

A message received in friends chat.
- #### FRIENDSCHATNOTIFICATION

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") FRIENDSCHATNOTIFICATION
```

A message received with information about the current friends chat.
- #### TRADE\_SENT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") TRADE_SENT
```

A trade request being sent.
- #### BROADCAST

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") BROADCAST
```

A game broadcast.
- #### SNAPSHOTFEEDBACK

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") SNAPSHOTFEEDBACK
```

An abuse report submitted.
- #### ITEM\_EXAMINE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") ITEM_EXAMINE
```

Examine item description.
- #### NPC\_EXAMINE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") NPC_EXAMINE
```

Examine NPC description.
- #### OBJECT\_EXAMINE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") OBJECT_EXAMINE
```

Examine object description.
- #### FRIENDNOTIFICATION

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") FRIENDNOTIFICATION
```

Adding player to friend list.
- #### IGNORENOTIFICATION

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") IGNORENOTIFICATION
```

Adding player to ignore list.
- #### CLAN\_CHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_CHAT
```

A chat message in a clan chat.
- #### CLAN\_MESSAGE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_MESSAGE
```

A system message in a clan chat.
- #### CLAN\_GUEST\_CHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GUEST_CHAT
```

A chat message in the guest clan chat.
- #### CLAN\_GUEST\_MESSAGE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GUEST_MESSAGE
```

A system message in the guest clan chat.
- #### AUTOTYPER

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") AUTOTYPER
```

An autotyper message from a player.
- #### MODAUTOTYPER

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") MODAUTOTYPER
```

An autotyper message from a mod.
- #### CONSOLE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CONSOLE
```

A game message. (ie. when a setting is changed)
- #### TRADEREQ

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") TRADEREQ
```

A message received when somebody sends a trade offer.
- #### TRADE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") TRADE
```

A message received when completing a trade or a duel
- #### CHALREQ\_TRADE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CHALREQ_TRADE
```

A message received when somebody sends a duel offer.
- #### CHALREQ\_FRIENDSCHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CHALREQ_FRIENDSCHAT
```

A message received when someone sends a friends chat challenge offer.
- #### SPAM

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") SPAM
```

A message that was filtered.
- #### PLAYERRELATED

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") PLAYERRELATED
```

A message that is relating to the player.
- #### TENSECTIMEOUT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") TENSECTIMEOUT
```

A message that times out after 10 seconds.
- #### WELCOME

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") WELCOME
```

The "Welcome to RuneScape" message
- #### CLAN\_CREATION\_INVITATION

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_CREATION_INVITATION
```

Clan creation invitation.
- #### CHALREQ\_CLANCHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CHALREQ_CLANCHAT
```

Challenge offer for the clan tab
- #### CLAN\_GIM\_FORM\_GROUP

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GIM_FORM_GROUP
```
- #### CLAN\_GIM\_GROUP\_WITH

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GIM_GROUP_WITH
```
- #### CLAN\_GIM\_CHAT

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GIM_CHAT
```
- #### CLAN\_GIM\_MESSAGE

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") CLAN_GIM_MESSAGE
```
- #### DIALOG

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") DIALOG
```

Chat type for npc and player dialog
- #### MESBOX

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") MESBOX
```

Chat type for dialog with a graphic/object
- #### NPC\_SAY

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") NPC_SAY
```

Chat type for some npcs overhead text
- #### DIDYOUKNOW

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") DIDYOUKNOW
```

Did you know?-es
- #### UNKNOWN

```
public static final [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") UNKNOWN
```

An unknown message type.

+ ### Method Detail

- #### values

```
public static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api")[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```

for (ChatMessageType c : ChatMessageType.values())
System.out.println(c);

```

Returns:
an array containing the constants of this enum type, in the order they are declared
- #### valueOf

```
public static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") valueOf​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
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
- #### of

```
public static [ChatMessageType](ChatMessageType.html "enum in net.runelite.api") of​(int type)
```

Utility method that maps the type value to its respective
[`ChatMessageType`](ChatMessageType.html "enum in net.runelite.api") value.

Parameters:
`type` - the raw type
Returns:
appropriate message type, or [`UNKNOWN`](#UNKNOWN)
- #### getType

```
public int getType()
```