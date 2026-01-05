# Nameable (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Nameable.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Nameable](Nameable.html "interface in net.runelite.api")>`

All Known Subinterfaces:
`[ChatPlayer](ChatPlayer.html "interface in net.runelite.api")`, `[ClanChannelMember](clan/ClanChannelMember.html "interface in net.runelite.api.clan")`, `[Friend](Friend.html "interface in net.runelite.api")`, `[FriendsChatMember](FriendsChatMember.html "interface in net.runelite.api")`, `[Ignore](Ignore.html "interface in net.runelite.api")`

---

```
public interface Nameable
extends [Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Nameable](Nameable.html "interface in net.runelite.api")>
```

Represents a chat entity that has a name.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The name of the player. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getPrevName](#getPrevName())()` | The previous name the player had. |

- ### Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")

`[compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true#compareTo(T) "class or interface in java.lang")`

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The name of the player.

Returns:
the name
- #### getPrevName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getPrevName()
```

The previous name the player had.

Returns:
the previous name