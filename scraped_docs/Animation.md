# Animation (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Animation.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface Animation
```

Represents an animation of a renderable

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getDuration](#getDuration())()` | How many frames the animation lasts |
| `int[]` | `[getFrameLengths](#getFrameLengths())()` | How many ticks each frame is. |
| `int` | `[getFrameStep](#getFrameStep())()` | How many frames to go back when looping |
| `int` | `[getId](#getId())()` | Get the id for this animation |
| `int` | `[getNumFrames](#getNumFrames())()` | Get how many distinct frames this animation has. |
| `int` | `[getRestartMode](#getRestartMode())()` | How this animation behaves when its restarted during playback |
| `boolean` | `[isMayaAnim](#isMayaAnim())()` | Is this animation a newer-style "maya" animation |
| `void` | `[setRestartMode](#setRestartMode(int))​(int restartMode)` | |

* + ### Method Detail

- #### getId

```
int getId()
```

Get the id for this animation

Returns:
See Also:
`AnimationID`
- #### isMayaAnim

```
boolean isMayaAnim()
```

Is this animation a newer-style "maya" animation
- #### getNumFrames

```
int getNumFrames()
```

Get how many distinct frames this animation has.

For animaya animations, this is the duration in client ticks. For classic
animations, this is how many keyframes it has, not it's duration in ticks.
- #### getRestartMode

```
int getRestartMode()
```

How this animation behaves when its restarted during playback
- #### setRestartMode

```
void setRestartMode​(int restartMode)
```

See Also:
[`getRestartMode()`](#getRestartMode())
- #### getDuration

```
int getDuration()
```

How many frames the animation lasts
- #### getFrameStep

```
int getFrameStep()
```

How many frames to go back when looping
- #### getFrameLengths

```
int[] getFrameLengths()
```

How many ticks each frame is.

`null` for [`isMayaAnim()`](#isMayaAnim()) animations