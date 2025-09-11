# Antiban (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/antiban/Antiban.html

**Package:** Packageorg.tribot.script.sdk.antiban

---

* java.lang.Object
* + org.tribot.script.sdk.antiban.Antiban

* ---

```
public class Antiban
extends java.lang.Object
```

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[Antiban](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[isScriptAiAntibanEnabled](#isScriptAiAntibanEnabled())()` | Checks if tribot's built-in antiban is enabled. |
| `static void` | `[setScriptAiAntibanEnabled](#setScriptAiAntibanEnabled(boolean))​(boolean enabled)` | Enables tribot's built-in antiban |
| `static boolean` | `[shouldCloseBankBeforeEquippingGear](#shouldCloseBankBeforeEquippingGear())()` | Determines if the current account should close bank to wear gear in bank task |
| `static boolean` | `[shouldCloseWithEscape](#shouldCloseWithEscape())()` | Determines if the current account should press escape to close a widget |
| `static boolean` | `[shouldLeftClickWithdraw](#shouldLeftClickWithdraw())()` | Determines if the current account should left click to withdraw items |
| `static boolean` | `[shouldRandomizeEquippingItemsOrder](#shouldRandomizeEquippingItemsOrder())()` | Determines if the current account should randomize equipping items order in bank task |
| `static boolean` | `[shouldRemoveItemFirst](#shouldRemoveItemFirst())()` | Determines if the current account should remove item into inv first before depositing into bank ( Bank Task ) |
| `static boolean` | `[shouldTurnOnRun](#shouldTurnOnRun())()` | |
| `static boolean` | `[shouldWithdrawItemsInBankOrder](#shouldWithdrawItemsInBankOrder())()` | Determines if the current account should withdraw items in bank order or not |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Antiban

```
public Antiban()
```

+ ### Method Detail

- #### shouldTurnOnRun

```
public static boolean shouldTurnOnRun()
```
- #### shouldCloseWithEscape

```
public static boolean shouldCloseWithEscape()
```

Determines if the current account should press escape to close a widget

Returns:
true if it should press escape to close a widget, false otherwise
- #### shouldCloseBankBeforeEquippingGear

```
public static boolean shouldCloseBankBeforeEquippingGear()
```

Determines if the current account should close bank to wear gear in bank task

Returns:
true if it should close bank, false otherwise
- #### shouldRandomizeEquippingItemsOrder

```
public static boolean shouldRandomizeEquippingItemsOrder()
```

Determines if the current account should randomize equipping items order in bank task

Returns:
true if it should randomize, false otherwise
- #### shouldRemoveItemFirst

```
public static boolean shouldRemoveItemFirst()
```

Determines if the current account should remove item into inv first before depositing into bank ( Bank Task )

Returns:
true if it should remove first, false otherwise
- #### isScriptAiAntibanEnabled

```
public static boolean isScriptAiAntibanEnabled()
```

Checks if tribot's built-in antiban is enabled.

This controls randomly performing actions like right clicking.

Returns:
true if it is enabled, false otherwise
- #### setScriptAiAntibanEnabled

```
public static void setScriptAiAntibanEnabled​(boolean enabled)
```

Enables tribot's built-in antiban

Parameters:
`enabled` - true to enable, false to disable
- #### shouldLeftClickWithdraw

```
public static boolean shouldLeftClickWithdraw()
```

Determines if the current account should left click to withdraw items

Returns:
true if it should, false otherwise
- #### shouldWithdrawItemsInBankOrder

```
public static boolean shouldWithdrawItemsInBankOrder()
```

Determines if the current account should withdraw items in bank order or not

Returns:
true if it should, false otherwise