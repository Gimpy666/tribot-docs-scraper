# TribotScript (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/script/TribotScript.html

**Package:** Packageorg.tribot.script.sdk.script

---

* ---

```
public interface TribotScript
```

This interface denotes a runnable tribot script. Classes that implement this interface are considered "scripts".

* + ### Method Summary

All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);) | Modifier and Type | Method | Description |
| `default void` | `[configure](#configure(org.tribot.script.sdk.script.ScriptConfig))​([ScriptConfig](ScriptConfig.html "class in org.tribot.script.sdk.script") config)` | Optional configuration for a script. |
| `void` | `[execute](#execute(java.lang.String))​(java.lang.String args)` | Runs the script! |

* + ### Method Detail

- #### configure

```
default void configure​([ScriptConfig](ScriptConfig.html "class in org.tribot.script.sdk.script") config)
```

Optional configuration for a script. It's expected that the implementer of the interface modifies the given
config object to what settings it wants. These settings are read BEFORE the script starts.

Parameters:
`config` - The configuration object to modify.
- #### execute

```
void execute​(java.lang.String args)
```

Runs the script!

Parameters:
`args` - The "args" string that the user can input.