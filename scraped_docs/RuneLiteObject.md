# RuneLiteObject (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/RuneLiteObject.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [net.runelite.api.RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")
+ - net.runelite.api.RuneLiteObject

* ---

```
public class RuneLiteObject
extends [RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[RuneLiteObject](#%3Cinit%3E(net.runelite.api.Client))​([Client](Client.html "interface in net.runelite.api") client)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `boolean` | `[finished](#finished())()` | Deprecated.
Use a custom [`AnimationController`](AnimationController.html "class in net.runelite.api") instead.
|
| `[Animation](Animation.html "interface in net.runelite.api")` | `[getAnimation](#getAnimation())()` | Deprecated.
Use [`getAnimationController()`](#getAnimationController()) or [`getPoseAnimationController()`](#getPoseAnimationController())
followed by [`AnimationController.getFrame()`](AnimationController.html#getFrame()).
|
| `[AnimationController](AnimationController.html "class in net.runelite.api")` | `[getAnimationController](#getAnimationController())()` | The animation of the RuneLiteObject. |
| `int` | `[getAnimationFrame](#getAnimationFrame())()` | Deprecated.
Use [`getAnimationController()`](#getAnimationController()) or [`getPoseAnimationController()`](#getPoseAnimationController())
followed by [`AnimationController.getFrame()`](AnimationController.html#getFrame()).
|
| `[Model](Model.html "interface in net.runelite.api")` | `[getBaseModel](#getBaseModel())()` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[getModel](#getModel())()` | Called every frame to get a model to render. |
| `[AnimationController](AnimationController.html "class in net.runelite.api")` | `[getPoseAnimationController](#getPoseAnimationController())()` | The optional pose animation of the RuneLiteObject. |
| `int` | `[getStartCycle](#getStartCycle())()` | |
| `boolean` | `[isActive](#isActive())()` | Gets the state of the RuneLiteObject |
| `void` | `[setActive](#setActive(boolean))​(boolean active)` | Sets the state of the RuneLiteObject. |
| `void` | `[setAnimation](#setAnimation(net.runelite.api.Animation))​([Animation](Animation.html "interface in net.runelite.api") animation)` | Sets the animation of the RuneLiteObject. |
| `void` | `[setAnimationController](#setAnimationController(net.runelite.api.AnimationController))​([AnimationController](AnimationController.html "class in net.runelite.api") animationController)` | Sets the animation controller of the RuneLiteObject. |
| `void` | `[setFinished](#setFinished(boolean))​(boolean finished)` | Deprecated.
Use a custom [`AnimationController`](AnimationController.html "class in net.runelite.api") instead
to despawn the object when it completes its animation.
|
| `void` | `[setLocation](#setLocation(net.runelite.api.coords.LocalPoint,int))​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int level)` | Sets the location in the scene for the RuneLiteObject |
| `void` | `[setModel](#setModel(net.runelite.api.Model))​([Model](Model.html "interface in net.runelite.api") baseModel)` | Sets the model to be rendered. |
| `void` | `[setPoseAnimationController](#setPoseAnimationController(net.runelite.api.AnimationController))​([AnimationController](AnimationController.html "class in net.runelite.api") poseAnimationController)` | The optional pose animation of the RuneLiteObject. |
| `void` | `[setShouldLoop](#setShouldLoop(boolean))​(boolean shouldLoop)` | Deprecated.
Use [`AnimationController.setOnFinished(Consumer)`](AnimationController.html#setOnFinished(java.util.function.Consumer)) with [`AnimationController.loop()`](AnimationController.html#loop()) instead.
|
| `void` | `[setStartCycle](#setStartCycle(int))​(int startCycle)` | |
| `void` | `[tick](#tick(int))​(int ticksSinceLastFrame)` | Called every frame the RuneLiteObject is registered and in the scene |

- ### Methods inherited from class net.runelite.api.[RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")

`[getLevel](RuneLiteObjectController.html#getLevel()), [getLocation](RuneLiteObjectController.html#getLocation()), [getOrientation](RuneLiteObjectController.html#getOrientation()), [getRadius](RuneLiteObjectController.html#getRadius()), [getWorldView](RuneLiteObjectController.html#getWorldView()), [getX](RuneLiteObjectController.html#getX()), [getY](RuneLiteObjectController.html#getY()), [getZ](RuneLiteObjectController.html#getZ()), [isDrawFrontTilesFirst](RuneLiteObjectController.html#isDrawFrontTilesFirst()), [setDrawFrontTilesFirst](RuneLiteObjectController.html#setDrawFrontTilesFirst(boolean)), [setLevel](RuneLiteObjectController.html#setLevel(int)), [setOrientation](RuneLiteObjectController.html#setOrientation(int)), [setRadius](RuneLiteObjectController.html#setRadius(int)), [setWorldView](RuneLiteObjectController.html#setWorldView(int)), [setX](RuneLiteObjectController.html#setX(int)), [setY](RuneLiteObjectController.html#setY(int)), [setZ](RuneLiteObjectController.html#setZ(int))`
- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### RuneLiteObject

```
public RuneLiteObject​([Client](Client.html "interface in net.runelite.api") client)
```

+ ### Method Detail

- #### setShouldLoop

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public void setShouldLoop​(boolean shouldLoop)
```

Deprecated.
Use [`AnimationController.setOnFinished(Consumer)`](AnimationController.html#setOnFinished(java.util.function.Consumer)) with [`AnimationController.loop()`](AnimationController.html#loop()) instead.

Sets whether the animation of the RuneLiteObject should loop when the animation ends.
If this is false the object will despawn when the animation ends.
Does nothing if the animation is null.
- #### setModel

```
public void setModel​([Model](Model.html "interface in net.runelite.api") baseModel)
```

Sets the model to be rendered.
If `animationController` is not null, this model will be passed to [`AnimationController.animate(Model)`](AnimationController.html#animate(net.runelite.api.Model)).
- #### setLocation

```
public void setLocation​([LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") point,
int level)
```

Sets the location in the scene for the RuneLiteObject

Overrides:
`[setLocation](RuneLiteObjectController.html#setLocation(net.runelite.api.coords.LocalPoint,int))` in class `[RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")`
- #### setAnimation

```
public void setAnimation​([Animation](Animation.html "interface in net.runelite.api") animation)
```

Sets the animation of the RuneLiteObject.
If animation is null, the model will be static.
- #### setAnimationController

```
public void setAnimationController​(@Nullable
[AnimationController](AnimationController.html "class in net.runelite.api") animationController)
```

Sets the animation controller of the RuneLiteObject.
If animationController is null, the model will be static.
- #### setActive

```
public void setActive​(boolean active)
```

Sets the state of the RuneLiteObject.
Set to true to spawn the object.
Set to false to despawn the object.
- #### isActive

```
public boolean isActive()
```

Gets the state of the RuneLiteObject

Returns:
true if the RuneLiteObject is added to the scene
- #### tick

```
public void tick​(int ticksSinceLastFrame)
```

Called every frame the RuneLiteObject is registered and in the scene

Overrides:
`[tick](RuneLiteObjectController.html#tick(int))` in class `[RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")`
Parameters:
`ticksSinceLastFrame` - The number of client ticks since the last frame
- #### getModel

```
public [Model](Model.html "interface in net.runelite.api") getModel()
```

Called every frame to get a model to render. The returned model is not modified and
can be a shared model.

Specified by:
`[getModel](RuneLiteObjectController.html#getModel())` in class `[RuneLiteObjectController](RuneLiteObjectController.html "class in net.runelite.api")`
- #### finished

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public boolean finished()
```

Deprecated.
Use a custom [`AnimationController`](AnimationController.html "class in net.runelite.api") instead.
- #### setFinished

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public void setFinished​(boolean finished)
```

Deprecated.
Use a custom [`AnimationController`](AnimationController.html "class in net.runelite.api") instead
to despawn the object when it completes its animation.
- #### getAnimation

```
public [Animation](Animation.html "interface in net.runelite.api") getAnimation()
```

Deprecated.
Use [`getAnimationController()`](#getAnimationController()) or [`getPoseAnimationController()`](#getPoseAnimationController())
followed by [`AnimationController.getFrame()`](AnimationController.html#getFrame()).
- #### getAnimationFrame

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
public int getAnimationFrame()
```

Deprecated.
Use [`getAnimationController()`](#getAnimationController()) or [`getPoseAnimationController()`](#getPoseAnimationController())
followed by [`AnimationController.getFrame()`](AnimationController.html#getFrame()).
- #### getBaseModel

```
public [Model](Model.html "interface in net.runelite.api") getBaseModel()
```
- #### getAnimationController

```
@Nullable
public [AnimationController](AnimationController.html "class in net.runelite.api") getAnimationController()
```

The animation of the RuneLiteObject.
If animation is null then the model will be static.
- #### setPoseAnimationController

```
public void setPoseAnimationController​(@Nullable
[AnimationController](AnimationController.html "class in net.runelite.api") poseAnimationController)
```

The optional pose animation of the RuneLiteObject.
If animation is null then the model from `animationController` will be used.
- #### getPoseAnimationController

```
@Nullable
public [AnimationController](AnimationController.html "class in net.runelite.api") getPoseAnimationController()
```

The optional pose animation of the RuneLiteObject.
If animation is null then the model from `animationController` will be used.
- #### getStartCycle

```
public int getStartCycle()
```
- #### setStartCycle

```
public void setStartCycle​(int startCycle)
```