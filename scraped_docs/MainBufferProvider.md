# MainBufferProvider (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/MainBufferProvider.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[BufferProvider](BufferProvider.html "interface in net.runelite.api")`

---

```
public interface MainBufferProvider
extends [BufferProvider](BufferProvider.html "interface in net.runelite.api")
```

Represents the clients primary image buffer.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Image](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Image.html?is-external=true "class or interface in java.awt")` | `[getImage](#getImage())()` | Gets the image currently loaded in the buffer. |

- ### Methods inherited from interface net.runelite.api.[BufferProvider](BufferProvider.html "interface in net.runelite.api")

`[getHeight](BufferProvider.html#getHeight()), [getPixels](BufferProvider.html#getPixels()), [getWidth](BufferProvider.html#getWidth())`

* + ### Method Detail

- #### getImage

```
[Image](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Image.html?is-external=true "class or interface in java.awt") getImage()
```

Gets the image currently loaded in the buffer.

Returns:
the loaded image