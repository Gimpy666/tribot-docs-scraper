# BankSettings (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/BankSettings.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.BankSettings

* ---

```
public class BankSettings
extends java.lang.Object
```

Utilities for interacting with the bank settings

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[BankSettings.WithdrawQuantity](BankSettings.WithdrawQuantity.html "enum in org.tribot.script.sdk")` | |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[BankSettings](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);) | Modifier and Type | Method | Description |
| `static int` | `[getDefaultWithdrawQuantity](#getDefaultWithdrawQuantity())()` | Gets the default withdraw quantity |
| `static [BankSettings.WithdrawQuantity](BankSettings.WithdrawQuantity.html "enum in org.tribot.script.sdk")` | `[getWithdrawQuantity](#getWithdrawQuantity())()` | Gets the withdraw quantity |
| `static int` | `[getWithdrawXQuantity](#getWithdrawXQuantity())()` | Gets the withdraw-x quantity |
| `static boolean` | `[isBankInventoryItemOptionEnabled](#isBankInventoryItemOptionEnabled())()` | Checks if bank inventory item option is enabled |
| `static boolean` | `[isDepositEquipmentEnabled](#isDepositEquipmentEnabled())()` | Checks if deposit equipment is enabled |
| `static boolean` | `[isNoteEnabled](#isNoteEnabled())()` | Checks if noting is enabled (ex. |
| `static boolean` | `[isPlaceholdersEnabled](#isPlaceholdersEnabled())()` | Checks if placeholders are enabled |
| `static boolean` | `[isPlaceholdersOn](#isPlaceholdersOn())()` | Deprecated. |
| `static boolean` | `[setNoteEnabled](#setNoteEnabled(boolean))​(boolean enabled)` | Attempts to enable/disable noting |
| `static boolean` | `[setWithdrawQuantity](#setWithdrawQuantity(org.tribot.script.sdk.BankSettings.WithdrawQuantity))​([BankSettings.WithdrawQuantity](BankSettings.WithdrawQuantity.html "enum in org.tribot.script.sdk") withdrawQuantity)` | Attempts to set the withdraw quantity |
| `static boolean` | `[setWithdrawXQuantity](#setWithdrawXQuantity(int))​(int quantity)` | Attempts to set the specified withdraw-x quantity |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### BankSettings

```
public BankSettings()
```

+ ### Method Detail

- #### isNoteEnabled

```
public static boolean isNoteEnabled()
```

Checks if noting is enabled (ex. items will be withdrawn as notes)

Returns:
true if noting is enabled, false otherwise
- #### setNoteEnabled

```
public static boolean setNoteEnabled​(boolean enabled)
```

Attempts to enable/disable noting

Parameters:
`enabled` - whether or not noting should be enabled
Returns:
true if noting was enabled (or disabled, based on the enabled param), false otherwise
- #### isPlaceholdersOn

```
@Deprecated
public static boolean isPlaceholdersOn()
```

Deprecated.
Checks if placeholders are enabled

Returns:
true if placeholders are enabled, false otherwise
See Also:
[`isPlaceholdersEnabled()`](#isPlaceholdersEnabled())
- #### isPlaceholdersEnabled

```
public static boolean isPlaceholdersEnabled()
```

Checks if placeholders are enabled

Returns:
true if placeholders are enabled, false otherwise
- #### isDepositEquipmentEnabled

```
public static boolean isDepositEquipmentEnabled()
```

Checks if deposit equipment is enabled

Returns:
true if deposit equipment is enabled, false otherwise
- #### isBankInventoryItemOptionEnabled

```
public static boolean isBankInventoryItemOptionEnabled()
```

Checks if bank inventory item option is enabled

Returns:
true if is enabled, false otherwise
- #### getDefaultWithdrawQuantity

```
public static int getDefaultWithdrawQuantity()
```

Gets the default withdraw quantity

Returns:
the default withdraw quantity
- #### getWithdrawXQuantity

```
public static int getWithdrawXQuantity()
```

Gets the withdraw-x quantity

Returns:
the withdraw-x quantity
- #### setWithdrawQuantity

```
public static boolean setWithdrawQuantity​([BankSettings.WithdrawQuantity](BankSettings.WithdrawQuantity.html "enum in org.tribot.script.sdk") withdrawQuantity)
```

Attempts to set the withdraw quantity

Parameters:
`withdrawQuantity` - the quantity to set
Returns:
true if the withdraw quantity was set, false otherwise
- #### setWithdrawXQuantity

```
public static boolean setWithdrawXQuantity​(int quantity)
```

Attempts to set the specified withdraw-x quantity

Parameters:
`quantity` - the withdraw-x quantity to set
Returns:
true if set successfully, false otherwise
- #### getWithdrawQuantity

```
public static [BankSettings.WithdrawQuantity](BankSettings.WithdrawQuantity.html "enum in org.tribot.script.sdk") getWithdrawQuantity()
```

Gets the withdraw quantity

Returns:
the withdraw quantity