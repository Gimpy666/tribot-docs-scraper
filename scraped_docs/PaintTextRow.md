# PaintTextRow (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/template/basic/PaintTextRow.html

**Package:** Packageorg.tribot.script.sdk.painting.template.basic

---

* java.lang.Object
* + org.tribot.script.sdk.painting.template.basic.PaintTextRow

* All Implemented Interfaces:
`[PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic")`

---

```
public final class PaintTextRow
extends java.lang.Object
implements [PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic")
```

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[PaintTextRow.PaintTextRowBuilder](PaintTextRow.PaintTextRowBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [PaintTextRow.PaintTextRowBuilder](PaintTextRow.PaintTextRowBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[builder](#builder())()` | |
| `java.awt.Rectangle` | `[paint](#paint(java.awt.Graphics,java.awt.Point,boolean,boolean))​(java.awt.Graphics g,
java.awt.Point base,
boolean topToBottom,
boolean leftToRight)` | Paints the row |
| `[PaintTextRow.PaintTextRowBuilder](PaintTextRow.PaintTextRowBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[toBuilder](#toBuilder())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### paint

```
public java.awt.Rectangle paint​(java.awt.Graphics g,
java.awt.Point base,
boolean topToBottom,
boolean leftToRight)
```

Description copied from interface: `[PaintRow](PaintRow.html#paint(java.awt.Graphics,java.awt.Point,boolean,boolean))`
Paints the row

Specified by:
`[paint](PaintRow.html#paint(java.awt.Graphics,java.awt.Point,boolean,boolean))` in interface `[PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic")`
Parameters:
`g` - the graphics object to paint
`base` - the base position of this row
`topToBottom` - true if the base position is the top, false if its the bottom
`leftToRight` - true if the base position is the left side, false if its the right
Returns:
the rectangle area that encompasses the area this row painted
- #### builder

```
public static [PaintTextRow.PaintTextRowBuilder](PaintTextRow.PaintTextRowBuilder.html "class in org.tribot.script.sdk.painting.template.basic") builder()
```
- #### toBuilder

```
public [PaintTextRow.PaintTextRowBuilder](PaintTextRow.PaintTextRowBuilder.html "class in org.tribot.script.sdk.painting.template.basic") toBuilder()
```