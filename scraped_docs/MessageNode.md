# MessageNode (RuneLite API 1.12.10 API)

**URL:** https://static.runelite.net/runelite-api/apidocs/net/runelite/api/MessageNode.html

**Package:** Packagenet.runelite.api

**Description:** If this value is not null, the message contents as returned bygetValue()will be replaced with the format set here
 when a message is processed....

---

* All Superinterfaces:
`[Node](Node.html "interface in net.runelite.api")`

---

```
public interface MessageNode
extends [Node](Node.html "interface in net.runelite.api")
```

Represents a message in the chatbox.

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) | Modifier and Type | Method | Description |
| `int` | `[getId](#getId())()` | Get the id for this message node |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getName](#getName())()` | Gets the name of the player that sent the message. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getRuneLiteFormatMessage](#getRuneLiteFormatMessage())()` | Gets the overriden message format. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getSender](#getSender())()` | Gets the sender of the message. |
| `int` | `[getTimestamp](#getTimestamp())()` | Get the timestamp for the message, in seconds from the unix epoch. |
| `[ChatMessageType](ChatMessageType.html "enum in net.runelite.api")` | `[getType](#getType())()` | Gets the type of message. |
| `[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")` | `[getValue](#getValue())()` | Gets the message contents. |
| `void` | `[setName](#setName(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)` | Sets the name of the player that sent the message. |
| `void` | `[setRuneLiteFormatMessage](#setRuneLiteFormatMessage(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") runeLiteFormatMessage)` | Sets the overriden message format. |
| `void` | `[setSender](#setSender(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)` | Sets the sender of the message. |
| `void` | `[setTimestamp](#setTimestamp(int))​(int timestamp)` | Set the timestamp of the message |
| `void` | `[setValue](#setValue(java.lang.String))​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)` | Sets the message contents. |

- ### Methods inherited from interface net.runelite.api.[Node](Node.html "interface in net.runelite.api")

`[getHash](Node.html#getHash()), [getNext](Node.html#getNext()), [getPrevious](Node.html#getPrevious())`

* + ### Method Detail

- #### getId

```
int getId()
```

Get the id for this message node

Returns:
- #### getType

```
[ChatMessageType](ChatMessageType.html "enum in net.runelite.api") getType()
```

Gets the type of message.

Returns:
the message type
- #### getName

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getName()
```

Gets the name of the player that sent the message.

Returns:
the player name
- #### setName

```
void setName​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") name)
```

Sets the name of the player that sent the message.

Parameters:
`name` - the new player name
- #### getSender

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getSender()
```

Gets the sender of the message. (ie. friends chat name)

Returns:
the message sender
- #### setSender

```
void setSender​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") sender)
```

Sets the sender of the message.

Parameters:
`sender` - the new message sender
- #### getValue

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getValue()
```

Gets the message contents.

Returns:
the message contents
- #### setValue

```
void setValue​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") value)
```

Sets the message contents.

Parameters:
`value` - the new message contents
- #### getRuneLiteFormatMessage

```
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") getRuneLiteFormatMessage()
```

Gets the overriden message format.

Returns:
the message format
- #### setRuneLiteFormatMessage

```
void setRuneLiteFormatMessage​([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang") runeLiteFormatMessage)
```

Sets the overriden message format.

If this value is not null, the message contents as returned by
[`getValue()`](#getValue()) will be replaced with the format set here
when a message is processed.

Parameters:
`runeLiteFormatMessage` - the new message format
- #### getTimestamp

```
int getTimestamp()
```

Get the timestamp for the message, in seconds from the unix epoch.

Returns:
- #### setTimestamp

```
void setTimestamp​(int timestamp)
```

Set the timestamp of the message

Parameters:
`timestamp` -