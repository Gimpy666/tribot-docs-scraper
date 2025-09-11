# Keyboard (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/input/Keyboard.html

**Package:** Packageorg.tribot.script.sdk.input

**Description:** This method uses key holding delay and repeat rates which are unique to every different botter (character
 randomization). Delay and repeat rates mimic the 'Keyboard Properties' of the Windows
 Contro...

---

* java.lang.Object
* + org.tribot.script.sdk.input.Keyboard

* ---

```
public class Keyboard
extends java.lang.Object
```

Utilities related to using the keyboard/typing in-game

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | Represents a key hold configuration |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Keyboard](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")` | `[hold](#hold())()` | Creates a new [`Keyboard.HoldAction`](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") |
| `static void` | `[holdKey](#holdKey(char,int,java.util.function.BooleanSupplier))​(char keyChar,
int keyCode,
java.util.function.BooleanSupplier stopCondition)` | Holds a key while the stopping condition returns false. |
| `static void` | `[pressBack](#pressBack())()` | Presses the backspace key |
| `static void` | `[pressEnter](#pressEnter())()` | Presses the enter key |
| `static void` | `[pressEscape](#pressEscape())()` | Presses the escape key |
| `static void` | `[typeLine](#typeLine(java.lang.String))​(java.lang.String chars)` | Types the specified string and presses enter after |
| `static void` | `[typeLine](#typeLine(java.lang.String,java.lang.String))​(java.lang.String desired,
java.lang.String current)` | Types the specified string, pressing backspace if needed in order to go from the 'current' string to the 'desired' string. |
| `static void` | `[typeString](#typeString(java.lang.String))​(java.lang.String chars)` | Types the specified string |
| `static void` | `[typeString](#typeString(java.lang.String,java.lang.String))​(java.lang.String desired,
java.lang.String current)` | Types the specified string, pressing backspace if needed in order to go from the 'current' string to the 'desired' string. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Keyboard

```
public Keyboard()
```

+ ### Method Detail

- #### typeString

```
public static void typeString​(java.lang.String chars)
```

Types the specified string

Parameters:
`chars` - the string to type
- #### typeString

```
public static void typeString​(java.lang.String desired,
java.lang.String current)
```

Types the specified string, pressing backspace if needed in order to go from the 'current' string to the 'desired' string.

Ex. if desired is "Iron ore" and current is "Iron b", this will press backspace once and then type "ore"

Parameters:
`desired` - the desired typed string
`current` - the currently typed string
- #### typeLine

```
public static void typeLine​(java.lang.String chars)
```

Types the specified string and presses enter after

Parameters:
`chars` - the string to type
- #### typeLine

```
public static void typeLine​(java.lang.String desired,
java.lang.String current)
```

Types the specified string, pressing backspace if needed in order to go from the 'current' string to the 'desired' string. It then presses enter.

Ex. if desired is "Iron ore" and current is "Iron b", this will press backspace once and then type "ore", then enter

Parameters:
`desired` - the desired typed string
`current` - the currently typed string
- #### pressEnter

```
public static void pressEnter()
```

Presses the enter key
- #### pressBack

```
public static void pressBack()
```

Presses the backspace key
- #### pressEscape

```
public static void pressEscape()
```

Presses the escape key
- #### holdKey

```
public static void holdKey​(char keyChar,
int keyCode,
java.util.function.BooleanSupplier stopCondition)
```

Holds a key while the stopping condition returns false. Will send KEY\_PRESSED while being held. If keyChar !=
KeyEvent.CHAR\_UNDEFINED, KEY\_TYPED will also be sent. KEY\_RELEASED is sent after
the stopping condition returns true.

This method uses key holding delay and repeat rates which are unique to every different botter (character
randomization). Delay and repeat rates mimic the 'Keyboard Properties' of the Windows
Control Panel (the machine's OS doesn't matter though).

The stopping condition is checked every millisecond. Try to make sure the stopping condition doesn't take
longer than 2ms to check. If it does, the method will be less human-like.

Parameters:
`keyChar` - The character to type/press. Use KeyEvent.CHAR\_UNDEFINED to not send KEY\_TYPED events.
`keyCode` - The key code.
`stopCondition` - The stopping condition. The bot will continue holding the key as long as the
condition returns false. Once it returns true, the bot will stop holding the key.
- #### hold

```
public static [Keyboard.HoldAction](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input") hold()
```

Creates a new [`Keyboard.HoldAction`](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")

Returns:
a new [`Keyboard.HoldAction`](Keyboard.HoldAction.html "class in org.tribot.script.sdk.input")