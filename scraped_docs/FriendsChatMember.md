# FriendsChatMember (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/FriendsChatMember.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[ChatPlayer](ChatPlayer.html "interface in net.runelite.api")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Nameable](Nameable.html "interface in net.runelite.api")>`, `[Nameable](Nameable.html "interface in net.runelite.api")`

---

```
public interface FriendsChatMember
extends [ChatPlayer](ChatPlayer.html "interface in net.runelite.api")
```

Represents a friends chat member.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api")` | `[getRank](#getRank())()` | Gets the rank of the friends chat member. |
| `int` | `[getWorld](#getWorld())()` | Gets the world the member is in. |

- ### Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")

`[compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true#compareTo(T) "class or interface in java.lang")`
- ### Methods inherited from interface net.runelite.api.[Nameable](Nameable.html "interface in net.runelite.api")

`[getName](Nameable.html#getName()), [getPrevName](Nameable.html#getPrevName())`

* + ### Method Detail

- #### getWorld

```
int getWorld()
```

Gets the world the member is in.

Specified by:
`[getWorld](ChatPlayer.html#getWorld())` in interface `[ChatPlayer](ChatPlayer.html "interface in net.runelite.api")`
Returns:
the world
- #### getRank

```
[FriendsChatRank](FriendsChatRank.html "enum in net.runelite.api") getRank()
```

Gets the rank of the friends chat member.

Returns:
the rank