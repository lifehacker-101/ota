If you are currently running any ROM not hosted on this site, you must clean flash!
{:.alert .alert-danger}

You must be rooted to complete installation.
{:.alert .alert-warning}

#### Section I - Prerequisites

1. Download ADB and fastboot using this guide: <https://wiki.lineageos.org/adb_fastboot_guide>
1. Download [copy-partitions-20220613-signed.zip](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip)
1. If you're on Windows, enable file extensions using this guide: <https://3ds.hacks.guide/file-extensions-(windows).html>

#### Section II - Installing a custom recovery

1. Download [Lineage Recovery](https://sourceforge.net/projects/lifehackerhansol-android/files/recovery/mh2lm/lineage-recovery-21.0-20240528-UNOFFICIAL-mh2lm-signed.img)
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

### Section III - Installing LineageOS

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
adb sideload <path to LineageOS ROM zip>
```
1. When prompted, select `Yes` to reboot back to recovery
1. If you wish to install Google apps, follow this guide: <https://wiki.lineageos.org/gapps/>
1. Reboot your phone

You are now booted into LineageOS.
{:.alert .alert-success}
