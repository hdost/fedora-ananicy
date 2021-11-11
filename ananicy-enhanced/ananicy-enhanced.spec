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
License: GPLv3
URL:     https://gitlab.com/ananicy-cpp/ananicy-cpp/
Source0: https://gitlab.com/ananicy-cpp/ananicy-cpp/-/archive/v%{ananicycppver}/%{ananicycpp}.tar.gz
Source1: https://github.com/Nefelim4ag/Ananicy/archive/refs/tags/%{ananicyver}.tar.gz
Source2: https://github.com/nlohmann/json/archive/refs/tags/v%{jsonver}.tar.gz
Source3: https://github.com/fmtlib/fmt/archive/refs/tags/%{fmtlibver}.tar.gz
Source4: https://github.com/gabime/spdlog/archive/refs/tags/v%{spdlogver}.tar.gz

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

%build
%cmake -DENABLE_SYSTEMD=yes \
-DUSE_EXTERNAL_JSON=yes -Dnlohmann_json_DIR=json-%{jsonver}\
-DUSE_EXTERNAL_SPDLOG=yes -Dspdlog_DIR=spdlog-%{spdlogver}\
-DUSE_EXTERNAL_FMTLIB=yes -Dfmt_DIR=fmt-%{fmtlibver}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}
cp -a Ananicy-%{ananicyver}/ananicy.d %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%{_bindir}/ananicy-cpp
%{_unitdir}/ananicy-cpp.service
%{_sysconfdir}/*

%changelog
* Wed Nov 10 2021 Harold Dost <github@hdost.com> 1.0.0-rc4+2.1.1-1
- Initial packaging.

