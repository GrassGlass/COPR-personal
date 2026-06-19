First, enable this repository:
```bash
dnf copr enable grassglass/personal
```
To set up [`ble.sh`](https://github.com/akinomyoga/ble.sh), we use a variant of the official [instructions](https://github.com/akinomyoga/ble.sh/releases/tag/nightly):
```bash
sudo dnf install ble-sh
# Add the following line near the top of ~/.bashrc
[[ "$-" == *i* ]] && source ~/usr/share/blesh/ble.sh --attach=none
# Add the following line at the end of ~/.bashrc
[[ ! "${BLE_VERSION-}" ]] || ble-attach
```
