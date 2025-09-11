# EnterInputScreen (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/EnterInputScreen.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.EnterInputScreen

* ---

```
public class EnterInputScreen
extends java.lang.Object
```

Contains methods for inspecting and interacting with the commonly used 'enter input' screen that appears over the chatbox

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[EnterInputScreen](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[enter](#enter(int))​(int quantity)` | Enters the specified number into the enter input screen, and presses enter |
| `static boolean` | `[enter](#enter(java.lang.String))​(java.lang.String input)` | Enters the specified input into the enter input screen, and presses enter |
| `static java.lang.String` | `[getCurrentInput](#getCurrentInput())()` | Gets the currently entered input |
| `static java.lang.String` | `[getPromptMessage](#getPromptMessage())()` | Gets the enter amount screen prompt message
Ex. |
| `static java.util.Optional<java.lang.Integer>` | `[getType](#getType())()` | The input type (ex. |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the enter input screen is open |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### EnterInputScreen

```
public EnterInputScreen()
```

+ ### Method Detail

- #### getType

```
public static java.util.Optional<java.lang.Integer> getType()
```

The input type (ex. 14 is grand exchange)

Returns:
enter input type
- #### getPromptMessage

```
public static java.lang.String getPromptMessage()
```

Gets the enter amount screen prompt message
Ex. "Enter amount:"

Returns:
the enter amount screen prompt message, or an empty string if not open
- #### getCurrentInput

```
public static java.lang.String getCurrentInput()
```

Gets the currently entered input

Returns:
the currently entered input
- #### isOpen

```
public static boolean isOpen()
```

Checks if the enter input screen is open

Returns:
true if the enter input screen is open, false otherwise
- #### enter

```
public static boolean enter​(int quantity)
```

Enters the specified number into the enter input screen, and presses enter

Parameters:
`quantity` - the quantity to enter
Returns:
true if entered successfully, false otherwise
- #### enter

```
public static boolean enter​(java.lang.String input)
```

Enters the specified input into the enter input screen, and presses enter

Parameters:
`input` - the input to enter
Returns:
true if entered successfully, false otherwise