# IntegerNode (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/IntegerNode.html

**Package:** Packagenet.runelite.api

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface IntegerNode
extends [Node](Node.html "interface in net.runelite.api")
```

Represents an integer typically in a [`HashTable`](HashTable.html "interface in net.runelite.api").

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getValue](#getValue())()` | Gets the value of the node. |
| `void` | `[setValue](#setValue(int))​(int value)` | Sets the value of the node. |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getValue

```
int getValue()
```

Gets the value of the node.

Returns:
the int value
- #### setValue

```
void setValue​(int value)
```

Sets the value of the node.

Parameters:
`value` - the new int value