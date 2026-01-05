# AnimationController (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/AnimationController.html

**Package:** Packagenet.runelite.api

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.AnimationController

* ---

```
public class AnimationController
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[AnimationController](#%3Cinit%3E(net.runelite.api.Client,int))​([Client](Client.html "interface in net.runelite.api") client,
int animationID)` | |
| `[AnimationController](#%3Cinit%3E(net.runelite.api.Client,net.runelite.api.Animation))​([Client](Client.html "interface in net.runelite.api") client,
[Animation](Animation.html "interface in net.runelite.api") animation)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `[Model](Model.html "interface in net.runelite.api")` | `[animate](#animate(net.runelite.api.Model))​([Model](Model.html "interface in net.runelite.api") model)` | |
| `[Model](Model.html "interface in net.runelite.api")` | `[animate](#animate(net.runelite.api.Model,net.runelite.api.AnimationController))​([Model](Model.html "interface in net.runelite.api") model,
[AnimationController](AnimationController.html "class in net.runelite.api") other)` | |
| `[Animation](Animation.html "interface in net.runelite.api")` | `[getAnimation](#getAnimation())()` | |
| `int` | `[getFrame](#getFrame())()` | |
| `void` | `[loop](#loop())()` | |
| `void` | `[reset](#reset())()` | |
| `void` | `[setAnimation](#setAnimation(net.runelite.api.Animation))​([Animation](Animation.html "interface in net.runelite.api") animation)` | |
| `[AnimationController](AnimationController.html "class in net.runelite.api")` | `[setFrame](#setFrame(int))​(int frame)` | |
| `[AnimationController](AnimationController.html "class in net.runelite.api")` | `[setOnFinished](#setOnFinished(java.util.function.Consumer))​(@NonNull [Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[AnimationController](AnimationController.html "class in net.runelite.api")> onFinished)` | |
| `void` | `[tick](#tick(int))​(int ticks)` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### AnimationController

```
public AnimationController​([Client](Client.html "interface in net.runelite.api") client,
int animationID)
```
- #### AnimationController

```
public AnimationController​([Client](Client.html "interface in net.runelite.api") client,
[Animation](Animation.html "interface in net.runelite.api") animation)
```

+ ### Method Detail

- #### setAnimation

```
public void setAnimation​(@Nullable
[Animation](Animation.html "interface in net.runelite.api") animation)
```
- #### reset

```
public void reset()
```
- #### loop

```
public void loop()
```
- #### tick

```
public void tick​(int ticks)
```
- #### animate

```
public [Model](Model.html "interface in net.runelite.api") animate​([Model](Model.html "interface in net.runelite.api") model)
```
- #### animate

```
public [Model](Model.html "interface in net.runelite.api") animate​([Model](Model.html "interface in net.runelite.api") model,
@Nullable
[AnimationController](AnimationController.html "class in net.runelite.api") other)
```
- #### getAnimation

```
@Nullable
public [Animation](Animation.html "interface in net.runelite.api") getAnimation()
```
- #### setOnFinished

```
public [AnimationController](AnimationController.html "class in net.runelite.api") setOnFinished​(@NonNull
@NonNull [Consumer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/function/Consumer.html?is-external=true "class or interface in java.util.function")<[AnimationController](AnimationController.html "class in net.runelite.api")> onFinished)
```

Returns:
`this`.
- #### getFrame

```
public int getFrame()
```
- #### setFrame

```
public [AnimationController](AnimationController.html "class in net.runelite.api") setFrame​(int frame)
```

Returns:
`this`.