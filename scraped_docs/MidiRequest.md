# MidiRequest (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/MidiRequest.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface MidiRequest
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getArchiveId](#getArchiveId())()` | Currently playing track/jingle id |
| `boolean` | `[isJingle](#isJingle())()` | True if this midi request is a jingle, otherwise it is a track. |

* + ### Method Detail

- #### isJingle

```
boolean isJingle()
```

True if this midi request is a jingle, otherwise it is a track.

Returns:
- #### getArchiveId

```
int getArchiveId()
```

Currently playing track/jingle id

Returns: