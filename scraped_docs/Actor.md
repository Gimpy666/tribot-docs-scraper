# Actor (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Actor.html

**Package:** Packagenet.runelite.api

**Description:** Examples of interaction include:A monster focusing an Actor to attackTargetting a player to tradeFollowing a player...

---

* All Superinterfaces:
`[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`, `[Node](Node.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`

All Known Subinterfaces:
`[NPC](NPC.html "interface in net.runelite.api")`, `[Player](Player.html "interface in net.runelite.api")`

---

```
public interface Actor
extends [Renderable](Renderable.html "interface in net.runelite.api"), [CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")
```

Represents a RuneScape actor/entity.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `void` | `[clearSpotAnims](#clearSpotAnims())()` | Remove all actor spotanims |
| `void` | `[createSpotAnim](#createSpotAnim(int,int,int,int))​(int id,
int spotAnimId,
int height,
int delay)` | Create an actor spotanim |
| `int` | `[getAnimation](#getAnimation())()` | Gets the current animation the actor is performing. |
| `int` | `[getAnimationFrame](#getAnimationFrame())()` | Get the frame of the animation the actor is performing |
| `int` | `[getAnimationHeightOffset](#getAnimationHeightOffset())()` | Get the height offset of the actor from their current animation |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasImageLocation](#getCanvasImageLocation(java.awt.image.BufferedImage,int))​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image,
int heightOffset)` | Gets the point at which an image should be drawn, relative to the
current location with the given z-axis offset. |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasSpriteLocation](#getCanvasSpriteLocation(net.runelite.api.SpritePixels,int))​([SpritePixels](SpritePixels.html "interface in net.runelite.api") sprite,
int heightOffset)` | Gets the point at which a sprite should be drawn, relative to the
current location with the given z-axis offset. |
| `[Point](Point.html "class in net.runelite.api")` | `[getCanvasTextLocation](#getCanvasTextLocation(java.awt.Graphics2D,java.lang.String,int))​([Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int heightOffset)` | Gets the point at which text should be drawn, relative to the
current location with the given z-axis offset. |
| `[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt")` | `[getCanvasTilePoly](#getCanvasTilePoly())()` | Gets the canvas area of the current tiles the actor is standing on. |
| `int` | `[getCombatLevel](#getCombatLevel())()` | Gets the combat level of the actor. |
| `[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt")` | `[getConvexHull](#getConvexHull())()` | Gets the convex hull of the actors model. |
| `int` | `[getCurrentOrientation](#getCurrentOrientation())()` | Gets the current orientation of the actor. |
| `int` | `[getGraphic](#getGraphic())()` | Deprecated.
see [`hasSpotAnim(int)`](#hasSpotAnim(int))
|
| `int` | `[getGraphicHeight](#getGraphicHeight())()` | Deprecated.
see [`ActorSpotAnim.getHeight()`](ActorSpotAnim.html#getHeight())
|
| `int` | `[getHealthRatio](#getHealthRatio())()` | Gets the health of the actor in [`getHealthScale()`](#getHealthScale()) units. |
| `int` | `[getHealthScale](#getHealthScale())()` | Gets the maximum value [`getHealthRatio()`](#getHealthRatio()) can return

For actors with the default size health bar this is 30, but
for bosses with a larger health bar this can be a larger number. |
| `int` | `[getIdlePoseAnimation](#getIdlePoseAnimation())()` | The idle pose animation. |
| `int` | `[getIdleRotateLeft](#getIdleRotateLeft())()` | Animation used for rotating left if the actor is also not walking |
| `int` | `[getIdleRotateRight](#getIdleRotateRight())()` | Animation used for rotating right if the actor is also not walking |
| `[Actor](Actor.html "interface in net.runelite.api")` | `[getInteracting](#getInteracting())()` | Gets the actor being interacted with. |
| `[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords")` | `[getLocalLocation](#getLocalLocation())()` | Gets the client-side location of the actor. |
| `int` | `[getLogicalHeight](#getLogicalHeight())()` | Gets the logical height of the actors model. |
| `[Point](Point.html "class in net.runelite.api")` | `[getMinimapLocation](#getMinimapLocation())()` | Gets a point on the canvas of where this actors mini-map indicator
should appear. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the actor. |
| `int` | `[getOrientation](#getOrientation())()` | Gets the target orientation of the actor. |
| `int` | `[getOverheadCycle](#getOverheadCycle())()` | Get the number of cycles/client ticks remaining before the overhead text is timed out |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getOverheadText](#getOverheadText())()` | Gets the overhead text that is displayed above the actor |
| `int` | `[getPoseAnimation](#getPoseAnimation())()` | Gets the secondary animation the actor is performing. |
| `int` | `[getPoseAnimationFrame](#getPoseAnimationFrame())()` | Get the frame of the idle animation the actor is performing |
| `int` | `[getRunAnimation](#getRunAnimation())()` | Animation used for running |
| `int` | `[getSpotAnimFrame](#getSpotAnimFrame())()` | Deprecated.
see [`ActorSpotAnim.getFrame()`](ActorSpotAnim.html#getFrame())
|
| `[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[ActorSpotAnim](ActorSpotAnim.html "interface in net.runelite.api")>` | `[getSpotAnims](#getSpotAnims())()` | Get the spotanims on the actor. |
| `int` | `[getWalkAnimation](#getWalkAnimation())()` | Animation used for walking |
| `int` | `[getWalkRotate180](#getWalkRotate180())()` | Animation used for an about-face while walking |
| `int` | `[getWalkRotateLeft](#getWalkRotateLeft())()` | Animation used for rotating left while walking |
| `int` | `[getWalkRotateRight](#getWalkRotateRight())()` | Animation used for rotating right while walking |
| `[WorldArea](coords/WorldArea.html "class in net.runelite.api.coords")` | `[getWorldArea](#getWorldArea())()` | Gets the world area that the actor occupies. |
| `[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords")` | `[getWorldLocation](#getWorldLocation())()` | Gets the server-side location of the actor. |
| `[WorldView](WorldView.html "interface in net.runelite.api")` | `[getWorldView](#getWorldView())()` | Get the [`WorldView`](WorldView.html "interface in net.runelite.api") this actor belongs to |
| `boolean` | `[hasSpotAnim](#hasSpotAnim(int))​(int spotAnimId)` | Check if the actor has a spotanim |
| `boolean` | `[isDead](#isDead())()` | Returns true if this actor has died |
| `boolean` | `[isInteracting](#isInteracting())()` | Gets if the actor is interacting with another actor. |
| `void` | `[removeSpotAnim](#removeSpotAnim(int))​(int id)` | Remove an actor spotanim |
| `void` | `[setActionFrame](#setActionFrame(int))​(int frame)` | Deprecated.
use setAnimationFrame
|
| `void` | `[setAnimation](#setAnimation(int))​(int animation)` | Sets an animation for the actor to perform. |
| `void` | `[setAnimationFrame](#setAnimationFrame(int))​(int frame)` | Sets the frame of the animation the actor is performing. |
| `void` | `[setDead](#setDead(boolean))​(boolean dead)` | Sets the dead status of this actor |
| `void` | `[setGraphic](#setGraphic(int))​(int graphic)` | Deprecated.
see [`createSpotAnim(int, int, int, int)`](#createSpotAnim(int,int,int,int))
|
| `void` | `[setGraphicHeight](#setGraphicHeight(int))​(int height)` | Deprecated.
see [`ActorSpotAnim.setHeight(int)`](ActorSpotAnim.html#setHeight(int))
|
| `void` | `[setIdlePoseAnimation](#setIdlePoseAnimation(int))​(int animation)` | |
| `void` | `[setIdleRotateLeft](#setIdleRotateLeft(int))​(int animationID)` | |
| `void` | `[setIdleRotateRight](#setIdleRotateRight(int))​(int animationID)` | |
| `void` | `[setOverheadCycle](#setOverheadCycle(int))​(int cycles)` | Set the number of cycles/client ticks before the overhead text is timed out |
| `void` | `[setOverheadText](#setOverheadText(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") overheadText)` | Sets the overhead text that is displayed above the actor |
| `void` | `[setPoseAnimation](#setPoseAnimation(int))​(int animation)` | Set the idle pose animation. |
| `void` | `[setPoseAnimationFrame](#setPoseAnimationFrame(int))​(int frame)` | Set the frame of the idle animation the actor is performing |
| `void` | `[setRunAnimation](#setRunAnimation(int))​(int animationID)` | |
| `void` | `[setSpotAnimFrame](#setSpotAnimFrame(int))​(int spotAnimFrame)` | Deprecated.
see [`ActorSpotAnim.setFrame(int)`](ActorSpotAnim.html#setFrame(int))
|
| `void` | `[setWalkAnimation](#setWalkAnimation(int))​(int animationID)` | |
| `void` | `[setWalkRotate180](#setWalkRotate180(int))​(int animationID)` | |
| `void` | `[setWalkRotateLeft](#setWalkRotateLeft(int))​(int animationID)` | |
| `void` | `[setWalkRotateRight](#setWalkRotateRight(int))​(int animationID)` | |

- ### Methods inherited from interface net.runelite.api.[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")

`[getCameraFocus](CameraFocusableEntity.html#getCameraFocus())`
- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`
- ### Methods inherited from interface net.runelite.api.[Renderable](Renderable.html "interface in net.runelite.api")

`[getModel](Renderable.html#getModel()), [getModelHeight](Renderable.html#getModelHeight()), [setModelHeight](Renderable.html#setModelHeight(int))`

* + ### Method Detail

- #### getWorldView

```
[WorldView](WorldView.html "interface in net.runelite.api") getWorldView()
```

Get the [`WorldView`](WorldView.html "interface in net.runelite.api") this actor belongs to

Specified by:
`[getWorldView](CameraFocusableEntity.html#getWorldView())` in interface `[CameraFocusableEntity](CameraFocusableEntity.html "interface in net.runelite.api")`
Returns:
- #### getCombatLevel

```
int getCombatLevel()
```

Gets the combat level of the actor.

Returns:
the combat level
- #### getName

```
@Nullable
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the actor.

Returns:
the name
- #### isInteracting

```
boolean isInteracting()
```

Gets if the actor is interacting with another actor.
[`getInteracting()`](#getInteracting()) will return the interacting actor,
unless they are outside of the visibility range.

Returns:
- #### getInteracting

```
[Actor](Actor.html "interface in net.runelite.api") getInteracting()
```

Gets the actor being interacted with.

Examples of interaction include:

* A monster focusing an Actor to attack
* Targetting a player to trade
* Following a player

Returns:
the actor, null if no interaction is occurring
- #### getHealthRatio

```
int getHealthRatio()
```

Gets the health of the actor in [`getHealthScale()`](#getHealthScale()) units.

The server does not transmit actors' real health, only this value
between zero and [`getHealthScale()`](#getHealthScale()). Some actors may be
missing this info, in which case -1 is returned.
- #### getHealthScale

```
int getHealthScale()
```

Gets the maximum value [`getHealthRatio()`](#getHealthRatio()) can return

For actors with the default size health bar this is 30, but
for bosses with a larger health bar this can be a larger number.
Some actors may be missing this info, in which case -1 is returned.
- #### getWorldLocation

```
[WorldPoint](coords/WorldPoint.html "class in net.runelite.api.coords") getWorldLocation()
```

Gets the server-side location of the actor.

This value is typically ahead of where the client renders and is not
affected by things such as animations.

Returns:
the server location
- #### getLocalLocation

```
[LocalPoint](coords/LocalPoint.html "class in net.runelite.api.coords") getLocalLocation()
```

Gets the client-side location of the actor.

Returns:
the client location
- #### getOrientation

```
int getOrientation()
```

Gets the target orientation of the actor.

Returns:
the orientation
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getCurrentOrientation

```
int getCurrentOrientation()
```

Gets the current orientation of the actor.

Returns:
the orientation
See Also:
[`Angle`](coords/Angle.html "class in net.runelite.api.coords")
- #### getAnimation

```
int getAnimation()
```

Gets the current animation the actor is performing.

Returns:
the animation ID
See Also:
`AnimationID`
- #### getPoseAnimation

```
int getPoseAnimation()
```

Gets the secondary animation the actor is performing. Usually an idle animation, or one of the walking ones.

Returns:
the animation ID
See Also:
`AnimationID`
- #### setPoseAnimation

```
void setPoseAnimation​(int animation)
```

Set the idle pose animation.

Parameters:
`animation` -
See Also:
`AnimationID`
- #### getPoseAnimationFrame

```
int getPoseAnimationFrame()
```

Get the frame of the idle animation the actor is performing

Returns:
- #### setPoseAnimationFrame

```
void setPoseAnimationFrame​(int frame)
```

Set the frame of the idle animation the actor is performing

Parameters:
`frame` -
- #### getIdlePoseAnimation

```
int getIdlePoseAnimation()
```

The idle pose animation. If the actor is not walking or otherwise animating, this will be used
for their pose animation.

Returns:
the animation ID
See Also:
`AnimationID`
- #### setIdlePoseAnimation

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
void setIdlePoseAnimation​(int animation)
```
- #### getIdleRotateLeft

```
int getIdleRotateLeft()
```

Animation used for rotating left if the actor is also not walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setIdleRotateLeft

```
void setIdleRotateLeft​(int animationID)
```
- #### getIdleRotateRight

```
int getIdleRotateRight()
```

Animation used for rotating right if the actor is also not walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setIdleRotateRight

```
void setIdleRotateRight​(int animationID)
```
- #### getWalkAnimation

```
int getWalkAnimation()
```

Animation used for walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setWalkAnimation

```
void setWalkAnimation​(int animationID)
```
- #### getWalkRotateLeft

```
int getWalkRotateLeft()
```

Animation used for rotating left while walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setWalkRotateLeft

```
void setWalkRotateLeft​(int animationID)
```
- #### getWalkRotateRight

```
int getWalkRotateRight()
```

Animation used for rotating right while walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setWalkRotateRight

```
void setWalkRotateRight​(int animationID)
```
- #### getWalkRotate180

```
int getWalkRotate180()
```

Animation used for an about-face while walking

Returns:
the animation ID
See Also:
`AnimationID`
- #### setWalkRotate180

```
void setWalkRotate180​(int animationID)
```
- #### getRunAnimation

```
int getRunAnimation()
```

Animation used for running

Returns:
the animation ID
See Also:
`AnimationID`
- #### setRunAnimation

```
void setRunAnimation​(int animationID)
```
- #### setAnimation

```
[@VisibleForDevtools](annotations/VisibleForDevtools.html "annotation in net.runelite.api.annotations")
void setAnimation​(int animation)
```

Sets an animation for the actor to perform.

Parameters:
`animation` - the animation ID
See Also:
`AnimationID`
- #### getAnimationFrame

```
int getAnimationFrame()
```

Get the frame of the animation the actor is performing

Returns:
the frame
- #### setActionFrame

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setActionFrame​(int frame)
```

Deprecated.
use setAnimationFrame

Sets the frame of the animation the actor is performing.

Parameters:
`frame` - the animation frame
- #### setAnimationFrame

```
void setAnimationFrame​(int frame)
```

Sets the frame of the animation the actor is performing.

Parameters:
`frame` - the animation frame
- #### getSpotAnims

```
[IterableHashTable](IterableHashTable.html "interface in net.runelite.api")<[ActorSpotAnim](ActorSpotAnim.html "interface in net.runelite.api")> getSpotAnims()
```

Get the spotanims on the actor.
It is important to not modify the table directly or indirectly via
eg. iterator remove().

Returns:
See Also:
[`createSpotAnim(int, int, int, int)`](#createSpotAnim(int,int,int,int)),
[`removeSpotAnim(int)`](#removeSpotAnim(int)),
[`clearSpotAnims()`](#clearSpotAnims())
- #### hasSpotAnim

```
boolean hasSpotAnim​(int spotAnimId)
```

Check if the actor has a spotanim

Parameters:
`spotAnimId` - the spot anim id
Returns:
See Also:
`SpotanimID`
- #### createSpotAnim

```
void createSpotAnim​(int id,
int spotAnimId,
int height,
int delay)
```

Create an actor spotanim

Parameters:
`id` - key for the [`getSpotAnims()`](#getSpotAnims()) table
`spotAnimId` - spotanim id `SpotanimID`
`height` - height offspot for spot anim
`delay` - initial delay, in client ticks, before spotanim is active
- #### removeSpotAnim

```
void removeSpotAnim​(int id)
```

Remove an actor spotanim

Parameters:
`id` - key for the [`getSpotAnims()`](#getSpotAnims()) table
- #### clearSpotAnims

```
void clearSpotAnims()
```

Remove all actor spotanims
- #### getGraphic

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getGraphic()
```

Deprecated.
see [`hasSpotAnim(int)`](#hasSpotAnim(int))

Get the graphic/spotanim that is currently on the actor.
Actors can have multiple spotanims, this gets only one of them. Use [`hasSpotAnim(int)`](#hasSpotAnim(int)) instead.

Returns:
the spotanim of the actor
See Also:
`SpotanimID`
- #### setGraphic

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setGraphic​(int graphic)
```

Deprecated.
see [`createSpotAnim(int, int, int, int)`](#createSpotAnim(int,int,int,int))

Set the graphic/spotanim that is currently on the actor.

Parameters:
`graphic` - The spotanim id
See Also:
`SpotanimID`
- #### getGraphicHeight

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getGraphicHeight()
```

Deprecated.
see [`ActorSpotAnim.getHeight()`](ActorSpotAnim.html#getHeight())

Get the height of the graphic/spotanim on the actor

Returns:
- #### setGraphicHeight

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setGraphicHeight​(int height)
```

Deprecated.
see [`ActorSpotAnim.setHeight(int)`](ActorSpotAnim.html#setHeight(int))

Set the height of the graphic/spotanim on the actor

Parameters:
`height` -
- #### getSpotAnimFrame

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
int getSpotAnimFrame()
```

Deprecated.
see [`ActorSpotAnim.getFrame()`](ActorSpotAnim.html#getFrame())

Get the frame of the currently playing spotanim

Returns:
- #### setSpotAnimFrame

```
[@Deprecated](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Deprecated.html?is-external=true "class or interface in java.lang")
void setSpotAnimFrame​(int spotAnimFrame)
```

Deprecated.
see [`ActorSpotAnim.setFrame(int)`](ActorSpotAnim.html#setFrame(int))

Set the frame of the currently playing spotanim

Parameters:
`spotAnimFrame` -
- #### getCanvasTilePoly

```
[Polygon](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Polygon.html?is-external=true "class or interface in java.awt") getCanvasTilePoly()
```

Gets the canvas area of the current tiles the actor is standing on.

Returns:
the current tile canvas area
- #### getCanvasTextLocation

```
@Nullable
[Point](Point.html "class in net.runelite.api") getCanvasTextLocation​([Graphics2D](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Graphics2D.html?is-external=true "class or interface in java.awt") graphics,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") text,
int heightOffset)
```

Gets the point at which text should be drawn, relative to the
current location with the given z-axis offset.

Parameters:
`graphics` - engine graphics
`text` - the text to draw
`heightOffset` - the height offset
Returns:
the text drawing location
- #### getCanvasImageLocation

```
[Point](Point.html "class in net.runelite.api") getCanvasImageLocation​([BufferedImage](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/image/BufferedImage.html?is-external=true "class or interface in java.awt.image") image,
int heightOffset)
```

Gets the point at which an image should be drawn, relative to the
current location with the given z-axis offset.

Parameters:
`image` - the image to draw
`heightOffset` - the height offset
Returns:
the image drawing location
- #### getCanvasSpriteLocation

```
[Point](Point.html "class in net.runelite.api") getCanvasSpriteLocation​([SpritePixels](SpritePixels.html "interface in net.runelite.api") sprite,
int heightOffset)
```

Gets the point at which a sprite should be drawn, relative to the
current location with the given z-axis offset.

Parameters:
`sprite` - the sprite to draw
`heightOffset` - the height offset
Returns:
the sprite drawing location
- #### getMinimapLocation

```
[Point](Point.html "class in net.runelite.api") getMinimapLocation()
```

Gets a point on the canvas of where this actors mini-map indicator
should appear.

Returns:
mini-map location on canvas
- #### getLogicalHeight

```
int getLogicalHeight()
```

Gets the logical height of the actors model.

This z-axis offset is roughly where the health bar of the actor
is drawn.

Returns:
the logical height
- #### getConvexHull

```
[Shape](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/Shape.html?is-external=true "class or interface in java.awt") getConvexHull()
```

Gets the convex hull of the actors model.

Returns:
the convex hull
See Also:
[`Jarvis`](model/Jarvis.html "class in net.runelite.api.model")
- #### getWorldArea

```
[WorldArea](coords/WorldArea.html "class in net.runelite.api.coords") getWorldArea()
```

Gets the world area that the actor occupies.

Returns:
the world area
- #### getOverheadText

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getOverheadText()
```

Gets the overhead text that is displayed above the actor

Returns:
the overhead text
- #### setOverheadText

```
void setOverheadText​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") overheadText)
```

Sets the overhead text that is displayed above the actor

Parameters:
`overheadText` - the overhead text
- #### getOverheadCycle

```
int getOverheadCycle()
```

Get the number of cycles/client ticks remaining before the overhead text is timed out

Returns:
- #### setOverheadCycle

```
void setOverheadCycle​(int cycles)
```

Set the number of cycles/client ticks before the overhead text is timed out

Parameters:
`cycles` -
- #### isDead

```
boolean isDead()
```

Returns true if this actor has died

Returns:
- #### setDead

```
void setDead​(boolean dead)
```

Sets the dead status of this actor

Parameters:
`dead` -
See Also:
[`isDead()`](#isDead())
- #### getAnimationHeightOffset

```
int getAnimationHeightOffset()
```

Get the height offset of the actor from their current animation

Specified by:
`[getAnimationHeightOffset](Renderable.html#getAnimationHeightOffset())` in interface `[Renderable](Renderable.html "interface in net.runelite.api")`
Returns: