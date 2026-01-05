# OAuthApi (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/com/jagex/oldscape/pub/OAuthApi.html

**Package:** Packagecom.jagex.oldscape.pub

---

* All Known Subinterfaces:
`[Client](../../../../net/runelite/api/Client.html "interface in net.runelite.api")`

---

```
public interface OAuthApi
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `long` | `[getAccountHash](#getAccountHash())()` | Gets a unique per-RuneScape-Account identifier or `-1` if the client has not logged in yet |

* + ### Method Detail

- #### getAccountHash

```
long getAccountHash()
```

Gets a unique per-RuneScape-Account identifier or `-1` if the client has not logged in yet