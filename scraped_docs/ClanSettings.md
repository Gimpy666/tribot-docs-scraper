# ClanSettings (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/clan/ClanSettings.html

**Package:** Packagenet.runelite.api.clan

---

* ---

```
public interface ClanSettings
```

A clan's settings.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[ClanMember](ClanMember.html "interface in net.runelite.api.clan")` | `[findMember](#findMember(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Find a member of the clan. |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[ClanMember](ClanMember.html "interface in net.runelite.api.clan")>` | `[getMembers](#getMembers())()` | The members of the clan. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The clan name |
| `[ClanTitle](ClanTitle.html "class in net.runelite.api.clan")` | `[titleForRank](#titleForRank(net.runelite.api.clan.ClanRank))​([ClanRank](ClanRank.html "class in net.runelite.api.clan") clanRank)` | Get the clan title for a clan rank. |

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The clan name

Returns:
- #### getMembers

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[ClanMember](ClanMember.html "interface in net.runelite.api.clan")> getMembers()
```

The members of the clan. This includes all members, whether online or offline.

Returns:
- #### findMember

```
@Nullable
[ClanMember](ClanMember.html "interface in net.runelite.api.clan") findMember​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Find a member of the clan.

Parameters:
`name` -
Returns:
- #### titleForRank

```
@Nullable
[ClanTitle](ClanTitle.html "class in net.runelite.api.clan") titleForRank​([ClanRank](ClanRank.html "class in net.runelite.api.clan") clanRank)
```

Get the clan title for a clan rank.

Parameters:
`clanRank` - the rank
Returns:
See Also:
[`ClanRank`](ClanRank.html "class in net.runelite.api.clan")