# ClanRank (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/clan/ClanRank.html

**Package:** Packagenet.runelite.api.clan

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.clan.ClanRank

* ---

```
public final class ClanRank
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

A rank in a clan. The [`getRank()`](#getRank()) value is -1 to 127 representing the rank.
Some constants are defined for named ranks, but most ranks have configurable titles which must be
fetched via [`ClanSettings.titleForRank(ClanRank)`](ClanSettings.html#titleForRank(net.runelite.api.clan.ClanRank))

See Also:
[`JMOD`](#JMOD),
[`OWNER`](#OWNER),
[`DEPUTY_OWNER`](#DEPUTY_OWNER),
[`ADMINISTRATOR`](#ADMINISTRATOR),
[`GUEST`](#GUEST)

* + ### Field Summary

Fields | Modifier and Type | Field | Description |
| `static [ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[ADMINISTRATOR](#ADMINISTRATOR)` | |
| `static [ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[DEPUTY\_OWNER](#DEPUTY_OWNER)` | |
| `static [ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[GUEST](#GUEST)` | |
| `static [ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[JMOD](#JMOD)` | |
| `static [ClanRank](ClanRank.html "class in net.runelite.api.clan")` | `[OWNER](#OWNER)` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[ClanRank](#%3Cinit%3E(int))​(int rank)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `int` | `[getRank](#getRank())()` | The rank, -1 to 127. |
| `int` | `[hashCode](#hashCode())()` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Field Detail

- #### JMOD

```
public static final [ClanRank](ClanRank.html "class in net.runelite.api.clan") JMOD
```
- #### OWNER

```
public static final [ClanRank](ClanRank.html "class in net.runelite.api.clan") OWNER
```
- #### DEPUTY\_OWNER

```
public static final [ClanRank](ClanRank.html "class in net.runelite.api.clan") DEPUTY_OWNER
```
- #### ADMINISTRATOR

```
public static final [ClanRank](ClanRank.html "class in net.runelite.api.clan") ADMINISTRATOR
```
- #### GUEST

```
public static final [ClanRank](ClanRank.html "class in net.runelite.api.clan") GUEST
```

+ ### Constructor Detail

- #### ClanRank

```
public ClanRank​(int rank)
```

+ ### Method Detail

- #### getRank

```
public int getRank()
```

The rank, -1 to 127.
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