Dirty flashing between different ROMs, or migrating from another website's builds are not supported.
{:.alert .alert-danger}

{% if page.format_on_upgrade == true %}

If you are currently upgrading Android versions, you must format your data as encryption methods have changed.
{:.alert .alert-danger}

{% endif %}

You must be rooted to complete installation.
{:.alert .alert-warning}

#### Section I - Prerequisites

1. Download ADB and fastboot using this guide: <https://wiki.lineageos.org/adb_fastboot_guide>
1. Download [copy-partitions-20220613-signed.zip](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip)
1. If you're on Windows, enable file extensions using this guide: <https://3ds.hacks.guide/file-extensions-(windows).html>

#### Section II - Installing a custom recovery

1. Download [this custom recovery]({{ include.recoveryimage }})
1. Install it using ADB:
```
adb push <name of downloaded file> /sdcard/recovery.img
adb shell
su
dd if=/sdcard/recovery.img of=/dev/block/bootdevice/by-name/boot_a
dd if=/sdcard/recovery.img of=/dev/block/bootdevice/by-name/boot_b
exit
```
1. Reboot to custom recovery:
```
adb reboot recovery
```

### Section III - Installing the ROM

1. Navigate to `Factory Reset`
1. Select `Format data/factory reset`
1. Accept the warning
1. Go back to main menu
1. Select `Apply Update`
1. Select `Apply from ADB`
1. On your PC, run the following command:
```
adb sideload copy-partitions-20220613-signed.zip
```
1. When prompted, select `No` to avoid a reboot
1. Select `Apply Update`
1. Select `Apply from ADB`
1. On your PC, run the following command:
```
adb sideload <path to ROM zip>
```
1. When prompted, select `Yes` to reboot back to recovery
{%- unless page.has_gapps == true %}
1. If you wish to install Google apps, follow this guide: <https://wiki.lineageos.org/gapps/>
{%- endunless %}
1. Reboot your phone

You have completed installation.
{:.alert .alert-success}
