# GroundItem (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/types/GroundItem.html

**Package:** Packageorg.tribot.script.sdk.types

---

* java.lang.Object
* + org.tribot.script.sdk.types.GroundItem

* All Implemented Interfaces:
`[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`, `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`, `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`, `[ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")`, `[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`, `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`, `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`, `[Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces")`

---

```
public class GroundItem
extends java.lang.Object
implements [Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces"), [Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces"), [Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces"), [Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces"), [Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces"), [Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces"), [ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")
```

Represents an item on the ground

See Also:
[`Query.groundItems()`](../query/Query.html#groundItems())

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `boolean` | `[adjustCameraTo](#adjustCameraTo())()` | Moves the camera to a position where the given entity or position is in view. |
| `boolean` | `[click](#click())()` | Interacts with the entity, with the first action available. |
| `boolean` | `[click](#click(java.lang.String))​(java.lang.String action)` | Interacts with the entity, given a specific action. |
| `boolean` | `[equals](#equals(java.lang.Object))​(java.lang.Object o)` | |
| `java.util.List<java.lang.String>` | `[getActions](#getActions())()` | Gets the available actions for the entity, usually dependent on their definition. |
| `[ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions")` | `[getDefinition](#getDefinition())()` | Gets the ItemDefinition for this item, which contains more details about the item. |
| `int` | `[getDespawnTicks](#getDespawnTicks())()` | |
| `int` | `[getId](#getId())()` | Gets the ID of the entity |
| `java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")>` | `[getModel](#getModel())()` | Gets the entity model |
| `java.lang.String` | `[getName](#getName())()` | Determines the name of the entity of the object this method is called on. |
| `[GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types")` | `[getOwnerType](#getOwnerType())()` | |
| `int` | `[getRevealTick](#getRevealTick())()` | |
| `int` | `[getStack](#getStack())()` | Gets the stack of this item, which is how many of the item is occupying the item space. |
| `[WorldTile](WorldTile.html "class in org.tribot.script.sdk.types")` | `[getTile](#getTile())()` | Gets the WorldTile of this entity/position |
| `int` | `[hashCode](#hashCode())()` | |
| `boolean` | `[hover](#hover())()` | Moves the mouse to a human-randomized point on the entity. |
| `boolean` | `[interact](#interact(java.lang.String))​(java.lang.String action)` | Attempts to interact with the entity using the given action. |
| `boolean` | `[interact](#interact(java.lang.String,java.util.function.BooleanSupplier))​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)` | Attempts to interact with the entity using the given action. |
| `boolean` | `[isHovering](#isHovering())()` | Checks if the mouse is currently over this entity |
| `boolean` | `[isVisible](#isVisible())()` | Determines if the entity is on the screen and able to be clicked. |
| `java.lang.String` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")

`[hover](../interfaces/Clickable.html#hover(java.lang.String)), [hoverMenu](../interfaces/Clickable.html#hoverMenu(java.lang.String))`
- ### Methods inherited from interface org.tribot.script.sdk.interfaces.[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")

`[distance](../interfaces/Positionable.html#distance()), [distanceTo](../interfaces/Positionable.html#distanceTo(org.tribot.script.sdk.interfaces.Positionable))`

* + ### Method Detail

- #### getId

```
public int getId()
```

Description copied from interface: `[Identifiable](../interfaces/Identifiable.html#getId())`
Gets the ID of the entity

Specified by:
`[getId](../interfaces/Identifiable.html#getId())` in interface `[Identifiable](../interfaces/Identifiable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getName

```
public java.lang.String getName()
```

Description copied from interface: `[Named](../interfaces/Named.html#getName())`
Determines the name of the entity of the object this method is called on.
This method cannot return null. Therefore, expect any problems in the determination of the name to force this
method to return a blank string.

Specified by:
`[getName](../interfaces/Named.html#getName())` in interface `[Named](../interfaces/Named.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
The name of the entity
- #### getActions

```
public java.util.List<java.lang.String> getActions()
```

Description copied from interface: `[Actionable](../interfaces/Actionable.html#getActions())`
Gets the available actions for the entity, usually dependent on their definition.

Specified by:
`[getActions](../interfaces/Actionable.html#getActions())` in interface `[Actionable](../interfaces/Actionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getTile

```
public [WorldTile](WorldTile.html "class in org.tribot.script.sdk.types") getTile()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#getTile())`
Gets the WorldTile of this entity/position

Specified by:
`[getTile](../interfaces/Positionable.html#getTile())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
- #### click

```
public boolean click​(java.lang.String action)
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click(java.lang.String))`
Interacts with the entity, given a specific action. The "action" string is the part of the option that comes first.
For example, to attack an NPC, the action is "Attack". Case insensitive.

Specified by:
`[click](../interfaces/Clickable.html#click(java.lang.String))` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the entity was successfully clicked
- #### click

```
public boolean click()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#click())`
Interacts with the entity, with the first action available. This will generally perform a left-click, unless there is an action blocking in which case it will right click.

Specified by:
`[click](../interfaces/Clickable.html#click())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the entity was clicked, false otherwise
- #### hover

```
public boolean hover()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#hover())`
Moves the mouse to a human-randomized point on the entity.

Specified by:
`[hover](../interfaces/Clickable.html#hover())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
If the mouse successfully moved over the entity
- #### isVisible

```
public boolean isVisible()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#isVisible())`
Determines if the entity is on the screen and able to be clicked.

Specified by:
`[isVisible](../interfaces/Clickable.html#isVisible())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
- #### isHovering

```
public boolean isHovering()
```

Description copied from interface: `[Clickable](../interfaces/Clickable.html#isHovering())`
Checks if the mouse is currently over this entity

Specified by:
`[isHovering](../interfaces/Clickable.html#isHovering())` in interface `[Clickable](../interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
true if the mouse if over this entity, false otherwise
- #### adjustCameraTo

```
public boolean adjustCameraTo()
```

Description copied from interface: `[Positionable](../interfaces/Positionable.html#adjustCameraTo())`
Moves the camera to a position where the given entity or position is in view. Takes into account distance.
Uses an algorithm to move both the angle and rotation of the camera simultaneously at pseudo-random intervals
to simulate human camera movement.

Specified by:
`[adjustCameraTo](../interfaces/Positionable.html#adjustCameraTo())` in interface `[Positionable](../interfaces/Positionable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
True if the camera moved. False otherwise.
- #### getStack

```
public int getStack()
```

Description copied from interface: `[Stackable](../interfaces/Stackable.html#getStack())`
Gets the stack of this item, which is how many of the item is occupying the item space.

Specified by:
`[getStack](../interfaces/Stackable.html#getStack())` in interface `[Stackable](../interfaces/Stackable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getDefinition

```
public [ItemDefinition](definitions/ItemDefinition.html "class in org.tribot.script.sdk.types.definitions") getDefinition()
```

Description copied from interface: `[ItemDefinable](../interfaces/ItemDefinable.html#getDefinition())`
Gets the ItemDefinition for this item, which contains more details about the item.

Specified by:
`[getDefinition](../interfaces/ItemDefinable.html#getDefinition())` in interface `[ItemDefinable](../interfaces/ItemDefinable.html "interface in org.tribot.script.sdk.interfaces")`
- #### getModel

```
public java.util.Optional<[Model](Model.html "class in org.tribot.script.sdk.types")> getModel()
```

Description copied from interface: `[Modellable](../interfaces/Modellable.html#getModel())`
Gets the entity model

Specified by:
`[getModel](../interfaces/Modellable.html#getModel())` in interface `[Modellable](../interfaces/Modellable.html "interface in org.tribot.script.sdk.interfaces")`
Returns:
the entity model, or an empty optional if the model could not be obtained (ex. not visible on screen)
- #### equals

```
public boolean equals​(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`
- #### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`
- #### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`
- #### interact

```
public boolean interact​(java.lang.String action)
```

Description copied from interface: `[Interactable](../interfaces/Interactable.html#interact(java.lang.String))`
Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Specified by:
`[interact](../interfaces/Interactable.html#interact(java.lang.String))` in interface `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`
Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
Returns:
True if the entity was clicked, false otherwise
- #### interact

```
public boolean interact​(java.lang.String action,
java.util.function.BooleanSupplier interruptCondition)
```

Description copied from interface: `[Interactable](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))`
Attempts to interact with the entity using the given action. This method will adjust the camera to and walk to
the entity if needed.

As of now, the interactable entity must be reachable. In the future, support for obstacles such as doors may be added.

Specified by:
`[interact](../interfaces/Interactable.html#interact(java.lang.String,java.util.function.BooleanSupplier))` in interface `[Interactable](../interfaces/Interactable.html "interface in org.tribot.script.sdk.interfaces")`
Parameters:
`action` - The action to use when interacting with the entity (IE: "Attack", "Take", etc)
`interruptCondition` - a condition to interrupt the interaction attempt - if this condition is ever true, when checked, the interaction attempt with return early with a result of false
Returns:
True if the entity was clicked, false otherwise
- #### getOwnerType

```
public [GroundItem.OwnerType](GroundItem.OwnerType.html "enum in org.tribot.script.sdk.types") getOwnerType()
```
- #### getDespawnTicks

```
public int getDespawnTicks()
```
- #### getRevealTick

```
public int getRevealTick()
```