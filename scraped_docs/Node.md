# Node (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Node.html

**Package:** Packagenet.runelite.api

---

* All Known Subinterfaces:
`[Actor](Actor.html "interface in net.runelite.api")`, `[ActorSpotAnim](ActorSpotAnim.html "interface in net.runelite.api")`, `[DynamicObject](DynamicObject.html "interface in net.runelite.api")`, `[GraphicsObject](GraphicsObject.html "interface in net.runelite.api")`, `[IntegerNode](IntegerNode.html "interface in net.runelite.api")`, `[ItemContainer](ItemContainer.html "interface in net.runelite.api")`, `[MessageNode](MessageNode.html "interface in net.runelite.api")`, `[Model](Model.html "interface in net.runelite.api")`, `[ModelData](ModelData.html "interface in net.runelite.api")`, `[NPC](NPC.html "interface in net.runelite.api")`, `[Player](Player.html "interface in net.runelite.api")`, `[Projectile](Projectile.html "interface in net.runelite.api")`, `[Renderable](Renderable.html "interface in net.runelite.api")`, `[Scene](Scene.html "interface in net.runelite.api")`, `[Script](Script.html "interface in net.runelite.api")`, `[Texture](Texture.html "interface in net.runelite.api")`, `[TileItem](TileItem.html "interface in net.runelite.api")`, `[WidgetConfigNode](widgets/WidgetConfigNode.html "interface in net.runelite.api.widgets")`, `[WidgetNode](WidgetNode.html "interface in net.runelite.api")`

---

```
public interface Node
```

Represents a doubly linked node.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `long` | `[getHash](#getHash())()` | Gets the hash value of the node. |
| `[Node](Node.html "interface in net.runelite.api")` | `[getNext](#getNext())()` | Gets the next node. |
| `[Node](Node.html "interface in net.runelite.api")` | `[getPrevious](#getPrevious())()` | Gets the previous node. |

* + ### Method Detail

- #### getNext

```
[Node](Node.html "interface in net.runelite.api") getNext()
```

Gets the next node.

Returns:
the next node
- #### getPrevious

```
[Node](Node.html "interface in net.runelite.api") getPrevious()
```

Gets the previous node.

Returns:
the previous node
- #### getHash

```
long getHash()
```

Gets the hash value of the node.

Returns:
the hash value