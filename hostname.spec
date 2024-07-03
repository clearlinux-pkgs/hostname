#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : hostname
Version  : 3.23+nmu2
Release  : 21
URL      : https://mirrors.kernel.org/debian/pool/main/h/hostname/hostname_3.23+nmu2.tar.xz
Source0  : https://mirrors.kernel.org/debian/pool/main/h/hostname/hostname_3.23+nmu2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: hostname-bin = %{version}-%{release}
Requires: hostname-license = %{version}-%{release}
Requires: hostname-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: destdir.patch

%description
No detailed description available

%package bin
Summary: bin components for the hostname package.
Group: Binaries
Requires: hostname-license = %{version}-%{release}

%description bin
bin components for the hostname package.


%package license
Summary: license components for the hostname package.
Group: Default

%description license
license components for the hostname package.


%package man
Summary: man components for the hostname package.
Group: Default

%description man
man components for the hostname package.


%prep
%setup -q -n hostname-3.23+nmu1
cd %{_builddir}/hostname-3.23+nmu1
%patch -P 1 -p1
pushd ..
cp -a hostname-3.23+nmu1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720039855
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720039855
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hostname
cp %{_builddir}/hostname-3.23+nmu1/COPYRIGHT %{buildroot}/usr/share/package-licenses/hostname/87cf7aa221439c57d2f9220777b542884465aaf2 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/dnsdomainname
rm -f %{buildroot}*/usr/bin/domainname
rm -f %{buildroot}*/usr/bin/nisdomainname
rm -f %{buildroot}*/usr/bin/ypdomainname
rm -f %{buildroot}*/usr/share/man/man1/dnsdomainname.1
rm -f %{buildroot}*/usr/share/man/man1/domainname.1
rm -f %{buildroot}*/usr/share/man/man1/nisdomainname.1
rm -f %{buildroot}*/usr/share/man/man1/ypdomainname.1
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/hostname
/usr/bin/hostname

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hostname/87cf7aa221439c57d2f9220777b542884465aaf2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hostname.1
