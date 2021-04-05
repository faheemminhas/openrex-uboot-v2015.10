Summary: U-Boot bootloader with support for OpenRex board
Name: u-boot-openrex
Version: v2015.10+git0+7d8ddd7de7
Release: r0
License: GPLv2+
Group: bootloaders
Packager: Poky <poky@yoctoproject.org>
URL: http://www.denx.de/wiki/U-Boot/WebHome
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: openssl-native
BuildRequires: virtual/libc
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc

%description
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex

%package -n u-boot-openrex-dbg
Summary: U-Boot bootloader with support for OpenRex board - Debugging files
Group: devel

%description -n u-boot-openrex-dbg
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex  This package contains ELF symbols and
related sources for debugging purposes.

%package -n u-boot-openrex-staticdev
Summary: U-Boot bootloader with support for OpenRex board - Development files (Static Libraries)
Group: devel
Requires: u-boot-openrex-dev = v2015.10+git0+7d8ddd7de7-r0

%description -n u-boot-openrex-staticdev
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex  This package contains static libraries for
software development.

%package -n u-boot-openrex-dev
Summary: U-Boot bootloader with support for OpenRex board - Development files
Group: devel
Requires: u-boot-openrex = v2015.10+git0+7d8ddd7de7-r0

%description -n u-boot-openrex-dev
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex  This package contains symbolic links,
header files, and related items necessary for software development.

%package -n u-boot-openrex-doc
Summary: U-Boot bootloader with support for OpenRex board - Documentation files
Group: doc

%description -n u-boot-openrex-doc
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex  This package contains documentation.

%package -n u-boot-openrex-locale
Summary: U-Boot bootloader with support for OpenRex board
Group: bootloaders

%description -n u-boot-openrex-locale
U-Boot bootloader with support for OpenRex board. More info at
http://www.imx6rex.com/open-rex

%files
%defattr(-,-,-,-)
%dir "/boot"
"/boot/u-boot.imx-sd"
"/boot/u-boot-sd-v2015.10+gitAUTOINC+7d8ddd7de7-r0.imx"
"/boot/u-boot.imx"

%files -n u-boot-openrex-dbg
%defattr(-,-,-,-)

%files -n u-boot-openrex-dev
%defattr(-,-,-,-)

