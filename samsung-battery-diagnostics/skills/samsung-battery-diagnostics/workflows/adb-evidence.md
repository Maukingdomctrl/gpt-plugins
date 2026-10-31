# Optional: read-only adb evidence

For users comfortable with a computer. The **user** runs these on their own computer and pastes the output. The assistant never claims to have run them unless it actually has a tool connected to that computer and the output is in the conversation.

## Setup (user)
1. Phone: Settings > About phone > Software information > tap **Build number** 7 times (enables Developer options) [R].
2. Settings > Developer options > **USB debugging** on; connect USB; tap **Allow** on the phone [R].
3. Computer: install Android SDK Platform-Tools (Google), then run `adb devices`; the phone should show `device`.
4. When finished, USB debugging can be turned off again in Developer options (reverse).

## Allowed commands (read-only)
| Command | What it gives |
|---|---|
| `adb shell getprop ro.product.model` | Model code (e.g. SM-A146B) |
| `adb shell getprop ro.build.version.release` | Android version |
| `adb shell getprop ro.build.version.oneui` | One UI version as a number, e.g. 70000 = 7.0 [U: format not officially documented] |
| `adb shell getprop ro.build.display.id` | Firmware build |
| `adb shell dumpsys battery` | level, status, health, temperature (tenths °C), voltage (mV), power source |
| `adb shell dumpsys batterystats --charged > batterystats.txt` | battery history since last full charge (large). Ask for the "Estimated power use", "All partial wake locks" / "Wake lock" and "Kernel Wake lock" sections only, not the whole file |
| `adb shell settings get system screen_off_timeout` | timeout in ms |
| `adb shell dumpsys deviceidle` | Doze state summary |

Android documents `dumpsys` at developer.android.com/tools/dumpsys [R S27].

## Forbidden (state-changing) — never suggest
`dumpsys batterystats --reset`, `dumpsys battery set …`, `dumpsys battery unplug`, `dumpsys battery reset`, `cmd battery …`, `pm disable…`, `pm uninstall…`, `settings put …`, `svc …`, any `rm`, any root or "debloat" script.

## Interpreting
- Quote values exactly. Temperature 352 → 35.2 °C.
- `health: 2` means GOOD in Android's BatteryManager constants; other values (e.g. 3 overheat, 4 dead, 7 cold) are reported states, not a capacity measurement [R S27].
- Wake lock lines show a tag and a duration; a tag with hours of hold time during the night is strong evidence for which app/component kept the phone awake. Map the tag to an app only if the tag names it; otherwise say it's unknown.
- Do not infer battery capacity or cycle count from these outputs unless a field explicitly reports it.
