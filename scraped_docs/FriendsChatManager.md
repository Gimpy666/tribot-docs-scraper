# FriendsChatManager (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/FriendsChatManager.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[NameableContainer](NameableContainer.html "interface in net.runelite.api")<[FriendsChatMember](FriendsChatMember.html "interface in net.runelite.api")>`

---

```
public interface FriendsChatManager
extends [NameableContainer](NameableContainer.html "interface in net.runelite.api")<[FriendsChatMember](FriendsChatMember.html "interface in net.runelite.api")>
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")` | `[getKickRank](#getKickRank())()` | Get the rank required to kick members from the friends chat |
| `[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")` | `[getMyRank](#getMyRank())()` | Get the local player's rank in the friend chat |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the currently joined friends chat |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getOwner](#getOwner())()` | Gets the owner of the currently joined friends chat |

- ### Methods inherited from interface net.runelite.api.[NameableContainer](NameableContainer.html "interface in net.runelite.api")

`[findByName](NameableContainer.html#findByName(java.lang.String)), [getCount](NameableContainer.html#getCount()), [getMembers](NameableContainer.html#getMembers()), [getSize](NameableContainer.html#getSize())`

* + ### Method Detail

- #### getOwner

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getOwner()
```

Gets the owner of the currently joined friends chat

Returns:
- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the currently joined friends chat

Returns:
- #### getMyRank

```
[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") getMyRank()
```

Get the local player's rank in the friend chat

Returns:
- #### getKickRank

```
[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") getKickRank()
```

Get the rank required to kick members from the friends chat

Returns: