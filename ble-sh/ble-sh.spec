# Author: grassglass (https://github.com/GrassGlass)
# License: GNU GPL-3.0-or-later (https://www.gnu.org/licenses/gpl-3.0.en.html)
# References: 
#	1. https://docs.fedoraproject.org/fr/package-maintainers/Packaging_Tutorial_1_banner/
#	2. https://rpm-packaging-guide.github.io/#what-is-a-spec-file
#	3. https://rpm-software-management.github.io/rpm/man/rpm-macros.7
#	4. https://rpm-software-management.github.io/rpm/man/rpm-spec.5
# Versioning
# See: https://tmz.fedorapeople.org/guidelines/packaging-guidelines/Versioning/#_snapshots
%global snapinfo %(date +'%Y%m%d')
%global binary %{buildroot}%{_bindir}/ble.sh
Name: ble-sh
Version: nightly
Release: %{snapinfo}%{?dist}
Summary: Koichi Murase's Bash Line Editor

License: BSD-3-Clause
URL: https://github.com/akinomyoga/ble.sh 
Source0: %{url}/releases/download/nightly/ble-nightly.tar.xz

# Build-time dependencies
BuildRequires: procps-ng
# Run-time dependencies
Requires: bash
# No arch since ble.sh is a collection of shell scripts, and only requires the Bash shell to run
BuildArch: noarch

%description
Koichi Murase's Bash Line Editor―a line editor written in pure Bash with syntax highlighting, auto suggestions, vim modes, etc. for Bash interactive sessions.

%prep
%autosetup -n ble-nightly

%install
bash ble.sh --install %{buildroot}%{_datadir}
# 'ble.sh' isn't meant to be executed
# chmod 0755 %{buildroot}%{_datadir}/blesh/ble.sh
# mkdir --parents %{buildroot}%{_bindir}
# ln --symbolic %{_datadir}/blesh/ble.sh %{binary}

%check

%files
%license licenses/LICENSE.md
%doc doc/README.md
%{_datadir}/blesh/
# %%{_bindir}/ble.sh

%changelog
%autochangelog
