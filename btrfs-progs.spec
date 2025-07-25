#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v27
# autospec commit: 65cf152
#
Name     : btrfs-progs
Version  : 6.15
Release  : 164
URL      : https://mirrors.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v6.15.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v6.15.tar.gz
Summary  : libbtrfsutil library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: btrfs-progs-bin = %{version}-%{release}
Requires: btrfs-progs-config = %{version}-%{release}
Requires: btrfs-progs-lib = %{version}-%{release}
Requires: btrfs-progs-license = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : buildreq-configure
BuildRequires : lzo-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(botan-3)
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(ext2fs)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(libkcapi)
BuildRequires : pkgconfig(libsodium)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Userspace utilities to manage btrfs filesystems. Btrfs is a copy on write (COW)
filesystem for Linux aimed at implementing advanced features while focusing on
fault tolerance, repair and easy administration.

%package bin
Summary: bin components for the btrfs-progs package.
Group: Binaries
Requires: btrfs-progs-config = %{version}-%{release}
Requires: btrfs-progs-license = %{version}-%{release}

%description bin
bin components for the btrfs-progs package.


%package config
Summary: config components for the btrfs-progs package.
Group: Default

%description config
config components for the btrfs-progs package.


%package dev
Summary: dev components for the btrfs-progs package.
Group: Development
Requires: btrfs-progs-lib = %{version}-%{release}
Requires: btrfs-progs-bin = %{version}-%{release}
Provides: btrfs-progs-devel = %{version}-%{release}
Requires: btrfs-progs = %{version}-%{release}

%description dev
dev components for the btrfs-progs package.


%package lib
Summary: lib components for the btrfs-progs package.
Group: Libraries
Requires: btrfs-progs-license = %{version}-%{release}

%description lib
lib components for the btrfs-progs package.


%package license
Summary: license components for the btrfs-progs package.
Group: Default

%description license
license components for the btrfs-progs package.


%prep
%setup -q -n btrfs-progs-v6.15
cd %{_builddir}/btrfs-progs-v6.15
pushd ..
cp -a btrfs-progs-v6.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750774363
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1750774363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/btrfs-progs
cp %{_builddir}/btrfs-progs-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/btrfs-progs/ef1bcf369e4124b5f2558fefee17972f41b76cab || :
cp %{_builddir}/btrfs-progs-v%{version}/libbtrfsutil/COPYING %{buildroot}/usr/share/package-licenses/btrfs-progs/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
mkdir -p %{buildroot}/usr/include/linux
install -m 0644 kernel-lib/sizes.h %{buildroot}/usr/include/linux/sizes.h
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/btrfs
/V3/usr/bin/btrfs-convert
/V3/usr/bin/btrfs-find-root
/V3/usr/bin/btrfs-image
/V3/usr/bin/btrfs-map-logical
/V3/usr/bin/btrfs-select-super
/V3/usr/bin/btrfstune
/V3/usr/bin/mkfs.btrfs
/usr/bin/btrfs
/usr/bin/btrfs-convert
/usr/bin/btrfs-find-root
/usr/bin/btrfs-image
/usr/bin/btrfs-map-logical
/usr/bin/btrfs-select-super
/usr/bin/btrfsck
/usr/bin/btrfstune
/usr/bin/fsck.btrfs
/usr/bin/mkfs.btrfs

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/64-btrfs-dm.rules
/usr/lib/udev/rules.d/64-btrfs-zoned.rules

%files dev
%defattr(-,root,root,-)
/usr/include/btrfs/ctree.h
/usr/include/btrfs/ioctl.h
/usr/include/btrfs/kerncompat.h
/usr/include/btrfs/rbtree_types.h
/usr/include/btrfs/send-stream.h
/usr/include/btrfs/send-utils.h
/usr/include/btrfs/send.h
/usr/include/btrfs/version.h
/usr/include/btrfsutil.h
/usr/include/linux/sizes.h
/usr/lib64/libbtrfs.so
/usr/lib64/libbtrfsutil.so
/usr/lib64/pkgconfig/libbtrfsutil.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libbtrfs.so.0.1.4
/V3/usr/lib64/libbtrfsutil.so.1.3.2
/usr/lib64/libbtrfs.so.0
/usr/lib64/libbtrfs.so.0.1
/usr/lib64/libbtrfs.so.0.1.4
/usr/lib64/libbtrfsutil.so.1
/usr/lib64/libbtrfsutil.so.1.3
/usr/lib64/libbtrfsutil.so.1.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/btrfs-progs/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/btrfs-progs/ef1bcf369e4124b5f2558fefee17972f41b76cab
