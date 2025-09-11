# BasicPaintTemplate.BasicPaintTemplateBuilder (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/template/basic/BasicPaintTemplate.BasicPaintTemplateBuilder.html

**Package:** Packageorg.tribot.script.sdk.painting.template.basic

---

* java.lang.Object
* + org.tribot.script.sdk.painting.template.basic.BasicPaintTemplate.BasicPaintTemplateBuilder

* Enclosing class:
[BasicPaintTemplate](BasicPaintTemplate.html "class in org.tribot.script.sdk.painting.template.basic")

---

```
public static class BasicPaintTemplate.BasicPaintTemplateBuilder
extends java.lang.Object
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[BasicPaintTemplate](BasicPaintTemplate.html "class in org.tribot.script.sdk.painting.template.basic")` | `[build](#build())()` | |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[clearRows](#clearRows())()` | |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[drawOrigin](#drawOrigin(java.util.function.Supplier))​(java.util.function.Supplier<java.awt.Point> drawOrigin)` | The origin position for this paint frame |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[leftToRight](#leftToRight(boolean))​(boolean leftToRight)` | True if the [`BasicPaintTemplate.drawOrigin`](BasicPaintTemplate.html#drawOrigin) x coordinate should be considered the left side,
false if it should be the right side. |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[location](#location(org.tribot.script.sdk.painting.template.basic.PaintLocation))​([PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") location)` | |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[row](#row(org.tribot.script.sdk.painting.template.basic.PaintRow))​([PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic") row)` | |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[rows](#rows(java.util.Collection))​(java.util.Collection<? extends [PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic")> rows)` | |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[rowSpacing](#rowSpacing(int))​(int rowSpacing)` | The amount of space between each row, in pixels |
| `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[topToBottom](#topToBottom(boolean))​(boolean topToBottom)` | True if the [`BasicPaintTemplate.drawOrigin`](BasicPaintTemplate.html#drawOrigin) y coordinate should be considered the top side,
false if it should be the bottom side. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

- #### location

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") location​([PaintLocation](PaintLocation.html "enum in org.tribot.script.sdk.painting.template.basic") location)
```
- #### row

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") row​([PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic") row)
```
- #### rows

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") rows​(java.util.Collection<? extends [PaintRow](PaintRow.html "interface in org.tribot.script.sdk.painting.template.basic")> rows)
```
- #### clearRows

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") clearRows()
```
- #### drawOrigin

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") drawOrigin​(java.util.function.Supplier<java.awt.Point> drawOrigin)
```

The origin position for this paint frame

Returns:
`this`.
See Also:
[`BasicPaintTemplate.leftToRight`](BasicPaintTemplate.html#leftToRight),
[`BasicPaintTemplate.topToBottom`](BasicPaintTemplate.html#topToBottom)
- #### rowSpacing

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") rowSpacing​(int rowSpacing)
```

The amount of space between each row, in pixels

Returns:
`this`.
- #### leftToRight

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") leftToRight​(boolean leftToRight)
```

True if the [`BasicPaintTemplate.drawOrigin`](BasicPaintTemplate.html#drawOrigin) x coordinate should be considered the left side,
false if it should be the right side.

Returns:
`this`.
- #### topToBottom

```
public [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") topToBottom​(boolean topToBottom)
```

True if the [`BasicPaintTemplate.drawOrigin`](BasicPaintTemplate.html#drawOrigin) y coordinate should be considered the top side,
false if it should be the bottom side.

Returns:
`this`.
- #### build

```
public [BasicPaintTemplate](BasicPaintTemplate.html "class in org.tribot.script.sdk.painting.template.basic") build()
```
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`