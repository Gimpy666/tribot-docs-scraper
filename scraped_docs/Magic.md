# Magic (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/Magic.html

**Package:** Packageorg.tribot.script.sdk

---

* java.lang.Object
* + org.tribot.script.sdk.Magic

* ---

```
public class Magic
extends java.lang.Object
```

Utilities for interacting with the Magic Tab.

* + ### Nested Class Summary

Nested Classes | Modifier and Type | Class | Description |
| `static class` | `[Magic.SpellBook](Magic.SpellBook.html "enum in org.tribot.script.sdk")` | A magic spellbook |

+ ### Constructor Summary

Constructors | Constructor | Description |
| `[Magic](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static boolean` | `[castOn](#castOn(java.lang.String,org.tribot.script.sdk.interfaces.Clickable))​(java.lang.String spellName,
[Clickable](interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces") target)` | Casts the specified spell on the specified target. |
| `static boolean` | `[closeSpellFilters](#closeSpellFilters())()` | Closes the spell filters screen |
| `static boolean` | `[ensureSpellSelected](#ensureSpellSelected(java.lang.String))​(java.lang.String name)` | Selects the given spell, if it is not already selected |
| `static [Magic.SpellBook](Magic.SpellBook.html "enum in org.tribot.script.sdk")` | `[getActiveSpellBook](#getActiveSpellBook())()` | Gets the currently active spellbook |
| `static java.util.Optional<java.lang.String>` | `[getSelectedSpellName](#getSelectedSpellName())()` | Gets the name of the selected spell in the Magic Tab. |
| `static boolean` | `[isAnySpellSelected](#isAnySpellSelected())()` | Determines whether or not a spell is selected. |
| `static boolean` | `[isSpellFiltersOpen](#isSpellFiltersOpen())()` | Checks if the spell filters screen is open |
| `static boolean` | `[isSpellSelected](#isSpellSelected(java.lang.String))​(java.lang.String name)` | Checks if a spell with the specified name is selected |
| `static boolean` | `[selectSpell](#selectSpell(java.lang.String))​(java.lang.String name)` | Selects a given spell based on its name in the Magic Tab. |
| `static boolean` | `[selectSpell](#selectSpell(java.lang.String,java.lang.String))​(java.lang.String name,
java.lang.String action)` | Selects a given spell based on its name in the Magic Tab. |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### Magic

```
public Magic()
```

+ ### Method Detail

- #### selectSpell

```
public static boolean selectSpell​(java.lang.String name)
```

Selects a given spell based on its name in the Magic Tab.

Parameters:
`name` - The name of the spell to select.
Returns:
If the click to select the spell was successful
- #### selectSpell

```
public static boolean selectSpell​(java.lang.String name,
java.lang.String action)
```

Selects a given spell based on its name in the Magic Tab.

Parameters:
`name` - The name of the spell to select.
`action` - The action to select on the spell.
Returns:
If the click to select the spell was successful
- #### isAnySpellSelected

```
public static boolean isAnySpellSelected()
```

Determines whether or not a spell is selected.

Returns:
True if any spell is selected. False otherwise.
- #### isSpellSelected

```
public static boolean isSpellSelected​(java.lang.String name)
```

Checks if a spell with the specified name is selected

Parameters:
`name` - the spell name
Returns:
true if the spell is selected, false otherwise
- #### ensureSpellSelected

```
public static boolean ensureSpellSelected​(java.lang.String name)
```

Selects the given spell, if it is not already selected

Parameters:
`name` - the spell name
Returns:
true if the spell is selected, false otherwise
- #### closeSpellFilters

```
public static boolean closeSpellFilters()
```

Closes the spell filters screen

Returns:
true if closed successfully, false otherwise
- #### isSpellFiltersOpen

```
public static boolean isSpellFiltersOpen()
```

Checks if the spell filters screen is open

Returns:
true if the spell filters screen is open, false otherwise
- #### getSelectedSpellName

```
public static java.util.Optional<java.lang.String> getSelectedSpellName()
```

Gets the name of the selected spell in the Magic Tab.

Returns:
Optional that contains the spell name. Empty if no spell is selected.
- #### getActiveSpellBook

```
public static [Magic.SpellBook](Magic.SpellBook.html "enum in org.tribot.script.sdk") getActiveSpellBook()
```

Gets the currently active spellbook

Returns:
the current spellbook
- #### castOn

```
public static boolean castOn​(java.lang.String spellName,
[Clickable](interfaces/Clickable.html "interface in org.tribot.script.sdk.interfaces") target)
```

Casts the specified spell on the specified target.
Will travel to and adjust the camera if necessary.

Parameters:
`spellName` - the name of the spell to cast
`target` - the target to cast on
Returns:
true if the spell was cast on the target successfully, false otherwise