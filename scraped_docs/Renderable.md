# Renderable (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Renderable.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

All Known Subinterfaces:
`[Actor](Actor.html "interface in net.runelite.api")`, `[DynamicObject](DynamicObject.html "interface in net.runelite.api")`, `[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")`, `[Model](Model.html "interface in net.runelite.api")`, `[ModelData](ModelData.html "interface in net.runelite.api")`, `[NPC](NPC.html "interface in net.runelite.api")`, `[Player](Player.html "interface in net.runelite.api")`, `[Projectile](Projectile.html "interface in net.runelite.api")`, `[Scene](Scene.html "interface in net.runelite.api")`, `[TileItem](TileItem.html "interface in net.runelite.api")`

---

```
public interface Renderable
extends [Node](Node.html "interface in net.runelite.api")
```

Represents an object that can be rendered.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getAnimationHeightOffset](#getAnimationHeightOffset())()` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[getModel](#getModel())()` | Gets the model of the object. |
| `int` | `[getModelHeight](#getModelHeight())()` | Gets the height of the model. |
| `void` | `[setModelHeight](#setModelHeight(int))​(int modelHeight)` | |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getModel

```
[Model](Model.html "interface in net.runelite.api") getModel()
```

Gets the model of the object.
- #### getModelHeight

```
int getModelHeight()
```

Gets the height of the model.
- #### setModelHeight

```
void setModelHeight​(int modelHeight)
```
- #### getAnimationHeightOffset

```
int getAnimationHeightOffset()
```