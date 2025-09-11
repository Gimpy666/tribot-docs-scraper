# MouseSplinePaint (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/MouseSplinePaint.html

**Package:** Packageorg.tribot.script.sdk.painting

---

* ---

```
public interface MouseSplinePaint
```

An interface for painting the "mouse spline" (the traversed mouse path)

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[paintMouseSpline](#paintMouseSpline(java.awt.Graphics,java.util.List))​(java.awt.Graphics g,
java.util.List<java.awt.Point> points)` | Paints the mouse spline |

* + ### Method Detail

- #### paintMouseSpline

```
void paintMouseSpline​(java.awt.Graphics g,
java.util.List<java.awt.Point> points)
```

Paints the mouse spline

Parameters:
`g` - the graphics object to use for painting
`points` - the recently traversed mouse points