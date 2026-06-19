#!/usr/bin/env bash
# Updates the .spec files as necessary, commits the changes, and triggers a COPR rebuild
set -euo pipefail
my_realpath="$(realpath "$0")"
# # >>> ble.sh >>>
# declare -rA ble_sh=(
#     [URL]='https://github.com/akinomyoga/ble.sh'
#     [Source0]="${ble_sh[URL]}/releases/download/nightly/ble-nightly.tar.xz"
#     # [Git_API]="$(mktemp /tmp/ble-sh.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)"
# )
# wget --no-verbose 				\
#     --output-document="${ble_sh[Git_API]}"	\
#     --https-only 				\
#     --https-enforce=hard 			\
#     https://api.github.com/repos/akinomyoga/ble.sh/releases/tags/nightly 
# # ble_sh[snapinfo]="$(
# #     jq --monochrome-output 	\
# # 	'.name' 		\
# # 	"${git_api["ble.sh"]}" 	\
# #     | sed --regexp-extended 	\
# # 	--expression='s/"nightly ([0-9]{4})-([0-9]{2})-([0-9]{2}).*"/\1\2\3git/'
# # )"
# ble_sh[snapinfo]="$(date +'%Y%m%d')"
# # <<< ble.sh <<<
if systemd-detect-virt --quiet; then
    tito build --test 		\
	|| log --error "tito test build was unsuccessful"
    tito tag			\
	|| log --error "tito tag was unsuccessful"
    git push --follow-tags 	\
else
    log --error "No virual environment is detected. It is suggested to run this in a distrobox: 'distrobox-enter COPR -- $my_realpath"
fi
