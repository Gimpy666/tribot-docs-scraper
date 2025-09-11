# PreBreakStartListener (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/interfaces/PreBreakStartListener.html

**Package:** Packageorg.tribot.script.sdk.interfaces

---

* ---

```
public interface PreBreakStartListener
```

Represents a listener for tribot break starts

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[onBreakStart](#onBreakStart(long))​(long msLength)` | Called when a break is started |

* + ### Method Detail

- #### onBreakStart

```
void onBreakStart​(long msLength)
```

Called when a break is started

Parameters:
`msLength` - the length of the break in milliseconds