Name:       libpsl

Summary:    PSL is a collection of Top Level Domains suffixes.
Version:    0.21.0
Release:    0
License:    MIT
URL:        https://github.com/rockdaboot/libpsl
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  python3-devel

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}

%description
A Public Suffix List is a collection of Top Level Domains (TLDs) suffixes. TLDs 
include Global Top Level Domains (gTLDs) like .com and .net; Country Top Level 
Domains (ccTLDs) like .de and .cn; and Brand Top Level Domains like .apple and 
.google. Brand TLDs allows users to register their own top level domain that 
exist at the same level as ICANN's gTLDs. 

%description devel
A Public Suffix List development package.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}
sed -i -e "1s|#!.*|#!%{__python3}|" src/psl-make-dafsa

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        README NEWS AUTHORS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libpsl.so

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/pkgconfig/libpsl.pc

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
