# ClanChannel (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/clan/ClanChannel.html

**Package:** Packagenet.runelite.api.clan

---

* ---

```
public interface ClanChannel
```

A clan channel.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[ClanChannelMember](ClanChannelMember.html "interface in net.runelite.api.clan")` | `[findMember](#findMember(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Find a clan member by name |
| `[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[ClanChannelMember](ClanChannelMember.html "interface in net.runelite.api.clan")>` | `[getMembers](#getMembers())()` | The members currently online in the channel. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The name of the channel |

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The name of the channel

Returns:
- #### getMembers

```
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html?is-external=true "class or interface in java.util")<[ClanChannelMember](ClanChannelMember.html "interface in net.runelite.api.clan")> getMembers()
```

The members currently online in the channel.

Returns:
- #### findMember

```
@Nullable
[ClanChannelMember](ClanChannelMember.html "interface in net.runelite.api.clan") findMember​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Find a clan member by name

Parameters:
`name` -
Returns: