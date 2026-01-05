# ClanMember (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/clan/ClanMember.html

**Package:** Packagenet.runelite.api.clan

---

* ---

```
public interface ClanMember
```

A member of a clan.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[LocalDate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/LocalDate.html?is-external=true "class or interface in java.time")` | `[getJoinDate](#getJoinDate())()` | The clan member's join date |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The clan member's name |
| `[ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[getRank](#getRank())()` | The clan member's rank |

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The clan member's name
- #### getRank

```
[ClanRank](ClanRank.html "class in net.runelite.api.clan") getRank()
```

The clan member's rank
- #### getJoinDate

```
[LocalDate](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/LocalDate.html?is-external=true "class or interface in java.time") getJoinDate()
```

The clan member's join date