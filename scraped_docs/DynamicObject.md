# DynamicObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/DynamicObject.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

---

```
public interface DynamicObject
extends [Renderable](Renderable.html "interface in net.runelite.api")
```

An animated object

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `[Animation](Animation.html "interface in net.runelite.api")` | `[getAnimation](#getAnimation())()` | Get the animation applied to the object |
| `int` | `[getAnimCycle](#getAnimCycle())()` | Get the frame cycle. |
| `int` | `[getAnimFrame](#getAnimFrame())()` | Get the frame of the current animation |
| `[Model](Model.html "interface in net.runelite.api")` | `[getModelZbuf](#getModelZbuf())()` | Like [`Renderable.getModel()`](Renderable.html#getModel()) but is threadsafe and doesn't support animations. |
| `[ObjectComposition](ObjectComposition.html "interface in net.runelite.api")` | `[getRecordedObjectComposition](#getRecordedObjectComposition())()` | The object composition for the model returned by [`getModelZbuf()`](#getModelZbuf()) |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset()), [getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getAnimation

```
[Animation](Animation.html "interface in net.runelite.api") getAnimation()
```

Get the animation applied to the object

Returns:
- #### getAnimFrame

```
int getAnimFrame()
```

Get the frame of the current animation

Returns:
- #### getAnimCycle

```
int getAnimCycle()
```

Get the frame cycle. The number of ticks the client has been on this frame.

Returns:
- #### getModelZbuf

```
[Model](Model.html "interface in net.runelite.api") getModelZbuf()
```

Like [`Renderable.getModel()`](Renderable.html#getModel()) but is threadsafe and doesn't support animations.

Returns:
- #### getRecordedObjectComposition

```
[ObjectComposition](ObjectComposition.html "interface in net.runelite.api") getRecordedObjectComposition()
```

The object composition for the model returned by [`getModelZbuf()`](#getModelZbuf())

Returns: