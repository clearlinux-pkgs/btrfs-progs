#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : btrfs-progs
Version  : 4.16.1
Release  : 77
URL      : https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v4.16.1.tar.xz
Source0  : https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v4.16.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: btrfs-progs-bin
Requires: btrfs-progs-lib
BuildRequires : acl-dev
BuildRequires : lzo-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(ext2fs)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : setuptools
BuildRequires : zstd-dev

%description
Userspace utilities to manage btrfs filesystems. Btrfs is a copy on write (COW)
filesystem for Linux aimed at implementing advanced features while focusing on
fault tolerance, repair and easy administration.

%package bin
Summary: bin components for the btrfs-progs package.
Group: Binaries

%description bin
bin components for the btrfs-progs package.


%package dev
Summary: dev components for the btrfs-progs package.
Group: Development
Requires: btrfs-progs-lib
Requires: btrfs-progs-bin
Provides: btrfs-progs-devel

%description dev
dev components for the btrfs-progs package.


%package lib
Summary: lib components for the btrfs-progs package.
Group: Libraries

%description lib
lib components for the btrfs-progs package.


%prep
%setup -q -n btrfs-progs-v4.16.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524676319
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1524676319
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/include/linux
install -m 0644 kernel-lib/sizes.h %{buildroot}/usr/include/linux/sizes.h
## make_install_append end

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
/usr/include/*.h
/usr/include/btrfs/btrfs-list.h
/usr/include/btrfs/btrfsck.h
/usr/include/btrfs/crc32c.h
/usr/include/btrfs/ctree.h
/usr/include/btrfs/extent-cache.h
/usr/include/btrfs/extent_io.h
/usr/include/btrfs/ioctl.h
/usr/include/btrfs/kerncompat.h
/usr/include/btrfs/list.h
/usr/include/btrfs/radix-tree.h
/usr/include/btrfs/raid56.h
/usr/include/btrfs/rbtree.h
/usr/include/btrfs/send-stream.h
/usr/include/btrfs/send-utils.h
/usr/include/btrfs/send.h
/usr/include/btrfs/sizes.h
/usr/include/btrfs/version.h
/usr/include/linux/sizes.h
/usr/lib64/libbtrfs.so
/usr/lib64/libbtrfsutil.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbtrfs.so.0
/usr/lib64/libbtrfs.so.0.1
/usr/lib64/libbtrfsutil.so.1
/usr/lib64/libbtrfsutil.so.1.0.0
