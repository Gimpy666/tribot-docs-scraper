# CameraFocusableEntity (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/CameraFocusableEntity.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[Actor](Actor.html "interface in net.runelite.api")`, `[NPC](NPC.html "interface in net.runelite.api")`, `[Player](Player.html "interface in net.runelite.api")`, `[WorldEntity](WorldEntity.html "interface in net.runelite.api")`

---

```
public interface CameraFocusableEntity
```

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getCameraFocus](#getCameraFocus())()` | |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView())()` | |

* + ### Method Detail

- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView()
```
- #### getCameraFocus

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getCameraFocus()
```