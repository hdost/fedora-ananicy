%global ananicycppver 1.0.0-rc4
%global ananicycpp ananicy-cpp-v%{ananicycppver}
%global ananicyver 2.2.1
%global jsonver 3.9.1
%global fmtlibver 8.0.1
%global spdlogver 1.9.2

Name:    ananicy-enhanced
Version: 1.%{ananicyver}
Release: 1%{?dist}
Summary: The runtime of ananicy-cpp with the rules from the original ananicy.

Group:   System Environment/Daemons
License: GPL-3.0
URL:     https://gitlab.com/ananicy-cpp/ananicy-cpp/
Source0: https://gitlab.com/ananicy-cpp/ananicy-cpp/-/archive/v%{ananicycppver}/%{ananicycpp}.zip
Source1: https://github.com/Nefelim4ag/Ananicy/archive/refs/tags/%{ananicyver}.zip
Source2: https://github.com/nlohmann/json/archive/refs/tags/v%{jsonver}.zip
Source3: https://github.com/fmtlib/fmt/archive/refs/tags/%{fmtlibver}.zip
Source4: https://github.com/gabime/spdlog/archive/refs/tags/v%{spdlogver}.zip

BuildArch: noarch
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

%setup -q -n %{ananicycpp}
%setup -q -T -D -a 1 -n %{ananicycpp}
%setup -q -T -D -a 2 -n %{ananicycpp}
%setup -q -T -D -a 3 -n %{ananicycpp}
%setup -q -T -D -a 4 -n %{ananicycpp}
mv v%{jsonver} nlohmann_json-%{jsonver}
mv %{fmtlibver} fmt-%{fmtlibver}
mv v%{spdlogver} spdlog-%{spdlogver}

%build
%cmake -DENABLE_SYSTEMD=yes -DUSE_EXTERNAL_JSON=yes -DUSE_EXTERNAL_SPDLOG=yes -DUSE_EXTERNAL_FMTLIB=yes
%cmake_build

%install
%cmake_install

%license LICENSE

%changelog
* Wed Nov 10 2021 Harold Dost <github@hdost.com> 1.0.0-rc4+2.1.1-1
- Initial packaging.

