# MousePaint (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/MousePaint.html

**Package:** Packageorg.tribot.script.sdk.painting

---

* ---

```
public interface MousePaint
```

An interface for displaying the mouse position

See Also:
[`Painting.setMousePaint(MousePaint)`](Painting.html#setMousePaint(org.tribot.script.sdk.painting.MousePaint))

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[paintMouse](#paintMouse(java.awt.Graphics,java.awt.Point,java.awt.Point))​(java.awt.Graphics g,
java.awt.Point mousePos,
java.awt.Point dragPos)` | Paints the mouse |

* + ### Method Detail

- #### paintMouse

```
void paintMouse​(java.awt.Graphics g,
java.awt.Point mousePos,
java.awt.Point dragPos)
```

Paints the mouse

Parameters:
`g` - the graphics object to use for painting
`mousePos` - the mouse position
`dragPos` - the drag position