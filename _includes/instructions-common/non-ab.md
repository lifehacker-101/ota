If you are currently running any ROM not hosted on this site, you must clean flash!
{:.alert .alert-danger}

{% if page.format_on_upgrade == true %}

If you are currently running LineageOS 21 and upgrading to 22.1, you must clean flash as encryption methods have changed.
{:.alert .alert-danger}

{% endif %}

You must be rooted to complete installation.
{:.alert .alert-warning}

#### Section I - Prerequisites

1. Download ADB and fastboot using this guide: <https://wiki.lineageos.org/adb_fastboot_guide>
1. If you're on Windows, enable file extensions using this guide: <https://3ds.hacks.guide/file-extensions-(windows).html>

#### Section II - Installing a custom recovery

1. Download [Lineage Recovery]({{ include.recoveryimage }})
1. Install it using ADB:
```
adb push <name of downloaded file> /sdcard/recovery.img
adb shell
su
dd if=/sdcard/recovery.img of=/dev/block/bootdevice/by-name/recovery
exit
```
1. Reboot to custom recovery:
```
adb reboot recovery
```

### Section III - Installing LineageOS

1. Navigate to `Factory Reset`
1. Select `Format data/factory reset`
1. Accept the warning
1. Go back to main menu
1. Select `Apply Update`
1. Select `Apply from ADB`
1. On your PC, run the following command:
```
adb sideload <path to LineageOS ROM zip>
```
1. When prompted, select `Yes` to reboot back to recovery
1. If you wish to install Google apps, follow this guide: <https://wiki.lineageos.org/gapps/>
1. Reboot your phone

You are now booted into LineageOS.
{:.alert .alert-success}
