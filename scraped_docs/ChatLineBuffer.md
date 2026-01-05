# ChatLineBuffer (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/ChatLineBuffer.html

**Package:** Packagenet.runelite.api

---

* ---

```
public interface ChatLineBuffer
```

Represents the buffer containing all messages in the chatbox.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getLength](#getLength())()` | Gets the length of the [`getLines()`](#getLines()) array. |
| `[MessageNode](MessageNode.html "interface in net.runelite.api")[]` | `[getLines](#getLines())()` | Gets an array of message nodes currently in the chatbox. |
| `void` | `[removeMessageNode](#removeMessageNode(net.runelite.api.MessageNode))​([MessageNode](MessageNode.html "interface in net.runelite.api") node)` | Removes a message node. |

* + ### Method Detail

- #### getLines

```
[MessageNode](MessageNode.html "interface in net.runelite.api")[] getLines()
```

Gets an array of message nodes currently in the chatbox.

Returns:
messages in the chatbox
- #### getLength

```
int getLength()
```

Gets the length of the [`getLines()`](#getLines()) array.

Returns:
the length
- #### removeMessageNode

```
void removeMessageNode​([MessageNode](MessageNode.html "interface in net.runelite.api") node)
```

Removes a message node.

This method modifies the underlying MessageNode array. If removing multiple MessageNodes at a time,
clone the original [`getLines()`](#getLines()) array; as items in the array will get modified and be left in an
inconsistent state.

Parameters:
`node` - the [`MessageNode`](MessageNode.html "interface in net.runelite.api") to remove