# ChatPlayer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ChatPlayer.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Nameable](Nameable.html "interface in net.runelite.api")>`, `[Nameable](Nameable.html "interface in net.runelite.api")`

All Known Subinterfaces:
`[ClanChannelMember](clan/ClanChannelMember.html "interface in net.runelite.api.clan")`, `[Friend](Friend.html "interface in net.runelite.api")`, `[FriendsChatMember](FriendsChatMember.html "interface in net.runelite.api")`

---

```
public interface ChatPlayer
extends [Nameable](Nameable.html "interface in net.runelite.api")
```

Represents a player in the chat.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getWorld](#getWorld())()` | |

- ### Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")

`[compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true#compareTo(T) "class or interface in java.lang")`
- ### Methods inherited from interface net.runelite.api.[Nameable](Nameable.html "interface in net.runelite.api")

`[getName](Nameable.html#getName()), [getPrevName](Nameable.html#getPrevName())`

* + ### Method Detail

- #### getWorld

```
int getWorld()
```