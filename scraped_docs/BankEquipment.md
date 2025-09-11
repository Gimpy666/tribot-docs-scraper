# BankEquipment (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/BankEquipment.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.BankEquipment

* ---

```
public class BankEquipment
extends java.lang.Object
```

Contains methods related to the equipment screen available when at a bank

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[BankEquipment](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[bankItem](#bankItem(org.tribot.script.sdk.Equipment.Slot))​([Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") slot)` | Attempts to bank the item in the specified slot |
| `static boolean` | `[close](#close())()` | Closes the bank equipment screen, returning back to the bank screen |
| `static boolean` | `[isOpen](#isOpen())()` | Checks if the bank equipment screen is open |
| `static boolean` | `[open](#open())()` | Attempts to open the bank equipment screen, given that the bank is already open |
| `static boolean` | `[removeItem](#removeItem(org.tribot.script.sdk.Equipment.Slot))​([Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") slot)` | Attempts to remove the specified item slot |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### BankEquipment

```
public BankEquipment()
```

+ ### Method Detail

- #### isOpen

```
public static boolean isOpen()
```

Checks if the bank equipment screen is open

Returns:
true if the bank equipment screen is open, false otherwise
- #### open

```
public static boolean open()
```

Attempts to open the bank equipment screen, given that the bank is already open

Returns:
true if th bank equipment screen was opened, false otherwise
- #### close

```
public static boolean close()
```

Closes the bank equipment screen, returning back to the bank screen

Returns:
true if 'hide worn items' was clicked successfully, false otherwise
- #### removeItem

```
public static boolean removeItem​([Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") slot)
```

Attempts to remove the specified item slot

Parameters:
`slot` - the slot to remove
Returns:
true if removed successfully, false otherwise
- #### bankItem

```
public static boolean bankItem​([Equipment.Slot](Equipment.Slot.html "enum in org.tribot.script.sdk") slot)
```

Attempts to bank the item in the specified slot

Parameters:
`slot` - the slot to bank
Returns:
true if banked successfully, false otherwise