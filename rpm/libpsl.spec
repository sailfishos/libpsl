Name:       libpsl

Summary:    PSL is a collection of Top Level Domains suffixes.
Version:    0.21.5
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

%package -n psl
Summary: Commandline utility to explore the Public Suffix List

%description -n psl
This package contains a commandline utility to explore the Public Suffix List,
for example it checks if domains are public suffixes, checks if cookie-domain
is acceptable for domains and so on.

%package -n psl-make-dafsa
Summary: Compiles the Public Suffix List into DAFSA form
BuildArch: noarch

%description -n psl-make-dafsa
This script produces C/C++ code or an architecture-independent binary object
which represents a Deterministic Acyclic Finite State Automaton (DAFSA)
from a plain text Public Suffix List.

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
%license LICENSE
%{_libdir}/libpsl.so.*

%files devel
%{_libdir}/libpsl.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libpsl.pc

%files doc
%{_docdir}/%{name}-%{version}

%files -n psl
%license LICENSE
%{_bindir}/psl
%{_mandir}/man1/psl.1*

%files -n psl-make-dafsa
%license LICENSE
%{_bindir}/psl-make-dafsa
%{_mandir}/man1/psl-make-dafsa.1*
