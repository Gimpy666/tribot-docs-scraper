# GameEngine (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/GameEngine.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[Client](Client.html "interface in net.runelite.api")`

---

```
public interface GameEngine
```

Represents the client game engine.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Canvas](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Canvas.html?is-external=true "class or interface in java.awt")` | `[getCanvas](#getCanvas())()` | Gets the canvas that contains everything. |
| `[Thread](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Thread.html?is-external=true "class or interface in java.lang")` | `[getClientThread](#getClientThread())()` | Gets the client main thread. |
| `boolean` | `[isClientThread](#isClientThread())()` | Checks whether this code is executing on the client main thread. |
| `void` | `[resizeCanvas](#resizeCanvas())()` | |

* + ### Method Detail

- #### getCanvas

```
[Canvas](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Canvas.html?is-external=true "class or interface in java.awt") getCanvas()
```

Gets the canvas that contains everything.

Returns:
the game canvas
- #### getClientThread

```
[Thread](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Thread.html?is-external=true "class or interface in java.lang") getClientThread()
```

Gets the client main thread.

Returns:
the main thread
- #### isClientThread

```
boolean isClientThread()
```

Checks whether this code is executing on the client main thread.

Returns:
true if on the main thread, false otherwise
- #### resizeCanvas

```
void resizeCanvas()
```