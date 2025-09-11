# BankPinScreen (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/BankPinScreen.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.BankPinScreen

* ---

```
public class BankPinScreen
extends java.lang.Object
```

Utilities for interacting with the Bank Pin screen.

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[BankPinScreen](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[closeBankPinSettingScreen](#closeBankPinSettingScreen())()` | Closes the bank pin settings interface. |
| `static boolean` | `[closePendingPinMessage](#closePendingPinMessage())()` | Closes the message interface regarding a pending pin. |
| `static boolean` | `[inputPin](#inputPin())()` | Inputs the bank pin for the current account as per the Account Manager. |
| `static boolean` | `[inputPin](#inputPin(java.lang.String))​(java.lang.String pin)` | Inputs the bank pin. |
| `static boolean` | `[isBankPinSettingsOpen](#isBankPinSettingsOpen())()` | Determines if bank pin settings screen is open or not. |
| `static boolean` | `[isOpen](#isOpen())()` | Determines if the pin screen interface is open and visible. |
| `static boolean` | `[isPendingPinMessageOpen](#isPendingPinMessageOpen())()` | Determines if the message regarding a pending pin is open. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### BankPinScreen

```
public BankPinScreen()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Determines if the pin screen interface is open and visible.

Returns:
True if the pin screen is showing. False otherwise.
- #### isPendingPinMessageOpen

```
public static boolean isPendingPinMessageOpen()
```

Determines if the message regarding a pending pin is open.

Returns:
True if the message interface is open and visible. False otherwise.
- #### closePendingPinMessage

```
public static boolean closePendingPinMessage()
```

Closes the message interface regarding a pending pin.

Returns:
True if the click happens. False otherwise.
- #### inputPin

```
public static boolean inputPin()
```

Inputs the bank pin for the current account as per the Account Manager.

Returns:
True if the pin was passed. False otherwise.
- #### inputPin

```
public static boolean inputPin​(java.lang.String pin)
```

Inputs the bank pin.

Parameters:
`pin` - The 4 digit pin in string form. Ex: "1234".
Returns:
True if the pin was passed. False otherwise.
- #### isBankPinSettingsOpen

```
public static boolean isBankPinSettingsOpen()
```

Determines if bank pin settings screen is open or not.

Returns:
True if the bank pin setting is open and visible. False otherwise.
- #### closeBankPinSettingScreen

```
public static boolean closeBankPinSettingScreen()
```

Closes the bank pin settings interface.

Returns:
True if the click happens. False otherwise.