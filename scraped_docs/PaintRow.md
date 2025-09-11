# PaintRow (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/template/basic/PaintRow.html

**Package:** Packageorg.tribot.script.sdk.painting.template.basic

---

* All Known Implementing Classes:
`[PaintTextRow](PaintTextRow.html "class in org.tribot.script.sdk.painting.template.basic")`

---

```
public interface PaintRow
```

Describes a paint row that can exist in a paint frame.

Note that for now this is experimental and the interface contract may change. It's not recommended creating custom paint rows \*yet\*.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `java.awt.Rectangle` | `[paint](#paint(java.awt.Graphics,java.awt.Point,boolean,boolean))​(java.awt.Graphics g,
java.awt.Point base,
boolean topToBottom,
boolean leftToRight)` | Paints the row |

* + ### Method Detail

- #### paint

```
java.awt.Rectangle paint​(java.awt.Graphics g,
java.awt.Point base,
boolean topToBottom,
boolean leftToRight)
```

Paints the row

Parameters:
`g` - the graphics object to paint
`base` - the base position of this row
`topToBottom` - true if the base position is the top, false if its the bottom
`leftToRight` - true if the base position is the left side, false if its the right
Returns:
the rectangle area that encompasses the area this row painted