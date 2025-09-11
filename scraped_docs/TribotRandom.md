# TribotRandom (tribot-script-sdk 1.0.70 API)

**URL:** https://runeautomation.com/docs/sdk/javadocs/org/tribot/script/sdk/util/TribotRandom.html

**Package:** Packageorg.tribot.script.sdk.util

---

* java.lang.Object
* + org.tribot.script.sdk.util.TribotRandom

* ---

```
public class TribotRandom
extends java.lang.Object
```

Utility class to generate random numbers

* + ### Constructor Summary

Constructors | Constructor | Description |
| `[TribotRandom](#%3Cinit%3E())()` | |

+ ### Method Summary

All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);) | Modifier and Type | Method | Description |
| `static double` | `[normal](#normal(double,double))​(double mean,
double sd)` | |
| `static double` | `[normal](#normal(double,double,double,double))​(double min,
double max,
double mean,
double sd)` | |
| `static int` | `[normal](#normal(int,int))​(int mean,
int sd)` | |
| `static int` | `[normal](#normal(int,int,int,int))​(int min,
int max,
int mean,
int sd)` | |
| `static double` | `[uniform](#uniform(double,double))​(double min,
double max)` | |
| `static int` | `[uniform](#uniform(int,int))​(int min,
int max)` | |

- ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

- #### TribotRandom

```
public TribotRandom()
```

+ ### Method Detail

- #### uniform

```
public static int uniform​(int min,
int max)
```
- #### uniform

```
public static double uniform​(double min,
double max)
```
- #### normal

```
public static int normal​(int mean,
int sd)
```
- #### normal

```
public static int normal​(int min,
int max,
int mean,
int sd)
```
- #### normal

```
public static double normal​(double mean,
double sd)
```
- #### normal

```
public static double normal​(double min,
double max,
double mean,
double sd)
```