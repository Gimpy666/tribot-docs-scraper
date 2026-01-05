# ClanChannelMember (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/clan/ClanChannelMember.html

**Package:** Packagenet.runelite.api.clan

---

* All Superinterfaces:
`[ChatPlayer](../ChatPlayer.html "interface in net.runelite.api")`, `[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[Nameable](../Nameable.html "interface in net.runelite.api")>`, `[Nameable](../Nameable.html "interface in net.runelite.api")`

---

```
public interface ClanChannelMember
extends [ChatPlayer](../ChatPlayer.html "interface in net.runelite.api")
```

A member of a clan channel

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The member name |
| `[ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[getRank](#getRank())()` | The member's rank relative to the other members. |
| `int` | `[getWorld](#getWorld())()` | The world the member is on |

- ### Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true "class or interface in java.lang")

`[compareTo](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html?is-external=true#compareTo(T) "class or interface in java.lang")`
- ### Methods inherited from interface net.runelite.api.[Nameable](../Nameable.html "interface in net.runelite.api")

`[getPrevName](../Nameable.html#getPrevName())`

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The member name

Specified by:
`[getName](../Nameable.html#getName())` in interface `[Nameable](../Nameable.html "interface in net.runelite.api")`
Returns:
- #### getRank

```
[ClanRank](ClanRank.html "class in net.runelite.api.clan") getRank()
```

The member's rank relative to the other members. To get the member title,
see ClanSettings.

Returns:
See Also:
[`ClanRank`](ClanRank.html "class in net.runelite.api.clan"),
[`ClanSettings.titleForRank(ClanRank)`](ClanSettings.html#titleForRank(net.runelite.api.clan.ClanRank))
- #### getWorld

```
int getWorld()
```

The world the member is on

Specified by:
`[getWorld](../ChatPlayer.html#getWorld())` in interface `[ChatPlayer](../ChatPlayer.html "interface in net.runelite.api")`
Returns: