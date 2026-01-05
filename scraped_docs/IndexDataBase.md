# IndexDataBase (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IndexDataBase.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface IndexDataBase
```

Represents an index in the cache

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int[]` | `[getFileIds](#getFileIds(int))​(int archiveId)` | Get the child file ids for a given archive |
| `boolean` | `[isOverlayOutdated](#isOverlayOutdated())()` | Returns true if any cache overlay in this index is outdated due to hash mismatch |
| `byte[]` | `[loadData](#loadData(int,int))​(int archiveID,
int fileID)` | |

* + ### Method Detail

- #### isOverlayOutdated

```
boolean isOverlayOutdated()
```

Returns true if any cache overlay in this index is outdated due to hash mismatch
- #### getFileIds

```
int[] getFileIds​(int archiveId)
```

Get the child file ids for a given archive

Parameters:
`archiveId` -
Returns:
- #### loadData

```
byte[] loadData​(int archiveID,
int fileID)
```