%global ananicycppver 1.0.0-rc4
%global ananicycpp ananicy-cpp-v%{ananicycppver}
%global ananicyver 2.2.1

Name:    ananicy-enhanced
Version: 1.%{ananicyver}
Release: 1%{?dist}
Summary: The runtime of ananicy-cpp with the rules from the original ananicy.

Group:   System Environment/Daemons
License: GPL-3.0
URL:     https://gitlab.com/ananicy-cpp/ananicy-cpp/
Source0: https://gitlab.com/ananicy-cpp/ananicy-cpp/-/archive/v%{ananicycppver}/%{ananicycpp}.zip
Source1: https://github.com/Nefelim4ag/Ananicy/archive/refs/tags/%{ananicyver}.zip

BuildArch:     x86_64
BuildRequires: cmake
BuildRequires: g++
BuildRequires: git
BuildRequires: systemd-devel
Requires:      systemd

%description
ananicy-cpp is a rewrite of ananicy in C++ which targets lower CPU/Memory usage.
This package utilizes the executable of that combined with the rules from the
original ananicy project.

%prep

%setup -n %{ananicycpp}
%setup -T -D -a 1 -n %{ananicycpp}


%build
%cmake -DENABLE_SYSTEMD=yes
%cmake_build

%install
%cmake_install

%license LICENSE

%changelog
* Wed Nov 10 2021 Harold Dost <github@hdost.com> 1.0.0-rc4+2.1.1-1
- Initial packaging.

