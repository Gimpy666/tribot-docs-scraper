# BasicPaintTemplate (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/painting/template/basic/BasicPaintTemplate.html

**Package:** Packageorg.tribot.script.sdk.painting.template.basic

---

* java.lang.Object
* + org.tribot.script.sdk.painting.template.basic.BasicPaintTemplate

* All Implemented Interfaces:
`[PaintComponent](../../PaintComponent.html "interface in org.tribot.script.sdk.painting")`

---

```
public final class BasicPaintTemplate
extends java.lang.Object
implements [PaintComponent](../../PaintComponent.html "interface in org.tribot.script.sdk.painting")
```

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic")` | `[builder](#builder())()` | |
| `void` | `[render](#render(java.awt.Graphics))​(java.awt.Graphics g)` | Paints this paint frame |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

- #### render

```
public void render​(java.awt.Graphics g)
```

Paints this paint frame

Specified by:
`[render](../../PaintComponent.html#render(java.awt.Graphics))` in interface `[PaintComponent](../../PaintComponent.html "interface in org.tribot.script.sdk.painting")`
Parameters:
`g` - the graphics object
- #### builder

```
public static [BasicPaintTemplate.BasicPaintTemplateBuilder](BasicPaintTemplate.BasicPaintTemplateBuilder.html "class in org.tribot.script.sdk.painting.template.basic") builder()
```