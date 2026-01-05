# ClanMemberJoined (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/ClanMemberJoined.html

**Package:** Packagenet.runelite.api.events

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.ClanMemberJoined

* ---

```
public final class ClanMemberJoined
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event when a clan member joins a clan channel.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ClanMemberJoined](#%3Cinit%3E(net.runelite.api.clan.ClanChannel,net.runelite.api.clan.ClanChannelMember))​([ClanChannel](../clan/ClanChannel.html "interface in net.runelite.api.clan") clanChannel,
[ClanChannelMember](../clan/ClanChannelMember.html "interface in net.runelite.api.clan") clanMember)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `[ClanChannel](../clan/ClanChannel.html "interface in net.runelite.api.clan")` | `[getClanChannel](#getClanChannel())()` | |
| `[ClanChannelMember](../clan/ClanChannelMember.html "interface in net.runelite.api.clan")` | `[getClanMember](#getClanMember())()` | |
| `int` | `[hashCode](#hashCode())()` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### ClanMemberJoined

```
public ClanMemberJoined​([ClanChannel](../clan/ClanChannel.html "interface in net.runelite.api.clan") clanChannel,
[ClanChannelMember](../clan/ClanChannelMember.html "interface in net.runelite.api.clan") clanMember)
```

+ ### Method Detail

- #### getClanChannel

```
public [ClanChannel](../clan/ClanChannel.html "interface in net.runelite.api.clan") getClanChannel()
```
- #### getClanMember

```
public [ClanChannelMember](../clan/ClanChannelMember.html "interface in net.runelite.api.clan") getClanMember()
```
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`