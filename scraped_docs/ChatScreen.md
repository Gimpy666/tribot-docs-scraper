# ChatScreen (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/ChatScreen.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.ChatScreen

* ---

```
public class ChatScreen
extends java.lang.Object
```

Contains methods for inspecting and interacting with the dialog screen that appears over the chatbox, such as when talking to an NPC

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk")` | The config for the chat handler. |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[ChatScreen](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[clickContinue](#clickContinue())()` | Attempts to click continue |
| `static boolean` | `[containsMessage](#containsMessage(java.lang.String...))​(java.lang.String... message)` | Checks if any of the specified messages is contained in the current message |
| `static boolean` | `[containsOption](#containsOption(java.lang.String...))​(java.lang.String... options)` | Checks if any available option contains any of the specified options. |
| `static boolean` | `[containsText](#containsText(java.lang.String...))​(java.lang.String... text)` | Checks if the specified text is contained in any chat interface that is currently being displayed |
| `static [ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk")` | `[getConfig](#getConfig())()` | Gets the current config for the chat screen handler |
| `static java.util.Optional<java.lang.String>` | `[getMessage](#getMessage())()` | Attempts to read the current message in the click continue window |
| `static java.util.Optional<java.lang.String>` | `[getName](#getName())()` | Attempts to read the name of the player/npc talking (the text at the top of the click continue interface) |
| `static java.util.List<java.lang.String>` | `[getOptions](#getOptions())()` | Gets all available chat screen options |
| `static boolean` | `[handle](#handle(java.lang.String...))​(java.lang.String... options)` | Attempts to converse, selecting the specified options. |
| `static boolean` | `[handle](#handle(java.util.function.BooleanSupplier,java.lang.String...))​(java.util.function.BooleanSupplier stopCondition,
java.lang.String... options)` | Attempts to converse, selecting the specified options. |
| `static boolean` | `[isClickContinueOpen](#isClickContinueOpen())()` | Checks if the click continue interface dialog is open |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if any chat screen is open |
| `static boolean` | `[isSelectOptionOpen](#isSelectOptionOpen())()` | Checks if the select option screen is open |
| `static boolean` | `[selectOption](#selectOption(java.lang.String...))​(java.lang.String... options)` | Attempts to select an available option that contains any of the specified options. |
| `static boolean` | `[selectOption](#selectOption(java.util.function.Predicate))​(java.util.function.Predicate<java.lang.String> filter)` | Attempts to select an available option that matches the specified predicate |
| `static void` | `[setConfig](#setConfig(org.tribot.script.sdk.ChatScreen.Config))​([ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk") config)` | Sets the config for the chat screen handler |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### ChatScreen

```
public ChatScreen()
```

+ ### Method Detail

- #### getConfig

```
public static [ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk") getConfig()
```

Gets the current config for the chat screen handler

Returns:
the current config for the chat screen handler
- #### setConfig

```
public static void setConfig​([ChatScreen.Config](ChatScreen.Config.html "class in org.tribot.script.sdk") config)
```

Sets the config for the chat screen handler

Parameters:
`config` - the chat screen handler
- #### isOpen

```
public static boolean isOpen()
```

Checks if any chat screen is open

Returns:
true if any chat screen is open, false otherwise
- #### getOptions

```
public static java.util.List<java.lang.String> getOptions()
```

Gets all available chat screen options

Returns:
the available chat screen options
- #### containsOption

```
public static boolean containsOption​(java.lang.String... options)
```

Checks if any available option contains any of the specified options.

For example, if there is an available option 'Yes, I would like that', and one of the specified options is 'Yes',
this would return true.

Parameters:
`options` - the options to check if any are present
Returns:
true if any available option contains any of the specified options, false otherwise
- #### isClickContinueOpen

```
public static boolean isClickContinueOpen()
```

Checks if the click continue interface dialog is open

Returns:
true if the click continue interface is open, false otherwise
- #### isSelectOptionOpen

```
public static boolean isSelectOptionOpen()
```

Checks if the select option screen is open

Returns:
true if the options screen is open, false otherwise
- #### getName

```
public static java.util.Optional<java.lang.String> getName()
```

Attempts to read the name of the player/npc talking (the text at the top of the click continue interface)

Returns:
the name of the actor currently talking
- #### getMessage

```
public static java.util.Optional<java.lang.String> getMessage()
```

Attempts to read the current message in the click continue window

Returns:
the message in the current click continue window
- #### containsMessage

```
public static boolean containsMessage​(java.lang.String... message)
```

Checks if any of the specified messages is contained in the current message

Parameters:
`message` - the messages to check
Returns:
true if any of the specified messages is contained in the current message, false otherwise
- #### containsText

```
public static boolean containsText​(java.lang.String... text)
```

Checks if the specified text is contained in any chat interface that is currently being displayed

Parameters:
`text` - the text to check if is present anywhere
Returns:
true if the specified text is contained in any chat interface that is currently being displayed, false otherwise
- #### selectOption

```
public static boolean selectOption​(java.lang.String... options)
```

Attempts to select an available option that contains any of the specified options.

This selects options by finding if an available option equals any specified option first,
then checks if any option contains any of the specified options. Options are prioritized based on the order specified.

Parameters:
`options` - the options to search for and select
Returns:
true if an option was selected, false otherwise
- #### selectOption

```
public static boolean selectOption​(java.util.function.Predicate<java.lang.String> filter)
```

Attempts to select an available option that matches the specified predicate

Parameters:
`filter` - the predicate to search for an available option with
Returns:
true if an option was selected, false otherwise
- #### clickContinue

```
public static boolean clickContinue()
```

Attempts to click continue

Returns:
true if click continue was selected
- #### handle

```
public static boolean handle​(java.lang.String... options)
```

Attempts to converse, selecting the specified options. This will handle click continue interfaces and selecting the specified options,
until there is an unknown option or the chat is over.

This selects options by finding if an available option equals any specified option first,
then checks if any option contains any of the specified options. Options are prioritized based on the order specified.

Parameters:
`options` - the options to select
Returns:
true if the chat window is no longer open after conversing, false otherwise
- #### handle

```
public static boolean handle​(java.util.function.BooleanSupplier stopCondition,
java.lang.String... options)
```

Attempts to converse, selecting the specified options. This will handle click continue interfaces and selecting the specified options,
until there is an unknown option or the chat is over.

This selects options by finding if an available option equals any specified option first,
then checks if any option contains any of the specified options. Options are prioritized based on the order specified.

Parameters:
`stopCondition` - the stop condition that should cut terminate the chat handling
`options` - the options to select
Returns:
true if the chat window is no longer open after conversing or the stop condition is true, false otherwise