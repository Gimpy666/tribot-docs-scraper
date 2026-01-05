# PendingLogin (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/PendingLogin.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface PendingLogin
```

A pending friend login/out. This is used to suppress world hop notifications
by buffering the pending logins to try to match a pending logout with a pending
login and cancel both.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The name of the player |
| `short` | `[getWorld](#getWorld())()` | The world the player logged into, or 0 if a logout. |

* + ### Method Detail

- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The name of the player

Returns:
- #### getWorld

```
short getWorld()
```

The world the player logged into, or 0 if a logout.

Returns: