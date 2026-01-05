# JavaScriptCallback (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/widgets/JavaScriptCallback.html

**Package:** Packagenet.runelite.api.widgets

---

* Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

```
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/FunctionalInterface.html?is-external=true "class or interface in java.lang")
public interface JavaScriptCallback
```

An object that can be set as the first argument to a [`Widget`](Widget.html "interface in net.runelite.api.widgets") listener
to handle ScriptEvents with Java code, rather than cs2.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `void` | `[run](#run(net.runelite.api.ScriptEvent))​([ScriptEvent](../ScriptEvent.html "interface in net.runelite.api") event)` | |

* + ### Method Detail

- #### run

```
void run​([ScriptEvent](../ScriptEvent.html "interface in net.runelite.api") event)
```