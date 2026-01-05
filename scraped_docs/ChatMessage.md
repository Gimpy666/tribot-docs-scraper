# ChatMessage (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/events/ChatMessage.html

**Package:** Packagenet.runelite.api.events

**Description:** SeeChatMessageTypefor different message types that can be
 received.Note: This event will not trigger for NPC dialogues....

---

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + net.runelite.api.events.ChatMessage

* ---

```
public class ChatMessage
extends [Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
```

An event where a new chat message is received.

See [`ChatMessageType`](../ChatMessageType.html "enum in net.runelite.api") for different message types that can be
received.

Note: This event will not trigger for NPC dialogues.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[ChatMessage](#%3Cinit%3E())()` | |
| `[ChatMessage](#%3Cinit%3E(net.runelite.api.MessageNode,net.runelite.api.ChatMessageType,java.lang.String,java.lang.String,java.lang.String,int))​([MessageNode](../MessageNode.html "interface in net.runelite.api") messageNode,
[ChatMessageType](../ChatMessageType.html "enum in net.runelite.api") type,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender,
int timestamp)` | |

+ ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `protected boolean` | `[canEqual](#canEqual(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)` | |
| `boolean` | `[equals](#equals(java.lang.Object))​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` | |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getMessage](#getMessage())()` | The contents of the message. |
| `[MessageNode](../MessageNode.html "interface in net.runelite.api")` | `[getMessageNode](#getMessageNode())()` | The underlying MessageNode for the message. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | The name of the player that sent the message. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getSender](#getSender())()` | The sender of the message. |
| `int` | `[getTimestamp](#getTimestamp())()` | Timestamp of the message. |
| `[ChatMessageType](../ChatMessageType.html "enum in net.runelite.api")` | `[getType](#getType())()` | The type of message received. |
| `int` | `[hashCode](#hashCode())()` | |
| `void` | `[setMessage](#setMessage(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message)` | The contents of the message. |
| `void` | `[setMessageNode](#setMessageNode(net.runelite.api.MessageNode))​([MessageNode](../MessageNode.html "interface in net.runelite.api") messageNode)` | The underlying MessageNode for the message. |
| `void` | `[setName](#setName(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | The name of the player that sent the message. |
| `void` | `[setSender](#setSender(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)` | The sender of the message. |
| `void` | `[setTimestamp](#setTimestamp(int))​(int timestamp)` | Timestamp of the message. |
| `void` | `[setType](#setType(net.runelite.api.ChatMessageType))​([ChatMessageType](../ChatMessageType.html "enum in net.runelite.api") type)` | The type of message received. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[toString](#toString())()` | |

- ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#clone() "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#finalize() "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#getClass() "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notify() "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#notifyAll() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait() "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#wait(long,int) "class or interface in java.lang")`

* + ### Constructor Detail

- #### ChatMessage

```
public ChatMessage​([MessageNode](../MessageNode.html "interface in net.runelite.api") messageNode,
[ChatMessageType](../ChatMessageType.html "enum in net.runelite.api") type,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender,
int timestamp)
```
- #### ChatMessage

```
public ChatMessage()
```

+ ### Method Detail

- #### getMessageNode

```
public [MessageNode](../MessageNode.html "interface in net.runelite.api") getMessageNode()
```

The underlying MessageNode for the message.
- #### getType

```
public [ChatMessageType](../ChatMessageType.html "enum in net.runelite.api") getType()
```

The type of message received.
- #### getName

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

The name of the player that sent the message.
- #### getMessage

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getMessage()
```

The contents of the message.
- #### getSender

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getSender()
```

The sender of the message.

This field is only used for friends chat messages and refers to the
current name of the friends chat the client is in.
- #### getTimestamp

```
public int getTimestamp()
```

Timestamp of the message.
- #### setMessageNode

```
public void setMessageNode​([MessageNode](../MessageNode.html "interface in net.runelite.api") messageNode)
```

The underlying MessageNode for the message.
- #### setType

```
public void setType​([ChatMessageType](../ChatMessageType.html "enum in net.runelite.api") type)
```

The type of message received.
- #### setName

```
public void setName​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

The name of the player that sent the message.
- #### setMessage

```
public void setMessage​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") message)
```

The contents of the message.
- #### setSender

```
public void setSender​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)
```

The sender of the message.

This field is only used for friends chat messages and refers to the
current name of the friends chat the client is in.
- #### setTimestamp

```
public void setTimestamp​(int timestamp)
```

Timestamp of the message.
- #### equals

```
public boolean equals​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Overrides:
`[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#equals(java.lang.Object) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### canEqual

```
protected boolean canEqual​([Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang") other)
```
- #### hashCode

```
public int hashCode()
```

Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#hashCode() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`
- #### toString

```
public [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
`[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true#toString() "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")`