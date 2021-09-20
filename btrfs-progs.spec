#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : btrfs-progs
Version  : 5.14.1
Release  : 114
URL      : https://mirrors.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v5.14.1.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v5.14.1.tar.xz
Summary  : libbtrfsutil library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: btrfs-progs-bin = %{version}-%{release}
Requires: btrfs-progs-lib = %{version}-%{release}
Requires: btrfs-progs-license = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : lzo-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(ext2fs)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(libkcapi)
BuildRequires : pkgconfig(libsodium)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : zstd-dev

%description
Userspace utilities to manage btrfs filesystems. Btrfs is a copy on write (COW)
filesystem for Linux aimed at implementing advanced features while focusing on
fault tolerance, repair and easy administration.

%package bin
Summary: bin components for the btrfs-progs package.
Group: Binaries
Requires: btrfs-progs-license = %{version}-%{release}

%description bin
bin components for the btrfs-progs package.


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
%setup -q -n btrfs-progs-v5.14.1
cd %{_builddir}/btrfs-progs-v5.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632158641
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1632158641
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/btrfs-progs
cp %{_builddir}/btrfs-progs-v5.14.1/COPYING %{buildroot}/usr/share/package-licenses/btrfs-progs/ef1bcf369e4124b5f2558fefee17972f41b76cab
cp %{_builddir}/btrfs-progs-v5.14.1/libbtrfsutil/COPYING %{buildroot}/usr/share/package-licenses/btrfs-progs/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
## install_append content
mkdir -p %{buildroot}/usr/include/linux
install -m 0644 kernel-lib/sizes.h %{buildroot}/usr/include/linux/sizes.h
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files dev
%defattr(-,root,root,-)
/usr/include/btrfs/crc32c.h
/usr/include/btrfs/ctree.h
/usr/include/btrfs/extent-cache.h
/usr/include/btrfs/extent_io.h
/usr/include/btrfs/ioctl.h
/usr/include/btrfs/kerncompat.h
/usr/include/btrfs/list.h
/usr/include/btrfs/radix-tree.h
/usr/include/btrfs/rbtree.h
/usr/include/btrfs/send-stream.h
/usr/include/btrfs/send-utils.h
/usr/include/btrfs/send.h
/usr/include/btrfs/sizes.h
/usr/include/btrfs/version.h
/usr/include/btrfsutil.h
/usr/include/linux/sizes.h
/usr/lib64/libbtrfs.so
/usr/lib64/libbtrfsutil.so
/usr/lib64/pkgconfig/libbtrfsutil.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbtrfs.so.0
/usr/lib64/libbtrfs.so.0.1
/usr/lib64/libbtrfsutil.so.1
/usr/lib64/libbtrfsutil.so.1.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/btrfs-progs/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/btrfs-progs/ef1bcf369e4124b5f2558fefee17972f41b76cab
