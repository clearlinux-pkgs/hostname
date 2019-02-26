#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hostname
Version  : 3.21
Release  : 16
URL      : http://ftp.us.debian.org/debian/pool/main/h/hostname/hostname_3.21.tar.gz
Source0  : http://ftp.us.debian.org/debian/pool/main/h/hostname/hostname_3.21.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: hostname-bin = %{version}-%{release}
Requires: hostname-license = %{version}-%{release}
Requires: hostname-man = %{version}-%{release}
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
%setup -q -n hostname
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551149853
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1551149853
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hostname
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/hostname/COPYRIGHT
cp debian/copyright %{buildroot}/usr/share/package-licenses/hostname/debian_copyright
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/dnsdomainname
%exclude /usr/bin/domainname
%exclude /usr/bin/nisdomainname
%exclude /usr/bin/ypdomainname
/usr/bin/hostname

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hostname/COPYRIGHT
/usr/share/package-licenses/hostname/debian_copyright

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man1/dnsdomainname.1
%exclude /usr/share/man/man1/domainname.1
%exclude /usr/share/man/man1/nisdomainname.1
%exclude /usr/share/man/man1/ypdomainname.1
/usr/share/man/man1/hostname.1
