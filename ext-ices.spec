%global app                     ices
%global d_bin                   %{_bindir}
%global release_prefix          100

Name:                           ext-ices
Version:                        1.0.1
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure IceS
License:                        MIT

Source10:                       %{app}.local.xml
Source20:                       %{app}.playlist.sh

Requires:                       ices

%description
META-package for install and configure IceS.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{_sysconfdir}/%{app}.local.xml
%{__install} -Dp -m 0755 %{SOURCE20} \
  %{buildroot}%{d_bin}/%{app}.playlist.sh


%files
%config %{_sysconfdir}/%{app}.local.xml
%{d_bin}/%{app}.playlist.sh


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Move to GitHub.
- UPD: License.
- UPD: "ices.playlist.sh".

* Thu Aug 01 2019 Package Store <pkgstore@pm.me> - 1.0.0-106
- UPD: Shell scripts.

* Wed Jul 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-105
- UPD: SPEC-file.

* Wed Jul 10 2019 Package Store <pkgstore@pm.me> - 1.0.0-104
- UPD: Scripts & configs.

* Tue Jul 02 2019 Package Store <pkgstore@pm.me> - 1.0.0-103
- UPD: SPEC-file.

* Sat Mar 30 2019 Package Store <pkgstore@pm.me> - 1.0.0-102
- NEW: 1.0.0-102.

* Sat Mar 30 2019 Package Store <pkgstore@pm.me> - 1.0.0-101
- NEW: 1.0.0-101.

* Fri Feb 15 2019 Package Store <pkgstore@pm.me> - 1.0.0-100
- Initial build.
