# AutomationClient (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/AutomationClient.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.AutomationClient

* ---

```
public class AutomationClient
extends java.lang.Object
```

Utilities for interacting with and extending the functionality of the TRiBot automation client

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[AutomationClient.AutomationException](AutomationClient.AutomationException.html "class in org.tribot.script.sdk.util")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[AutomationClient](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static void` | `[sendMessage](#sendMessage(java.lang.String))​(java.lang.String message)` | Sends a message to the server. |
| `static <T> T` | `[sendRequest](#sendRequest(java.lang.String,java.lang.Class))​(java.lang.String request,
java.lang.Class<T> returnType)` | Sends a request to the server and waits for a response. |
| `static void` | `[setMessageListener](#setMessageListener(java.util.function.Consumer))​(java.util.function.Consumer<java.lang.String> listener)` | Sets a custom message listener. |
| `static void` | `[setRequestHandler](#setRequestHandler(java.util.function.Function))​(java.util.function.Function<java.lang.String,​java.lang.Object> requestHandler)` | Sets a custom request handler. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### AutomationClient

```
public AutomationClient()
```

+ ### Method Detail

- #### setMessageListener

```
public static void setMessageListener​(java.util.function.Consumer<java.lang.String> listener)
```

Sets a custom message listener. This will be triggered when the server calls `sendScriptMessage` with the message.

Parameters:
`listener` - the listener to accept all server messages via `sendScriptMessage`
- #### setRequestHandler

```
public static void setRequestHandler​(java.util.function.Function<java.lang.String,​java.lang.Object> requestHandler)
```

Sets a custom request handler. This will be triggered when the server calls `sendScriptRequest` with the request.
The request handler should return an object that will be serialized to json. The json will then be sent to the server as a response.

Parameters:
`requestHandler` - the requestHandler to handle server requests send via `sendScriptRequest`
- #### sendMessage

```
public static void sendMessage​(java.lang.String message)
```

Sends a message to the server.
This triggers an onEvent method to be called, with the type `custom`, and the body is the message.

Parameters:
`message` - the message to send to the server
- #### sendRequest

```
public static <T> T sendRequest​(java.lang.String request,
java.lang.Class<T> returnType)
throws [AutomationClient.AutomationException](AutomationClient.AutomationException.html "class in org.tribot.script.sdk.util")
```

Sends a request to the server and waits for a response.

Type Parameters:
`T` - the return type
Parameters:
`request` - the request body (can include the type, params, whatever you want. the server will parse it)
`returnType` - the return type of the json sent back by the server
Returns:
the json response from the server, converted to a java class
Throws:
`[AutomationClient.AutomationException](AutomationClient.AutomationException.html "class in org.tribot.script.sdk.util")` - if there was an issue getting a response from the server